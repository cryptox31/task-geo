"""
Source of dataset: https://data.humdata.org/
hdx : Humanitarian Data Exchange
acap: Organization providing the dataset
"""
import logging

import pandas as pd
from hdx.data.dataset import Dataset
from hdx.data.resource import Resource
from hdx.hdx_configuration import Configuration
from hdx.utilities.easy_logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

Configuration.create(hdx_site='prod', user_agent='CoronaWhy', hdx_read_only=True)


def hdx_acap_connector():
    """Connects to HDX, and fetches acaps covid 19 government measures dataset
    Arguments: None

    Returns: pandas.DataFrame

    """
    dataset = Dataset.read_from_hdx('acaps-covid19-government-measures-dataset')
    logger.info("Dataset Fetched from: %s", dataset.get_hdx_url())
    logger.info('Expected Update Frequency: %s', dataset.get_expected_update_frequency())
    resources = dataset.get_resources()
    logger.info('Description: %s', resources[0]['description'])
    logger.info('Last Modified: %s, Revision Last Updated: %s', resources[0]['last_modified'],
                resources[0]['revision_last_updated'])
    logger.info('Size: %sMb', resources[0]['size'] / (1024 ** 2))
    logger.info('Dataset Url: %s', resources[0]['url'])
    tags = dataset.get_tags()
    logger.info('Tags: %s', tags)
    resource = Resource.read_from_hdx(resources[0]['id'])
    url, absolute_path = resource.download('./')
    logger.info('Downloaded dataset at path: %s', absolute_path)
    xl = pd.ExcelFile(absolute_path)
    logger.info(xl.sheet_names)
    df = xl.parse('Database')
    return df, resources[0], tags
