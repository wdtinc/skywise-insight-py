from tests.e2e import InsightE2ETest
from skywiseinsight import DailyPrecipitation


class DailyPrecipitationTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        DailyPrecipitation.location(lat, lon)
        DailyPrecipitation.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        DailyPrecipitation.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        DailyPrecipitation.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            DailyPrecipitation.asset(asset.id)
            DailyPrecipitation.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyPrecipitation.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyPrecipitation.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            DailyPrecipitation.contours(asset.id)
            DailyPrecipitation.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            DailyPrecipitation.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            DailyPrecipitation.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
