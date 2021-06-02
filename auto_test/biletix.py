from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from collections import OrderedDict

# browser
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
webwait = WebDriverWait(driver, 20)

print(" ************ Part A *******************")
print("# 1. open websıte")
driver.get("https://www.biletix.com/anasayfa/TURKIYE/tr")

print("# 2. accept the cookies")
driver.find_element_by_id("_evidon-accept-button").click()

print("# 3. close the popup advert")
webwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dialog_close"))).click()

print("# 4. select Muzik from categories drop down")
ddown_list = driver.find_element_by_id("category_sb")
sel = Select(ddown_list)
sel.select_by_visible_text('MÜZİK')

print("# 5.select the date")
ddown_list1 = driver.find_element_by_id("date_sb")
sel1 = Select(ddown_list1)
sel1.select_by_visible_text("Önümüzdeki 30 Gün")

print("# 6. select the location")
ddown_list2 = driver.find_element_by_id("city_sb")
sel2 = Select(ddown_list2)
sel2.select_by_visible_text("Tüm Türkiye")

print("# 7. Search and wait for the results")
driver.find_element_by_xpath('//button[@class="discoverbar__button"]').click()
webwait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='combo_result_header']/span[@id='searchResultCount']")))

print(" ************ Part B *******************")



#ı expected
# to creat list
#events = [eventName, eventStatus, eventDateOne + eventDateTwo] for each row by for loop with using incrementing (eventCount =+1 )
#and put the result inside dictionary(collectionList) by allCollectionList.append(eachrow)

allCollecitonList = []
events = [eventName, eventStatus, eventDateOne + eventDateTwo]


print("# printing the big list of all events")
print(allCollecitonList)

print(" ************ Part C *******************")


print("# 1. removing the record with date 'Paz, 10/01/21' from the result set")
for collection in allCollecitonList:
    if collection.get("EventDate") == "Paz, 10/01/21":
        # if collection.get("EventDate") == "Cmt, 05/06/21":  # existing date
        allCollecitonList.remove(collection)

print("saving the result to activiteler.txt file.")
with open('activiteler.txt', 'w') as f:
    for a in allCollecitonList:
        for v in a:
            f.write(v)

print("task is completed.")
