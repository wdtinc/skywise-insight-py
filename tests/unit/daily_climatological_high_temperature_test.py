from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import DailyClimatologicalHighTemperature


class DailyClimatologicalHighTemperatureTest(InsightTest):

    def test_location(self):
        json = load_fixture('daily_climatological_high_temperature_location')
        self.adapter.register_uri('GET', '/climatology/daily-high-temperature/35/-97',
                                  json=json)
        okc_precip = DailyClimatologicalHighTemperature.location(35, -97)
        self.assertEqual(len(okc_precip.series), 3)

    def test_asset(self):
        json = load_fixture('daily_climatological_high_temperature_asset')
        self.adapter.register_uri('GET', '/climatology/daily-high-temperature/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_precip = DailyClimatologicalHighTemperature.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_precip.timeSeriesStatistics['mean'], 34.3)

    def test_contour(self):
        json = load_fixture('daily_climatological_high_temperature_contour')
        self.adapter.register_uri('GET', '/climatology/daily-high-temperature/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        DailyClimatologicalHighTemperature.contours('fe68c33d-e718-4449-acae-351072ce7749')
