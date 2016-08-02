from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import DailyPrecipitation


class DailyPrecipitationTest(InsightTest):

    def test_location(self):
        json = load_fixture('daily_precipitation_location')
        self.adapter.register_uri('GET', '/daily-precipitation/35/-97',
                                  json=json)
        okc_precip = DailyPrecipitation.location(35, -97)
        self.assertEqual(len(okc_precip.series), 3)

    def test_asset(self):
        json = load_fixture('daily_precipitation_asset')
        self.adapter.register_uri('GET', '/daily-precipitation/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_precip = DailyPrecipitation.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_precip.accumulationStatistics['mean'], 21.5)

    def test_contour(self):
        json = load_fixture('daily_precipitation_contour')
        self.adapter.register_uri('GET', '/daily-precipitation/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        DailyPrecipitation.contours('fe68c33d-e718-4449-acae-351072ce7749')
