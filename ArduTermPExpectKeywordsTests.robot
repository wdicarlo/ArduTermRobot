*** Settings ***
Documentation     Arduino Test cases using the keyword-driven testing approach.
...
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           ArduTermPExpectRobot.py

*** Test Cases ***
Send Print Message
    Send Message        print "hello"
    Result should be    hello

Send Calc Request Message
    Send Message        print 3*2
    Result should be    6

Send Function Example Message
    Send Message        i=2; function ipp { i++; }; ipp; print i
    Result should be    3
