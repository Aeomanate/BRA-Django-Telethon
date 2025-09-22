from unittest.mock import patch

from django.test import TestCase

from django.test import TestCase
from .exchange_rates.rates import get_usd_to_uah_rate



class ThirdPartyTest(TestCase):
    @patch('requests.get')
    def test_get_exchange_rate(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [
            {"cc": "EUR", "rate": 40.0},
            {"cc": "USD", "rate": 36.57},
            {"cc": "GBP", "rate": 45.0},
        ]

        rate = get_usd_to_uah_rate()
        self.assertAlmostEqual(rate, 36.57, places=2)
        mock_get.assert_called_once_with(
            "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json",
            timeout=5
        )

