from bs4 import BeautifulSoup
import ssl
import re
import urllib.error
import urllib.parse
import urllib.request
import time
import socket


def Simulate_Web_Brower(urlLink):
    mysock = socket.socket()
    mysock.connect(('data.pr4e.org', 80))
    # \r\n means end of line and \r\n\r\n means nothign between two end of line sequence.
    cmd = ('GET ' + urlLink + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        # receives data in 512-character chunks from the socket
        data = mysock.recv(512)
        if len(data) < 1:  # untill there is no data left
            break
        print(data.decode(), end='')

# Simulate_Web_Brower('http://data.pr4e.org/intro-short.txt')


def download_image():
    HOST = 'data.pr4e.org'
    PORT = 80
    mysock = socket.socket()
    mysock.connect((HOST, PORT))
    mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
    count = 0
    picture = b""

    # receiving data
    while True:
        data = mysock.recv(5120)
        if len(data) < 1:
            break
        time.sleep(0.25)
        count = count + len(data)
        print(len(data), count)
        picture = picture + data

    mysock.close()

    # Look for the end of the header (2 CRLF)
    pos = picture.find(b"\r\n\r\n")
    print('Header length', pos)
    print(picture[:pos].decode())

    # Skip past the header and save the picture data
    picture = picture[pos+4:]  # (2 CRLF) each size 2
    fhand = open("stuff.jpg", "wb")
    fhand.write(picture)
    fhand.close()


###################### using urllib ######################
def reading_webpages_using_urllib():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())


def reading_binary_files_using_urllib1():
    img = urllib.request.urlopen(
        'http://data.pr4e.org/cover3.jpg').read()  # reading in one go
    fhand = open('cover3.jpg', 'wb')
    fhand.write(img)
    fhand.close()


def reading_binary_files_using_urllib2():  # reading in batches
    img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
    fhand = open('cover3.jpg', 'wb')
    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1:
            break
        size = size + len(info)
        fhand.write(info)
    print(size, 'copied!')
    fhand.close()

# > A thing to implement: Google spider / web scraping.... visitng a page and then going to all links that page contains and so on.


# Parsing web pages using regular expressions ######################################################

def give_me_simple_web_page():
    a = """<h1>The First Page</h1>
        <p>
            If you like, you can switch to the
            <a href="http://www.dr-chuck.com/page2.htm">
            <a href="">
            Second Page</a>.
        </p>"""
    return a


def parse_simple_html(regex_str, str_to_parse):
    href = regex_str
    lst = re.findall(href, str_to_parse)
    print("Regex:\t", regex_str)
    for ex in lst:
        print("Value:\t", ex)
    print("\n\n")


'''
re = "http[s]?://.+?"

    http[s]?  means find either http or https, ie. http followed by zero or more 's'

    .+? means one or more characters in non-greedy fashion i.e. smallest possible matching string
        and greedy is when mtach tries to find the largest possible matching string.
'''


def parsing_many():
    parse_simple_html("http[s]?://.+?", give_me_simple_web_page())
    parse_simple_html("http[s]?://.+", give_me_simple_web_page())
    parse_simple_html("href=\"(.*)\"", give_me_simple_web_page())
    parse_simple_html("href=\"(.+)\"", give_me_simple_web_page())


def print_decoded(patternBytes, html):
    links = re.findall(patternBytes, html)
    for link in links:
        print(link.decode())


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def findall_links(patternBytes):
    url = "https://docs.python.org"
    html = urllib.request.urlopen(url).read()
    print_decoded(patternBytes, html)


# findall_links(b'href=\"(.*)\"')
# print("##########################################################################")
# findall_links(b'href="(http[s]?://.*?)"')

def using_bs(url, tag_to_find):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup(tag_to_find)
    for tag in tags:
        # Look at the parts of a tag
        print('TAG:', tag)
        print('URL:', tag.get('href', None))
        print('Contents:', tag.contents[0])
        print('Attrs:', tag.attrs)
        print("\n\n")

# using_bs("https://docs.python.org", 'a')


def excersie(url, tag_to_find):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup(tag_to_find)
    num_lst = list()
    for tag in tags:
        # Look at the parts of a tag
        print('TAG:', tag)
        print('Contents:', tag.contents)
        num_lst.append(int(tag.contents[0]))
        print("\n\n")
    return sum(num_lst)

# print(excersie('http://py4e-data.dr-chuck.net/comments_42.html', 'span'))
# print(excersie('http://py4e-data.dr-chuck.net/comments_305130.html', 'span'))


def extract_values(url, tag_to_find, attribute):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup(tag_to_find)
    lst = list()
    for tag in tags:
        # Look at the parts of a tag
        # print('TAG:', tag)
        # print('Contents:', tag.contents)
        lst.append(tag.get(attribute, None))
        # print("\n\n")
    return lst



def exercise2(inURL, inPos, inCount):
    url = input("Enter URL:")
    count = input("Enter count:")
    position = input("Enter position:")

    if len(url) < 1:
        url = inURL
    if len(count) < 1:
        count = inCount
    if len(position) < 1:
        position = inPos
    while count > 0:
        newlst = extract_values(url, 'a', 'href')
        url = newlst[position-1]
        print(url)
        count -= 1

    name = re.findall('http://.*known_by_(.*).html', url)
    print(name[0])


exercise2('http://py4e-data.dr-chuck.net/known_by_Fikret.html', 3, 4)
exercise2('http://py4e-data.dr-chuck.net/known_by_Elivia.html', 18, 7)
