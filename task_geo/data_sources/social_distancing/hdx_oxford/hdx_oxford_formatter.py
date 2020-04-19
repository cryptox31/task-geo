from task_geo.common.country_codes import iso3_to_iso2


def hdx_oxford_formatter(raw):
    """Formats raw pandas.DataFrame
    - Drops columns ending with _note
    - Orders Columns
    - Converts ISO3 to ISO2 country codes

    Arguments:
        raw (pandas.DataFrame): from hdx_acap_connector

    Returns: pandas.DataFrame

    """
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]
    # Remove columns with notes
    drop_columns = [column for column in data.columns if column.find("_note") > -1]
    data = data.drop(drop_columns, axis=1)
    # Convert ISO3 Country code to ISO2 Country Code
    data['country_iso2'] = data.countrycode.apply(iso3_to_iso2)
    # Rename Column
    data.rename(columns={"countryname": "country"}, inplace=True)
    # Reorder Columns
    column_order = ['country', 'country_iso2', 'date', 's1_school closing',
                    's1_isgeneral', 's2_workplace closing', 's2_isgeneral',
                    's3_cancel public events', 's3_isgeneral', 's4_close public transport',
                    's4_isgeneral', 's5_public information campaigns', 's5_isgeneral',
                    's6_restrictions on internal movement', 's6_isgeneral',
                    's7_international travel controls', 's8_fiscal measures',
                    's9_monetary measures', 's10_emergency investment in health care',
                    's11_investment in vaccines', 's12_testing framework',
                    's13_contact tracing', 'confirmedcases', 'confirmeddeaths',
                    'stringencyindex', 'stringencyindexfordisplay']
    return data[column_order]
