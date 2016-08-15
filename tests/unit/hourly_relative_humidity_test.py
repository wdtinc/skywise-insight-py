from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyRelativeHumidity


class HourlyRelativeHumidityTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_relative_humidity_location')
        self.adapter.register_uri('GET', '/hourly-relative-humidity/35/-97',
                                  json=json)
        okc_rh = HourlyRelativeHumidity.location(35, -97)
        self.assertEqual(len(okc_rh.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_relative_humidity_asset')
        self.adapter.register_uri('GET', '/hourly-relative-humidity/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_rh = HourlyRelativeHumidity.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_rh.timeSeriesStatistics['mean'], 96.2)

    def test_contour(self):
        json = load_fixture('hourly_relative_humidity_contour')
        self.adapter.register_uri('GET', '/hourly-relative-humidity/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlyRelativeHumidity.contours('fe68c33d-e718-4449-acae-351072ce7749')
