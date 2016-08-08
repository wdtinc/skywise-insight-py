# -*- coding: utf-8 -*-
"""
    skywiseinsight.daily_et_tall_crop
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Daily ET Tall Crop resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContourByValidDate)


class DailyEtTallCrop(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily ET Tall Crop time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyEtTallCropByLocation.find(latitude=lat, longitude=lon,
                                               start=start, end=end, unit=unit,
                                               **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Daily ET Tall Crop areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyEtTallCropByAsset.find(asset_uuid=asset_uuid, start=start,
                                            end=end, unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, validDate=None, unit=None, **kwargs):
        """Retrieves Daily ET Tall Crop contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _DailyEtTallCropContours.find(asset_uuid=asset_uuid, validDate=validDate,
                                             unit=unit, **kwargs)


class _DailyEtTallCropByLocation(DailyResourceLocation):

    _path = '/daily-evapotranspiration-tall-crop/{latitude}/{longitude}'

    _args = DailyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyEtTallCropByAsset(DailyTimeSeriesResourceAsset):

    _path = '/daily-evapotranspiration-tall-crop/{asset_uuid}'

    _args = DailyTimeSeriesResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyEtTallCropContours(DailyResourceContourByValidDate):

    _path = '/daily-evapotranspiration-tall-crop/{asset_uuid}/contours'

    _args = DailyResourceContourByValidDate._args.extend({
        'unit': Any('millimeters', 'inches')
    })
