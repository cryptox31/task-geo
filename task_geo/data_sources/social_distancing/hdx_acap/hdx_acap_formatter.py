from task_geo.common.country_codes import iso3_to_iso2


def hdx_acap_formatter(raw):
    """Formats raw pandas.DataFrame
    - Drops 'pcode', 'admin_level_name', 'alternative source' columns
    - Orders Columns

    Arguments:
        raw (pandas.DataFrame): from hdx_acap_connector

    Returns: pandas.DataFrame

    """
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]
    data = data.drop(['pcode', 'admin_level_name', 'alternative source'], axis=1)
    column_order = ['id', 'country', 'country_iso', 'log_type', 'category', 'measure',
                    'targeted_pop_group', 'comments', 'non_compliance', 'date_implemented',
                    'source', 'source_type', 'entry_date', 'link']
    # Convert ISO3 Country code to ISO2 Country Code
    data['country_iso'] = data.iso.apply(iso3_to_iso2)
    return data[column_order]
