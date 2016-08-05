# -*- coding: utf-8 -*-
"""
    skywiseinsight.daily_precipitation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Daily Precip resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyAccumulationResourceAsset,
                              DailyResourceContours)


class DailyPrecipitation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Precip time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyPrecipByLocation.find(latitude=lat, longitude=lon,
                                           start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Precip areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyPrecipByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                        unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily Precip contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyPrecipContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                         unit=unit, **kwargs)


class _DailyPrecipByLocation(DailyResourceLocation):

    _path = '/daily-precipitation/{latitude}/{longitude}'

    _deserialize = DailyResourceLocation._deserialize.extend({
        'precipitation': float
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'precipitation': float
    })

    _args = DailyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyPrecipByAsset(DailyAccumulationResourceAsset):

    _path = '/daily-precipitation/{asset_uuid}'

    _deserialize = DailyAccumulationResourceAsset._deserialize.extend({
        'precipitation': float
    })

    _serialize = DailyAccumulationResourceAsset._serialize.extend({
        'precipitation': float
    })

    _args = DailyAccumulationResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyPrecipContours(DailyResourceContours):

    _path = '/daily-precipitation/{asset_uuid}/contours'

    _args = DailyResourceContours._args.extend({
        'unit': Any('millimeters', 'inches')
    })
