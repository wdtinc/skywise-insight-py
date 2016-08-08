Resources
---------

Insight resources are lightweight wrappers around the API's endpoints. Top-level attributes for endpoint responses can be accessed directly::

    >>> from skywiseinsight import DailyPrecipitation as DP
    >>> okc_precip = DP.location(35, -97)
    >>> okc_precip.longitude
    -97.0
    >>> okc_precip.startDate
    datetime.date(2016, 8, 5)
    >>> [item['value'] for item in okc.series]
    [0.3, 0.7, 0.2, 0.7, 2.0, 0.7]

Response values are automatically deserialized into native Python types for you when accessed in this manner.

After making a call to the API, you can also invoke the `json()` method to retrieve all
values as returned by the resource's endpoint. The structure should match the response examples given
in the [HTTP API docs](http://docs.api.wdtinc.com/insight-api/en/latest/overview.html)::

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

