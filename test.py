########### Python 2.7 #############
import httplib, urllib, base64

headers = {
# Request headers
	'Content-Type': 'application/json',
	'Ocp-Apim-Subscription-Key': '984d1b67b5f64968b4f7a1a8fd322bd7',
}

params = urllib.urlencode({
# Request parameters
})

try:
	conn = httplib.HTTPSConnection('api.projectoxford.ai')
	conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{body}", headers)
	response = conn.getresponse()
	data = response.read()
	print(data)
	conn.close()
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
