import re


def generate_var_dict(
    df, column_tags=[r"SPEND", r"PRICE", r"SALES_VALUE", r"IMPRESSIONS", r"TRP"]
):
    """Create dictionary of variable types, e.g. Spend, Sales, TV, etc. using column name regexes"""
    var_dict = {}
    columns = df.columns.to_list()
    regex_list = [re.compile(i) for i in column_tags]
    regex_dict = dict(zip(column_tags, regex_list))

    for i in column_tags:
        var_dict[i] = []
        for j in columns:
            if regex_dict[i].search(j) is None:
                pass
            else:
                var_dict[i].append(j)

    return var_dict
