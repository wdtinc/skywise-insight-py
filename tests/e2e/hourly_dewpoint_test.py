from tests.e2e import InsightE2ETest
from skywiseinsight import HourlyDewpoint


class HourlyDewpointTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        HourlyDewpoint.location(lat, lon)
        HourlyDewpoint.location(lat, lon, self.analysis_start_datetime, self.analysis_end_datetime)
        HourlyDewpoint.location(lat, lon, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
        HourlyDewpoint.location(lat, lon, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_by_asset(self):
        for asset in self.assets:
            HourlyDewpoint.asset(asset.id)
            HourlyDewpoint.asset(asset.id, self.analysis_start_datetime, self.analysis_end_datetime)
            HourlyDewpoint.asset(asset.id, self.analysis_and_forecast_start_datetime, self.analysis_and_forecast_end_datetime)
            HourlyDewpoint.asset(asset.id, self.forecast_start_datetime, self.forecast_end_datetime)

    def test_contours_by_asset(self):
        for asset in self.assets:
            HourlyDewpoint.contours(asset.id)
            HourlyDewpoint.contours(asset.id, self.analysis_start_datetime)
            HourlyDewpoint.contours(asset.id, self.forecast_start_datetime)
