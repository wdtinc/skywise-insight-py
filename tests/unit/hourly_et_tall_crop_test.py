from tests import load_fixture
from tests.unit import InsightTest

from skywiseinsight import HourlyEtTallCrop


class HourlyEtTallCropTest(InsightTest):

    def test_location(self):
        json = load_fixture('hourly_et_tall_crop_location')
        self.adapter.register_uri('GET', '/hourly-evapotranspiration-tall-crop/35/-97',
                                  json=json)
        okc_et = HourlyEtTallCrop.location(35, -97)
        self.assertEqual(len(okc_et.series), 4)

    def test_asset(self):
        json = load_fixture('hourly_et_tall_crop_asset')
        self.adapter.register_uri('GET', '/hourly-evapotranspiration-tall-crop/fe68c33d-e718-4449-acae-351072ce7749',
                                  json=json)
        HourlyEtTallCrop.asset('fe68c33d-e718-4449-acae-351072ce7749')

    def test_contour(self):
        json = load_fixture('hourly_et_tall_crop_contour')
        self.adapter.register_uri('GET', '/hourly-evapotranspiration-tall-crop/fe68c33d-e718-4449-acae-351072ce7749/contours',
                                  json=json)
        HourlyEtTallCrop.contours('fe68c33d-e718-4449-acae-351072ce7749')
