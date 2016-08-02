from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyAccumulationResourceAsset,
                               HourlyResourceContours)


class HourlyPrecipitation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyPrecipByLocation.find(latitude=lat, longitude=lon,
                                            start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyPrecipByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                         unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyPrecipContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                          unit=unit, **kwargs)


class _HourlyPrecipByLocation(HourlyResourceLocation):

    _path = '/hourly-precipitation/{latitude}/{longitude}'

    _deserialize = HourlyResourceLocation._deserialize.extend({
        'precipitation': float
    })

    _serialize = HourlyResourceLocation._serialize.extend({
        'precipitation': float
    })

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyPrecipByAsset(HourlyAccumulationResourceAsset):

    _path = '/hourly-precipitation/{asset_uuid}'

    _deserialize = HourlyAccumulationResourceAsset._deserialize.extend({
        'precipitation': float
    })

    _serialize = HourlyAccumulationResourceAsset._serialize.extend({
        'precipitation': float
    })

    _args = HourlyAccumulationResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyPrecipContours(HourlyResourceContours):

    _path = '/hourly-precipitation/{asset_uuid}/contours'
