def tupleFunc():
    t = 1, 2, 3, 4
    print(t)

    t = (9, 0, 8, 7, 6)
    print(t)

    t = 9,
    print(t)
    t = (9,)
    print(t)

    t = tuple()
    print(t)

    # t = tuple(1234)# < --- Error: TypeError: 'int' object is not iterable
    # print(t)

    t = tuple('spam spam')
    print(t[2])
    print(t[:6])  # from index 0 to index 5


def comparingTuples():
    a = (0, 1, 2) < (0, 3, 4)
    print(a)


def DSU():
    txt = 'but soft what light in yonder window breaks'
    words = txt.split()
    t = list()
    for word in words:
        tupple = (len(word), word)
        t.append(tupple)

    print(t)
    t.sort(reverse=True)

    result = list()
    for length, word in t:  # iterate over list of tuples with access to each item in a tuple
        result.append(word)

    print(result)


def tuple_assignment():
    m = ['spam1', 'spam2']
    x, y = m
    print(x)
    print(y)
    print('-----')
    m = ('spam3', 'spam4')
    x, y = m
    print(x)
    print(y)
    print('-----')
    m = ('spam3', 'spam4')
    (x, y) = m
    print(x)
    print(y)
    print('-----')
    x, y = y, x
    print(x)
    print(y)

    address = "spam@hotmail.com"
    user, domain = address.split("@")
    print(user, "...", domain)


def dict_and_tuples():
    d = {'z': 10, 'b': 1, 'c': 22}
    t = list(d.items())
    print(t)
    t.sort()
    print(t)


def sosrt():
    d = {'z': 10, 'b': 1, 'c': 22}
    al1 = list()
    al2 = list()
    for key, value in list(d.items()):
        al1.append((key, value))
        al2.append((value, key))
    al1.sort()
    print(al1)
    al2.sort()
    print(al2)


def composites():
    first = 'Mr'
    last = 'Spammer'
    number = 1234567890
    dicti = dict()
    dicti[last, first] = number
    dicti["last", "first"] = number

    for key in dicti:
        print("Key:", key, " and Value:", dicti[key])

    for last, first in dicti:
        print("Key:", last, first, "and Value:", dicti[last, first])


def exercise():
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
    d = dict()
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            if len(words) > 4:
                word = words[5]
                timeLst = word.split(':')
                d[timeLst[0]] = d.get(timeLst[0], 0) + 1
    t = list(d.items())
    t.sort()

    for hour, count in t:
        print(hour, count)
