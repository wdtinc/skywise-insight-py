from tests.e2e import InsightE2ETest
from skywiseinsight import HourlySolarRadiation


class HourlySolarRadiationTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlySolarRadiation.location(lat, lon)
        HourlySolarRadiation.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlySolarRadiation.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlySolarRadiation.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlySolarRadiation.asset(asset.id)
            HourlySolarRadiation.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlySolarRadiation.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlySolarRadiation.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlySolarRadiation.contours(asset.id)
            HourlySolarRadiation.contours(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlySolarRadiation.contours(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlySolarRadiation.contours(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)
