import os
import urllib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Instructions
# 1. Install necessary requirements with pip install requirements.txt
# 2. Download ChromeDriver from https://sites.google.com/chromium.org/driver/ and place in the same directory as the script.
# 3. Set the path to the workshop mod below.
# 4. Success!

# Settings
directory = r"C:\Users\path\to\mod"  # Mod Path
url = "https://translate.google.com/?sl=auto&tl=en&text={0}&op=translate"  # Google Translate URL

# Selenium
service = Service("chromedriver.exe")  # Download From https://sites.google.com/chromium.org/driver/
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")


def translate(string):
    # Google Translate with Selenium
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url.format(urllib.parse.quote(string)))
    time.sleep(2)
    response = driver.find_elements(By.CLASS_NAME, "VIiyi")[0].text.title()
    driver.close()
    driver.quit()
    return response


for subdir, dirs, files in os.walk(directory):
    for file in files:
        # Path of File
        path = os.path.join(subdir, file)

        # Only English Files
        if file == "Schinese.dat":
            # Responses
            lines = []

            # Read & Translate
            with open(path, encoding="utf8") as srcs:
                for src in srcs:
                    response = translate(src)
                    lines.append(response)
                    print(response)

            # Write Lines
            with open(path, "w", encoding="utf8") as out:
                for line in lines:
                    out.write("%s\n" % line)
