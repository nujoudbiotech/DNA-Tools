# 🧬 Bioinformatics DNA Analysis Tool - FASTA Parser & Protein Translator

> Developed a Python-based bioinformatics tool for molecular biology analysis - Practical application for Stem Cell research and molecular genetics.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Bioinformatics](https://img.shields.io/badge/Bioinformatics-DNA_Analysis-green?style=for-the-badge&logo=dna)](https://github.com/nujoudbiotech/DNA-Tools)
[![Biotechnology](https://img.shields.io/badge/Field-Biotechnology-orange?style=for-the-badge)](https://github.com/nujoudbiotech)

## 📖 Project Overview
This tool was developed in October 2026 as a practical demonstration of computational biology skills relevant to Stem Cell research and molecular genetics.

It performs complete molecular biology analysis from DNA to Protein.

## 🛠️ Features

- ✅ **DNA Sequence Analysis & Validation** - Checks if DNA is valid (ATGC only)
- ✅ **GC Content Calculation** - Calculates %GC for stability analysis
- ✅ **DNA to RNA Transcription** - Converts DNA to RNA (T → U)
- ✅ **RNA to Protein Translation** - Using full genetic codon table (64 codons)
- ✅ **FASTA File Parsing** - Reads NCBI format FASTA files
- ✅ **Stop Codon Handling** - Correctly stops at TAA, TAG, TGA

## 🧪 Technologies
- **Python**
- **Anaconda**
- **Biopython concepts**

## 🚀 How to Use

```python
from dna_tools import validate_dna, gc_content, transcribe, translate, parse_fasta

# Example FASTA
fasta_text = """>NM_000546.6 Homo sapiens p53
ATGGAGGAGCCGCAGTCAGATCCTAGCGT"""

# 1. Parse FASTA
seqs = parse_fasta(fasta_text)

# 2. Analyze
for id, dna in seqs.items():
    print(f"Valid: {validate_dna(dna)}")
    print(f"GC%: {gc_content(dna):.2f}%")
    rna = transcribe(dna)
    protein = translate(rna)
    print(f"Protein: {protein}")
