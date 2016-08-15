from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyEtShortCrop(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyEtShortCropByLocation.find(latitude=lat, longitude=lon,
                                                 start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyEtShortCropByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                              unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        return _HourlyEtShortCropContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                               unit=unit, **kwargs)


class _HourlyEtShortCropByLocation(HourlyResourceLocation):

    _path = '/hourly-evapotranspiration-short-crop/{latitude}/{longitude}'

    _args = HourlyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyEtShortCropByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-evapotranspiration-short-crop/{asset_uuid}'

    _args = HourlyTimeSeriesResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _HourlyEtShortCropContours(HourlyResourceContourByValidTime):

    _path = '/hourly-evapotranspiration-short-crop/{asset_uuid}/contours'

    _args = HourlyResourceContourByValidTime._args.extend({
        'unit': Any('inches', 'millimeters')
    })
