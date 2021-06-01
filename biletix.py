from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
from collections import OrderedDict

driver.get("https://www.biletix.com/anasayfa/TURKIYE/tr")

driver.find_element_by_css_selector("button[id=_evidon-accept-button]").click()

# ı didn't get any popup
#when an alert box pops up, useer have to click "OK" button to proceed (Java script alert box"

#if it say like onclick="myAlertFunction()" that mean is it  is javascript
#driver.find_element_by_xpath("//button[@onclick='myAlertFunction()']").click()
#alert = driver.switch_to.alert()
#alert.text
#it will say 'ı am an alert box'
#alert.ac

driver.implicitly_wait(20)
driver.maximize_window()


ddown_list = driver.find_element_by_id("category_sb")
sel = Select(ddown_list)
sel.select_by_visible_text('MÜZİK')

ddown_list1 = driver.find_element_by_id("date_sb")
sel1 = Select(ddown_list1)
sel1.select_by_visible_text("Önümüzdeki 30 Gün")

ddown_list2 = driver.find_element_by_id("city_sb")
sel2 = Select(ddown_list2)
sel2.select_by_visible_text("Tüm Türkiye")



driver.find_element_by_css_selector('button[class="discoverbar__button"]').click()

#git = driver.find_element_by_css_selector('button[class="discoverbar__button"]')
#git.send_keys(Keys.RETURN)


print('***b part****')

rowLoc = "//*[@id=\"paginator\"]/ul/li"

allrowsele = driver.find_elements_by_xpath(rowLoc)

allheadersnames = ["EventName" , "EventStatus" , "EventDate"]
allCollecitonList = [OrderedDict()]
clickCount = 3
for clickCount in range(clickCount,len(allrowsele)):
    eventRowLoc = "//*[@id=\"all_result\"]/div[4]"
    specificRowLoc = "//*[@id=\"paginator\"]/ul/li[" + str(clickCount) + "]"      #2.sayfanın alanı

    allResultLoc = driver.find_element_by_xpath(eventRowLoc)
    allResultEventList = allResultLoc.find_elements_by_class_name("grid_21")

    itemCount = 1
    for allResult in allResultEventList:
        eventNameLoc = "//*[@id=\"all_result\"]/div[4]/div[" + str(itemCount) + "]/div/div[3]/div[2]/a"
        eventStatusLoc = "//*[@id=\"all_result\"]/div[4]/div[" + str(itemCount) + "]/div/div[3]/div[2]/span"
        eventDateOneLoc = "//*[@id=\"all_result\"]/div[4]/div[" + str(itemCount) + "]/div/div[5]/div/span[1]"
        eventDateTwoLoc = "//*[@id=\"all_result\"]/div[4]/div[" + str(itemCount) + "]/div/div[5]/div/span[2]"

        eventName = allResult.find_element_by_xpath(eventNameLoc).text
        eventStatus = allResult.find_element_by_xpath(eventStatusLoc).text
        eventDateOne = allResult.find_element_by_xpath(eventDateOneLoc).text
        eventDateTwo = allResult.find_element_by_xpath(eventDateTwoLoc).text

        events = [eventName, eventStatus, eventDateOne+eventDateTwo]

        eachRowData = OrderedDict()
        j= 0
        for j in range(len(allheadersnames)):
            eachRowData[allheadersnames[j]] = events[j]
        itemCount = itemCount + 1
        allCollecitonList.append(eachRowData)
    driver.find_element_by_xpath(specificRowLoc).click()
print(allCollecitonList)
collection = OrderedDict()
test=[OrderedDict]
with open ('activiteler.txt', 'w') as f:

    for a in allCollecitonList:
        for v in a:
            f.write(v)
for collection in allCollecitonList:
    if collection.get("EventDate") == "Cmt, 05/06/21":
        test.append(collection)
print(test)

