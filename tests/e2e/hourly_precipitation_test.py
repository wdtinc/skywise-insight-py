from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyPrecipitation


class HourlyPrecipitationTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyPrecipitation.location(lat, lon)
        HourlyPrecipitation.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyPrecipitation.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyPrecipitation.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyPrecipitation.asset(asset.id)
            HourlyPrecipitation.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyPrecipitation.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyPrecipitation.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyPrecipitation.contours(asset.id)
            HourlyPrecipitation.contours(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyPrecipitation.contours(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyPrecipitation.contours(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)
