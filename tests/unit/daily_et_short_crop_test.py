from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import DailyEtShortCrop


class DailyEtShortCropTest(InsightTest):

    def test_location(self):
        json = load_fixture('daily_et_short_crop_location')
        self.adapter.register_uri('GET', '/daily-evapotranspiration-short-crop/35/-97',
                                  json=json)
        okc_et = DailyEtShortCrop.location(35, -97)
        self.assertEqual(len(okc_et.series), 3)

    def test_asset(self):
        json = load_fixture('daily_et_short_crop_asset')
        self.adapter.register_uri('GET', '/daily-evapotranspiration-short-crop/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        DailyEtShortCrop.asset('fe68c33d-e718-4449-acae-351072ce7749')

    def test_contour(self):
        json = load_fixture('daily_et_short_crop_contour')
        self.adapter.register_uri('GET', '/daily-evapotranspiration-short-crop/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        DailyEtShortCrop.contours('fe68c33d-e718-4449-acae-351072ce7749')
