.. skywise-insight-py documentation master file, created by
   sphinx-quickstart on Thu Aug  4 14:49:43 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _api:

API Reference
-------------

Configuration
=============

Configuration of the client's App ID and Key can be made directly to the `InsightResource` base-class.

.. autoclass:: skywiseinsight.InsightResource
   :members:

Assets
======

.. autoclass:: skywiseinsight.Asset
   :members:

Asset objects expose the following attributes:

   .. attribute:: description

      A string describing your asset.

   .. attribute:: shape

      A valid geojson `Polygon <https://pypi.python.org/pypi/geojson/#polygon>`_ object.

Resources
=========

Insight resources are lightweight wrappers around the API's endpoints. After
making a call to the API, you can invoke the `json()` method to retrieve all
values. The structure of this object should match the response examples given
in the [HTTP API docs]()::

    >>> from skywiseinsight import DailyPrecipitation as DP
    >>> okc_precip = DP.location(35, -97)
    >>> okc_precip.json()

    {
      u'startDate':u'2016-08-05',
      u'endDate':u'2016-08-10',
      u'series':[
         {
            u'validDate':u'2016-08-10',
            u'value':0.3
         },
         {
            u'validDate':u'2016-08-09',
            u'value':0.7
         },
         {
            u'validDate':u'2016-08-08',
            u'value':0.2
         },
         {
            u'validDate':u'2016-08-07',
            u'value':0.7
         },
         {
            u'validDate':u'2016-08-06',
            u'value':2.0
         },
         {
            u'validDate':u'2016-08-05',
            u'value':0.7
         }
      ],
      u'longitude':-97.0,
      u'latitude':35.0,
      u'precipitation':4.6,
      u'unit':{
         u'description':u'millimeters',
         u'label':u'mm'
      }
    }

Top-level attributes can be accessed directly::

    >>> okc_precip.longitude
    -97.0
    >>> okc_precip.startDate
    datetime.date(2016, 8, 5)
    >>> [item['value'] for item in okc.series]
    [0.3, 0.7, 0.2, 0.7, 2.0, 0.7]

Notice that all dates/datetimes JSON strings are automatically deserialized for you when accessed directly.

-----------
Degree Days
-----------

----

.. autoclass:: skywiseinsight.Cdd
   :members:

.. autoclass:: skywiseinsight.Gdd
   :members:

.. autoclass:: skywiseinsight.Hdd
   :members:

-------------
Precipitation
-------------

----

.. autoclass:: skywiseinsight.DailyPrecipitation
   :members:

.. autoclass:: skywiseinsight.HourlyPrecipitation
   :members:

-----------------
Relative Humidity
-----------------

----

.. autoclass:: skywiseinsight.HourlyRelativeHumidity
   :members:

---------------
Solar Radiation
---------------

----

.. autoclass:: skywiseinsight.DailySolarRadiation
   :members:

.. autoclass:: skywiseinsight.HourlySolarRadiation
   :members:

-----------
Temperature
-----------

----

.. autoclass:: skywiseinsight.HourlyTemperature
   :members:

.. autoclass:: skywiseinsight.DailyHighTemperature
   :members:

.. autoclass:: skywiseinsight.DailyLowTemperature
   :members:

----
Wind
----

----

.. autoclass:: skywiseinsight.HourlyWindSpeed
   :members:

.. autoclass:: skywiseinsight.HourlyWindDirection
   :members:

------------------
Evapotranspiration
------------------

----

.. autoclass:: skywiseinsight.DailyEtShortCrop
   :members:

.. autoclass:: skywiseinsight.DailyEtTallCrop
   :members:

.. autoclass:: skywiseinsight.HourlyEtShortCrop
   :members:

.. autoclass:: skywiseinsight.HourlyEtTallCrop
   :members:

