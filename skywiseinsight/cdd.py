# -*- coding: utf-8 -*-
"""
    skywiseinsight.cdd
    ~~~~~~~~~~~~~~~~~~
    Implementation of the Cdd resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Cdd(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves CDD time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _CddByLocation.find(latitude=lat, longitude=lon, start=start, end=end,
                                   base=base, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves CDD areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _CddByAsset.find(asset_uuid, start=start, end=end, base=base,
                                unit=unit, **kwargs)

    @classmethod
    def contours(self, asset_uuid, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves CDD contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _CddAssetContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                      base=base, unit=unit, **kwargs)


class _CddByLocation(DegreeDaysByLocation):

    _path = "/cooling-degree-days/{latitude}/{longitude}"


class _CddByAsset(DegreeDaysByAsset):

    _path = "/cooling-degree-days"


class _CddAssetContours(DegreeDaysAssetContours):

    _path = "/cooling-degree-days/{asset_uuid}/contours"
