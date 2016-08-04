from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyRelativeHumidity


class HourlyRelativeHumidityTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyRelativeHumidity.location(lat, lon)
        HourlyRelativeHumidity.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyRelativeHumidity.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyRelativeHumidity.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyRelativeHumidity.asset(asset.id)
            HourlyRelativeHumidity.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyRelativeHumidity.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyRelativeHumidity.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyRelativeHumidity.contours(asset.id)
            HourlyRelativeHumidity.contours(asset.id, self.analysis_start_datetime)
            HourlyRelativeHumidity.contours(asset.id, self.forecast_start_datetime)
