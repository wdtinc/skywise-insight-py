from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyWindSpeed


class HourlyWindSpeedTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_wind_speed_location')
        self.adapter.register_uri('GET', '/hourly-wind-speed/35/-97',
                                  json=json)
        okc_ws = HourlyWindSpeed.location(35, -97)
        self.assertEqual(len(okc_ws.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_wind_speed_asset')
        self.adapter.register_uri('GET', '/hourly-wind-speed/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_ws = HourlyWindSpeed.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_ws.timeSeriesStatistics['mean'], 15.0)

    def test_contour(self):
        json = load_fixture('hourly_wind_speed_contour')
        self.adapter.register_uri('GET', '/hourly-wind-speed/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlyWindSpeed.contours('fe68c33d-e718-4449-acae-351072ce7749')
