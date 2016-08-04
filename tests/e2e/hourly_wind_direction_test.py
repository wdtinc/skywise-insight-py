from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyWindDirection


class HourlyWindDirectionTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyWindDirection.location(lat, lon)
        HourlyWindDirection.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyWindDirection.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyWindDirection.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyWindDirection.asset(asset.id)
            HourlyWindDirection.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyWindDirection.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyWindDirection.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)
