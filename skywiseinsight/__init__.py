# -*- coding: utf-8 -*-
"""
    skywiseinsight
    ~~~~~~~~~~~~~~
    A Python client library for the SkyWise Insight API.

    :copyright: (c) 2016 by WDT Inc.
    :license: MIT, see LICENSE for more details.
"""
import os
from skywiserestclient import SkyWiseJSON, SkyWiseResource
from skywiserestclient import map_requests


def map_async(async_requests, raise_on_error=True):
    """ Asynchronously calls requests and blocks until all are complete.
    """
    map_requests(async_requests, raise_on_error=raise_on_error)


class InsightResource(SkyWiseJSON, SkyWiseResource):
    """ Base class for all Insight resources."""

    @classmethod
    def get_app_id(cls):
        """Returns the currently configured App ID."""
        return super(InsightResource, cls).get_user()

    @classmethod
    def set_app_id(cls, app_id):
        """Sets your App ID."""
        super(InsightResource, cls).set_user(app_id)

    @classmethod
    def get_app_key(cls):
        """Returns your current App Key."""
        return super(InsightResource, cls).get_password()

    @classmethod
    def set_app_key(cls, app_key):
        """Sets your App Key."""
        super(InsightResource, cls).set_password(app_key)


_site = os.getenv('SKYWISE_INSIGHT_SITE', 'http://insight.api.wdtinc.com')
_user = os.getenv('SKYWISE_INSIGHT_APP_ID', '')
_password = os.getenv('SKYWISE_INSIGHT_APP_KEY', '')

InsightResource.set_site(_site)
InsightResource.set_user(_user)
InsightResource.set_password(_password)

from skywiseinsight.cdd import Cdd
from skywiseinsight.gdd import Gdd
from skywiseinsight.hdd import Hdd
from skywiseinsight.daily_low_temperature import DailyLowTemperature
from skywiseinsight.daily_high_temperature import DailyHighTemperature
from skywiseinsight.daily_precipitation import DailyPrecipitation
from skywiseinsight.hourly_precipitation import HourlyPrecipitation
from skywiseinsight.daily_solar_radiation import DailySolarRadiation
from skywiseinsight.hourly_solar_radiation import HourlySolarRadiation
from skywiseinsight.hourly_temperature import HourlyTemperature
from skywiseinsight.hourly_dewpoint import HourlyDewpoint
from skywiseinsight.hourly_wind_speed import HourlyWindSpeed
from skywiseinsight.hourly_wind_direction import HourlyWindDirection
from skywiseinsight.hourly_relative_humidity import HourlyRelativeHumidity
from skywiseinsight.daily_et_short_crop import DailyEtShortCrop
from skywiseinsight.daily_et_tall_crop import DailyEtTallCrop
from skywiseinsight.hourly_et_short_crop import HourlyEtShortCrop
from skywiseinsight.hourly_et_tall_crop import HourlyEtTallCrop
from skywiseinsight.asset import Asset

__all__ = [Asset, Cdd, Gdd, Hdd, DailyLowTemperature, DailyHighTemperature, DailyPrecipitation,
           DailySolarRadiation, HourlySolarRadiation, HourlyTemperature, HourlyDewpoint,
           HourlyWindSpeed, HourlyWindDirection, HourlyRelativeHumidity, DailyEtShortCrop,
           DailyEtTallCrop, HourlyEtShortCrop, HourlyEtTallCrop, map_async]
