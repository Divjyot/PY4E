import string


def dicti():
    adict = dict()
    adict['l'] = [1, 2, 3]
    adict['o'] = 123
    adict['ll'] = '123'
    print(adict)
    print(adict.values())
    print('o' in adict)
    print('123' in adict)
    print('123' in adict.values())


def counting():
    word = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbccccccccccceeeeeee'
    d = dict()
    for c in word:
        d[c] = d.get(c, 0) + 1
    print(d)


def stringTransform():
    print(string.punctuation)


def exercise():
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
    d = dict()
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            d[words[1]] = d.get(words[1], 0) + 1
    max_key = 0
    max_val = 0
    for key in d.keys():
        if max_val < d[key]:
            max_val = d[key]
            max_key = key
    print(max_key, max_val)

