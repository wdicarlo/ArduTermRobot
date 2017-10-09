*** Settings ***
Documentation     Example test cases using the data-driven testing approach.
...
...               The _data-driven_ style works well when you need to repeat
...               the same workflow multiple times.
...
...               Tests use ``ExecCommand`` keyword created in this file, that in
...               turn uses keywords in ``CalculatorLibrary.py``. An exception
...               is the last test that has a custom _template keyword_.
...
...               Notice that one of these tests fails on purpose to show how
...               failures look like.
Test Template     ExecCommand
Library           ArduTermPExpectRobot

*** Test Cases ***    Expression    	Expected
Addition              print 12 + 2 + 2    16
                      print 2 + -3        -1

Subtraction           print 12 - 2 - 2    8
                      print 2 - -3        5

Multiplication        print 12 * 2 * 2    48
                      print 2 * -3        -6

Division              print 12 / 2 / 2    3
                      print -6 / 2        -3

Failing               print 1 + 1         3

Command error         [Template]    	Command should fail
                      print 1 + "k" 	unexpected number
                      print 1 / $   	unexpected char

*** Keywords ***
ExecCommand
    [Arguments]    	${expression}    ${expected}
    Send Message	${expression}
    Result should be    ${expected}

Command should fail
    [Arguments]    	${expression}    	${expected}
    		     	Send Message     	${expression}
    ${error} = 		Get Expected Error      ${expected}
    Should be equal    	${expected}    	 ${error}    # Using `BuiltIn` keyword
