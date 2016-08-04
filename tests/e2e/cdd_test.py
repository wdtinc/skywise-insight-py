from tests.e2e import InsightE2ETest
from skywiseinsight import Cdd


class CddTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        Cdd.location(lat, lon)
        Cdd.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        Cdd.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        Cdd.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            Cdd.asset(asset.id)
            Cdd.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            Cdd.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Cdd.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            Cdd.contours(asset.id)
            Cdd.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            Cdd.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Cdd.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
