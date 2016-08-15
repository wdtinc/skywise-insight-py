from voluptuous import Any, Optional, Schema
from skywiserestclient.validation import date, date_to_str, latitude, longitude, polygon, multipolygon

from skywiseinsight import InsightResource


class DailyResource(InsightResource):

    _args = Schema({
        'start': date_to_str,
        'end': date_to_str
    })

    _deserialize = Schema({
        'startDate': date,
        'endDate': date,
        'unit': {
            'description': unicode,
            'label': unicode
        }
    }, required=True)

    _serialize = Schema({
        'startDate': date_to_str,
        'endDate': date_to_str,
        'unit': {
            'description': unicode,
            'label': unicode
        }
    })


class DailyResourceLocation(DailyResource):

    _deserialize = DailyResource._deserialize.extend({
        'latitude': latitude,
        'longitude': longitude,
        'series': [{
            'value': float,
            'validDate': date
        }]
    })

    _serialize = DailyResource._serialize.extend({
        'latitude': latitude,
        'longitude': longitude,
        'series': [{
            'value': float,
            'validDate': date_to_str
        }]
    })


class DailyResourceAsset(DailyResource):

    _deserialize = DailyResource._deserialize.extend({
        'asset': unicode,
        Optional('contours'): unicode,
        'series': [{
            'validDate': date,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
        }]
    })

    _serialize = DailyResource._serialize.extend({
        'asset': unicode,
        'contours': unicode,
        'series': [{
            'validDate': date_to_str,
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            }
        }]
    })


class DailyTimeSeriesResourceAsset(DailyResourceAsset):

    _deserialize = DailyResourceAsset._deserialize.extend({
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })

    _serialize = DailyResourceAsset._serialize.extend({
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })


class DailyAccumulationResourceAsset(DailyResourceAsset):

    _deserialize = DailyResourceAsset._deserialize.extend({
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })

    _serialize = DailyResourceAsset._serialize.extend({
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })


class DailyResourceContours(DailyResource):

    _deserialize = DailyResource._deserialize.extend({
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

    _serialize = DailyResource._serialize.extend({
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


class DailyResourceContourByValidDate(InsightResource):

    _args = Schema({
        'validDate': date_to_str
    })

    _deserialize = Schema({
        'validDate': date,
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
        'validDate': date_to_str,
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
