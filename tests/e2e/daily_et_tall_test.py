from tests.e2e import InsightE2ETest
from skywiseinsight import DailyEtTallCrop


class DailyETTallTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailyEtTallCrop.location(lat, lon)
        DailyEtTallCrop.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailyEtTallCrop.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailyEtTallCrop.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailyEtTallCrop.asset(asset.id)
            DailyEtTallCrop.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyEtTallCrop.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyEtTallCrop.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailyEtTallCrop.contours(asset.id)
            DailyEtTallCrop.contours(asset.id, self.analysis_start_date)
            DailyEtTallCrop.contours(asset.id, self.analysis_and_forecast_end_date)
            DailyEtTallCrop.contours(asset.id, self.forecast_end_date)
