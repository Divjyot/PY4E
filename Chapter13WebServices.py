import urllib.error
import urllib.parse
import urllib.request
import ssl
import json
import xml.etree.ElementTree as ET

xmldata = '''
    <person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>'''

xmldata2 = '''
    <stuff>
    <users>
        <user x="2">
        <id>001</id>
        <name>Chuck</name>
        </user>
        <user x="7">
        <id>009</id>
        <name>Brent</name>
        </user>
    </users>
    </stuff>'''


def print_Name_Attr(data):
    tree = ET.fromstring(data)
    print('Name:', tree.find('name').text)
    print('Attr:', tree.find('email').get('hide'))


def more_find(data):
    tree = ET.fromstring(data)
    lst = tree.findall('users/user')
    print('User :', lst)
    print('User count:', len(lst))

    for item in lst:
        print('Name', item.find('name').text)
        print('Id', item.find('id').text)
        print('Attribute', item.get('x'))

# more_find(xmldata2)

##########################################################################
# JSON


data2 = '''

[
  { "id" : "001", 
    "x" : "2",
    "name" : "Sal" 
  } ,
  { "id" : "002",
    "x" : "3",
    "name" : "Sally" 
  }
]'''


jsonData = json.loads(data2)
for item in jsonData:
    print(item)
    print(item["id"])
    print(item["x"])
    print(item["name"])


###############################################################################
def GoogleWebService():
    api_key = False
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        parms = dict()
        parms['address'] = address
        if api_key is not False:
            parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(json.dumps(js, indent=4))

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)


def exercise1():
    address = input('Enter location: ')

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    comments = tree.find("comments")
    i = 0
    summ = 0
    for comment in comments:
        count = comment.find("count").text
        print(count)
        i = i + 1
        summ = summ + int(count)
    print("Count:", i)
    print("Sum:", summ)

    # counts = tree.findall('.//count')
    # countsInt = (lambda x: int(x.text) for x in counts)

    # print("Count:", len(counts))
    # print("Sum:", sum(countsInt))


def exercise2():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        print('Retrieving', address)
        uh = urllib.request.urlopen(address, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)

        lst = list()
        for item in js["comments"]:
            lst.append(item["count"])

        print("Count:", len(lst))
        print("Sum:", sum(lst))


def exercise3():
    api_key = False
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        parms = dict()
        parms['address'] = address
        if api_key is not False:
            parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(json.dumps(js, indent=4))
        placeID = js["results"][0]["place_id"]
        print(placeID)


exercise3()
