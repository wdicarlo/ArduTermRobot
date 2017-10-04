from Connector import Connector

class Arduino:

    def __init__(self,connector):
        if isinstance(connector,Connector) == False: 
            raise ValueError("Bad Connector")
        self._connector = connector

    def getConnectorName(self):
        return self._connector.getName()

    def send(self,msg):
        return self._connector.send(msg)

