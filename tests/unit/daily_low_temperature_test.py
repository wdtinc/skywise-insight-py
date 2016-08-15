from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import DailyLowTemperature


class DailyLowTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('daily_low_temperature_location')
        self.adapter.register_uri('GET', '/daily-low-temperature/35/-97',
                                  json=json)
        okc_low_temp = DailyLowTemperature.location(35, -97)
        self.assertEqual(len(okc_low_temp.series), 3)

    def test_asset(self):
        json = load_fixture('daily_low_temperature_asset')
        self.adapter.register_uri('GET', '/daily-low-temperature/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_hi_temp = DailyLowTemperature.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_hi_temp.timeSeriesStatistics['mean'], 34.3)

    def test_contour(self):
        json = load_fixture('daily_low_temperature_contour')
        self.adapter.register_uri('GET', '/daily-low-temperature/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        DailyLowTemperature.contours('fe68c33d-e718-4449-acae-351072ce7749')
