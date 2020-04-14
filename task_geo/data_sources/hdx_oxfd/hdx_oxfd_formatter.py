import logging
from task_geo.common.country_codes import iso3_to_iso2, iso2_to_iso3
from datetime import datetime
import pandas as pd

logger = logging.getLogger(__name__)


def hdx_oxfd_formatter(raw, start_date, end_date, country_iso2):
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
    # Filter by country(s)
    iso3 = []
    for c in country_iso2:
        iso3.append(iso2_to_iso3(c))
    data = filter_by_country(data, iso3)
    # Filter by date
    data = filter_with_date(data, start_date, end_date)
    # Convert ISO3 Country code to ISO2 Country Code
    if len(data) > 0:
        data['country_iso2'] = data.apply(lambda x: iso3_to_iso2(x['countrycode']), axis=1)
    else:
        return data

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
    data = data[column_order]
    return data


def filter_with_date(data, start_date=None, end_date=None):
    """Filter dataframe by start_date and end_date

    Arguments:
        data (): pandas.DataFrame
        start_date (): date iso format %Y-%m-%d
        end_date (): date iso format %Y-%m-%d

    Returns:
        pandas.DataFrame
    """
    if start_date is None:
        return
    if end_date is None:
        end_date = datetime.now().date().isoformat()  # ISO Format : 2020-04-14 : %Y %m %d
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    # Convert data['date'] to date format
    data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')
    # Set date filter
    date_filter = (data['date'] >= start_date) & (data['date'] <= end_date)
    # Filter dataframe by date
    return data[date_filter]


def filter_by_country(data, country_iso3):
    """Filters dataframe by country_iso3 code

    Arguments:
        data : pandas.DataFrame
        country_iso3 : str

    Returns:
        pandas.DataFrame
    """
    if country_iso3 is None:
        return
    else:
        return data[data['countrycode'].isin(country_iso3)]
