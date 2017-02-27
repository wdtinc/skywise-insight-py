from voluptuous import Any

from ._climatology_resource import (ClimatologyResourceLocation,
                                    ClimatologyResourceAsset,
                                    ClimatologyResourceContours)


class DailyClimatologicalLowTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalLowTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                                 start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalLowTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                              unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalLowTemperatureContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                                               unit=unit, **kwargs)


class _DailyClimatologicalLowTemperatureByLocation(ClimatologyResourceLocation):

    _path = '/climatology/daily-low-temperature/{latitude}/{longitude}'

    _args = ClimatologyResourceLocation._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyClimatologicalLowTemperatureByAsset(ClimatologyResourceAsset):

    _path = '/climatology/daily-low-temperature/{asset_uuid}'

    _args = ClimatologyResourceAsset._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })

    _deserialize = ClimatologyResourceAsset._deserialize.extend({
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })

    _serialize = ClimatologyResourceAsset._serialize.extend({
        'timeSeriesStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })


class _DailyClimatologicalLowTemperatureContours(ClimatologyResourceContours):

    _path = '/climatology/daily-low-temperature/{asset_uuid}/contours'

    _args = ClimatologyResourceContours._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })
