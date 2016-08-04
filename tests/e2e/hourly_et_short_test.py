from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyEtShortCrop


class HourlyETShortTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyEtShortCrop.location(lat, lon)
        HourlyEtShortCrop.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        HourlyEtShortCrop.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        HourlyEtShortCrop.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyEtShortCrop.asset(asset.id)
            HourlyEtShortCrop.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            HourlyEtShortCrop.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            HourlyEtShortCrop.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyEtShortCrop.contours(asset.id)
            HourlyEtShortCrop.contours(asset.id, self.analysis_end_date)
            HourlyEtShortCrop.contours(asset.id, self.analysis_and_forecast_end_date)
            HourlyEtShortCrop.contours(asset.id, self.forecast_end_date)
