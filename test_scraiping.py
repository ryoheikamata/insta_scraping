from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import pandas as pd
import random



load_dotenv()
path = os.environ['DRIVER_PATH']
chrome_path = os.path.join(path, 'chromedriver')

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://www.instagram.com/?hl=ja'
driver.get(url)

sleep(random.randint(5, 10))

user = os.environ['USER_NAME']
passwd = os.environ['PASSWORD']

user_input_box = driver.find_element(By.NAME, 'username')
passwd_input_box = driver.find_element(By.NAME, 'password')
user_input_box.send_keys(user)

sleep(random.randint(4,7))

passwd_input_box.send_keys(passwd)
log_btn = driver.find_element(By.CLASS_NAME, 'L3NKy')
log_btn.click()

sleep(random.randint(4, 7))

df = pd.read_excel('./menber.xlsx', sheet_name='Sheet1')

menber_list = []

for menbers_url in df['url']:
    sleep(random.randint(3, 5))

    driver.get(menbers_url)
    account_name = driver.find_element(By.CLASS_NAME, '_7UhW9').text
    id_name = driver.find_element(By.CLASS_NAME, "_7UhW9").text
    img_url = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
    # follower = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a/div/span').get_attribute('title')
    follower = driver.find_element(By.CLASS_NAME, 'g47SY').get_attribute('title')

    sleep(random.randint(1,4))

    menber_detail = {
        'name': account_name,
        'id_name': id_name,
        'follower': follower,
        'img_url': img_url
    }
    sleep(random.randint(1,3))

    menber_list.append(menber_detail)

df = pd.DataFrame(menber_list)
df.to_csv('menber_detail.csv')

sleep(random.randint(2, 3))

driver.close()


