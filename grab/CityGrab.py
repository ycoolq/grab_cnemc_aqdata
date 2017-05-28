from wcf  import records
from grab import BaseGrab
from entity import Point
from const import Consts
class CityGrab(BaseGrab.BaseGrab):
    '抓取城市信息'

    tag = Consts.CITY_ENTITY_TAG

    def parseEntity(self,element):
        if (isinstance(element, records.elements.ShortElementRecord) == False):
            return
        cityId = cityJc = cityCode = cityName = None
        for i in element.__getattribute__("childs"):
            label = str(i)
            value = str(i.__getattribute__('childs')[0])
            if label == "<b:CityCode>":
                cityCode = value
            elif label == "<b:CityJC>":
                cityJc = value
            elif label == "<b:CityName>":
                cityName = value
            elif label == "<b:Id>":
                cityId = value
        curCity = Point.City(cityId, cityCode, cityJc, cityName)
        return curCity