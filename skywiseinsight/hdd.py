# -*- coding: utf-8 -*-
"""
    skywiseinsight.hdd
    ~~~~~~~~~~~~~~~~~~
    Implementation of the Heating Degree Days resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Hdd(object):

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
        return _HddByLocation.find(latitude=lat, longitude=lon, start=start, end=end,
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
        return _HddByAsset.find(asset_uuid, start=start, end=end, base=base,
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
        return _HddAssetContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                      base=base, unit=unit, **kwargs)


class _HddByLocation(DegreeDaysByLocation):

    _path = "/heating-degree-days/{latitude}/{longitude}"


class _HddByAsset(DegreeDaysByAsset):

    _path = "/heating-degree-days"


class _HddAssetContours(DegreeDaysAssetContours):

    _path = "/heating-degree-days/{asset_uuid}/contours"
