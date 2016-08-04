"""
WARNING: Running these tests against your Insight account will remove ALL ASSETS.
"""
from geojson import MultiPolygon, Polygon

from skywiseinsight.asset import Asset
from tests.e2e import InsightE2ETest


class AssetsE2ETest(InsightE2ETest):

    def setUp(self):
        assets = Asset.find()
        for asset in assets:
            asset.destroy()

    def tearDown(self):
        assets = Asset.find()
        for asset in assets:
            asset.destroy()

    def test_asset_creation(self):
        asset = Asset()
        asset.description = 'Arthur Farm'
        asset.shape = MultiPolygon([
            ([(-97.194156646728, 35.667442627764),
              (-97.191281318664, 35.668349114403),
              (-97.185573577880, 35.672497902647),
              (-97.185616493225, 35.676402447539),
              (-97.194499969482, 35.671591463121),
              (-97.194156646728, 35.667442627764)])
        ])
        self.assertEqual(len(asset.geometries), 1)
        asset.save()
        self.assertIsNotNone(asset.id)

        qasset = Asset.find(asset.id)
        self.assertEqual(qasset.id, asset.id)
        self.assertEqual(qasset.description, asset.description)
        self.assertEqual(len(qasset.geometries), len(asset.geometries))

    def test_polygon(self):
        asset = Asset()
        asset.description = 'TLC Garden Centers - Memorial'
        asset.shape = Polygon([
            [(-97.51611828804016, 35.612816541250574),
             (-97.5161075592041, 35.6092752385082),
             (-97.51530289649963, 35.60931885156433),
             (-97.51426219940186, 35.61288631904003),
             (-97.51611828804016, 35.612816541250574)]
        ])
        asset.save()
        self.assertIsNotNone(asset.id)
        self.assertEqual(len(asset.geometries), 1)

    def test_asset_update(self):
        asset = Asset()
        asset.description = 'Arthur Farm - NW Asset'
        asset.shape = MultiPolygon([
            ([(-97.184243202209, 35.681457154948),
              (-97.182183265686, 35.685117260431),
              (-97.176904678344, 35.687801231068),
              (-97.176904678344, 35.681352578039),
              (-97.184243202209, 35.681457154948)])
        ])
        asset.save()

        qasset = Asset.find(asset.id)
        new_descr = 'Arthur Farm - Northwest Asset'
        qasset.description = new_descr
        qasset.save()

        qasset = Asset.find(asset.id)
        self.assertEqual(qasset.description, new_descr)
        self.assertEqual(len(qasset.geometries), len(asset.geometries))

    def test_asset_removal(self):
        asset = Asset()
        asset.description = 'Arthur Farm - NW Asset'
        asset.shape = MultiPolygon([
            ([(-97.184243202209, 35.681457154948),
              (-97.182183265686, 35.685117260431),
              (-97.176904678344, 35.687801231068),
              (-97.176904678344, 35.681352578039),
              (-97.184243202209, 35.681457154948)])
        ])
        asset.save()

        self.assertIsNotNone(asset.id)
        asset_id = asset.id
        asset.destroy()

        try:
            Asset.find(asset_id)
            self.assertTrue(False, 'When querying a destroyed asset, an exception should have been thrown.')
        except:
            self.assertTrue(True)

    def test_asset_list(self):
        """ Queries all of our assets. """
        assets = Asset.find()
        self.assertEqual(len(assets), 0)

        asset = Asset()
        asset.description = 'Arthur Farm - SE Asset'
        asset.shape = MultiPolygon([
            ([(-97.194156646728, 35.667442627764),
              (-97.191281318664, 35.668349114403),
              (-97.185573577880, 35.672497902647),
              (-97.185616493225, 35.676402447539),
              (-97.194499969482, 35.671591463121),
              (-97.194156646728, 35.667442627764)])
        ])
        asset.save()

        asset = Asset()
        asset.description = 'Arthur Farm - NW Asset'
        asset.shape = MultiPolygon([
            ([(-97.184243202209, 35.681457154948),
              (-97.182183265686, 35.685117260431),
              (-97.176904678344, 35.687801231068),
              (-97.176904678344, 35.681352578039),
              (-97.184243202209, 35.681457154948)])
        ])
        asset.save()

        assets = Asset.find()
        self.assertEqual(len(assets), 2)
