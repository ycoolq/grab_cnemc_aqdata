class Base:

    def toString(self):
        for i in dir(self):
            if(i.__contains__("__") or i=='toString'):
                continue
            value = self.__getattribute__(i)
            print(i,end='')
            print("=",end='')
            print(value,end='')
            print(",",end='')