from selenium import webdriver
import time, string
driver = webdriver.Chrome()
driver.get("https://google.com")
search_form = driver.find_element("name","q")
keywords = []
for letter in string.ascii_lowercase:
    search_form.clear()
    search_form.send_keys("python " + letter)
    time.sleep( 5 )
    list_box = driver.find_elements("tag name","li")
    for i in list_box:
        keywords.append( i.text )
print( keywords )
