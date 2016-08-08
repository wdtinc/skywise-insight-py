# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_wind_speed
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Wind Speed resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyWindSpeed(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Wind Speed time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'kph' or 'mph'
        """
        return _HourlyWindSpeedByLocation.find(latitude=lat, longitude=lon,
                                               start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Wind Speed areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'kph' or 'mph'
        """
        return _HourlyWindSpeedByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                            unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        """Retrieves Hourly Wind Speed contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime valid_time: The datetime you're requesting contours for.
        :ivar string unit: 'kph' or 'mph'
        """
        return _HourlyWindSpeedContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                             unit=unit, **kwargs)


class _HourlyWindSpeedByLocation(HourlyResourceLocation):

    _path = '/hourly-wind-speed/{latitude}/{longitude}'

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('mph', 'kph')
    })


class _HourlyWindSpeedByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-wind-speed/{asset_uuid}'

    _args = HourlyTimeSeriesResourceAsset._args.extend({
        'unit': Any('mph', 'kph')
    })


class _HourlyWindSpeedContours(HourlyResourceContourByValidTime):

    _path = '/hourly-wind-speed/{asset_uuid}/contours'

    _args = HourlyResourceContourByValidTime._args.extend({
        'unit': Any('mph', 'kph')
    })
