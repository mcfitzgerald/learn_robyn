import streamlit as st
import pandas as pd
import plotly.io as pio
import plotly.express as px
import jinja2
from robyn_input_helper_funcs import generate_var_dict
import mcf_plotly_theme

pio.templates.default = "mike"

st.title("Robyn Input Prep")

st.header("Upload a CSV containing Robyn Input")
uploaded_file = st.file_uploader("Choose a file")

st.header("Data Preview")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.info(f"""👆 Upload a CSV file first.""")
    st.stop()

columns = df.columns.to_list()

# Create dictionary of variable types, e.g. Spend, Sales, TV, etc. for easier prep
var_dict = generate_var_dict(
    df, column_tags=[r"SPEND", r"PRICE", r"SALES_VALUE", r"IMPRESSIONS|TRP"]
)

st.header("Configuration")
model_name = st.text_input("Model Name (reference name for model files)", value="robyn_model")
prophet_country = st.text_input("Country (used for Prophet configuration)")
window_start = st.text_input("Model start date (YYYY-MM-DD)")
window_end = st.text_input("Model end date (YYYY-MM-DD)")

st.header("Variable Selection")
date_var = st.selectbox(
    "Select independent variable (e.g. date variable)", columns, index=0
)
dep_var = st.selectbox(
    "Select response variable (e.g. Sales)",
    var_dict["SALES_VALUE"],
)
order_warning = '<p style="color:Red;"><b>NOTE: media spends and media impact vars must be in same order</b></p>'
st.markdown(order_warning, unsafe_allow_html=True)
paid_media_spends = st.multiselect("Select media spends", var_dict["SPEND"])
paid_media_vars = st.multiselect(
    "Select media impact variables (e.g. impressions)", var_dict["IMPRESSIONS|TRP"]
)
context_vars = st.multiselect(
    "Select covariates (e.g. competitor sales, product price)",
    (var_dict["PRICE"] + var_dict["SALES_VALUE"]),
)

st.header("Look at your data!")

# Create figs
response_var_fig = px.line(
    df,
    x=date_var,
    y=dep_var,
    title="Response (e.g. Sales) vs. Date",
    color_discrete_sequence=px.colors.sequential.Agsunset,
)
media_spend_fig = px.bar(
    df,
    x=date_var,
    y=paid_media_spends,
    title="Media Spend vs. Date",
    color_discrete_sequence=px.colors.qualitative.Prism,
)
media_vars_fig = px.bar(
    df,
    x=date_var,
    y=paid_media_vars,
    title="Media Impressions vs. Date",
    color_discrete_sequence=px.colors.qualitative.Prism,
)

covariate_vars_fig = px.line(
    df,
    x=date_var,
    y=context_vars,
    title="Covariates vs. Date",
    color_discrete_sequence=px.colors.sequential.Agsunset,
)

# Display figs
st.plotly_chart(response_var_fig)
st.plotly_chart(media_spend_fig)
st.plotly_chart(media_vars_fig)
st.plotly_chart(covariate_vars_fig)

# Create Robyn Input Data File
robyn_csv = df[([date_var] + [dep_var] + paid_media_spends + paid_media_vars + context_vars)].to_csv(index=False).encode('utf-8')
data_input_filename = model_name + "_data.csv"



# Create Jinja data dict
robyn_input = {
    "config": {
        "model_name": model_name,
        "data_input_filename": data_input_filename
    },
    "header": {
        "dt_input": "dat",
        "dt_holidays": "dt_prophet_holidays",
        "date_var": date_var,
        "dep_var": dep_var,
        "dep_var_type": "revenue",
        "prophet_vars": ["trend", "season", "holiday"],
        "prophet_country": prophet_country,
        "window_start": window_start,
        "window_end": window_end,
        "adstock": "geometric",
    },
    "variables": {
        "context_vars": context_vars,
        "paid_media_spends": paid_media_spends,
        "paid_media_vars": paid_media_vars,
    },
}

# Create Robyn Input R File
env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"),lstrip_blocks=True)
template = env.get_template("robyn_input_template.jinja")
robyn_input_file = template.render(robyn_input)

st.header("Download Robyn Input")
robyn_input_filename = model_name + "_input.R"
st.download_button(label="Download Robyn Input", file_name=robyn_input_filename, data=robyn_input_file)

st.header("Download Robyn Data CSV")
st.download_button(
     label="Download data as CSV",
     data=robyn_csv,
     file_name=data_input_filename,
     mime='text/csv',
 )