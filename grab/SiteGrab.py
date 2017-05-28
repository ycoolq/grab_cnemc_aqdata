from grab import BaseGrab
from wcf  import records
from const import Consts
from entity import Point
class SiteGrab(BaseGrab.BaseGrab):
    '站点抓取服务'

    tag = Consts.SITE_ENTITY_TAG

    def parseEntity(self,element):
        if (isinstance(element, records.elements.ShortElementRecord) == False):
            return
        id = area = cityCode = stationCode = uniqueCode = positionName = latitude \
            = longitude = isContrast = isPublish = orderID = None
        print("---------------")
        for i in element.__getattribute__("childs"):
            label = str(i)
            value = str(i.__getattribute__('childs')[0])
            print(label)
            if label == "<b:Id>":
                id = value
            elif label == "<b:Area>":
                area = value
            elif label == "<b:CityCode>":
                cityCode = value
            elif label == "<b:IsContrast>":
                isContrast = value
            elif label == "<b:IsPublish>":
                isPublish = value
            elif label == "<b:Latitude>":
                latitude = value
            elif label == "<b:Longitude>":
                longitude = value
            elif label == "<b:OrderId>":
                orderID = value
            elif label == "<b:PositionName>":
                positionName = value
            elif label == "<b:StationCode>":
                stationCode = value
            elif label == "<b:UniqueCode>":
                uniqueCode = value
        curSite = Point.Site(id,area,cityCode,stationCode,uniqueCode,
                 positionName,latitude,longitude,isContrast,
                 isPublish,orderID)
       #print(curCity.toString())
        return curSite
