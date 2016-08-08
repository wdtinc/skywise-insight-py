# -*- coding: utf-8 -*-
"""
    skywiseinsight.daily_solar_radiation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Daily Solar Radiation resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._daily_resource import (DailyResourceLocation,
                              DailyAccumulationResourceAsset,
                              DailyResourceContours)


class DailySolarRadiation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        """Retrieves Daily Solar Radiation time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _DailySolarByLocation.find(latitude=lat, longitude=lon,
                                          start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        """Retrieves Daily Solar Radiation areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _DailySolarByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                       **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, **kwargs):
        """Retrieves Daily Solar Radiation contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _DailySolarContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                        **kwargs)


class _DailySolarByLocation(DailyResourceLocation):

    _path = '/daily-solar-radiation/{latitude}/{longitude}'

    _deserialize = DailyResourceLocation._deserialize.extend({
        'solarRadiation': float
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'solarRadiation': float
    })


class _DailySolarByAsset(DailyAccumulationResourceAsset):

    _path = '/daily-solar-radiation/{asset_uuid}'

    _deserialize = DailyAccumulationResourceAsset._deserialize.extend({
        'solarRadiation': float
    })

    _serialize = DailyAccumulationResourceAsset._serialize.extend({
        'solarRadiation': float
    })


class _DailySolarContours(DailyResourceContours):

    _path = '/daily-solar-radiation/{asset_uuid}/contours'
