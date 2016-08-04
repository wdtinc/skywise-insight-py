from tests.e2e import InsightE2ETest
from skywiseinsight import Gdd


class GddTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        Gdd.location(lat, lon)
        Gdd.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        Gdd.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        Gdd.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            Gdd.asset(asset.id)
            Gdd.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            Gdd.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Gdd.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            Gdd.contours(asset.id)
            Gdd.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            Gdd.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Gdd.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
