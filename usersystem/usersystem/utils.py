
import httplib2
from urllib.parse import urlencode



def http_get(url, result_decoder="utf-8"):
	http = httplib2.Http()
	response, content = http.request(url)
	return content.decode(result_decoder)


def call_api(data, result_decoder="utf-8"):
	http = httplib2.Http()
	print("http://app.internetware.cn/jwd/?" + urlencode(data))
	response, content = http.request("http://app.internetware.cn/jwd/?" + urlencode(data))
	return content.decode(result_decoder)