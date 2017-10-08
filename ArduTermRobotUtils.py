
class ArduTermRobotUtils(object):
    def __init__(self):
        self._name = "arduino"

    def process_message(self, msg):
        return self._name + ": " + msg
