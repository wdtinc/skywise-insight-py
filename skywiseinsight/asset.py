# -*- coding: utf-8 -*-
"""
    skywiseinsight.asset
    ~~~~~~~~~~~~~~~~~~~~
    Implementation of the Asset resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any, Schema
from skywiserestclient.validation import latitude, longitude, multipolygon, polygon

from skywiseinsight import InsightResource


class UnsupportedGeometryException(Exception):
    pass


class Asset(InsightResource):
    """ The Asset class implements the schemas and validation required
    to CRUD asset objects::

        from geojson import Polygon
        from skywiseinsight import Asset

        asset = Asset()
        asset.description = "My area of interest."
        asset.shape = Polygon([[
          [-109.3359375, 38.272688535980976],
          [-109.3359375, 42.553080288955826],
          [-99.84374999999999, 42.553080288955826],
          [-99.84374999999999, 38.272688535980976],
          [-109.3359375, 38.272688535980976]
        ]])
        asset.save()

    """
    _path = "/assets"

    _deserialize = Schema({
        'id': unicode,
        'description': unicode,
        'type': unicode,
        'geometries': [Any(polygon, multipolygon)],
        'centroid': {
            'latitude': latitude,
            'longitude': longitude
        }
    })

    _serialize = Schema({
        'description': basestring,
        'type': basestring,
        'geometries': [Any(polygon, multipolygon)]
    })

    def __init__(self):
        super(Asset, self).__init__()
        self.type = 'GeometryCollection'
        self.geometries = []

    def __getattr__(self, name):
        if name == 'shape':
            return self._data['geometries'][0]
        return super(Asset, self).__getattr__(name)

    def __setattr__(self, name, value):
        if name == 'shape':
            self.add_geometry(value)
        else:
            super(Asset, self).__setattr__(name, value)

    def add_geometry(self, geometry):
        g = geometry
        if g.type == 'MultiPolygon':
            self._add_mp(g)
        elif g.type == 'Polygon':
            self._add_p(g)
        else:
            raise UnsupportedGeometryException('Only Polygons/MultiPolygons supported.')

    def _add_p(self, p):
        g = {
            'type': 'Polygon',
            'coordinates': p.coordinates
        }
        self.geometries.append(g)

    def _add_mp(self, mp):
        g = {
            'type': 'MultiPolygon',
            'coordinates': [mp.coordinates]
        }
        self.geometries.append(g)
