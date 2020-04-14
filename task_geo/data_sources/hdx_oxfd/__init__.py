from task_geo.data_sources.hdx.hdx_connector import hdx_acap_connector, hdx_oxfd_connector
from task_geo.data_sources.hdx.hdx_formatter import hdx_acap_formatter, hdx_oxfd_formatter


def hdx_acap():
    """Retrieves formatted Government Measures Dataset from HDX DataSource
    Example:
    >>> hdx_acap()

    Returns: pandas.DataFrame
    """
    raw = hdx_acap_connector()
    return hdx_acap_formatter(raw)


def hdx_oxfd(from_date, to_date, country_iso2):
    """Retrieves formatted Oxford COVID-19 Government Response Tracker Dataset from HDX DataSource
    Example:
    >>> hdx_oxfd()

    Returns: pandas.DataFrame
    """
    raw = hdx_oxfd_connector()
    return hdx_oxfd_formatter(raw)


def main():
    hdx_oxfd()


if __name__ == '__main__':
    main()
