Abstract: Deterministic finite automata implemented in python

    Please read following steps to successfully run the program

    Finite state machine implementations

    'ndfa.py' currently contains a DFA class.

Requirement: Python must be installed in your system to run this code.

Run: Run the follwing command in your command line(Terminal).

    Run Script: python dfaexample.py machine/m4/m4.dfa  machine/m4/m4.in machine/m4/m4.out

    Here dfaexample.py is main program and it will take there argument.
        - First argument is file which contains DFA machine in JSON format(.dfa file).
        - Second argument is file that contains DFA input string(.in file).
        - Third argument file is output file generated from program(.out file).
    
    machine folder contains all dfa example and its input, output and dfa files.

    To run this code, you must provide three file as argument in order.

    folder m3 and m4 contains 1.6 b and c from homework 2.


The DFA class uses the python logging module. To see basic output, set log
level to INFO:

    By running with verbose option, you can get more detail description of the DFA.

    DEBUG for more verbose output:

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    >>> dfa.test('aba')
    Testing word "aba"...
    Initial state: 0
    Current symbol: a
    New state: 1
    Current symbol: b
    New state: 1
    Current symbol: a
    New state: 0
    Final state: 0
    Accepted: True

