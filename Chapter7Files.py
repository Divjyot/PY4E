
# program can count the lines in any size file using very little memory since each line is read, counted, and then discarded.


def line_by_line_reader():
    try:
        fileHandler = open('mbox.txt')
    except:
        print('File doesnt exists')
        exit()

    count = 0
    for line in fileHandler:
        count = count + 1
    print('Lines in mbox.txt ', count)


def collective_file_reader():
    try:
        fileHandler = open('mbox.txt')
        filedata = fileHandler.read()
        print('Characters in mbox.txt 1', len(filedata))
        print('Characters in mbox.txt 2 ', len(fileHandler.read()))
    except:
        print('File doesnt exists')


def searching_through_file():
    try:
        fileHandler = open('mbox.txt')
    except:
        print('File doesnt exists')
        exit()
    count = 0
    for line in fileHandler:
        if(line.startswith('From: ')):
            count = count + 1
            print(line.rstrip())
    print(count)


def writing_files():
    fout = open('output.txt', 'w')
    line = 'Koalas are always with spam again\n'
    fout.write(line)
    fout.close()


def reading_strings_with_escape_characters():
    s = '1\n2\t3\r\n4'
    print(s)
    print(repr(s))


def exercise():
    # Use the file name mbox-short.txt as the file name
    fname = input("Enter file name: ")
    total = 0.0
    count = 0
    try:
        fh = open(fname)
    except:
        print('File doesnt exsits!')
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        count = count + 1
        colon_pos = line.find(':')
        total = total + float(line[colon_pos+1:])
    if count == 0:
        print('Error')
        exit()
    print('Average spam confidence: %s' % str(round(total/count, 12)))


exercise()
