from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Hdd(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        return _HddByLocation.find(latitude=lat, longitude=lon, start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        return _HddByAsset.find(asset_uuid, start=start, end=end, **kwargs)

    @classmethod
    def contours(self, asset_uuid, start=None, end=None, **kwargs):
        return _HddAssetContours.find(asset_uuid=asset_uuid, start=start, end=end, **kwargs)


class _HddByLocation(DegreeDaysByLocation):

    _path = "/heating-degree-days/{latitude}/{longitude}"


class _HddByAsset(DegreeDaysByAsset):

    _path = "/heating-degree-days"


class _HddAssetContours(DegreeDaysAssetContours):

    _path = "/heating-degree-days/{asset_uuid}/contours"
