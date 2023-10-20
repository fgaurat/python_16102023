import requests
from bs4 import BeautifulSoup
from pprint import pprint
import glob
import re

def main():
    log_files = glob.glob("*.log")
    # log_files = sorted(log_files)
    log_files.sort()
    
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                # result = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
                # result = re.findall(r"^(.+?)\s",line)
                result = re.findall(r"\"\s(\d{3})\s",line)
                if '404' in result:
                    print(result)

def main_download():
    main_url = "http://logs.eolem.com/"
    response = requests.get(main_url,timeout=10)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # all_a = soup.find_all('a')
    # for a in all_a:
    #     if ".log" in a['href']: 
    #         print(a['href'])

    all_a = [main_url+a['href'] for a in soup.find_all('a') if ".log" in a['href']]
    for a in all_a:
        log_file = a.split('/')[-1]
        response = requests.get(a,timeout=10)
        text = response.text
        with open(log_file,"w") as f:
            f.write(text)


if __name__ == '__main__':
    main()
