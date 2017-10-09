import os, sys, re, getopt, getpass
import pexpect

#
# Some constants.
#
COMMAND_PROMPT = '[#$?>] '

class ArduTermPExpectRobot(object):
    """Test library for testing *Arduino* business logic.

    """

    def __init__(self):
        self._arduino = pexpect.spawn('python arduterm.py')
        i = self._arduino.expect([pexpect.TIMEOUT, pexpect.EOF, COMMAND_PROMPT])
        if i == 0: # Timeout
            print('Timeout!!!')
            sys.exit (1)
        if i == 2:
            print ('Ready!!!')

    def send_message(self, msg):
        """Send the specified ``msg``.

        Examples:
        | Send Message | help |
        | Send Message | help gpio |

        """
        self._arduino.sendline(msg)

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Send Message     | help |
        | Result Should Be | This is the help |
        """
        self._result = self._arduino.expect_exact ([expected,COMMAND_PROMPT])
        if self._result != 0:
            raise AssertionError('%s: not received' % (expected))

    def get_expected_error(self, expected):
        self._result = None
        i = self._arduino.expect_exact([pexpect.TIMEOUT, expected, COMMAND_PROMPT])
        if i == 0: # Timeout
            print("Timeout!!!")
            sys.exit (1)
        if i == 1:
            self._result = expected
        return self._result
