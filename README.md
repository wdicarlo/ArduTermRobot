# ArduTermRobot
Arduino experiments with Robot Framework

## Requirements
* [Arduino UNO](https://store.arduino.cc/arduino-uno-rev3) 
* [bitlash](https://github.com/billroy/bitlash)
* [python](https://www.python.org)
* [Robot Framework](http://robotframework.org)
* make
* linux

## Installation
Steps to do the experiments:
1. Install bitlash in the Arduino
1. Install python and robot framework
1. Clone ArduTermRobot repository
```
	git clone https://github.com/wdicarlo/ArduTermRobot.git
```
## Testing
```
	cd ArduTermRobot; make all
```

Example of output:
```
python bitlash-test.py
Connected to Arduino!!!
Sending line: stop *;print millis
stop *;print millis
2513929
> Sending line: print abs(-1), abs(0), abs(1)
print abs(-1), abs(0), abs(1)
1 0 1
Detected: 1 0 1
> Sending line: print sign(-10), sign(0), sign(10)
print sign(-10), sign(0), sign(10)
-1 0 1
> Detected: -1 0 1
Sending line: if 1 print 1; else print 0
if 1 prinDetected: 1
t 1; else print 0
1
> Sending line: if 0 print 1; else print 0
if 0 print 1; elsDetected: 0
e print 0
0
> Sending line: i=0; while i<5 {print i,"",;i++;} print;
i=0; while i<5 {print i,"",;i++;} print;
0 1 2 3 4 
> Detected: 0 1 2 3 4
Sending line: rm foo
rm foo
> Sending line: function foo {switch arg(1) {print 0,;print 1,;print 2,;}}
function foo {switch arg(1) {print 0,;print 1,;print 2,;}}
saved
Detected: saved
> Sending line: i=-2; while i<4 foo(i++); print;
i=-2; while i<4 foo(i++); print;
000122Detected: 000122

> Sending line: rm foo
rm foo
> Sending line: i=0;while i<1000 {i++; if i>100 return 4; } print i;
i=0;while i<1000 {i++; if i>100 return 4; } print i;
Detected: 4
> Sending line: q=0; while q<10 {if q&1 {print "odd ",;} else {print "even ",;} q++;} print "done";
q=0; while q<10 {if q&1 {print "odd ",;} else {print "even ",;} q++;} print "done";
even odd even odd even odd even odd even odd done
> Detected: even odd even odd even odd even odd even odd done
Sending line: t=millis;i=1000;while i {if i&1 j++; else j--; i--;} print millis-t,"done";
t=millis;i=1000;while i {if i&1 j++; else j--; i--;} print millis-t,"done";
Detected: done
633 done
> Sending line: i=-2;while i++<3 if i<=0 print 0,;else print 1,; print;
i=-2;while i++<3 if i<=0 print 0,;else print 1,; print;
00111
Detected: 00111
> Sending line: print millis
print millis
2515450
> Sending line: i=-2;while i++<3 {if i<=0 print 0,;else print 1,;} print;
i=-2;while i++<3 {if i<=0 print 0,;else print 1,;} print;
00111
> Detected: 00111
Sending line: i=0; while i<32 print br(0xaaaaaaaa,i++),; print;
i=0; while i<32 print br(0xaaaaaaaa,i++),; print;
01010101010101010101010101010101
> Detected: 01010101010101010101010101010101
Sending line: i=0; while i<32 print br(0x55555555,i++),; print;
i=0; while i<32 print br(0x55555555,i++),; print;
10101010101010101010101010101010
> Detected: 10101010101010101010101010101010
Sending line: x=0;i=0;while i<32 x=bs(x,i++); print x;
x=0;i=0;while i<32 x=bs(x,i++); print x;
-1
> Detected: -1
Sending line: x=-1;i=0;while i<32 x=bc(x,i++); print x;
x=-1;i=0;whiDetected: 0
le i<32 x=bc(x,i++); print x;
0
> Sending line: print millis
print millis
2515984
> python bitlash_arduterm.py
Ready!!!
---------------------------------------
Report of commands run on remote host.
---------------------------------------
print 'hello'
Good!!!
i=12; print i;
Good!!!
i=45; print i;
Good!!!
i=55; i++; print i;
Good!!!
i=1; while(i<6) { print i; i++; }
Good!!!
i=2; function ipp { i++; }; ipp; print i
Good!!!
ls
Good!!!
rm ipp
Good!!!
bye bye!!!
python ArduTermDemo.py
Arduino Connector: SerialConnector
> help
bitlash here! v2.0 (c) 2013 Bill Roy -type HELP- 662 bytes freehttp://bitlash.netSee LICENSE for licensePins: d0-22,a0-22  Variables: a-z, 32 bit long integersOperators: + - * / ( ) < <= > >= == != << >> ! ^ & | ++ -- :=Commands: arg boot else function help if ls peep print ps return rm run stop switch whileFunctions:abs ar aw baud bc beep br bs bw constrain delay dr dw er ew free getkey getnum inb isstr max millis min outb pinmode printf pulsein random sign snoozefadergb fadehsb setrgb red green blue setfade setaddr
python -m robot ArduTermKeywordsTests.robot
==============================================================================
ArduTermKeywordsTests :: Arduino Test cases using the keyword-driven testin...
==============================================================================
Send Print Message                                                    | PASS |
------------------------------------------------------------------------------
Send Calc Request Message                                             | PASS |
------------------------------------------------------------------------------
Send Function Example Message                                         | PASS |
------------------------------------------------------------------------------
ArduTermKeywordsTests :: Arduino Test cases using the keyword-driv... | PASS |
3 critical tests, 3 passed, 0 failed
3 tests total, 3 passed, 0 failed
==============================================================================
Output:  /home/sparky/Projects/ArduTermRobot/output.xml
Log:     /home/sparky/Projects/ArduTermRobot/log.html
Report:  /home/sparky/Projects/ArduTermRobot/report.html
python -m robot ArduTermPExpectKeywordsTests.robot
==============================================================================
ArduTermPExpectKeywordsTests :: Arduino Test cases using the keyword-driven...
==============================================================================
Send Print Message                                                    | PASS |
------------------------------------------------------------------------------
Send Calc Request Message                                             | PASS |
------------------------------------------------------------------------------
Send Function Example Message                                         | PASS |
------------------------------------------------------------------------------
ArduTermPExpectKeywordsTests :: Arduino Test cases using the keywo... | PASS |
3 critical tests, 3 passed, 0 failed
3 tests total, 3 passed, 0 failed
==============================================================================
Output:  /home/sparky/Projects/ArduTermRobot/output.xml
Log:     /home/sparky/Projects/ArduTermRobot/log.html
Report:  /home/sparky/Projects/ArduTermRobot/report.html
```
