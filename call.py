from const import Urls
from grab import CityGrab
from grab import SiteGrab
from utils import GrabUtil

grabService = CityGrab.CityGrab(Urls.GET_CITY_URL)
#grabService = SiteGrab.SiteGrab(Urls.GET_SITE_URL)
#grabService = SiteGrab.SiteGrab(Urls.GET_CITY_DAILY_AQI)
entitys = GrabUtil.grab(grabService)
for entity in entitys:
    print(entity.toString())

