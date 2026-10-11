"""
Bioinformatics DNA Analysis Tool
Developed by: Nujoud | October 2026
For: Stem Cell Research & Molecular Genetics Applications
"""

# Full Codon Table
CODON_TABLE = {
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'UAU':'Y', 'UAC':'Y', 'UAA':'*', 'UAG':'*',
    'UGU':'C', 'UGC':'C', 'UGA':'*', 'UGG':'W',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

def validate_dna(sequence):
    """Validate DNA sequence"""
    valid_bases = set('ATGCatgc')
    return all(base in valid_bases for base in sequence)

def gc_content(dna_sequence):
    """Calculate GC content"""
    dna = dna_sequence.upper()
    gc = dna.count('G') + dna.count('C')
    return (gc / len(dna) * 100) if len(dna) > 0 else 0

def transcribe(dna_sequence):
    """DNA to RNA transcription"""
    return dna_sequence.upper().replace('T', 'U')

def translate(rna_sequence):
    """RNA to Protein translation with Stop Codon handling"""
    rna = rna_sequence.upper()
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3:
            break
        amino_acid = CODON_TABLE.get(codon, 'X')
        if amino_acid == '*': # Stop codon
            protein += '*'
            break
        protein += amino_acid
    return protein

def parse_fasta(fasta_text):
    """Parse FASTA format (NCBI format)"""
    sequences = {}
    current_id = ""
    for line in fasta_text.split('\n'):
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
    return sequences

# --- Example for Stem Cell Research ---
if __name__ == "__main__":
    # Example FASTA from NCBI
    fasta_example = """>NM_000546.6 Homo sapiens tumor protein p53
ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAAC
TTTTGACATAGTGTGGTGGTGCCCTATGAGCCGCCTGAGGTTGGCTGACTGT
ACCACCATCCACTACAACTACATGTGTAACAGTTCCTGCATGGGCGGCATGAA
CCGGAGGCCCATCTCCTCATCATCACACTGGAAGACTCCAGTGGTAATCTACT
GGGACGGAACAGCTTTGAGGTGCGTGTTTGTGCCTGTCCTGGGAGAGACCGG
CGCACAGAGGAAGAGAATCTCCGCAAGAAAGGGGAGCCTCACCACGAGCTGCC
CCCAGGGAGCACTAAGCGAGCACTGCCCAACAACACCAGCTCCTCTCCCCAG
CCAAAGAAGAAACCACTGGATGGAGAATATTTCACCCTTCAGATCCGTGGGCG
TGAGCGCTTCGAGATGTTCCGAGAGCTGAATGAGGCCTTGGAACTCAAGGATG
CCCAGGCTGGGAAGGAGCCAGGGGGGAGCAGGGCTCACTCCAGCCACCTGAAG
TCCAAAAAGGGTCAGTCTACCTCCCGCCATAAAAAACTCATGTTCAAGACAGA
AGGGCCTGACTCAGACTGA"""

    print("🧬 Bioinformatics DNA Analysis Tool")
    print("="*40)
    
    sequences = parse_fasta(fasta_example)
    for seq_id, dna_seq in sequences.items():
        print(f"\nID: {seq_id}")
        print(f"Valid DNA: {validate_dna(dna_seq)}")
        print(f"GC Content: {gc_content(dna_seq):.2f}%")
        
        rna = transcribe(dna_seq)
        protein = translate(rna)
        
        print(f"RNA (first 50 bases): {rna[:50]}...")
        print(f"Protein (first 50 aa): {protein[:50]}...")
        print(f"Protein Length: {len(protein)} aa")
