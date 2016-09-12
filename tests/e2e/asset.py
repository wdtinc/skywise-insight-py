import geojson
from skywiseinsight import Asset, InsightResource
from tests import FIXTURE_DIR
from tests.e2e import SkywiseInsightE2E

# InsightResource.set_site('http://insight-api.dev.us-east-1.wdtinc.com')
InsightResource.set_site('http://localhost:5000')


class AssetTest(SkywiseInsightE2E):

    def test_create_asset(self):

        with open(FIXTURE_DIR + '/Adair.geo.json', 'r') as f:
            gj = geojson.loads(f.read())

        asset = Asset()
        asset.description = gj['features'][0]['properties']['name']
        asset.shape = gj['features'][0]['geometry']
        asset.save()
