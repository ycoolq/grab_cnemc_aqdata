class CityDailyAqi:

    def __init__(self,id,aqi,area,cityCode,timePoint,
                 so2_24h,co_24h,no2_24h,o3_8h_24h,pm10_24h,pm2_5_24h,
                 quality,primaryPollutant,measure,unheathful):
        self.id = id
        self.aqi = aqi
        self.area = area
        self.cityCode = cityCode
        self.timePoint = timePoint
        self.so2_24h = so2_24h
        self.co_24h = co_24h
        self.no2_24h = no2_24h
        self.o3_8h_24h = o3_8h_24h
        self.pm2_5_24h = pm2_5_24h
        self.pm10_24h = pm10_24h
        self.quality = quality
        self.primaryPollutant = primaryPollutant
        self.measure = measure
        self.unheathful = unheathful