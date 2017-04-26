import re 
import itertools

def clean(line):
    return re.sub(r'\W+', ' ', line.strip()).lower()


def count_words(cuv = 'with', path = 'shakespeare.txt'):
    count = 0
    with open(path,'r') as fis:
        word_lst = (clean(line).split() for line in fis)
        words = itertools.chain.from_iterable(word_lst)
        for word in words:
            if word == cuv:
                count += 1
    print (count)

if __name__ == '__main__':
    count_words()