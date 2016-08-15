from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlySolarRadiation


class HourlySolarRadiationTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_solar_radiation_location')
        self.adapter.register_uri('GET', '/hourly-solar-radiation/35/-97',
                                  json=json)
        okc_solar = HourlySolarRadiation.location(35, -97)
        self.assertEqual(len(okc_solar.series), 3)

    def test_asset(self):
        json = load_fixture('hourly_solar_radiation_asset')
        self.adapter.register_uri('GET', '/hourly-solar-radiation/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        HourlySolarRadiation.asset('fe68c33d-e718-4449-acae-351072ce7749')

    def test_contour(self):
        json = load_fixture('hourly_solar_radiation_contour')
        self.adapter.register_uri('GET', '/hourly-solar-radiation/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlySolarRadiation.contours('fe68c33d-e718-4449-acae-351072ce7749')
