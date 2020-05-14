"""

Good inputs: 'ACGTCCCGTAGCAACATTAACCCTG', 'agctaatcccgagt', 'GATTACA'

Bad inputs: 25, 'f', 'ACGTCCCGTAGCAACATTAACCCTG', 'aCGTCCCGtAGCaACAtTAACCcTG', 'ACG7CCCGTA23CAACAT]AACCCTG'

Edge cases: '', 'a', 

"""

# NOTE: what's with exercism? All the good stuff is locked up >:/
def rna_transcription(dna_string: str):
    rna_return = ''

    for nucleotide in dna_string.upper():
        if nucleotide is 'G':
            rna_return += 'C'
        elif nucleotide is 'C':
            rna_return += 'G'
        elif nucleotide is 'T':
            rna_return += 'A'
        elif nucleotide is 'A':
            rna_return += 'U'
        else:
            raise Exception('Please enter a valid DNA nucleotide sequence.')
    return rna_return