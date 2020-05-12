import pandas as pd
import os
from pathlib import Path
import requests
import time
from tqdm import tqdm

list = pd.read_excel("Free+English+textbooks.xlsx")

if not os.path.exists('books'):
    os.makedirs('books')

def convert_url_to_download_link(x):
    url = x.replace("http://doi.org/", "")
    url = url.replace("/", "%2F")
    url = "https://link.springer.com/content/pdf/" + url + ".pdf"
    return(url)

for ii in tqdm(range(len(list))):
    download_link = convert_url_to_download_link(list["DOI URL"][ii])
    book_name = list["Book Title"][ii]
    book_path = Path(os.getcwd() + "/books/" + str(book_name) + ".pdf")
    
    print(f"Downloading book '{book_name}' | {ii} out of {len(list)} books")
    r = requests.get(download_link, allow_redirects = True)
    open(book_path, 'wb').write(r.content)