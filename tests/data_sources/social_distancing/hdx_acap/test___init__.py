from unittest import TestCase

from task_geo.data_sources.social_distancing.hdx_acap.hdx_acap_connector import hdx_acap_connector
from task_geo.data_sources.social_distancing.hdx_acap.hdx_acap_formatter import hdx_acap_formatter
from task_geo.testing import check_dataset_format


class TestHdxApi(TestCase):

    def test_validate_format_raw_output(self):
        """Validate datasource output.

        This tests is skipped intentionally on the main suite due to it taking to long.
        Is kept for developing porpouses.
        """
        # Setup
        raw = hdx_acap_connector()

        # Run
        data = hdx_acap_formatter(raw)

        # Check.
        check_dataset_format(data)
