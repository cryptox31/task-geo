import logging

from task_geo.common.country_codes import iso3_to_iso2

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
    # Convert ISO3 Country code to ISO2 Country Code
    if len(data) > 0:
        data['country_iso2'] = data.apply(lambda x: iso3_to_iso2(x['iso']), axis=1)
    else:
        return data
    data = data[column_order]
    return data
