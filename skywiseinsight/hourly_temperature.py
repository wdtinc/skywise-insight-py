# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_temperature
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Temperature resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyTemperature(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Temperature time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _HourlyTempByLocation.find(latitude=lat, longitude=lon,
                                          start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Temperature areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _HourlyTempByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                       unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        """Retrieves Hourly Temperature areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime valid_time: The datetime you're requesting contours for.
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
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
