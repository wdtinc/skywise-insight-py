# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_solar_radiation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Solar Radiation resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlySolarRadiation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        """Retrieves Hourly Solar Radiation time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlySolarByLocation.find(latitude=lat, longitude=lon,
                                           start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        """Retrieves Hourly Solar Radiation areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlySolarByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                        **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, **kwargs):
        """Retrieves Hourly Solar Radiation contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime valid_time: The datetime you're requesting contours for.
        """
        return _HourlySolarContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                         **kwargs)


class _HourlySolarByLocation(HourlyResourceLocation):
    _path = '/hourly-solar-radiation/{latitude}/{longitude}'


class _HourlySolarByAsset(HourlyTimeSeriesResourceAsset):
    _path = '/hourly-solar-radiation/{asset_uuid}'


class _HourlySolarContours(HourlyResourceContourByValidTime):
    _path = '/hourly-solar-radiation/{asset_uuid}/contours'
