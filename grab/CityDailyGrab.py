from wcf  import records
from grab import BaseGrab
from entity import Data
from const import Consts
class CityDailyGrab(BaseGrab.BaseGrab):
    '城市日报抓取服务'

    tag = Consts.CITY_DAILY_TAG

    def parseEntity(self, element):
        if (isinstance(element, records.elements.ShortElementRecord) == False):
            return
        id = aqi = area = cityCode = timePoint = \
        so2_24h = co_24h = no2_24h = o3_8h_24h = pm10_24h = pm2_5_24h = \
        quality =  primaryPollutant = measure = unheathful = None


        for i in element.__getattribute__("childs"):
            label = str(i)
            value = str(i.__getattribute__('childs')[0])
            if label == "<b:AQI>":
                aqi = value
            elif label == "<b:Area>":
                area = value
            elif label == "<b:CO_24h>":
                co_24h = value
            elif label == "<b:CityCode>":
                cityCode = value
            elif label == "<b:Id>":
                id = value
            elif label == "<b:Measure>":
                measure = value
            elif label == "<b:NO2_24h>":
                no2_24h = value
            elif label == "<b:O3_8h_24h>":
                o3_8h_24h = value
            elif label == "<b:PM10_24h>":
                pm10_24h = value
            elif label == "<b:PM2_5_24h>":
                pm2_5_24h = value
            elif label == "<b:PrimaryPollutant>":
                primaryPollutant = value
            elif label == "<b:Quality>":
                quality = value
            elif label == "<b:SO2_24h>":
                so2_24h = value
            elif label == "<b:TimePoint>":
                timePoint = value
            elif label == "<b:Unheathful>":
                unheathful = value
            curData = Data.CityDailyAqi(id,aqi,area,cityCode,timePoint,
                 so2_24h,co_24h,no2_24h,o3_8h_24h,pm10_24h,pm2_5_24h,
                 quality,primaryPollutant,measure,unheathful)
        # print(curCity.toString())
        return curData
