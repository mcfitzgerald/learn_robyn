import pandas as pd
from functools import reduce
from dateutil.relativedelta import *

def nearest_monday(pandas_timestamp, format='%Y-%m-%d'):
    # cast to python datetime
    stamp = pandas_timestamp.to_pydatetime()

    # cray cray datetime math
    last_monday = stamp + relativedelta(weekday=MO(-1))
    next_monday = stamp + relativedelta(weekday=MO(1))
    diff_last_monday = abs((stamp - last_monday).days)
    diff_next_monday = abs((stamp - next_monday).days)

    if diff_last_monday == diff_next_monday:
        return last_monday.strftime(format)
    elif diff_last_monday < diff_next_monday:
        return last_monday.strftime(format)
    else:
        return next_monday.strftime(format)


def brand_campaign_agg(df,channel_label,campaign_id = 'Brand', index_col = 'Date', variable_cols = ['Spend','Impressions','Clicks']):

    # Fix Dates
    formatted_date = pd.to_datetime(df['Date'])
    formatted_date = formatted_date.apply(lambda x: nearest_monday(x))
    df['Date'] = formatted_date

    # Format campaign names (usually brand name)
    df[campaign_id] = df[campaign_id].str.upper()
    df[campaign_id] = df[campaign_id].str.replace(' ','_')

    # Create unique columns names for output
    all_campaigns = df[campaign_id].unique().tolist()
    campaign_var_labels = [[(channel_label + '_' + i + ('_' + j)).upper() for i in variable_cols] for j in all_campaigns]

    # Create list of datframes for each campaign
    campaign_masks = [df[campaign_id] == i for i in all_campaigns]
    single_campaign_dfs = [df[i] for i in campaign_masks]
    
    # Select only columns of interest
    clean_single_campaign_dfs = [i[([index_col] + variable_cols)] for i in single_campaign_dfs]

    # Group variables by week
    grouped_by_date = []
    for i in clean_single_campaign_dfs:
        grouped = i.groupby(by=index_col).sum().reset_index()
        grouped_by_date.append(grouped)
    
    # Rename columns
    renamed_cols = []
    for i,j in enumerate(grouped_by_date):
        new = j.rename(columns=dict(zip(variable_cols,campaign_var_labels[i])))
        renamed_cols.append(new)

    # Merge the separate dataframes
    merged = reduce(lambda x, y: pd.merge(x, y, on = 'Date',how = 'outer'), renamed_cols)
    merged.fillna(0.0,inplace=True)

    return merged