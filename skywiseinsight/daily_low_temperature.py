# -*- coding: utf-8 -*-
"""
    skywiseinsight.daily_low_temperature
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Daily Low Temp resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContours)


class DailyLowTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Low Temperature time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _DailyLowTemperatureByLocation.find(latitude=lat, longitude=lon,
                                                   start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Low Temperature areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _DailyLowTemperatureByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Low Temperature contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
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
