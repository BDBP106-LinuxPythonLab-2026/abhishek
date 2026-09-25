# A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
# sequence called a codon. For example, the sequence fragment AGTCTTATATCT con-
# tains the codons AGT, CTT, ATA, TCT if read from the first position. If read from
# the second position, it yields the codons GTC, TTA, TAT and if read from the third
# position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
# 3-letter strings given a sequence and from what position (input as an integer) the se-
# quence should be read. As an example, output the 3-letter strings from the sequence
# GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position?
def extract_codons(sequence, start):
    codons = []

    for i in range(start, len(sequence) - 2, 3):  # Start from position(0th index) and move 3 places each time
        codons.append(sequence[i:i+3])  # Take 3 letters at a time

    return codons

print(extract_codons("GTTTCGATTATAACG",0))
print(extract_codons("GTTTCGATTATAACG",2))

