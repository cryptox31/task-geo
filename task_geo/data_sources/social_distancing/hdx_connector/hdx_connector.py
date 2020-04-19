"""
Source of dataset: https://data.humdata.org/
hdx : Humanitarian Data Exchange
"""
import logging

import pandas as pd
from hdx.data.dataset import Dataset
from hdx.data.resource import Resource
from hdx.hdx_configuration import Configuration
from hdx.utilities.easy_logging import setup_logging

logger = logging.getLogger(__name__)


def hdx_connector(data_source_name):
    """Connects to HDX, and fetches data_source_name datasets

    Arguments:
        data_source_name(str): Name of the dataset on HDX

    Returns:
        path(str): Path at which the dataset is downloaded

    """
    setup_logging()

    Configuration.create(hdx_site='prod', user_agent='CoronaWhy', hdx_read_only=True)

    dataset = Dataset.read_from_hdx(data_source_name)
    logger.debug("Dataset Fetched from: %s", dataset.get_hdx_url())
    logger.debug('Expected Update Frequency: %s', dataset.get_expected_update_frequency())
    resources = dataset.get_resources()
    logger.debug('Description: %s', resources[0]['description'])
    logger.debug('Last Modified: %s, Revision Last Updated: %s', resources[0]['last_modified'],
                 resources[0]['revision_last_updated'])
    logger.debug('Size: %sMb', resources[0]['size'] / (1024 ** 2))
    logger.debug('Dataset Url: %s', resources[0]['url'])
    logger.debug('Tags: %s', dataset.get_tags())
    resource = Resource.read_from_hdx(resources[0]['id'])
    url, absolute_path = resource.download('./')
    logger.debug('Downloaded dataset at path: %s', absolute_path)
    return absolute_path
