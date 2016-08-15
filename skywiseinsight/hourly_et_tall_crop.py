from voluptuous import Any

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyEtTallCrop(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyEtTallCropByLocation.find(latitude=lat, longitude=lon,
                                                start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyEtTallCropByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                             unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
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
