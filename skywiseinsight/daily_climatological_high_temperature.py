from voluptuous import Any

from ._climatology_resource import (ClimatologyResourceLocation,
                                    ClimatologyResourceAsset,
                                    ClimatologyResourceContours)


class DailyClimatologicalHighTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalHighTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                                  start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalHighTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                               unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalHighTemperatureContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                                                unit=unit, **kwargs)


class _DailyClimatologicalHighTemperatureByLocation(ClimatologyResourceLocation):

    _path = '/climatology/daily-high-temperature/{latitude}/{longitude}'

    _args = ClimatologyResourceLocation._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyClimatologicalHighTemperatureByAsset(ClimatologyResourceAsset):

    _path = '/climatology/daily-high-temperature/{asset_uuid}'

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


class _DailyClimatologicalHighTemperatureContours(ClimatologyResourceContours):

    _path = '/climatology/daily-high-temperature/{asset_uuid}/contours'

    _args = ClimatologyResourceContours._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })
