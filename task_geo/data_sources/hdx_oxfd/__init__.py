from task_geo.data_sources.hdx_oxfd.hdx_oxfd_connector import hdx_oxfd_connector
from task_geo.data_sources.hdx_oxfd.hdx_oxfd_formatter import hdx_oxfd_formatter


def hdx_oxfd(start_date=None, end_date=None, country_iso2=None):
    """Retrieves formatted Oxford COVID-19 Government Response Tracker Dataset from HDX DataSource
    Examples:
    >>> df = hdx_oxfd("2020-03-01", "2020-03-30", ["US"])
    >>> df1 = hdx_oxfd("2020-04-01", None, None)
    >>> df2 = hdx_oxfd("2020-04-01", None, ["US"])

    Returns: pandas.DataFrame
    """
    raw, metadata, keywords = hdx_oxfd_connector()
    df = hdx_oxfd_formatter(raw, start_date, end_date, country_iso2)
    return df
