def gc_content(dna_sequence):
    """Calculate GC content percentage in DNA sequence"""
    dna = dna_sequence.upper()
    gc_count = dna.count('G') + dna.count('C')
    total = len(dna)
    if total == 0:
        return 0
    return (gc_count / total) * 100

def reverse_complement(dna_sequence):
    """Get reverse complement of DNA sequence"""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    dna = dna_sequence.upper()
    return ''.join(complement.get(base, base) for base in reversed(dna))

# Example
my_dna = "ATGCGCGATATATGCGC"
print(f"DNA: {my_dna}")
print(f"GC Content: {gc_content(my_dna):.2f}%")
print(f"Reverse Complement: {reverse_complement(my_dna)}")
