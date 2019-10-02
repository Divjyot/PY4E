astring = 'abcdefghijklmnopqrstuvwxyz'


def astringFunc():
    for l in astring:
        print(l, l.upper())
    print(astring[:])  # [inclusive, exclusive]


print('ab' in astring)
