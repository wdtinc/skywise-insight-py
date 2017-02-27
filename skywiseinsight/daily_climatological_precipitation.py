from voluptuous import Any

from ._climatology_resource import (ClimatologyResourceLocation,
                                    ClimatologyResourceAsset,
                                    ClimatologyResourceContours)


class DailyClimatologicalPrecipitation(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalPrecipitationByLocation.find(latitude=lat, longitude=lon,
                                                                start=start, end=end, unit=unit, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalPrecipitationByAsset.find(asset_uuid=asset_uuid, start=start, end=end,
                                                             unit=unit, **kwargs)

    @classmethod
    def contours(cls, asset_uuid, start=None, end=None, unit=None, **kwargs):
        return _DailyClimatologicalPrecipitationContours.find(asset_uuid=asset_uuid, start=start, end=end,
                                                              unit=unit, **kwargs)


class _DailyClimatologicalPrecipitationByLocation(ClimatologyResourceLocation):

    _path = '/climatology/daily-precipitation/{latitude}/{longitude}'

    _args = ClimatologyResourceLocation._args.extend({
        'unit': Any('millimeters', 'inches')
    })


class _DailyClimatologicalPrecipitationByAsset(ClimatologyResourceAsset):

    _path = '/climatology/daily-precipitation/{asset_uuid}'

    _args = ClimatologyResourceAsset._args.extend({
        'unit': Any('millimeters', 'inches')
    })

    _deserialize = ClimatologyResourceAsset._deserialize.extend({
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })

    _serialize = ClimatologyResourceAsset._serialize.extend({
        'accumulationStatistics': {
            'mean': float,
            'minimum': float,
            'maximum': float
        }
    })


class _DailyClimatologicalPrecipitationContours(ClimatologyResourceContours):

    _path = '/climatology/daily-precipitation/{asset_uuid}/contours'

    _args = ClimatologyResourceContours._args.extend({
        'unit': Any('millimeters', 'inches')
    })
