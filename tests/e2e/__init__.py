import arrow
import logging
from unittest import TestCase

from geojson import MultiPolygon, Polygon
from skywiseinsight import InsightResource, Asset
from tests import load_fixture

logging.basicConfig(level=logging.DEBUG)
FIELDS_TO_TEST = 1

common_arrow = arrow.utcnow().floor('hour')


class InsightE2ETest(TestCase):

    location = (35.0, -97.0)

    analysis_start_date = common_arrow.replace(days=-2).date()
    analysis_end_date = common_arrow.replace(days=-1).date()
    analysis_start_datetime = common_arrow.replace(hours=-12).datetime
    analysis_end_datetime = common_arrow.replace(hours=-1).datetime

    analysis_and_forecast_start_date = common_arrow.replace(days=-2).date()
    analysis_and_forecast_end_date = common_arrow.replace(days=+3).date()
    analysis_and_forecast_start_datetime = common_arrow.replace(hours=-6).datetime
    analysis_and_forecast_end_datetime = common_arrow.replace(hours=+6).datetime

    forecast_start_date = common_arrow.replace(days=+1).date()
    forecast_end_date = common_arrow.replace(days=+3).date()
    forecast_start_datetime = common_arrow.replace(hours=+1).datetime
    forecast_end_datetime = common_arrow.replace(hours=+12).datetime

    @classmethod
    def setUpClass(cls):
        cls._setup_asset_list()

    @classmethod
    def _load_asset_fixture(cls, asset, fixture):
        asset.description = fixture['description']
        if fixture['geometries'][0]['type'] == 'Polygon':
            asset.add_geometry(Polygon(fixture['geometries'][0]['coordinates']))
        elif fixture['geometries'][0]['type'] == 'MultiPolygon':
            asset.add_geometry(MultiPolygon(fixture['geometries'][0]['coordinates']))
        else:
            raise Exception('Unsupported type in fixture.')
        return asset

    @classmethod
    def _setup_asset_list(cls):
        cls.assets = []

        assets_json = load_fixture('asset_list')
        asset_count = 0
        for fixture in assets_json['assets']:
            asset = Asset()
            cls._load_asset_fixture(asset, fixture)
            asset.save()
            cls.assets.append(asset)
            asset_count += 1
            if asset_count > FIELDS_TO_TEST:
                return

    def _setup_locations(self):
        capitals_json = load_fixture('state_capital_locations')
        self.locations = capitals_json['capitals']
