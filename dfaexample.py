# coding=utf-8
#!/usr/bin/env python

import sys
import logging
import json
from ndfa import DFA

dfas = []
jsonData = {}

def test(dfa, words, outFile):
    """Test function. Tests each word in input file with the provided dfa."""
    for word in words:
        try:
            dfa.test(word, outFile)
        except AssertionError as e:
            logging.error('ERROR: %s\n' % e.message)

def dfaFunc(jsonData):
    """DFA that accepts strings would print true else false"""
    states = jsonData["states"]
    alphabet = jsonData["alphabet"]
    trans = {}
    for tran in jsonData["transition"]:
        trans[(tran["current_state"], tran["next_symbol"])] = tran["new_state"]    
    transitions = trans
    start = jsonData["start_state"]
    accepts = jsonData["final_states"]
    return states, alphabet, transitions, start, accepts

if __name__ == '__main__':

    # Configure logging
    args = sys.argv[1:]
    # NFA machine file
    nfaFile = sys.argv[1]
    # input string file
    inputFile = sys.argv[2]
    # program output file
    outFile = open(sys.argv[3],"w") 
    jsonData = json.load(open(nfaFile))
    inputString = [inputString.rstrip('\n') for inputString in open(inputFile)]
    fmt = '%(message)s'
    if set(['-v', '--verbose']).isdisjoint(args):
        logging.basicConfig(level=logging.INFO, format=fmt)
    else:
        logging.basicConfig(level=logging.DEBUG, format=fmt)

    dfaFunc(jsonData);
    dfas.append((dfaFunc, inputString))
    for func, words in dfas:
        outFile.write('-' * 50+'\n')
        outFile.write('TESTING '+ jsonData["dfa_name"]+'\n')
        outFile.write('-' * 50+'\n')
        dfa = DFA(*func(jsonData))
        test(dfa, words, outFile)
