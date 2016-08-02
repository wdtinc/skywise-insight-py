from ._hourly_resource import (HourlyResourceLocation,
                               HourlyTimeSeriesResourceAsset,
                               HourlyResourceContourByValidTime)


class HourlySolarRadiation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlySolarByLocation.find(latitude=lat, longitude=lon,
                                           start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlySolarByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                        unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, valid_time=None, unit=None, **kwargs):
        return _HourlySolarContours.find(asset_uuid=asset_uuid, validTime=valid_time,
                                         unit=unit, **kwargs)


class _HourlySolarByLocation(HourlyResourceLocation):
    _path = '/hourly-solar-radiation/{latitude}/{longitude}'


class _HourlySolarByAsset(HourlyTimeSeriesResourceAsset):
    _path = '/hourly-solar-radiation/{asset_uuid}'


class _HourlySolarContours(HourlyResourceContourByValidTime):
    _path = '/hourly-solar-radiation/{asset_uuid}/contours'
