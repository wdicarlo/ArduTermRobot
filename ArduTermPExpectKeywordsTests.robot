*** Settings ***
Documentation     Arduino Test cases using the keyword-driven testing approach.
...
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           ArduTermPExpectRobot
Library		  ArduTermRobotUtils
Variables	  ArduTermPExpectRobotVariables.py

*** Test Cases ***
Send Print Message
    Send Message        print "${HELLO_WORLD_LABEL}"
    Result should be    ${HELLO_WORLD_LABEL}

Send Print Processed Message
    ${msg} =            Process Message 	${HELLO_WORLD_LABEL}
    Send Message        print "${msg}" 
    Result should be    arduino: ${HELLO_WORLD_LABEL}

Send Calc Request Message
    Send Message        print 3*2
    Result should be    6

Send Function Example Message
    Send Message        i=2; function ipp { i++; }; ipp; print i
    Result should be    3
