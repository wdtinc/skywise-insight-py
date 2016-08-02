from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyTempByLocation.find(latitude=lat, longitude=lon,
                                          start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyTempByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                       unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        return _HourlyTempContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                        unit=unit, **kwargs)


class _HourlyTempByLocation(HourlyResourceLocation):

    _path = '/hourly-temperature/{latitude}/{longitude}'

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class _HourlyTempByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-temperature/{asset_uuid}'

    _args = HourlyTimeSeriesResourceAsset._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })


class _HourlyTempContours(HourlyResourceContourByValidTime):

    _path = '/hourly-temperature/{asset_uuid}/contours'

    _args = HourlyResourceContourByValidTime._args.extend({
        'unit': Any('Celsius', 'Fahrenheit', 'celsius', 'fahrenheit')
    })
