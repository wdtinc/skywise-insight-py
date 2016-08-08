# -*- coding: utf-8 -*-
"""
    skywiseinsight.hourly_wind_direction
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implementation of the Hourly Wind Direction resource.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
from skywiserestclient.validation import datetime, datetime_to_str

from ._hourly_resource import (HourlyResourceLocation,
                               HourlyResource)


class HourlyWindDirection(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        """Retrieves Hourly Wind Direction time series data for a specified point.

        :ivar float lat: Latitude
        :ivar float lon: Longitude
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlyWindDirectionByLocation.find(latitude=lat, longitude=lon,
                                                   start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        """Retrieves Hourly Wind Direction areal statistics and time series data for the specified asset.

        :ivar string asset_uuid: Asset UUID
        :ivar datetime start: Start of your query.
        :ivar datetime end: End of your query.
        """
        return _HourlyWindDirectionByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                **kwargs)


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
