# Regular insertion sort (increasing order)
def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and key < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key


# Regular insertion sort (decreasing order)
def insertion_sort_dec(seq):
    print(seq)
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] < key:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key
    print(seq)


# A Recursive insertion sort
# Here we start from the end of the array and go down swapping when necessary
# The idea is to assume that the sub array from 0 to i-1 is already sorted
# So the only thing left to do is to place the item at i in the correct place
def ins_sort_rec_helper(seq, i):
    if i == 0:
        return 
    ins_sort_rec_helper(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

def ins_sort_rec(seq):
    ins_sort_rec_helper(seq, len(seq)-1)
    return seq

if __name__ == "__main__":
    insertion_sort_dec([2, 3, 4, 5, 1, 7])
