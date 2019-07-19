import sys
import json
import array
import traceback
import os

##########################################################################################
# sttConfidenceExtractor.py
#
# Converts a file with JSON on a line into a nodes visited summary
#
##########################################################################################

def findInWA(filename:str):
    with open(filename, 'r') as myfile:
        data=myfile.read()

    lines = json.loads(data)

    #Start in the dialog nodes section
    for line in lines['dialog_nodes']:
        #Is the node a response condition
        if line['type'] == "response_condition":
            #Make sure the conditions key exists
            if 'conditions' in line:
                #Look for a specific condition
                if line['conditions'] == "$retryCounter >= $maxTries":
                    #Print node info when action object is not configured
                    if 'action' not in line:
                        print(line)

def main():
    findInWA(sys.argv[1])


if __name__ == '__main__':
    if(len(sys.argv) < 1):
        print("ERROR: Required arguments: filename")
        exit()
main()
