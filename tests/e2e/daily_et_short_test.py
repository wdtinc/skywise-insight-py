from tests.e2e import InsightE2ETest
from skywiseinsight import DailyEtShortCrop


class DailyETShortTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailyEtShortCrop.location(lat, lon)
        DailyEtShortCrop.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailyEtShortCrop.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailyEtShortCrop.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailyEtShortCrop.asset(asset.id)
            DailyEtShortCrop.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyEtShortCrop.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyEtShortCrop.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailyEtShortCrop.contours(asset.id)
            DailyEtShortCrop.contours(asset.id, self.analysis_end_date)
            DailyEtShortCrop.contours(asset.id, self.analysis_and_forecast_end_date)
            DailyEtShortCrop.contours(asset.id, self.forecast_end_date)
