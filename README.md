# Overview
A Python client library for the SkyWise Insight API. For more detailed 
usage info, check out the [client API reference](http://docs.api.wdtinc.com/skywise-insight-py/en/latest/) 
to see all Insight API resources that the client library exposes.

## Prerequisites

- [Python 2.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

> **Windows Users**
> You will most likely need to install **gevent** beforehand. You can typically find the latest wheel [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent).

## Installation

```bash
pip install skywise-insight
```

## Configure App ID/Key
The easiest (and recommended) way to configure authentication to the API is by setting the following environment variables:

```bash
SKYWISE_INSIGHT_APP_ID='{YOUR_APP_ID}'
SKYWISE_INSIGHT_APP_KEY='{YOUR_APP_KEY}'
```

Otherwise, you'll need to set your App ID/Key explicitly in your app/script before making API calls:

```python
from skywiseinsight import InsightResource

InsightResource.set_user('{YOUR_APP_ID}')
InsightResource.set_password('{YOUR_APP_KEY}')
```

> **API Signup**
> If you don't already have an app id and key, [sign up](http://skywise.wdtinc.com) for a free demo account.

## Try It Out
Let's test out our install by requesting the latest Daily Precipitation data for OKC:

```python
>>> import json
>>> from skywiseinsight import DailyPrecipitation as dp

>>> precip = dp.location(35.4, -97.5)
>>> precip.json()
 {
   "startDate":"2016-08-03",
   "endDate":"2016-08-08",
   "series":[
      {
         "validDate":"2016-08-08",
         "value":0.3
      },
      {
         "validDate":"2016-08-07",
         "value":0.1
      },
      {
         "validDate":"2016-08-06",
         "value":0.8
      },
      {
         "validDate":"2016-08-05",
         "value":0.3
      },
      {
         "validDate":"2016-08-04",
         "value":0.1
      },
      {
         "validDate":"2016-08-03",
         "value":0.2
      }
   ],
   "longitude":-97.5,
   "latitude":35.4,
   "precipitation":1.8,
   "unit":{
      "description":"millimeters",
      "label":"mm"
   }
 }
```

The `json()` method will output the response as it was returned 
from the API. You can also access response attributes directly and benefit
from on the fly deserialization of response values to Python types 
such as date/datetime:

```python
>>> okc_precip.startDate
datetime.date(2016, 8, 5)
>>> okc_precip.startDate > okc_precip.endDate
True
```

