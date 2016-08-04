from tests.e2e import InsightE2ETest
from skywiseinsight import DailyLowTemperature


class DailyLowTemperatureTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailyLowTemperature.location(lat, lon)
        DailyLowTemperature.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailyLowTemperature.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailyLowTemperature.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailyLowTemperature.asset(asset.id)
            DailyLowTemperature.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyLowTemperature.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyLowTemperature.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailyLowTemperature.contours(asset.id)
            DailyLowTemperature.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyLowTemperature.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyLowTemperature.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
