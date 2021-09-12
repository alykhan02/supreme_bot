# import statements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Item Details STC based on user's pref
information = ["Ash Ketchup", "AshKetchup@gmail.com", "1234567890", "123 Seasame Street", "", "M4B1J5", "Toronto", "ON", "CANADA"]
card_information = ["1234123412341234", "10", "2022", "123"]
cart_link = "https://www.supremenewyork.com/shop/cart"
categories = ["jackets", "shirts", "tops_sweaters", "sweatshirts", "pants", "hats", "bags", "accessories", "shoes", "skate"]
item_title = "Small Box Crewneck"
shop_link = "https://www.supremenewyork.com/shop/all/"
STYLE_NUMBER = 3
size_list = ["SMALL", "MEDIUM", "LARGE", "XLARGE"]
size = size_list[0]
PATH = "/Users/alykhanversi/PycharmProjects/supreme_bot/chromedriver"
driver = webdriver.Chrome(PATH)

# Starts the bot does everything to get the item in the basked
def boot_up():
    item_link = shop_link + categories[STYLE_NUMBER]
    driver.get(item_link)
    item_tab = driver.find_element_by_link_text(item_title)
    item_tab.click()
    time.sleep(1)

    if STYLE_NUMBER < 4:
        select_size = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[1]/select")
        select_size.send_keys(size)
    add_to_cart = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input")
    add_to_cart.click()
    driver.get(cart_link)
    checkout_link = driver.find_element_by_partial_link_text("checkout now")
    checkout_link.click()
    check_out()

# Starts the checkout process by inputting user's details into checkout field
def check_out():
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input")
    for i in range(len(information)):
        element.send_keys(information[i])
        element.send_keys(Keys.TAB)
        element = driver.switch_to.active_element
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[3]/select")
    element.send_keys(information[-2])

    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[5]/div[1]/input")
    for i in range(len(card_information)):
        element.send_keys(card_information[i])
        element.send_keys((Keys.TAB))
        element = driver.switch_to.active_element

    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label/div/ins")
    element.click()
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/div[2]/input")
    element.click()

boot_up()