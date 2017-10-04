# Makefile for ArduTerm experiments
#
#
ROBOT=python -m robot

all: bitlash-test bitlash_arduterm ArduTermDemo ArduTermKeywordsTests ArduTermPExpectKeywordsTests

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

clean:
	-@rm -f *.log screenlog.* *.html *.pyc *.txt
