#!/usr/bin/env python

'''
'''

#from __future__ import print_function
#
#from __future__ import absolute_import

import os, sys, re, getopt, getpass
import pexpect


try:
    raw_input
except NameError:
    raw_input = input


#
# Some constants.
#
COMMAND_PROMPT = '[#$?>] '

def exit_with_usage():

    print(globals()['__doc__'])
    os._exit(1)

def main():

    global COMMAND_PROMPT
    ######################################################################
    ## Parse the options, arguments, get ready, etc.
    ######################################################################
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'h?', ['help','h','?'])
    except Exception as e:
        print(str(e))
        exit_with_usage()
    options = dict(optlist)
    if len(args) > 1:
        exit_with_usage()

    if [elem for elem in options if elem in ['-h','--h','-?','--?','--help']]:
        print("Help:")
        exit_with_usage()

    child = pexpect.spawn('python arduterm.py')
    #child.sendline ('help')
    #child.sendline (b'\n')
    i = child.expect([pexpect.TIMEOUT, pexpect.EOF, COMMAND_PROMPT])
    if i == 0: # Timeout
        print('ERROR! could not login with SSH. Here is what SSH said:')
        print(child.before, child.after)
        print(str(child))
        sys.exit (1)
    if i == 2:
        print ('Ready!!!')
        #child.sendline ('help')
        #child.expect (COMMAND_PROMPT)
        #print("Before: %s"%(child.before)) #
        #print("After : %s"%(child.after)) #

    # Now we should be at the command prompt and ready to run some commands.
    print('---------------------------------------')
    print('Report of commands run on remote host.')
    print('---------------------------------------')

    print ('print \'hello\'')
    child.sendline ('print \'hello\'')
    i = child.expect_exact (["hello",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('i=12; print i;')
    child.sendline ('i=12; print i;')
    i = child.expect_exact (["12",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('i=45; print i;')
    child.sendline ('i=45; print i;')
    i = child.expect_exact (["45",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('i=55; i++; print i;')
    child.sendline ('i=55; i++; print i;')
    i = child.expect_exact (["56",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('i=1; while(i<6) { print i; i++; }')
    child.sendline ('i=1; while(i<6) { print i; i++; }')
    #i = child.expect (["1\r\n2\r\n3\r\n4\r\n5",COMMAND_PROMPT])
    i = child.expect_exact (["5",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #


    print ('i=2; function ipp { i++; }; ipp; print i')
    child.sendline ('i=2; function ipp { i++; }; ipp; print i')
    i = child.expect_exact (["3",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('ls')
    child.sendline ('ls')
    i = child.expect_exact (["ipp",COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    print ('rm ipp')
    child.sendline ('rm ipp')
    i = child.expect ([COMMAND_PROMPT])
    if i == 0:
        print ("Good!!!")
    if i == 1:
        print ("Bad!!!")
        print("len: %d"%len(child.before))
        print("Before: %s"%(child.before)) #
        print("After : %s"%(child.after)) #

    # Now exit the remote host.
    child.sendline ('quit')
    i = child.expect([pexpect.EOF, "(?i)bye"])
    if i == 1:
        print("bye bye!!!")

if __name__ == "__main__":
    main()
