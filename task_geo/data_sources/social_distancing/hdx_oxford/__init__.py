from task_geo.data_sources.social_distancing.hdx_oxford.hdx_oxford_connector import (
    hdx_oxford_connector)
from task_geo.data_sources.social_distancing.hdx_oxford.hdx_oxford_formatter import (
    hdx_oxford_formatter)


def hdx_oxford():
    """Retrieves formatted Oxford COVID-19 Government Response Tracker Dataset from HDX DataSource
    Examples:
    >>> from task_geo.data_sources import get_data_source
    >>> hdx_acap = get_data_source('hdx_oxford')
    >>> df = hdx_oxford()

    Returns: pandas.DataFrame
    """
    raw = hdx_oxford_connector()
    return hdx_oxford_formatter(raw)
