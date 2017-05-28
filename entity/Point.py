from entity import Base
class Site(Base.Base):

    def __init__(self,id,area,cityCode,stationCode,uniqueCode,
                 positionName,latitude,longitude,isContrast,
                 isPublish,orderID):
        self.id = id
        self.area = area
        self.cityCode = cityCode
        self.stationCode = stationCode
        self.uniqueCode = uniqueCode
        self.positionName = positionName
        self.latitude = latitude
        self.longitude = longitude
        self.isContrast = isContrast
        self.isPublish = isPublish
        self.orderID = orderID

class City(Base.Base):
    def __init__(self,cityId,cityJc,cityCode,cityName):
        self.cityId = cityId
        self.cityJc = cityJc
        self.cityCode = cityCode
        self.cityName = cityName

