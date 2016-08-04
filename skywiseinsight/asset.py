from voluptuous import Any, Optional, Schema
from skywiserestclient.validation import latitude, longitude, multipolygon, polygon

from skywiseinsight import InsightResource


class UnsupportedGeometryException(Exception):
    pass


class Asset(InsightResource):

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

    def add_geometry(self, g):
        """ Deprecated. Used for backwards-compatibility only. Use
            `asset.shape = geometry` instead. """
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
