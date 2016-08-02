from voluptuous import Any

from ._daily_resource import (DailyResourceLocation,
                              DailyTimeSeriesResourceAsset,
                              DailyResourceContourByValidDate)


class DailyEtShortCrop(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyEtShortCropByLocation.find(latitude=lat, longitude=lon,
                                                start=start, end=end, unit=unit,
                                                **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyEtShortCropByAsset.find(asset_uuid=asset_uuid, start=start,
                                             end=end, unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, validDate=None, unit=None, **kwargs):
        return _DailyEtShortCropContours.find(asset_uuid=asset_uuid, validDate=validDate, unit=unit, **kwargs)


class _DailyEtShortCropByLocation(DailyResourceLocation):

    _path = '/daily-evapotranspiration-short-crop/{latitude}/{longitude}'

    _args = DailyResourceLocation._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyEtShortCropByAsset(DailyTimeSeriesResourceAsset):

    _path = '/daily-evapotranspiration-short-crop/{asset_uuid}'

    _args = DailyTimeSeriesResourceAsset._args.extend({
        'unit': Any('inches', 'millimeters')
    })


class _DailyEtShortCropContours(DailyResourceContourByValidDate):

    _path = '/daily-evapotranspiration-short-crop/{asset_uuid}/contours'

    _args = DailyResourceContourByValidDate._args.extend({
        'unit': Any('millimeters', 'inches')
    })
