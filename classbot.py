from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
import schedule as sc
from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver 
def hetcollegeconnected():
    browser = webdriver.Chrome() 
    for i in range(0,10):
        print("Connecting with the COllege Server...")
    browser.get('https://erp.mit.asia/') 

# Let's the user see and also load the element 
    time.sleep(2) 

    print("Successfully COnnected with College Server")

    ans=str(input("Do you want to close th browser ?"))

    if ans =="yes" or ans=="YES":
        browser.close()

    
if __name__ == '__main__':
    sc.every().day.at("21:00").do(hetcollegeconnected)