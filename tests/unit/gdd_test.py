from tests import load_fixture
from tests.unit import InsightTest
from skywiseinsight import Gdd


class GddTest(InsightTest):

    def test_location(self):
        json = load_fixture('gdd_location')
        self.adapter.register_uri('GET', '/growing-degree-days/35/-97',
                                  json=json)
        okc_gdd = Gdd.location(35, -97)
        self.assertEqual(len(okc_gdd.series), 3)

    def test_asset(self):
        json = load_fixture('gdd_asset')
        self.adapter.register_uri('GET', '/growing-degree-days/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        asset_gdd = Gdd.asset('fe68c33d-e718-4449-acae-351072ce7749')
        self.assertEqual(asset_gdd.accumulationStatistics['mean'], 15.6)

    def test_contour(self):
        json = load_fixture('gdd_contour')
        self.adapter.register_uri('GET', '/growing-degree-days/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        Gdd.contours('fe68c33d-e718-4449-acae-351072ce7749')
