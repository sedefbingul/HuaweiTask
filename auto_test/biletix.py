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

rowLoc = "//div[@id='paginator']/ul/li"

allrowsele = webwait.until(EC.presence_of_all_elements_located((By.XPATH, rowLoc)))

allheadersnames = ["EventName", "EventStatus", "EventDate"]
allCollecitonList = [OrderedDict()]
clickCount = 3  # clicking 3 times because we have 4 pages

for clickCount in range(clickCount, len(allrowsele)):
    eventRowLoc = "//*[@id='all_result']/div[4]"
    specificRowLoc = f"//div[@id='paginator']/ul/li[{clickCount}]"  # 2.sayfanın alanı

    allResultLoc = driver.find_element_by_xpath(eventRowLoc)
    allResultEventList = allResultLoc.find_elements_by_class_name("grid_21")
    # row_xpath = "//div[@class='result_render']//div[@class='grid_21 alpha omega listevent searchResultEvent']"

    eventCount = 1
    for allResult in allResultEventList:
        eventNameLoc = f"//*[@id=\"all_result\"]/div[4]/div[{eventCount}]/div/div[3]/div[2]/a"
        eventStatusLoc = f"//*[@id=\"all_result\"]/div[4]/div[{eventCount}]/div/div[3]/div[2]/span"
        eventDateOneLoc = f"//*[@id=\"all_result\"]/div[4]/div[{eventCount}]/div/div[5]/div/span[1]"
        eventDateTwoLoc = f"//*[@id=\"all_result\"]/div[4]/div[{eventCount}]/div/div[5]/div/span[2]"

        # reading the each event row
        eventName = allResult.find_element_by_xpath(eventNameLoc).text
        eventStatus = allResult.find_element_by_xpath(eventStatusLoc).text
        eventDateOne = allResult.find_element_by_xpath(eventDateOneLoc).text
        eventDateTwo = allResult.find_element_by_xpath(eventDateTwoLoc).text

        # saving it in the list
        events = [eventName, eventStatus, eventDateOne + eventDateTwo]

        # saving the values from 'events' list in the dictionary called eachRowData
        eachRowData = OrderedDict()
        for j in range(len(allheadersnames)):
            eachRowData[allheadersnames[j]] = events[j]

        # incrementing to go to next row
        eventCount = eventCount + 1

        print("# adding the dictionary of each row to the main list of events")
        allCollecitonList.append(eachRowData)

    print("# clicks next page after getting all rows from the current page")
    driver.find_element_by_xpath(specificRowLoc).click()

print("# printing the big list of all events")
print(allCollecitonList)

print(" ************ Part C *******************")
collection = OrderedDict()

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
