import os
import urllib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Instructions are located at https://github.com/connorgillespie/Linguist

directory = r"C:\Users\path\to\mod"  # Set the Unturned Workshop mod path here

# Do NOT change anything past this line

url = "https://translate.google.com/?sl=auto&tl=en&text={0}&op=translate"

service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")


def translate(string):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url.format(urllib.parse.quote(string)))
    time.sleep(2)
    response = driver.find_elements(By.CLASS_NAME, "VIiyi")[0].text.title()
    driver.close()
    driver.quit()
    return response


for subdir, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(subdir, file)

        if file == "English.dat":
            lines = []

            with open(path, encoding="utf8") as srcs:
                for src in srcs:
                    response = translate(src)
                    lines.append(response)
                    print(response)

            with open(path, "w", encoding="utf8") as out:
                for line in lines:
                    out.write("%s\n" % line)
