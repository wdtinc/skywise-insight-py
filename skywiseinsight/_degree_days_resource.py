from voluptuous import Any
from skywiserestclient.validation import temp_to_str

from ._daily_resource import (DailyResourceLocation, DailyAccumulationResourceAsset,
                              DailyResourceContours)


class DegreeDaysByLocation(DailyResourceLocation):

    _deserialize = DailyResourceLocation._deserialize.extend({
        'baseTemperature': float,
        'degreeDays': float
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'baseTemperature': float,
        'degreeDays': float
    })

    _args = DailyResourceLocation._args.extend({
        'base': temp_to_str,
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class DegreeDaysByAsset(DailyAccumulationResourceAsset):

    _deserialize = DailyAccumulationResourceAsset._deserialize.extend({
        'baseTemperature': float,
        'degreeDays': float
    })

    _serialize = DailyAccumulationResourceAsset._serialize.extend({
        'baseTemperature': float,
        'degreeDays': float
    })

    _args = DailyAccumulationResourceAsset._args.extend({
        'base': temp_to_str,
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class DegreeDaysAssetContours(DailyResourceContours):

    _deserialize = DailyResourceContours._deserialize.extend({
        'baseTemperature': float
    })

    _serialize = DailyResourceContours._serialize.extend({
        'baseTemperature': float
    })

    _args = DailyResourceContours._args.extend({
        'base': temp_to_str,
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })
