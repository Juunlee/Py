import urllib
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



for i in range(2):
    url = 'https://abvd.shh.mpg.de/utils/save/?type=csv&section=austronesian&language='+ str(i+1)
    print(url)
    response = urllib.request.urlopen(url)
    webContent = response.read()
    f = open('abvd/lang'+str(i+1)+'.csv', 'wb')
    f.write(webContent)
    f.close
    print(webContent[0:])


