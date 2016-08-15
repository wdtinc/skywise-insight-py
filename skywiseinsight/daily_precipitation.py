from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyAccumulationResourceAsset,
                              DailyResourceContours)


class DailyPrecipitation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyPrecipByLocation.find(latitude=lat, longitude=lon,
                                           start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyPrecipByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                        unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyPrecipContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                         unit=unit, **kwargs)


class _DailyPrecipByLocation(DailyResourceLocation):

    _path = '/daily-precipitation/{latitude}/{longitude}'

    _deserialize = DailyResourceLocation._deserialize.extend({
        'precipitation': float
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'precipitation': float
    })

    _args = DailyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyPrecipByAsset(DailyAccumulationResourceAsset):

    _path = '/daily-precipitation/{asset_uuid}'

    _deserialize = DailyAccumulationResourceAsset._deserialize.extend({
        'precipitation': float
    })

    _serialize = DailyAccumulationResourceAsset._serialize.extend({
        'precipitation': float
    })

    _args = DailyAccumulationResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyPrecipContours(DailyResourceContours):

    _path = '/daily-precipitation/{asset_uuid}/contours'

    _args = DailyResourceContours._args.extend({
        'unit': Any('millimeters', 'inches')
    })
