from unittest import TestCase, skip

from task_geo.data_sources.social_distancing.hdx_oxford import hdx_oxford_connector
from task_geo.data_sources.social_distancing.hdx_oxford.hdx_oxford_formatter import (
    hdx_oxford_formatter)
from task_geo.testing import check_dataset_format


@skip
class TestHdxApi(TestCase):

    def test_validate_format_raw_output(self):
        """Validate datasource output.

        This tests is skipped intentionally on the main suite due to it taking to long.
        Is kept for developing porpouses.
        """
        # Setup
        raw = hdx_oxford_connector()

        # Run
        data = hdx_oxford_formatter(raw)

        # Check.
        check_dataset_format(data)
