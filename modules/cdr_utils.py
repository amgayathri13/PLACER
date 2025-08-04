"""Utility functions for identifying and targeting CDR loops"""

def parse_cdr_definition(cdr_file):
    """Parse a file containing CDR definitions in the format:
    chain:resnum1,resnum2,...
    Example: H:27,28,29,30,31,32,33,34
    
    Returns a dictionary mapping chain IDs to lists of residue numbers
    """
    cdr_residues = {}
    
    with open(cdr_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(':')
            if len(parts) != 2:
                continue
                
            chain = parts[0].strip()
            residues = [int(r.strip()) for r in parts[1].split(',')]
            
            if chain not in cdr_residues:
                cdr_residues[chain] = []
            cdr_residues[chain].extend(residues)
    
    return cdr_residues
