# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_et_tall_crop
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly ET Tall Crop resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyEtTallCrop(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly ET Tall Crop time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyEtTallCropByLocation.find(latitude=lat, longitude=lon,
                                                start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        """Retrieves Hourly ET Tall Crop areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyEtTallCropByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                             unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        """Retrieves Hourly ET Tall Crop contour data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        :ivar string unit: 'inches' or 'millimeters'
        """
        return _HourlyEtTallCropContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                              unit=unit, **kwargs)


class _HourlyEtTallCropByLocation(HourlyResourceLocation):

    _path = '/hourly-evapotranspiration-tall-crop/{latitude}/{longitude}'

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyEtTallCropByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-evapotranspiration-tall-crop/{asset_uuid}'

    _args = HourlyTimeSeriesResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyEtTallCropContours(HourlyResourceContourByValidTime):

    _path = '/hourly-evapotranspiration-tall-crop/{asset_uuid}/contours'

    _args = HourlyResourceContourByValidTime._args.extend({
        'unit': Any('inches', 'millimeters')
    })
