from tests.e2e import InsightE2ETest
from skywise.insight import DailySolarRadiation


class DailySolarRadiationTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailySolarRadiation.location(lat, lon)
        DailySolarRadiation.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailySolarRadiation.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailySolarRadiation.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailySolarRadiation.asset(asset.id)
            DailySolarRadiation.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailySolarRadiation.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailySolarRadiation.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailySolarRadiation.contours(asset.id)
            DailySolarRadiation.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailySolarRadiation.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailySolarRadiation.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
