from unittest import TestCase

import pandas as pd

from task_geo.data_sources.social_distancing.hdx_acap.hdx_acap_formatter import hdx_acap_formatter
from task_geo.testing import check_dataset_format


class TestHdxApi(TestCase):

    def test_validate_formatter(self):
        """Validate Output of datasource."""
        # Setup
        raw = pd.read_csv('tests/fixtures/hdx_acap_fixture.csv')

        # Run
        data = hdx_acap_formatter(raw)

        # Check.
        check_dataset_format(data)
