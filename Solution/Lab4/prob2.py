def count_until(n):
    for i in range(n):
        yield i

def count_word(word='the',path = 'shakespeare.txt'):
    count = 0
    with open(path,'r') as fis:
        x = fis.readline().replace('.', '').replace(',','').replace('/','').replace('\\','').replace(',','').strip().lower().split()
        for cuv in x:
            if cuv == word:
                count = count + 1
    return count