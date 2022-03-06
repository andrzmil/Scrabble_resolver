import pandas as pd

dct = pd.read_csv('dictionary.txt', header=None)
words = dct[0].tolist()
words = [x.upper() for x in words]
sorted_words = [''.join(sorted(x)) for x in words]

itr = 0 

while itr < 10000000:

    print("Your letters:")
    curr_lt = input().upper()
    print("Additional letters:")
    add_lt = input().upper()
    curr_lt_sorted = ''.join(sorted(''.join([curr_lt,add_lt])))

    for cnt, sw in enumerate(sorted_words):
        if sw in curr_lt_sorted:
            print('{} / {} -> {}'.format(curr_lt, add_lt, words[cnt]))
          
        
    