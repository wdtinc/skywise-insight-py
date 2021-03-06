from voluptuous import Any, Schema, Optional
from skywiserestclient.validation import (datetime, datetime_to_str, latitude, longitude,
                                          polygon, multipolygon)

from skywiseinsight import InsightResource


class HourlyResource(InsightResource):

    _args = Schema({
        'start': datetime_to_str,
        'end': datetime_to_str
    })

    _deserialize = Schema({
        'startTime': datetime,
        'endTime': datetime,
        'unit': {
            'description': unicode,
            'label': unicode
        }
    }, required=True)

    _serialize = Schema({
        'startTime': datetime_to_str,
        'endTime': datetime_to_str,
        'unit': {
            'description': unicode,
            'label': unicode
        }
    })


class HourlyResourceLocation(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'latitude': latitude,
        'longitude': longitude,
        'series': [{
            'value': Any(float, None),
            'validTime': datetime,
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'latitude': latitude,
        'longitude': longitude,
        'series': [{
            'value': Any(float, None),
            'validTime': datetime_to_str,
            Optional('products'): [Any(str, unicode)]
        }]
    })


class HourlyTimeSeriesResourceAsset(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'timeSeriesStatistics': {
            'mean': Any(float, None),
            'minimum': Any(float, None),
            'maximum': Any(float, None)
        },
        'series': [{
            'validTime': datetime,
            'value': Any(float, None),
            'contours': unicode,
            'assetStatistics': {
                'mean': Any(float, None),
                'minimum': Any(float, None),
                'maximum': Any(float, None)
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'timeSeriesStatistics': {
            'mean': Any(float, None),
            'minimum': Any(float, None),
            'maximum': Any(float, None)
        },
        'series': [{
            'validTime': datetime_to_str,
            'value': Any(float, None),
            'contours': unicode,
            'assetStatistics': {
                'mean': Any(float, None),
                'minimum': Any(float, None),
                'maximum': Any(float, None)
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })


class HourlyAccumulationResourceAsset(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'contours': unicode,
        'accumulationStatistics': {
            'mean': Any(float, None),
            'minimum': Any(float, None),
            'maximum': Any(float, None)
        },
        'series': [{
            'validTime': datetime,
            'value': Any(float, None),
            'contours': unicode,
            'assetStatistics': {
                'mean': Any(float, None),
                'minimum': Any(float, None),
                'maximum': Any(float, None)
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'contours': unicode,
        'accumulationStatistics': {
            'mean': Any(float, None),
            'minimum': Any(float, None),
            'maximum': Any(float, None)
        },
        'series': [{
            'validTime': datetime_to_str,
            'value': Any(float, None),
            'contours': unicode,
            'assetStatistics': {
                'mean': Any(float, None),
                'minimum': Any(float, None),
                'maximum': Any(float, None)
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })


class HourlyResourceContours(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'type': unicode,
        'features': [{
            'type': unicode,
            'properties': {
                unicode: float
            },
            'geometry': Any(polygon, multipolygon)
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'type': unicode,
        'features': [{
            'type': unicode,
            'properties': {
                unicode: float
            },
            'geometry': Any(polygon, multipolygon)
        }]
    })


class HourlyResourceContourByValidTime(InsightResource):

    _args = Schema({
        'validTime': datetime_to_str
    })

    _deserialize = Schema({
        'validTime': datetime,
        'asset': unicode,
        'type': unicode,
        'features': [{
            'type': unicode,
            'properties': {
                unicode: float
            },
            'geometry': Any(polygon, multipolygon)
        }]
    })

    _serialize = Schema({
        'validTime': datetime_to_str,
        'asset': unicode,
        'type': unicode,
        'features': [{
            'type': unicode,
            'properties': {
                unicode: float
            },
            'geometry': Any(polygon, multipolygon)
        }]
    })
