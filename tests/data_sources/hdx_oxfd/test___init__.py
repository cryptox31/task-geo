from datetime import datetime
from unittest import TestCase, skip

from task_geo.data_sources.hdx_oxfd.hdx_oxfd_connector import hdx_oxfd_connector
from task_geo.data_sources.hdx_oxfd.hdx_oxfd_formatter import hdx_oxfd_formatter
from task_geo.testing import check_dataset_format


class TestHdxApi(TestCase):

    @skip
    def test_validate_format_raw_output(self):
        """Validate datasource output.

        This tests is skipped intentionally on the main suite due to it taking to long.
        Is kept for developing porpouses.
        """
        # Setup
        start_date = datetime(2020, 3, 1).date().isoformat()
        end_date = datetime(2020, 3, 15).date().isoformat()
        countries = ['US']
        raw = hdx_oxfd_connector()

        # Run
        data = hdx_oxfd_formatter(raw, start_date, end_date, countries)

        # Check.
        check_dataset_format(data)
