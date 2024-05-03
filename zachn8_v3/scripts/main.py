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

# print(config)
# range={
#     "1": 1,
#     "2": 2,
#     "5": 3,
#     "10": 4,
#     "20": 5,
#     "40": 6,
#     "60": 7,
#     "80": 8,
#     "100": 9,
#     "250": 10,
#     "500": 11
       
#        }

###################


# Set Chrome options for running in headless mode
# chrome_options = Options()


####################

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

driver.get("https://www.facebook.com")
# https://www.facebook.com/marketplace

# # driver.quit()
# email
# passContainer
# /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a

# driver.find_element(By.ID, "email").

# driver.get("https://google.com")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "email"))
)

input_element = driver.find_element(By.ID, "email")
input_element.clear()
# input_element.send_keys("tech with tim" + Keys.ENTER)
input_element.send_keys(config["fbuser"] )

input_element = driver.find_element(By.ID, "pass")
input_element.clear()
# input_element.send_keys("tech with tim" + Keys.ENTER)
input_element.send_keys(config["fbpass"])


link = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
link.click()

time.sleep(3)
driver.get("https://www.facebook.com/marketplace")


# link.clear()
# time.sleep(10)
productlinks=[]
iterationNum=1
j=0
cities=["Pittsburgh, Pennsylvania","Milwaukee, Wisconsin","Minneapolis, Minnesota","Detroit, Michigan","IOWA"]
while True:
    print(f"Checking {iterationNum} time")
    for city in cities:
        j=j+1
        time.sleep(3)
        link=WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder,'Search Marketplace')]"))
        )
        link.send_keys(Keys.CONTROL + "a")
        link.send_keys(Keys.DELETE)

        link.send_keys("Table pool")
        link.send_keys(Keys.ENTER)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]'))
        )
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]')
        link.click()
        input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/label/div/div[2]/input')))
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/label/div/div[2]/input')
        link.click()
        time.sleep(10)

        print("Checking for :", city)
        
        link.send_keys(city)
        time.sleep(2)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div/div/div'))
        )
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div/div/div')
        link.click()  
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[3]/div/div/label/div'))
        )
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[3]/div/div/label/div')
        link.click()

        link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[{config["rangePossibleValues"][str(config["range"])]}]')
        link.click()
        link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div')

        link.click()
        time.sleep(5)
        link=WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[3]/div[2]/span[2]/label/input'))
        )
        link.send_keys("1000")
        link.send_keys(Keys.ENTER)
# //*[@id="seo_filters"]/div[2]/div[8]

        time.sleep(3)
        link=driver.find_element(By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]')
   
        driver.execute_script("arguments[0].scrollIntoView();", link)
        time.sleep(3)
        if j==1:
            link=WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]'))
            ).click()
        
        # link = driver.find_element(By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]')
        # link=WebDriverWait(driver, 5).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]'))
        # )
        # link.click()
        # test=input("enter: ")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[9]/div/div[1]/div[2]/div'))
        ).click()
        # link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[8]')
        # link.click()
        # link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[9]/div/div[1]/div[2]/div')
        # link.click()
        # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/span[2]/label/input
        # //*[@id="seo_filters"]/div[2]/div[9]/div/div[1]/div[2]/div
        
        # time.sleep(5000)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        try:

            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//div/div/div[2]/div[.//span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "pool table")]]'))
            )
            elements = driver.find_elements(By.XPATH, '//div/div/div[2]/div[.//span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "pool table")]]')   #  | .//span[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "billiard")]
        

            for element in elements:
                # print(element.text)
                try:
                    elements_with_href = element.find_element(By.XPATH,".//*[@href]")
                    elements_with_location = element.find_element(By.XPATH,".//div/div/span/div/div/a/div/div[2]/div[3]")
                    elements_category = element.find_element(By.XPATH,".//div/div/span/div/div/a/div/div[2]/div[2]")
                    elements_price = element.find_element(By.XPATH,".//div/div/span/div/div/a/div/div[2]/div[1]")
                    # for href_element in elements_with_href:
                    href_value = elements_with_href.get_attribute("href")
                    price=elements_price.text
                    match = re.findall(r'\$[0-9,]*', price) 
                    telegram_message=''
                    product_link=href_value.split("?")[0]
                    # print(match)
                    if ("free" in price.lower() or len(match)>=0) and product_link not in productlinks:
                        numeric_value=2000
                        isFree=False
                        if "free" in price.lower():
                            telegram_message=f'<b>Price: </b>{price}'
                        else:

                            numeric_string = ''.join(filter(str.isdigit, match[0]))
                            # Convert to integer
                            numeric_value = int(numeric_string)
                            if numeric_value<=1000:
                                telegram_message=f'<b>Price: </b>{match[0]}'
                                if len(match)>1:
                                    # print(match[1])
                                    telegram_message=telegram_message+f' \n<b>Old Price: </b><del>{match[1]}</del>'
                        
                            # print("The href attribute value:", href_value)
                            # print("#################",elements_with_location.text)
                            # print("#################",elements_category.text)
                            # print("#################",match[0])
                            
                            
                        telegram_message=telegram_message+f' \n<b>Category: </b>{elements_category.text}'
                        telegram_message=telegram_message+f' \n<b>Location: </b>{elements_with_location.text}'
                        telegram_message=telegram_message+f'\n<b>Click</b> <a href="{product_link}"> Here</a>\n '
                        # print(telegram_message)
                        send_message(telegram_message, config["chatID"])
                        productlinks.append(product_link)

                except NoSuchElementException as e:
                    # print(e)
                    pass
        except TimeoutException as e:
            print("Possible Internet connection problem:")
        time.sleep(config["reloadTime"])
        driver.refresh()
    iterationNum+=1

time.sleep(2000)