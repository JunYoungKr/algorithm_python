from itertools import product

def solution(word):
    
    answer = 0
    letters = ['A', 'E', 'I', 'O', 'U']
    word_array = []
    for length in range(1, 6):
        for p in product(letters, repeat=length):
            word_array.append(''.join(p))
    
    sorted_array = sorted(word_array)
    # print(sorted_array.index(word))
    return sorted_array.index(word) + 1