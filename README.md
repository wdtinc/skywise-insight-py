[![Build Status](https://travis-ci.org/wdtinc/skywise-insight-py.svg?branch=master)](https://travis-ci.org/wdtinc/skywise-insight-py)

# Overview
A Python client library for the SkyWise Insight API. Check out [the API docs](http://docs.api.wdtinc.com/insight-api/en/latest/overview.html) to reference exposed endpoints. Also check out [some examples](https://github.com/wdtinc/Insight-API).

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

## Try It Out
Let's test out our install by requesting the latest Daily Precipitation data for OKC:

```python
import json
from skywiseinsight import DailyPrecipitation as dp

precip = dp.location(35.4, -97.5)
print json.dumps(precip.json())
```

Your output should look something similar to this:

```bash
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
