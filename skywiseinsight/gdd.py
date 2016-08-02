from ._degree_days_resource import DegreeDaysByLocation, DegreeDaysByAsset, DegreeDaysAssetContours


class Gdd(object):

    @classmethod
    def location(cls, lat, lon, start=None, end=None, **kwargs):
        return _GddByLocation.find(latitude=lat, longitude=lon, start=start, end=end, **kwargs)

    @classmethod
    def asset(cls, asset_uuid, start=None, end=None, **kwargs):
        return _GddByAsset.find(asset_uuid, start=start, end=end, **kwargs)

    @classmethod
    def contours(self, asset_uuid, start=None, end=None, **kwargs):
        return _GddAssetContours.find(asset_uuid=asset_uuid, start=start, end=end, **kwargs)


class _GddByLocation(DegreeDaysByLocation):

    _path = "/growing-degree-days/{latitude}/{longitude}"


class _GddByAsset(DegreeDaysByAsset):

    _path = "/growing-degree-days"


class _GddAssetContours(DegreeDaysAssetContours):

    _path = "/growing-degree-days/{asset_uuid}/contours"
