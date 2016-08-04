from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyEtTallCrop


class HourlyETTallTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyEtTallCrop.location(lat, lon)
        HourlyEtTallCrop.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        HourlyEtTallCrop.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        HourlyEtTallCrop.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyEtTallCrop.asset(asset.id)
            HourlyEtTallCrop.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            HourlyEtTallCrop.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            HourlyEtTallCrop.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyEtTallCrop.contours(asset.id)
            HourlyEtTallCrop.contours(asset.id, self.analysis_end_date)
            HourlyEtTallCrop.contours(asset.id, self.analysis_and_forecast_end_date)
            HourlyEtTallCrop.contours(asset.id, self.forecast_end_date)
