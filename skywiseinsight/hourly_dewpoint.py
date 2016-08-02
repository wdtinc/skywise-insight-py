from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyDewpoint(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyDPByLocation.find(latitude=lat, longitude=lon,
                                        start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyDPByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                     unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        return _HourlyDPContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                      unit=unit, **kwargs)


class _HourlyDPByLocation(HourlyResourceLocation):

    _path = '/hourly-dewpoint/{latitude}/{longitude}'

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class _HourlyDPByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-dewpoint/{asset_uuid}'

    _args = HourlyTimeSeriesResourceAsset._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class _HourlyDPContours(HourlyResourceContourByValidTime):

    _path = '/hourly-dewpoint/{asset_uuid}/contours'

    _args = HourlyResourceContourByValidTime._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })
