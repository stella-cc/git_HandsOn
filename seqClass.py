#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser 

# to recieve arguments from the user
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# if not, help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# convert to upper case 
args.seq = args.seq.upper()

# check if is dna or rna
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

