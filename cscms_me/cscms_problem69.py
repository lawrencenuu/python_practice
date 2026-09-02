rna = str(input()).upper() 
patterns = [rna[i:i+3] for i in range(0, len(rna), 3)]

# leu =['CUU', 'CUC', 'CUA', 'CUG']
# pro =['CCU', 'CCC', 'CCA', 'CCG']
# his =['CAC', 'CAU']
# gln =['CAA', 'CAG']
# arg =['CGU', 'CGC', 'CGA', 'CGG']

# count=[0,0,0,0,0]

# for pattern in patterns: 
#     if pattern in leu:
#         count[0] += 1
#     elif pattern in pro:
#         count[1] += 1
#     elif pattern in his:
#         count[2] += 1
#     elif pattern in gln:
#         count[3] += 1
#     elif pattern in arg:
#         count[4] += 1 

# print(*count)

codons = {
    'CUU': 'leu',
    'CUC': 'leu',
    'CUA': 'leu',
    'CUG': 'leu',

    'CCU': 'pro',
    'CCC': 'pro',
    'CCA': 'pro',
    'CCG': 'pro',

    'CAC': 'his',
    'CAU': 'his',

    'CAA': 'gln',
    'CAG': 'gln',

    'CGU': 'arg',
    'CGC': 'arg',
    'CGA': 'arg',
    'CGG': 'arg'
}

count = {
    'leu': 0,
    'pro': 0,
    'his': 0,
    'gln': 0,
    'arg': 0
}

for pattern in patterns:
    if pattern in codons:
        amino_acid = codons[pattern]
        count[amino_acid] += 1

print(*count.values())