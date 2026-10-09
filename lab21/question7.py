# #Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence.

def analyse_dna(sequence):
    def GC_content():
        GC=sequence.count("G")+sequence.count("c")
        return (GC/len(sequence))*100
    Percentage=GC_content()
    if Percentage > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
    print(f"GC% in a sequence is {GC_content()} that is less than 50")
(analyse_dna("ATGCATCG"))