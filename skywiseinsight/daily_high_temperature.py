# -*- coding: utf-8 -*-
"""
    skywiseinsight.daily_high_temperature
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Daily High Temperature resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContours)


class DailyHighTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily High Temperature time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _DailyHighTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                    start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily High Temperature areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _DailyHighTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                 unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily High Temperature contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
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
