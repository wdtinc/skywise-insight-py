from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyDewpoint


class HourlyDewpointTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_dewpoint_location')
        self.adapter.register_uri('GET', '/hourly-dewpoint/35/-97',
                                  json=json)
        okc_dp = HourlyDewpoint.location(35, -97)
        self.assertEqual(len(okc_dp.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_dewpoint_asset')
        self.adapter.register_uri('GET', '/hourly-dewpoint/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_dp = HourlyDewpoint.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_dp.timeSeriesStatistics['mean'], 17.7)

    def test_contour(self):
        json = load_fixture('hourly_dewpoint_contour')
        self.adapter.register_uri('GET', '/hourly-dewpoint/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlyDewpoint.contours('fe68c33d-e718-4449-acae-351072ce7749')
