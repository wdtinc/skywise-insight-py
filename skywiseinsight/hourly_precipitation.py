# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_precipitation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Precipitation resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyAccumulationResourceAsset,
                               HourlyResourceContours)


class HourlyPrecipitation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Precip time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyPrecipByLocation.find(latitude=lat, longitude=lon,
                                            start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Precip areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyPrecipByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                         unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly Precip contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyPrecipContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                          unit=unit, **kwargs)


class _HourlyPrecipByLocation(HourlyResourceLocation):

    _path = '/hourly-precipitation/{latitude}/{longitude}'

    _deserialize = HourlyResourceLocation._deserialize.extend({
        'precipitation': float
    })

    _serialize = HourlyResourceLocation._serialize.extend({
        'precipitation': float
    })

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyPrecipByAsset(HourlyAccumulationResourceAsset):

    _path = '/hourly-precipitation/{asset_uuid}'

    _deserialize = HourlyAccumulationResourceAsset._deserialize.extend({
        'precipitation': float
    })

    _serialize = HourlyAccumulationResourceAsset._serialize.extend({
        'precipitation': float
    })

    _args = HourlyAccumulationResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyPrecipContours(HourlyResourceContours):

    _path = '/hourly-precipitation/{asset_uuid}/contours'
