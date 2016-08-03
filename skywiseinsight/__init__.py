import os
from skywiserestclient import SkyWiseJSON, SkyWiseResource


class InsightResource(SkyWiseJSON, SkyWiseResource):
    pass

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
           DailyEtTallCrop, HourlyEtShortCrop, HourlyEtTallCrop]
