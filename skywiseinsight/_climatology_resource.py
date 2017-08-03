from voluptuous import Any, Optional
from ._daily_resource import (DailyResourceLocation,
                              DailyResourceAsset,
                              DailyResourceContours)


class ClimatologyResourceLocation(DailyResourceLocation):

    _deserialize = DailyResourceLocation._deserialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode),
        'series': [{
            'value': float,
            'validDate': Any(str, unicode),
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode),
        'series': [{
            'value': float,
            'validDate': Any(str, unicode),
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _args = DailyResourceLocation._args.extend({
        'start': Any(str, unicode),
        'end': Any(str, unicode),
        'years': Any(10, 30)
    })


class ClimatologyResourceAsset(DailyResourceAsset):

    _deserialize = DailyResourceAsset._deserialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode),
        'series': [{
            'validDate': Any(str, unicode),
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _serialize = DailyResourceAsset._serialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode),
        'series': [{
            'validDate': Any(str, unicode),
            'value': float,
            'contours': unicode,
            'assetStatistics': {
                'mean': float,
                'minimum': float,
                'maximum': float
            },
            Optional('products'): [Any(str, unicode)]
        }]
    })

    _args = DailyResourceAsset._args.extend({
        'start': Any(str, unicode),
        'end': Any(str, unicode),
        'years': Any(10, 30)
    })


class ClimatologyResourceContours(DailyResourceContours):

    _deserialize = DailyResourceContours._deserialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode)
    })

    _serialize = DailyResourceContours._serialize.extend({
        'startDate': Any(str, unicode),
        'endDate': Any(str, unicode)
    })

    _args = DailyResourceContours._args.extend({
        'start': Any(str, unicode),
        'end': Any(str, unicode),
        'years': Any(10, 30)
    })
