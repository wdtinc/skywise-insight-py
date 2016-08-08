# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_relative_humidity
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Relative Humidity resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyRelativeHumidity(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        """Retrieves Hourly Relative Humidity time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlyRHByLocation.find(latitude=lat, longitude=lon,
                                        start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        """Retrieves Hourly Relative Humidity areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlyRHByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                     **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, **kwargs):
        """Retrieves Hourly Relative Humidity contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime valid_time: The datetime you're requesting contours for.
        """
        return _HourlyRHContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                      **kwargs)


class _HourlyRHByLocation(HourlyResourceLocation):

    _path = '/hourly-relative-humidity/{latitude}/{longitude}'


class _HourlyRHByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-relative-humidity/{asset_uuid}'


class _HourlyRHContours(HourlyResourceContourByValidTime):

    _path = '/hourly-relative-humidity/{asset_uuid}/contours'
