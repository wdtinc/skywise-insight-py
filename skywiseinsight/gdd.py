# -*- coding: utf-8 -*-
"""
    skywiseinsight.gdd
    ~~~~~~~~~~~~~~~~~~
    Implementation of the Growing Degree Days resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Gdd(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves GDD time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _GddByLocation.find(latitude=lat, longitude=lon, start=start, end=end,
                                   base=base, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves GDD areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _GddByAsset.find(asset_uuid, start=start, end=end, base=base,
                                unit=unit, **kwargs)

    @classmethod
    def contours(self, asset_uuid, start=None, end=None, base=None, unit=None, **kwargs):
        """Retrieves GDD contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar float base: Base Temperature
        :ivar string unit: 'fahrenheit' or 'celsius'
        """
        return _GddAssetContours.find(asset_uuid=asset_uuid, start=start,
                                      end=end, base=base, unit=unit, **kwargs)


class _GddByLocation(DegreeDaysByLocation):

    _path = "/growing-degree-days/{latitude}/{longitude}"


class _GddByAsset(DegreeDaysByAsset):

    _path = "/growing-degree-days"


class _GddAssetContours(DegreeDaysAssetContours):

    _path = "/growing-degree-days/{asset_uuid}/contours"
