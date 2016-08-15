from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContours)


class DailyHighTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyHighTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                    start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyHighTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                 unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyHighTemperatureContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                                  unit=unit, **kwargs)


class _DailyHighTemperatureByLocation(DailyResourceLocation):

    _path = '/daily-high-temperature/{latitude}/{longitude}'

    _args = DailyResourceLocation._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyHighTemperatureByAsset(DailyTimeSeriesResourceAsset):

    _path = '/daily-high-temperature/{asset_uuid}'

    _args = DailyTimeSeriesResourceAsset._args.extend({
        'unit': Any('celsius', 'fahrenheit')
    })


class _DailyHighTemperatureContours(DailyResourceContours):

    _path = '/daily-high-temperature/{asset_uuid}/contours'
