# Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence. (copy this code from Lab 21 to Lab 22 folder)

def analyse_dna_decorator(func):
    def wrapper(sequence):
        gc = sequence.count('G') + sequence.count('C')
        percentage = (gc / len(sequence)) * 100

        print(f"GC Content: {percentage}%")

        if percentage > 50:
            print("GC rich sequence")
        else:
            print("AT rich sequence")

        return func(sequence)
    return wrapper

@analyse_dna_decorator
def analyse_dna(sequence):
    return sequence

analyse_dna("ATGCGTACGTCA")
