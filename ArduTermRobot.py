from Arduino import Arduino
from Singleton import Singleton
from SerialConnector import SerialConnector


class ArduTermRobot(object):
    """Test library for testing *Arduino* business logic.

    """

    def __init__(self):
        c = Singleton(SerialConnector)
        self._arduino = Arduino(c)
        self._result = ''

    def send_message(self, msg):
        """Send the specified ``msg``.

        Examples:
        | Send Message | help |
        | Send Message | help gpio |

        """
        self._result = self._arduino.send(msg)

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Send Message     | help |
        | Result Should Be | This is the help |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

