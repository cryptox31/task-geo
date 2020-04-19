"""Source of dataset: https://data.humdata.org/
hdx : Humanitarian Data Exchange
acap: Organization providing the dataset
"""
import logging

import pandas as pd
from task_geo.data_sources.social_distancing.hdx_connector.hdx_connector import hdx_connector

logger = logging.getLogger(__name__)


def hdx_acap_connector():
    """Connects to HDX, and fetches acaps covid 19 government measures dataset

    Arguments:
        None

    Returns:
        pandas.DataFrame

    """
    absolute_download_path = hdx_connector('acaps-covid19-government-measures-dataset')
    xl = pd.ExcelFile(absolute_download_path)
    logger.debug(xl.sheet_names)
    return xl.parse('Database')
