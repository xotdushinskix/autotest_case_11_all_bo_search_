from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


def searchFunctionForField(driver, getResultFromTable, searchButton, field, titlePagePath, resultAfterFieldSearch, columnPath, resetButton):
    pageTitle = driver.find_element_by_xpath(titlePagePath).text
    driver.implicitly_wait(3)
    searchingColumn = driver.find_element_by_xpath(columnPath).text
    textInfo = driver.find_element_by_xpath(getResultFromTable).text
    textLength = len(textInfo)
    if textLength != 0 and textInfo != '0': #and textLength != 1:
        driver.find_element_by_xpath(searchButton).click()
        driver.find_element_by_xpath(field).send_keys(textInfo)
        driver.find_element_by_xpath(field).send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        try:
            if driver.find_element_by_xpath(resultAfterFieldSearch).is_displayed:
                searchInfo = driver.find_element_by_xpath(resultAfterFieldSearch).text
                if textInfo == searchInfo:
                    print(pageTitle + ' : search by ' + searchingColumn + ' successfully displayed')
                else:
                    print(pageTitle + ' : SEARCH BY ' + searchingColumn + ' WAS NOT DISPLAYED ------------------')
                    driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_field_was_not_displayed.png')
                driver.find_element_by_xpath(searchButton).click()
                driver.find_element_by_xpath(resetButton).click()
            else:
                print(pageTitle + " : SEARCH BY " + searchingColumn + " DOES NOT HAVE RESULT")
                driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_field_does_not_have_result.png')
        except:
            print(pageTitle +  ": SEARCH BY " + searchingColumn + " DOES NOT HAVE RESULT")
            driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_field_does_not_have_result.png')
    else:
        print(pageTitle + " : TESTING  FIELD " + searchingColumn +  " MANUALLY")
        driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/testing_field_manually.png')



#search for created at fields
def searchByCreatedAtField(driver, getResultFromTable, searchButton, field, resultAfterFieldSearch, titlePagePath, columnPath, resetButton):
    pageTitle = driver.find_element_by_xpath(titlePagePath).text
    searchingColumn = driver.find_element_by_xpath(columnPath).text
    helpTextInfo = driver.find_element_by_xpath(getResultFromTable).text
    textLength = len(helpTextInfo)
    if textLength != 0:
        textInfo = helpTextInfo[:-9]
        driver.find_element_by_xpath(searchButton).click()
        driver.find_element_by_xpath(field).send_keys(textInfo)
        driver.find_element_by_xpath(field).send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        try:
            if driver.find_element_by_xpath(resultAfterFieldSearch).is_displayed():
                helpSearchInfo = driver.find_element_by_xpath(resultAfterFieldSearch).text
                searchInfo = helpSearchInfo[:-9]
                if textInfo == searchInfo:
                    print(pageTitle + ' : search by ' + searchingColumn + ' successfully displayed')
                else:
                    print(pageTitle + ' : SEARCH BY ' + searchingColumn + ' WAS NOT DISPLAYED ------------------')
                    driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_createdAtField_was_not_displayed.png')
                driver.find_element_by_xpath(searchButton).click()
                driver.find_element_by_xpath(resetButton).click()
            else:
               print(pageTitle + " : FIELD " + searchingColumn + " DOES NOT HAVE RESULT")
               driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_createdAtField_does_not_have_result.png')
        except:
            print(pageTitle + " : FIELD " + searchingColumn + " DOES NOT HAVE RESULT")
            driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_createdAtField_does_not_have_result.png')
    else:
        print(pageTitle + " : TESTING FIELD " + searchingColumn + " MANUALLY")




#search by select dropdown
def searchBySelectDropDown(driver, searchButton, selectMethodOrStatus, titlePagePath, displayQuantity, resetButton):
    pageTitle = driver.find_element_by_xpath(titlePagePath).text
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(searchButton).click()
    selectValue = Select(driver.find_element_by_xpath(selectMethodOrStatus))
    selectData = [o.text for o in selectValue.options]
    for sel in selectData:
        driver.find_element_by_xpath(searchButton).click()
        selectValue = Select(driver.find_element_by_xpath(selectMethodOrStatus))
        selectValue.select_by_visible_text(sel)
        driver.implicitly_wait(3)
        try:
            if driver.find_element_by_xpath(displayQuantity).is_displayed:
                productQuantity = driver.find_element_by_xpath(displayQuantity).text
                productQuantity = int(productQuantity)
                if productQuantity != 0:
                    print(pageTitle + " : search by " + sel + " successfully displayed")
                else:
                    print(pageTitle + " : SEARCH BY " + sel + " WAS NOT DISPLAYED ------------------")
                    driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_selectDropDown_does_not_have_result.png')
                driver.find_element_by_xpath(searchButton).click()
                driver.find_element_by_xpath(resetButton).click()
                driver.implicitly_wait(3)
            else:
                print(pageTitle + " : FIELD " + sel + " DOES NOT HAVE RESULT")
                driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_selectDropDown_does_not_have_result.png')
                driver.find_element_by_xpath(searchButton).click()
                driver.find_element_by_xpath(resetButton).click()
                driver.implicitly_wait(3)
        except:
            print(pageTitle + " : field " + sel + " does not have result")
            driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_selectDropDown_does_not_have_result.png')
            driver.find_element_by_xpath(searchButton).click()
            driver.find_element_by_xpath(resetButton).click()
            driver.implicitly_wait(3)




#search by select 2 dropdown (with field)
def searchBySelectTwo(driver, titlePagePath, searchButton,  columnPath, getResultFromTable, select2Field, field, notificationField, resultAfterFieldSearch, resetButton):
    pageTitle = driver.find_element_by_xpath(titlePagePath).text
    searchingColumn = driver.find_element_by_xpath(columnPath).text
    textInfo = driver.find_element_by_xpath(getResultFromTable).text
    textLength = len(textInfo)
    if textLength != 0 and textLength > 1:
        driver.find_element_by_xpath(searchButton).click()
        driver.find_element_by_xpath(select2Field).click()
        finalTextInfo = textInfo.split(" ")[0]
        driver.find_element_by_xpath(field).send_keys(finalTextInfo)
        driver.find_element_by_xpath(notificationField).click()
        time.sleep(2)
        try:
            if driver.find_element_by_xpath(resultAfterFieldSearch).is_displayed():
                searchInfo = driver.find_element_by_xpath(resultAfterFieldSearch).text
                if textInfo == searchInfo:
                    print(pageTitle + ' : search by ' + searchingColumn + ' successfully displayed')
                else:
                    print(pageTitle + ' : search by ' + searchingColumn + ' was not displayed ------------------')
                    driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_select2_dropDown_was_not_displayed.png')
                driver.find_element_by_xpath(searchButton).click()
                driver.find_element_by_xpath(resetButton).click()
            else:
                print(pageTitle + " : field " + searchingColumn + " does not have result")
                driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_select2_dropDown_does_not_have_result.png')
        except:
            print(pageTitle + " : field " + searchingColumn + " does not have result")
            driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_select2_dropDown_does_not_have_result.png')
    else:
       print(pageTitle + " : testing " + searchingColumn + " field manually")




#search by select dropdown without number quantity
def searchBySelectDropDownWithoutNumberQuantity(driver, searchButton, selectMethodOrStatus, titlePagePath, resultAfterSearch, resetButton):
    pageTitle = driver.find_element_by_xpath(titlePagePath).text
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(searchButton).click()
    selectValue = Select(driver.find_element_by_xpath(selectMethodOrStatus))
    selectData = [o.text for o in selectValue.options]
    for sel in selectData:
        driver.find_element_by_xpath(searchButton).click()
        selectValue = Select(driver.find_element_by_xpath(selectMethodOrStatus))
        selectValue.select_by_visible_text(sel)
        driver.implicitly_wait(3)
        if driver.find_element_by_xpath(resultAfterSearch).is_displayed:
            productAfterSearch = driver.find_element_by_xpath(resultAfterSearch).text
            #productQuantity = int(productQuantity)
            if productAfterSearch == sel:
                print(pageTitle + " : search by " + sel + " successfully displayed")
            else:
                print(pageTitle + " : search by " + sel + " was not displayed ------------------")
                driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_select_dropDown_WithootNumberQuantity_was_not_displayed.png')
            driver.find_element_by_xpath(searchButton).click()
            driver.find_element_by_xpath(resetButton).click()
            driver.implicitly_wait(3)
        else:
            print(pageTitle + " : field " + sel + " does not have result")
            driver.save_screenshot('/home/nikita/SeleniumGepard/11Case/search_by_select_dropDown_WithootNumberQuantity_does_not_have_result.png')
            driver.find_element_by_xpath(searchButton).click()
            driver.find_element_by_xpath(resetButton).click()
            driver.implicitly_wait(3)



#search by Last and Finish time without

