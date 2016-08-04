from tests.e2e import InsightE2ETest
from skywiseinsight.hdd import Hdd


class HddTest(InsightE2ETest):

    def test_by_location(self):
        lat, lon = self.location[0], self.location[1]
        Hdd.location(lat, lon)
        Hdd.location(lat, lon, self.analysis_start_date, self.analysis_end_date)
        Hdd.location(lat, lon, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
        Hdd.location(lat, lon, self.forecast_start_date, self.forecast_end_date)

    def test_by_asset(self):
        for asset in self.assets:
            Hdd.asset(asset.id)
            Hdd.asset(asset.id, self.analysis_start_date, self.analysis_end_date)
            Hdd.asset(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Hdd.asset(asset.id, self.forecast_start_date, self.forecast_end_date)

    def test_contours_by_asset(self):
        for asset in self.assets:
            Hdd.contours(asset.id)
            Hdd.contours(asset.id, self.analysis_start_date, self.analysis_end_date)
            Hdd.contours(asset.id, self.analysis_and_forecast_start_date, self.analysis_and_forecast_end_date)
            Hdd.contours(asset.id, self.forecast_start_date, self.forecast_end_date)
