from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyWindSpeed


class HourlyWindSpeedTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyWindSpeed.location(lat, lon)
        HourlyWindSpeed.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyWindSpeed.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyWindSpeed.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyWindSpeed.asset(asset.id)
            HourlyWindSpeed.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyWindSpeed.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyWindSpeed.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyWindSpeed.contours(asset.id)
            HourlyWindSpeed.contours(asset.id, self.analysis_start_datetime)
            HourlyWindSpeed.contours(asset.id, self.forecast_start_datetime)
