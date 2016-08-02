from ._daily_resource import (DailyResourceLocation,
                              DailyAccumulationResourceAsset,
                              DailyResourceContours)


class DailySolarRadiation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailySolarByLocation.find(latitude=lat, longitude=lon,
                                          start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailySolarByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                       unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailySolarContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                        unit=unit, **kwargs)


class _DailySolarByLocation(DailyResourceLocation):

    _path = '/daily-solar-radiation/{latitude}/{longitude}'

    _deserialize = DailyResourceLocation._deserialize.extend({
        'solarRadiation': float
    })

    _serialize = DailyResourceLocation._serialize.extend({
        'solarRadiation': float
    })


class _DailySolarByAsset(DailyAccumulationResourceAsset):

    _path = '/daily-solar-radiation/{asset_uuid}'

    _deserialize = DailyAccumulationResourceAsset._deserialize.extend({
        'solarRadiation': float
    })

    _serialize = DailyAccumulationResourceAsset._serialize.extend({
        'solarRadiation': float
    })


class _DailySolarContours(DailyResourceContours):

    _path = '/daily-solar-radiation/{asset_uuid}/contours'
