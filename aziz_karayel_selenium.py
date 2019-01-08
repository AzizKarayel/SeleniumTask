from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

browser = webdriver.Firefox()
time.sleep(5)
browser.get("https://www.amazon.com/")
time.sleep(2)

   

class AmazonTask:
    def login(mail, password):
        sign_in = browser.find_element_by_id("nav-link-accountList").click()
        username = browser.find_element_by_name("email").send_keys(mail)
        password = browser.find_element_by_name("password").send_keys(password)
        submit = browser.find_element_by_xpath("//*[@id='signInSubmit']").click()

    def search(search_text):
        sbox = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
        sbox.send_keys(search_text)
        time.sleep(2)
        act3 = browser.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()


    def add_delete():
        addlist = browser.find_element_by_xpath("//*[@id='add-to-wishlist-button-submit']").click()
        time.sleep(2)
        wievlist = browser.find_element_by_id("WLHUC_viewlist").click()
        print("Choosen product is enable on list.")
        delete = browser.find_element_by_name("submit.deleteItem").click()
        print("The product was deleted.")

    def amazon_search():
        if browser.current_url == "https://www.amazon.com/":
            print ("Main Page has opened! \n")
        else:
            print ("Sometimes this happens please close all browsers and re-run the code. \n")
        AmazonTask.login('your-email','your-password')
        AmazonTask.search('samsung')
        time.sleep(1)
        pagetwo = browser.find_element_by_xpath("//*[@id='pagn']/span[3]/a").click()
        time.sleep(1)
        itemname = browser.find_element_by_xpath("//*[@id='result_18']/div/div/div/div[2]/div[1]/div[1]/a").get_attribute("title")
        print(itemname, "\n")
        item = browser.find_element_by_xpath("//*[@id='result_18']/div/div/div/div[2]/div[1]/div[1]").click()
        time.sleep(2)
        AmazonTask.add_delete()
    

AmazonTask.amazon_search()
