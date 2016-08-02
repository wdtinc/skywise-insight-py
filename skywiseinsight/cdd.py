from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Cdd(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        return _CddByLocation.find(latitude=lat, longitude=lon, start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        return _CddByAsset.find(asset_uuid, start=start, end=end, **kwargs)

    @classmethod
    def contours(self, asset_uuid, start=None, end=None, **kwargs):
        return _CddAssetContours.find(asset_uuid=asset_uuid, start=start, end=end, **kwargs)


class _CddByLocation(DegreeDaysByLocation):

    _path = "/cooling-degree-days/{latitude}/{longitude}"


class _CddByAsset(DegreeDaysByAsset):

    _path = "/cooling-degree-days"


class _CddAssetContours(DegreeDaysAssetContours):

    _path = "/cooling-degree-days/{asset_uuid}/contours"
