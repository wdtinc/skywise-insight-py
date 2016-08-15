from skywiserestclient.validation import datetime, datetime_to_str

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyResource)


class HourlyWindDirection(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _HourlyWindDirectionByLocation.find(latitude=lat, longitude=lon,
                                                   start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _HourlyWindDirectionByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                unit=unit, **kwargs)


class _HourlyWindDirectionByLocation(HourlyResourceLocation):

    _path = '/hourly-wind-direction/{latitude}/{longitude}'


class _HourlyWindDirectionByAsset(HourlyResource):

    _path = '/hourly-wind-direction/{asset_uuid}'

    _deserialize = HourlyResource._deserialize.extend({
        'asset': unicode,
        'series': [{
            'validTime': datetime,
            'value': float
        }]
    })

    _serialize = HourlyResource._serialize.extend({
        'asset': unicode,
        'series': [{
            'validTime': datetime_to_str,
            'value': float
        }]
    })
