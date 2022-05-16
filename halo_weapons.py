import http.client, urllib.request, urllib.parse, urllib.error, base64

cabezera = {
    'Accept-Language': 'en',
    'Ocp-Apim-Subscription-Key': 'key',
}

parametros = urllib.parse.urlencode({
})

try:
    curl = http.client.HTTPSConnection('www.haloapi.com')
    curl.request("GET", "/metadata/h5/metadata/weapons?%s" % parametros, "{body}", cabezera)
    response = curl.getresponse()
    data = response.read()
    print(data)
    curl.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror)) 