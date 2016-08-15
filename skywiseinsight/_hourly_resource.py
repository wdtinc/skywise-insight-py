from voluptuous import Any, Schema
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
            'value': float,
            'validTime': datetime
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'latitude': latitude,
        'longitude': longitude,
        'series': [{
            'value': float,
            'validTime': datetime_to_str
        }]
    })


class HourlyTimeSeriesResourceAsset(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        },
        'series': [{
            'validTime': datetime,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        },
        'series': [{
            'validTime': datetime_to_str,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
        }]
    })


class HourlyAccumulationResourceAsset(HourlyResource):

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'contours': unicode,
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        },
        'series': [{
            'validTime': datetime,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'contours': unicode,
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        },
        'series': [{
            'validTime': datetime_to_str,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
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
