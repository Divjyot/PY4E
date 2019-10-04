import re


def find():
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        # if re.search('^From:', line):
        #    print(line)
        # if re.search('^F..m:', line):
        #    print(line)
        if re.search('^From:.+@', line):
            print(line)


# We are looking for substrings that have at least one non-whitespace character, followed by an at-sign,
# followed by at least one more non-whitespace character. The \S+ matches as many non-whitespace characters as possible.
def finall(s):
    lst = re.findall('[a-zA-Z0-9]\S*@\S*', s)
    if len(lst) > 0:
        print(lst)


def find_all():
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting 2PM@ 3PM'
    finall(s)  # would not match @2PM as there was no non-space character before @


# find_all()


def finall2(s):
    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', s)
    if len(lst) > 0:
        print(lst)


def find_all_in_file():
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        finall(line)


def finding_confidence():
    s = 'X-DSPAM-Confidence: 0023.98475'
    lst = re.findall('^X-.*: ([0-9]+[.][0-9]+)', s)
    print(lst)
    a = 'ab#)28cd'
    lst = re.findall('[^A-Za-z]+', a)
    print(lst)


def excercise(filename):
    h = open(filename)
    for line in h:
        lst = re.findall('[0-9]+', line)
        if len(lst) > 0:
            for item in lst:
                total = total + int(item)
    print(sum(lst))


excercise('regex_sum_42.txt')
excercise('regex_sum_305128.txt')
