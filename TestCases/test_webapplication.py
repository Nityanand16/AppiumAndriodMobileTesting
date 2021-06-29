import time

from appium import webdriver
from args import args
from selenium.webdriver.remote import command

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get("http://google.com")
print(driver.title)
#driver.find_element_by_xpath("//*[@name='q'").send_keys('Hello Appium!')
driver.find_element_by_css_selector("*[name='q']").send_keys("Hello Appium!")
#driver.find_element_by_name("q").send_keys("Hello Appium!")    #Exception error invalid locator so better to use the xpath/css selector
time.sleep(4)
driver.quit()
