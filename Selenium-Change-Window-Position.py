from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

my_url = "https://google.com/"

chrome_options = Options()

# You can change the initial window postion by adding this option.
chrome_options.add_argument('--window-position=-10000,0')

# This disables console logs
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options = chrome_options)

driver.get(my_url)

sleep(3)

# This line will set the window position at any given moment.
driver.set_window_position(0,0)
