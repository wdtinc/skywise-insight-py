from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import DailySolarRadiation


class DailySolarRadiationTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('daily_solar_radiation_location')
        self.adapter.register_uri('GET', '/daily-solar-radiation/35/-97',
                                  json=json)
        okc_solar = DailySolarRadiation.location(35, -97)
        self.assertEqual(len(okc_solar.series), 3)

    def test_asset(self):
        json = load_fixture('daily_solar_radiation_asset')
        self.adapter.register_uri('GET', '/daily-solar-radiation/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_solar = DailySolarRadiation.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_solar.accumulationStatistics['mean'], 164.1)

    def test_contour(self):
        json = load_fixture('daily_solar_radiation_contour')
        self.adapter.register_uri('GET', '/daily-solar-radiation/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        DailySolarRadiation.contours('fe68c33d-e718-4449-acae-351072ce7749')
