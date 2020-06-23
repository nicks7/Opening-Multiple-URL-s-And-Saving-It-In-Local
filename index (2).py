import shutil
import urllib.request


urls = ['https://example1.json', 'https://example2.json']

file_name = 'foo.txt'

def fetch_urls(urls):
    for i, url in enumerate(urls):
        file_name = "page-%s.html" % i
        response = urllib.request.urlopen(url)
        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

fetch_urls(urls)