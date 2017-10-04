from Arduino import Arduino
from SerialConnector import SerialConnector

c = SerialConnector()
a = Arduino(c)

print("Arduino Connector: " + a.getConnectorName())

print("> help")
print(a.send("help"))

