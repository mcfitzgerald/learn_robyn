robyn_input = {
    "header": {
        "dt_input": "dat",
        "dt_holidays": "dt_prophet_holidays",
        "date_var": "DATE",
        "dep_var": "revenue",
        "dep_var_type": "revenue",
        "prophet_vars": ["trend", "season", "holiday"],
        "prophet_country": "MX",
    },
    "variables": {
        "context_vars": [
            "TP_LUMINOUS_AVG_PRICE",
            "TP_NATURAL_EXTRACTS_AVG_PRICE",
            "TP_TOTAL_AVG_PRICE",
            "TP_COLGATE_NOAD_AVG_PRICE",
        ],
        "paid_media_spends": [
            "DV_LUMINOUS_SPEND",
            "FB_LUMINOUS_SPEND",
            "GL_LUMINOUS_SPEND",
            "DV_MW_TOTAL_12_SPEND",
        ],
    },
}
