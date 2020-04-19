from unittest import TestCase

import pandas as pd

from task_geo.data_sources.social_distancing.hdx_oxford.hdx_oxford_formatter import (
    hdx_oxford_formatter)
from task_geo.testing import check_dataset_format


class TestHdxApi(TestCase):

    def test_validate_formatter(self):
        """Validate datasource output."""
        # Setup
        raw = pd.read_csv('tests/fixtures/hdx_oxfd_fixture.csv')

        # Run
        data = hdx_oxford_formatter(raw)

        # Check.
        check_dataset_format(data)
