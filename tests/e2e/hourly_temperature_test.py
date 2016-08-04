from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyTemperature


class HourlyTemperatureTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyTemperature.location(lat, lon)
        HourlyTemperature.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyTemperature.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyTemperature.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyTemperature.asset(asset.id)
            HourlyTemperature.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyTemperature.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyTemperature.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyTemperature.contours(asset.id)
            HourlyTemperature.contours(asset.id, self.analysis_start_datetime)
            HourlyTemperature.contours(asset.id, self.forecast_start_datetime)
