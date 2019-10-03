def cheese():
    cheeses = ['Cheddar', 'Edam', 'Gouda']
    print('0\t: ', cheeses[0])
    print('1\t: ', cheeses[1])
    print('2\t: ', cheeses[2])
    print('-1\t: ', cheeses[-1])
    print('-2\t: ', cheeses[-2])
    print('-3\t: ', cheeses[-3])

##########################################################


def nested_lists():
    alist = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

    for item in alist:
        if type(item) is list:
            for item2 in item:
                print(item2)
        else:
            print(item)

##########################################################


def list_operations():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)
    # print(a + 1) <-- throws error TypeError: can only concatenate list (not "int") to list
    print(3 * a)


def list_operations2():
    a = [1, 2, 3]
    b = [4, 5, 6]
    a.extend(b)  # extends a with elements from b
    print(a)

    a.append(100)  # appends 100 to end
    print(a)

    a.append(b)  # appends b as a list
    print(a)

    popped = a.pop(2)
    print(a)
    print(popped)

    del a[0]
    print(a)

    a.remove(100)
    print(a)

    del a[:2]
    print(a)

##########################################################


def list_slices():
    t = ['a', 'b', 'c', 'd', 'e', 'f']
    t[1:3] = ['x', 'y']
    print(t)

##########################################################


def list_functions():
    nums = [3, 41, 12, 9, 74, 15]
    print('length:', len(nums), ' max:', max(nums),
          ' min:', min(nums), 'sums:', sum(nums))

##########################################################


def convertions():
    s = 'spam'
    print(s)
    t = list(s)
    print(t)

    s = 'I got spam'
    t = s.split()
    print(t)

    s = 'spam-spam-spam'
    t = s.split('-')
    print(t)

    delemiter = ' love '
    result = delemiter.join(t)
    print(result)

##########################################################


def Aliasing():
    # Equivalent is when two lists contains same objects
    # Identical is when two objects are same.

    a = 'spam'
    b = 'spam'
    print(a is b)

    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a is b)

    a = [1, 2, 3]
    b = a
    print(a is b)

    b[0] = 100
    print(a)

##########################################################


def delete_head(t):  # t is passed as reference
    del t[0]  # return t[1:]


def bad_delete_head(t):
    t = t[1:]  # that means this do not changed the 't' reference object
    print(t)


def list_arguments():
    letters = ['a', 'b', 'c']
    delete_head(letters)
    print(letters)
    bad_delete_head(letters)
    print('Should be [\'c\']!  Result:', letters)


def modify_vs_create_list():
    t1 = [1, 2, 3]
    c = t1.append(100)  # append return null
    print(c)  # = None
    c = t1
    print(c)

    t2 = t1 + [100]
    print(t2 is t1)


def split():
    s = ' z x y b  c a    '
    t = s.split()
    print('>>>', t, '<<<')
    t.sort()
    print(t)


def exercise1():
    #fname = input("Enter file name: ")
    fh = open('romeo.txt')
    lst = list()
    for line in fh:
        words = line.split()
        for word in words:
            if word in lst:
                continue
            lst.append(word)
    lst.sort()
    print(lst)


def exercise2():
    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "mbox-short.txt"

    fh = open(fname)
    count = 0
    for line in fh:
        if line.startswith('From '):
            lst = line.split()
            if len(lst) > 1:
                print(lst[1])
                count = count + 1

    print("There were", count, "lines in the file with From as the first word")


exercise2()
