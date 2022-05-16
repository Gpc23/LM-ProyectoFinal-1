import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    'Accept-Language': 'en',
    'Ocp-Apim-Subscription-Key': 'key',
}

params = urllib.parse.urlencode({
})

try:
    curl = http.client.HTTPSConnection('www.haloapi.com')
    curl.request("GET", "/metadata/h5/metadata/weapons?%s" % params, "{body}", headers)
    response = curl.getresponse()
    data = response.read()
    print(data)
    curl.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror)) 