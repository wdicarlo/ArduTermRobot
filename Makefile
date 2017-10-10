# Makefile for ArduTerm experiments
#
#
ROBOT=python -m robot

all: bitlash-test bitlash_arduterm ArduTermDemo ArduTermKeywordsTests ArduTermPExpectKeywordsTests

tests: test1 test2

bitlash-test: bitlash-test.py
	python $<

bitlash_arduterm: bitlash_arduterm.py
	python $<

ArduTermDemo: ArduTermDemo.py
	python $<

ArduTermKeywordsTests: ArduTermKeywordsTests.robot
	$(ROBOT) $<

ArduTermPExpectKeywordsTests: ArduTermPExpectKeywordsTests.robot
	$(ROBOT) $<

test1: ArduTermRobotVariables.py
	$(ROBOT) -t "send print message" --variablefile $< --name ArduTermRobotVariables --outputdir test1 ArduTermPExpectKeywordsTests.robot 

test2: ArduTermPExpectRobotVariables.py
	$(ROBOT) -t "send print message" --variablefile $< --name ArduTermPExpectRobotVariables --outputdir test2 ArduTermPExpectKeywordsTests.robot 

clean:
	-@rm -rf *.log screenlog.* *.html *.pyc *.txt output.xml test1 test2
