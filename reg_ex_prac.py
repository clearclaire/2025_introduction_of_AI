import re
import urllib.request

url = "https://bit.ly/3rxQFS4"
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_results = re.findall(r"([a-zA-Z0-9]+\*\*\*)", html_contents)

for result in id_results:
    print(result)
    