def recursive_sum(sequence, i=0):
    if i == len(sequence):
        return 0
    else:
        return recursive_sum(sequence, i+1) + sequence[i]
