
class BaseGrab:
    '抓取基类'

    tag = None
    def __init__(self,url):
        self.url = url
    def parseEntity(self,element):
        return None
    def getEntityTag(self):
        return self.tag