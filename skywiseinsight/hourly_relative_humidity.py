from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlyRelativeHumidity(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyRHByLocation.find(latitude=lat, longitude=lon,
                                        start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyRHByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                     unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyRHContours.find(asset_uuid=asset_uuid, validTime=end,
                                      unit=unit, **kwargs)


class _HourlyRHByLocation(HourlyResourceLocation):

    _path = '/hourly-relative-humidity/{latitude}/{longitude}'


class _HourlyRHByAsset(HourlyTimeSeriesResourceAsset):

    _path = '/hourly-relative-humidity/{asset_uuid}'


class _HourlyRHContours(HourlyResourceContourByValidTime):

    _path = '/hourly-relative-humidity/{asset_uuid}/contours'
