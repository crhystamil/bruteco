import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://comteco.com.bo/conexion.php'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; x4)'

for phone in range(4215032, 4795035):
    values={ 'valor1' : phone,
             'valor2' : '',
             'valor3' : '',
             'valor4' : '1',
             'valor6' : '0',
             'valor7' : '' }

    headers = { 'User-Agent' : user_agent }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
        text = response.read()
        aux = ''
        soup = BeautifulSoup(text)
        if (soup.find_all("td", class_="text_form_guia_resultado")):
            for tag in soup.find_all("td", class_="text_form_guia_resultado"):
                aux += tag.get_text()+' ; '
            print aux
    except:
        print 'error'

