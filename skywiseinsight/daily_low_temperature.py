from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContours)


class DailyLowTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyLowTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                   start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyLowTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyLowTemperatureContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                                 unit=unit, **kwargs)


class _DailyLowTemperatureByLocation(DailyResourceLocation):

    _path = '/daily-low-temperature/{latitude}/{longitude}'

    _args = DailyResourceLocation._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyLowTemperatureByAsset(DailyTimeSeriesResourceAsset):

    _path = '/daily-low-temperature/{asset_uuid}'

    _args = DailyTimeSeriesResourceAsset._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyLowTemperatureContours(DailyResourceContours):

    _path = '/daily-low-temperature/{asset_uuid}/contours'
