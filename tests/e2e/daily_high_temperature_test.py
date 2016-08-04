from tests.e2e import InsightE2ETest
from skywiseinsight import DailyHighTemperature


class DailyHighTemperatureTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailyHighTemperature.location(lat, lon)
        DailyHighTemperature.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailyHighTemperature.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailyHighTemperature.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailyHighTemperature.asset(asset.id)
            DailyHighTemperature.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyHighTemperature.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyHighTemperature.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailyHighTemperature.contours(asset.id)
            DailyHighTemperature.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyHighTemperature.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyHighTemperature.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
