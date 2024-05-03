from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import html
from selenium.webdriver.common.keys import Keys
from telegram_bot import send_message
import time
import re
from config import config

service = Service(executable_path="../driver/chromedriver.exe")


# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/121.0.6167.140 Chrome/121.0.6167.140 Safari/537.36")

if config["headless"] ==0:
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage as it's not needed in headless mode


# Create WebDriver instance with configured ChromeOptions
driver = webdriver.Chrome(options=chrome_options)


productlinks=[]
iterationNum=1
j=0
while True:
    print(f"Checking {iterationNum} time")
    for city in config["zipcodes"]:
        driver.get(f'https://minneapolis.craigslist.org/search/sss?bundleDuplicates=1&max_price={config["max_price"]}&postal={city}&postedToday=1&query=table%20pool&search_distance={config["range"]}&sort=date#search=1~gallery~0~0')

        # j=j+1
        # if j==1:
        #     continue
        print(city)
        # time.sleep(5000)
#         # time.sleep(5000)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # time.sleep(1000)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:

            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-page-1"]/ol/li/div[.//a/span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "pool table")]]'))
            )
            elements = driver.find_elements(By.XPATH, '//*[@id="search-results-page-1"]/ol/li/div[.//a/span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "pool table")]]')   #  | .//span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "billiard")]
            # time.sleep(10000)

            for element in elements:
                text=element.text
                
                try:
                    elements_with_href = element.find_element(By.XPATH,".//*[@href]").get_attribute("href")
                    if elements_with_href not in productlinks:
                        telegram_message=f' \n<b>{text}</b>'
                        telegram_message=telegram_message+f'\n<b>Click</b> <a href="{elements_with_href}"> Here</a>\n '
    #                         # print(telegram_message)
                        send_message(telegram_message, config["chatID"])
                        productlinks.append(elements_with_href)

                except NoSuchElementException as e:
                    print(e)
# #                     pass
        except Exception as e:
            print(e)
        time.sleep(config["reloadTime"])
#         driver.refresh()

    iterationNum+=1

time.sleep(2000)