from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyTemperature


class HourlyTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_temperature_location')
        self.adapter.register_uri('GET', '/hourly-temperature/35/-97',
                                  json=json)
        okc_temp = HourlyTemperature.location(35, -97)
        self.assertEqual(len(okc_temp.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_temperature_asset')
        self.adapter.register_uri('GET', '/hourly-temperature/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_temp = HourlyTemperature.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_temp.timeSeriesStatistics['mean'], 33.1)

    def test_contour(self):
        json = load_fixture('hourly_temperature_contour')
        self.adapter.register_uri('GET', '/hourly-temperature/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlyTemperature.contours('fe68c33d-e718-4449-acae-351072ce7749')
