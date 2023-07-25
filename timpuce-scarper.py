import hashlib
import io
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver

k = []
k.append("https://timetpucefactory.fr/99-art-de-la-table")
for x in range(2,6): 
    k.append("https://timetpucefactory.fr/99-art-de-la-table?page=" + str(x))
k.append("https://timetpucefactory.fr/263-deco-animation")
for x in range(2,10): 
    k.append("https://timetpucefactory.fr/263-deco-animation?page=" + str(x))
    
driver = webdriver.Chrome()
results = []

def parse_image_urls(classes, location, source):
    for a in soup.findAll(attrs={'class': classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))   
for x in k:
    driver.get(x)
    content = driver.page_source
    soup = BeautifulSoup(content)
    parse_image_urls("ttproduct-image", "img", "src")

df = pd.DataFrame({"links": results})
df.to_csv("links.csv", index=False, encoding="utf-8")

for b in results:
# Store the content from the URL to a variable
    image_content = requests.get(b).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")
    file_path = Path("Desktop/timpuce", hashlib.sha1(image_content).hexdigest()[:10] + ".png")
    image.save(file_path, "PNG", quality=80)