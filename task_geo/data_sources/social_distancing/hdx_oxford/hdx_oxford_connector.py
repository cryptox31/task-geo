"""Source of dataset: https://data.humdata.org/
hdx : Humanitarian Data Exchange
oxford: Organization providing the dataset
"""
import pandas as pd

from task_geo.data_sources.social_distancing.hdx_connector.hdx_connector import hdx_connector


def hdx_oxford_connector():
    """Connects to HDX, and fetches Oxford COVID-19 Government Response Tracker Dataset

    Arguments: None

    Returns: pandas.DataFrame

    """
    # Get dataset from hdx_connector api
    download_absolute_path = hdx_connector('oxford-covid-19-government-response-tracker')
    return pd.read_csv(download_absolute_path)
