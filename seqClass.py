#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser 

# to receive arguments from the user
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search for in the sequence")

# if not, help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# convert to upper case 
args.seq = args.seq.upper()

# function to calculate percentage of each nucleotide in the sequence
def calculate_percentage(sequence, nucleotide):
    return (sequence.count(nucleotide) / len(sequence)) * 100
    
# check if it is DNA, RNA, or neither
if re.search('^[ACGT]+$', args.seq):  # Check if it contains only A, C, G, T
    print('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):  # Check if it contains only A, C, G, U (for RNA)
    print('The sequence is RNA')
else:
    print('The sequence is neither DNA nor RNA')

# if a motif is provided, search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()  # Convert motif to uppercase for consistency
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"')
    if re.search(args.motif, args.seq):
        print("Motif FOUND")
    else:
        print("Motif NOT FOUND")

# calculate and print the percentage of each nucleotide in the sequence
if 'A' in args.seq:
    print(f"Percentage of A: {calculate_percentage(args.seq, 'A'):.2f}%")
if 'T' in args.seq:
    print(f"Percentage of T: {calculate_percentage(args.seq, 'T'):.2f}%")
if 'C' in args.seq:
    print(f"Percentage of C: {calculate_percentage(args.seq, 'C'):.2f}%")
if 'G' in args.seq:
    print(f"Percentage of G: {calculate_percentage(args.seq, 'G'):.2f}%")
if 'U' in args.seq:
    print(f"Percentage of U: {calculate_percentage(args.seq, 'U'):.2f}%")

