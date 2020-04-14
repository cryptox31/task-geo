import logging
import country_converter as coco

logger = logging.getLogger(__name__)


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
    column_order = ['id', 'country', 'region', 'country_iso2', 'category', 'measure',
                    'targeted_pop_group', 'comments', 'non_compliance', 'date_implemented',
                    'source', 'source_type', 'entry_date', 'link']
    data['country_iso2'] = data.apply(lambda x: coco.convert(names=x['iso'], to="ISO2"),
                                      axis=1)
    data = data[column_order]
    return data


def hdx_oxfd_formatter(raw, date_from, date_to, country_iso2):
    """Formats raw pandas.DataFrame
    - Drops columns ending with _note
    - Orders Columns

    Arguments:
        raw (pandas.DataFrame): from hdx_acap_connector

    Returns: pandas.DataFrame

    """
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]
    drop_columns = [column for column in data.columns if column.find("_note") > -1]
    data = data.drop(drop_columns, axis=1)
    data['country_iso2'] = data.apply(lambda x: coco.convert(names=x['countrycode'], to="ISO2"),
                                      axis=1)
    data.rename(columns={"countryname": "country"}, inplace=True)
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
    data = data[column_order]
    return data
