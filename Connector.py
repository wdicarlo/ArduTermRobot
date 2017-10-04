class Connector:

    def __init__(self,name):
        self._name = name

    def getName(self):
        return self._name

    def send(self,msg):
        return "None"


