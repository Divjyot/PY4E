astring = 'abcdefghijklmnopqrstuvwxyz'


def astringFunc():
    for l in astring:
        print(l, l.upper())
    print(astring[:])  # [inclusive, exclusive]
    print('a' in astring)
    print('ab' in astring)
    print('ax' in astring)


def astringFunc2():
    # Python does not handle uppercase and lowercase letters the same way that people do.
    # All the uppercase letters come before all the lowercase letters
    while True:
        word = input("Enter a word ")
        if word == 'done':
            break
        astring = 'Your word, Pineapple, comes before banana.'
        if word < 'banana':
            print('Your word,' + word + ', comes before banana.')
        elif word > 'banana':
            print('Your word,' + word + ', comes after banana.')
        else:
            print('All right, bananas.')


def astringFunc3():
    word = 'Banana'
    print(word.find('z'))  # returns index
    print(word.find('an'))
    print(word.find('an', 3))  # Find 'an' starting from index 3
    print(word.find('na', 3))
    print('find(b) ',  word.find('b'))
    print(word.startswith('b'))
    word = word.lower()
    print('find(b) ',  word.find('b'))
    print(word.startswith('h'))
    print(word.startswith('b'))


def findPost():
    data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
    atPosInx = data.find('@')
    spacePosAfterAtInx = data.find(' ', atPosInx)
    print(data[atPosInx + 1: spacePosAfterAtInx])


def StringFormatSpecifier():
    noOfKoalas = 52
    aword = 'I have %d %s with avarage height of %g cm' % (
        noOfKoalas, 'Koalas', 65.8)
    print(aword)


def ExtractFloat():
    data = 'X-DSPAM-Confidence:0.8475'
    colon_pos = data.find(':')
    floatVal = float(data[colon_pos+1:])
    print(floatVal)
