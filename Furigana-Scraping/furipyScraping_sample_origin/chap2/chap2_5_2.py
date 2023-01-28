import re
from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
pattern = re.compile('フラワー|Flower|flower')
for flower_text in soup.find_all(string=pattern):
    print(flower_text)
