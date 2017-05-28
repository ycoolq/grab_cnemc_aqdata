import urllib.request
import io
from wcf  import records
from grab import BaseGrab
entitys = []
def getNbsp(levelNum):
    nbsp = ""
    i = 0
    while i<levelNum:
        nbsp += "   "
        i += 1
    return str(levelNum)+nbsp
def recluseShortElementRecord(element,grabService,levelNum):
    if(isinstance(element,records.elements.ShortElementRecord)):
        levelNum += 1
        for  i in element.__getattribute__('attributes'):
            pass
        for i in element.__getattribute__('childs'):
            if (levelNum == 3 and str(i) == grabService.tag):
                if(isinstance(grabService,BaseGrab.BaseGrab)):
                    entity = grabService.parseEntity(i)
                    entitys.append(entity)
            elif(levelNum<3):
                recluseShortElementRecord(i,grabService,levelNum)

def grab(grabService):
    entitys.clear()
    fp = urllib.request.urlopen(grabService.url)
    mybytes = fp.read()
    fp.close()
    buf = io.BytesIO(mybytes)
    buf = records.Record.parse(buf)
    levelNum = 0
    for i in buf:
        recluseShortElementRecord(i, grabService,levelNum)
    return entitys

