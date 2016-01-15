from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
import data
import searchMethods


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://admin:secret@gepard.bintime.com/admin')



    def testLogin(self):
        driver = self.driver
        driver.maximize_window()



        self.logIn()
    def logIn(self):
        driver = self.driver

        #fill the email field
        driver.find_element_by_xpath(data.logInEmailField).send_keys(data.logInEmail)

        #fill the password field
        driver.find_element_by_xpath(data.logInPasswordField).send_keys(data.logInPassword)

        #click on login button
        driver.find_element_by_xpath(data.logInButton).click()
        #time.sleep(2)
        driver.implicitly_wait(5)



        self.openOrdersPage()
    def openOrdersPage(self):
        driver = self.driver

        #click on order button
        driver.find_element_by_xpath(data.ordersButton).click()

        #click on orders management
        driver.find_element_by_xpath(data.ordersManagementButton).click()
        #driver.implicitly_wait(5)
        time.sleep(2)

        self.searchInOrder()
    def searchInOrder(self):
        driver = self.driver

        print('Orders -> Orders Management')

        #search by Created At field
        searchMethods.searchByCreatedAtField(driver, data.ordersCreatedAtDataSource, data.ordersSearchButton, data.ordersCreatedAtField,
                               data.ordersCreatedAtResultAfterSearch, data.ordersManagementPageTitle, data.ordersCreatedAtColumnName,
                               data.ordersResetButton)

        #search by First Name field
        searchMethods.searchFunctionForField(driver, data.ordersFirstNameDataSource, data.ordersSearchButton, data.ordersFirstNameField,
                               data.ordersManagementPageTitle, data.ordersFirstNameResultAfterSearch, data.ordersFirstNameColumnName,
                               data.ordersResetButton)

        #search by Last Name field
        searchMethods.searchFunctionForField(driver, data.ordersLastNameDataSource, data.ordersSearchButton, data.ordersLastNameField,
                               data.ordersManagementPageTitle, data.ordersLastNameResultAfterSearch, data.ordersLastNameColumnName,
                               data.ordersResetButton)

        #search by Company field
        searchMethods.searchFunctionForField(driver, data.ordersCompanyDataSource, data.ordersSearchButton, data.ordersCompanyField,
                               data.ordersManagementPageTitle, data.ordersCompanyResultAfterSearch, data.ordersCompanyColumnName,
                               data.ordersResetButton)

        #search by shipping method select dropdown
        searchMethods.searchBySelectDropDown(driver, data.ordersSearchButton, data.ordersShippingMethodSelectDropDown,
                                             data.ordersManagementPageTitle, data.ordersSelectDropDownResultOnPage,
                                             data.ordersResetButton)

        #search by payment method select dropdown
        searchMethods.searchBySelectDropDown(driver, data.ordersSearchButton, data.ordersPaymentMethodSelectDropDown,
                                             data.ordersManagementPageTitle, data.ordersSelectDropDownResultOnPage,
                                             data.ordersResetButton)

        #search by status dropdown
        searchMethods.searchBySelectDropDown(driver, data.ordersSearchButton, data.ordersStatusSelectDropDown,
                                             data.ordersManagementPageTitle, data.ordersSelectDropDownResultOnPage,
                                             data.ordersResetButton)




        self.openProductsPage()
    def openProductsPage(self):
        driver = self.driver

        #click on catalog management page
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on products page
        driver.find_element_by_xpath(data.productsButton).click()
        driver.implicitly_wait(3)

        self.searchOnProductsPage()
    def searchOnProductsPage(self):
        driver = self.driver

        print
        print('Catalog Management -> Products')

        #search by id
        searchMethods.searchFunctionForField(driver, data.productsProdIdDataSource, data.productsSearchButton, data.productsProdIdField,
                                             data.productsManagementPageTitle, data.productsProdIdResultAfterSearch,
                                             data.productsProdIdColumnName, data.productsResetButton)

        #search by title
        searchMethods.searchFunctionForField(driver, data.productsTitleDataSource, data.productsSearchButton, data.productsTitleField,
                                             data.productsManagementPageTitle, data.productsTitleResultAfterSearch,
                                             data.productsTitleColumnName, data.productsResetButton)

        #search by MPN
        searchMethods.searchFunctionForField(driver, data.productsMPNDataSource, data.productsSearchButton, data.productsMPNField,
                                             data.productsManagementPageTitle, data.productsMPNResultAfterSearch,
                                             data.productsMPNColumnName, data.productsResetButton)

        #search by family name
        searchMethods.searchFunctionForField(driver, data.productsFamilyDataSource, data.productsSearchButton, data.productsFamilyField,
                                             data.productsManagementPageTitle, data.productsFamilyResultAfterSearch,
                                             data.productsFamilyColumnName, data.productsResetButton)

        #search by series name
        searchMethods.searchFunctionForField(driver, data.productsSeriesDataSource, data.productsSearchButton, data.productsSeriesField,
                                             data.productsManagementPageTitle, data.productsSeriesResultAfterSearch,
                                             data.productsSeriesColumnName, data.productsResetButton)

        #search by published select dropdown
        searchMethods.searchBySelectDropDown(driver, data.productsSearchButton, data.productsPublishedSelectDropDown,
                                             data.productsManagementPageTitle, data.productsSelectDropDownResultOnPage,
                                             data.productsResetButton)

        #search by stock select dropdown
        searchMethods.searchBySelectDropDown(driver, data.productsSearchButton, data.productsStockSelectDropDown,
                                             data.productsManagementPageTitle, data.productsSelectDropDownResultOnPage,
                                             data.productsResetButton)






        #refactoring!!! (must be full suggestion)

        # #search by manufacturer select2 dropdown with search field
        # searchMethods.searchBySelectTwo(driver, data.productsManagementPageTitle, data.productsSearchButton, data.productsManufacturerColumnName,
        #                                 data.productsManufacturerDataSource,data.productsManufacturerSelect2,
        #                                 data.productsManufacturerSelect2Field, data.productsManufacturerNotification,
        #                                 data.productsManufacturerResultAfterSearch,data.productsResetButton)
        #
        # #search by category select2 dropdown with search field
        # searchMethods.searchBySelectTwo(driver, data.productsManagementPageTitle, data.productsSearchButton, data.productsCategoryColumnName,
        #                                 data.productsCategoryDataSource, data.productsCategorySelect2,
        #                                 data.productsCategorySelect2Field, data.productsCategoryNotification,
        #                                 data.productsCategoryResultAfterSearch, data.productsResetButton)





        #search on Manufacturers page

        self.openManufacturersPage()
    def openManufacturersPage(self):
        driver = self.driver

        #click on catalog management page
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on products page
        driver.find_element_by_xpath(data.manufacturersButton).click()
        driver.implicitly_wait(3)

        self.searchOnManufacturersPage()
    def searchOnManufacturersPage(self):
        driver = self.driver

        print
        print('Catalog Management -> Manufacturers')

        #search by manufacturers ID field
        searchMethods.searchFunctionForField(driver, data.manufacturersManufacturerIDDataSource, data.manufacturersSearchButton,
                                             data.manufacturersManufacturerIDField, data.manufacturersPageTitle, data.manufacturersManufacturerIDResultAfterSearch,
                                             data.manufacturersManufacturerIDColumnName, data.manufacturersResetButton)

        #search by Name field
        searchMethods.searchFunctionForField(driver, data.manufacturersNameDataSource, data.manufacturersSearchButton,
                                             data.manufacturersNameField, data.manufacturersPageTitle, data.manufacturersNameResultAfterSearch,
                                             data.manufacturersNameColumnName, data.manufacturersResetButton)

        #search by update field
        searchMethods.searchByCreatedAtField(driver, data.manufacturersUpdateDataSource, data.manufacturersSearchButton, data.manufacturersUpdateField,
                                             data.manufacturersUpdateResultAfterSearch, data.manufacturersPageTitle,
                                             data.manufacturersUpdateColumnName, data.manufacturersResetButton)





        #0.0.0 search by Features

        #0.1.1 search by Features -> Groups -> CMS Groups Management

        self.openGroupsCMSGroupsManagement()
    def openGroupsCMSGroupsManagement(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on Groups button
        driver.find_element_by_xpath(data.featuresGroupsButton).click()

        #click on CMS Groups Management
        driver.find_element_by_xpath(data.featureGroupsCMSGroupsManagement).click()
        driver.implicitly_wait(3)

        #search on Features -> Groups -> CMS Groups Management
        self.searchOnCMSGroupsManagement()
    def searchOnCMSGroupsManagement(self):
        driver = self.driver

        print
        print('Features -> Groups -> CMS Groups Management')

        searchMethods.searchFunctionForField(driver, data.cmsGroupsManagementNameDataSource, data.cmsGroupsManagementSearchButton,
                                             data.cmsGroupsManagementNameField, data.cmsGroupsManagementTitlePage, data.cmsGroupsManagementNameResultAfterSearch,
                                             data.cmsGroupsManagementNameColumnName, data.cmsGroupsManagementResetButton)






        #0.1.2 search by Feature -> Groups -> Icecat Groups List
        self.openIcecatGroupsList()
    def openIcecatGroupsList(self):
        driver = self.driver

         #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on Groups button
        driver.find_element_by_xpath(data.featuresGroupsButton).click()

        #click on Icecat Groups List
        driver.find_element_by_xpath(data.icecatGroupsListButton).click()
        driver.implicitly_wait(3)


        #search on Icecat Groups List
        self.searchOnIcecatGroupsList()
    def searchOnIcecatGroupsList(self):
        driver = self.driver

        print
        print('Feature -> Groups -> Icecat Groups List')

        #search by ID
        searchMethods.searchFunctionForField(driver, data.icecatGroupsListIDDataSource, data.icecatGroupsListSearchButton,
                                             data.icecatGroupsListIDField, data.icecatGroupsListTitlePage, data.icecatGroupsListIDResultAfterSearch,
                                             data.icecatGroupsListIDColumnName, data.icecatGroupsListResetButton)

        #search by Category Name
        searchMethods.searchFunctionForField(driver, data.icecatGroupsListCategoryDataSource, data.icecatGroupsListSearchButton,
                                             data.icecatGroupsListCategoryField, data.icecatGroupsListTitlePage, data.icecatGroupsListCategoryResultAfterSearch,
                                             data.icecatGroupsListCategoryColumnName, data.icecatGroupsListResetButton)

        #search by group name
        searchMethods.searchFunctionForField(driver, data.icecatGroupsListGroupNameDataSource, data.icecatGroupsListSearchButton,
                                             data.icecatGroupsListGroupNameField, data.icecatGroupsListTitlePage, data.icecatGroupsListGroupNameResultAfterSearch,
                                             data.icecatGroupsListGroupNameColumnName, data.icecatGroupsListResetButton)





        #0.2.1 Feature -> Measure

        #0.2.2 Feature -> Measure -> CMS Measure Management
        self.openCMSMeasureManagement()
    def openCMSMeasureManagement(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on Measure button
        driver.find_element_by_xpath(data.measureButton).click()

        #click on CMS Measure Button
        driver.find_element_by_xpath(data.cmsMeasureManagementButton).click()
        driver.implicitly_wait(3)


        self.searchOnCMSMeasureManagement()
    def searchOnCMSMeasureManagement(self):
        driver = self.driver

        print
        print('Feature -> Measure -> CMS Measure Management')

        #search by Name
        searchMethods.searchFunctionForField(driver, data.cmsMeasureManagementNameDataSource, data.cmsMeasureManagementSearchButton,
                                             data.cmsMeasureManagementNameField, data.cmsMeasureManagementTitlePage, data.cmsMeasureManagementNameResultAfterSearch,
                                             data.cmsMeasureManagementNameColumnName, data.cmsMeasureManagementResetButton)

        #search by Sign
        searchMethods.searchFunctionForField(driver, data.cmsMeasureManagementSignDataSource, data.cmsMeasureManagementSearchButton,
                                             data.cmsMeasureManagementSignField, data.cmsMeasureManagementTitlePage, data.cmsMeasureManagementSignResultAfterSearch,
                                             data.cmsMeasureManagementSignColumnName, data.cmsMeasureManagementResetButton)





        #0.2.3 Feature -> Measure -> Icecat Measure List
        self.openIcecatMeasureList()
    def openIcecatMeasureList(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on Measure button
        driver.find_element_by_xpath(data.measureButton).click()

        #click on Icecat measure List
        driver.find_element_by_xpath(data.icecatMeasureListButton).click()
        driver.implicitly_wait(3)


        self.searchOnIcecatMeasureList()
    def searchOnIcecatMeasureList(self):
        driver = self.driver

        print
        print('Feature -> Measure -> Icecat Measure List')

        #search by measure ID
        searchMethods.searchFunctionForField(driver, data.icecatMeasureListMeasureIdDataSource, data.icecatMeasureListSearchButton,
                                             data.icecatMeasureListMeasureIdField, data.icecatMeasureListTitlePage, data.icecatMeasureListMeasureIdResultAfterSearch,
                                             data.icecatMeasureListMeasureIdColumnName, data.icecatMeasureListResetButton)

        #search by Name
        searchMethods.searchFunctionForField(driver, data.icecatMeasureListNameDataSource, data.icecatMeasureListSearchButton,
                                             data.icecatMeasureListNameField, data.icecatMeasureListTitlePage, data.icecatMeasureListNameResultAfterSearch,
                                             data.icecatMeasureListNameColumnName, data.icecatMeasureListResetButton)

        #search by sign name
        searchMethods.searchFunctionForField(driver, data.icecatMeasureListSignNameDataSource, data.icecatMeasureListSearchButton,
                                             data.icecatMeasureListSignNameField, data.icecatMeasureListTitlePage, data.icecatMeasureListSignNameResultAfterSearch,
                                             data.icecatMeasureListSignNameColumnName, data.icecatMeasureListResetButton)





        #0.3.1 Features -> Features -> CMS Features Management

        self.openCMSFeaturesManagement()
    def openCMSFeaturesManagement(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on second Features button
        driver.find_element_by_xpath(data.featuresFeaturesButton).click()

        #click on CMS Features Management
        driver.find_element_by_xpath(data.cmsFeaturesManagementButton).click()
        driver.implicitly_wait(3)

        self.searchOnCMSFeaturesManagement()
    def searchOnCMSFeaturesManagement(self):
        driver = self.driver

        print
        print('Features -> Features -> CMS Features Management')

        #search by Name
        searchMethods.searchFunctionForField(driver, data.cmsFeaturesManagementNameDataSource, data.cmsFeaturesManagementSearchButton,
                                             data.cmsFeaturesManagementNameField, data.cmsFeaturesManagementTitlePage, data.cmsFeaturesManagementNameResultAfterSearch,
                                             data.cmsFeaturesManagementNameColumnName, data.cmsFeaturesManagementResetButton)

        #search by Measure Name
        searchMethods.searchFunctionForField(driver, data.cmsFeaturesManagementMeasureNameDataSource, data.cmsFeaturesManagementSearchButton,
                                             data.cmsFeaturesManagementMeasureNameField, data.cmsFeaturesManagementTitlePage, data.cmsFeaturesManagementMeasureNameResultAfterSearch,
                                             data.cmsFeaturesManagementMeasureNameColumnName, data.cmsFeaturesManagementResetButton)





        #0.3.2 Features -> Features -> Icecat Feature List

        self.openIcecatFeatureList()
    def openIcecatFeatureList(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Features button
        driver.find_element_by_xpath(data.featuresButton).click()

        #click on second Features button
        driver.find_element_by_xpath(data.featuresFeaturesButton).click()

        #click on Icecat Feature List
        driver.find_element_by_xpath(data.icecatFeatureListButton).click()
        driver.implicitly_wait(3)

        self.searchOnIcecatFeatureList()
    def searchOnIcecatFeatureList(self):
        driver = self.driver

        print
        print('Features -> Features -> Icecat Feature List')

        #search by Feature ID
        searchMethods.searchFunctionForField(driver, data.icecatFeatureListFeatureIdDataSource, data.icecatFeatureListSearchButton,
                                             data.icecatFeatureListFeatureIdField, data.icecatFeatureListTitlePage, data.icecatFeatureListFeatureIdResultAfterSearch,
                                             data.icecatFeatureListFeatureIdColumnName, data.icecatFeatureListResetButton)

        #search by Name
        searchMethods.searchFunctionForField(driver, data.icecatFeatureListNameDataSource, data.icecatFeatureListSearchButton,
                                             data.icecatFeatureListNameField, data.icecatFeatureListTitlePage, data.icecatFeatureListNameResultAfterSearch,
                                             data.icecatFeatureListNameColumnName, data.icecatFeatureListResetButton)

        #search by Measure Name
        searchMethods.searchFunctionForField(driver, data.icecatFeatureListMeasureNameDataSource, data.icecatFeatureListSearchButton,
                                             data.icecatFeatureListMeasureNameField, data.icecatFeatureListTitlePage, data.icecatFeatureListMeasureNameResultAfterSearch,
                                             data.icecatFeatureListMeasureNameColumnName, data.icecatFeatureListResetButton)

        #search by Sign Name
        searchMethods.searchFunctionForField(driver, data.icecatFeatureListSignNameDataSource, data.icecatFeatureListSearchButton,
                                             data.icecatFeatureListSignNameField, data.icecatFeatureListTitlePage, data.icecatFeatureListSignNameResultAfterSearch,
                                             data.icecatFeatureListSignNameColumnName, data.icecatFeatureListResetButton)






        #open Catalog Management -> Mapping -> Mapping Manufacturer

        self.openMappingManufacturer()
    def openMappingManufacturer(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Mapping Manufacturer button
        driver.find_element_by_xpath(data.mappingManufacturerButton).click()
        driver.implicitly_wait(3)

        self.searchOnMappingManufacturer()
    def searchOnMappingManufacturer(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Mapping Manufacturer')

        #search by Import Provider select drop down
        searchMethods.searchBySelectDropDown(driver, data.mappingManufacturerSearchButton, data.mappingManufacturerImportProviderSelectDropDown,
                                             data.mappingManufacturerTitlePage, data.mappingManufacturerImportProviderResultOnPage,
                                             data.mappingManufacturerResetButton)

        #search by Distributor Manufacturer
        searchMethods.searchFunctionForField(driver, data.mappingManufacturerDistributorManufacturerDataSource, data.mappingManufacturerSearchButton,
                                             data.mappingManufacturerDistributorManufacturerField, data.mappingManufacturerTitlePage, data.mappingManufacturerDistributorManufacturerResultAfterSearch,
                                             data.mappingManufacturerDistributorManufacturerColumnName, data.mappingManufacturerResetButton)

        #search by CMS Manufacturer
        searchMethods.searchFunctionForField(driver, data.mappingManufacturerCMSManufacturerIdDataSource, data.mappingManufacturerSearchButton,
                                             data.mappingManufacturerCMSManufacturerIdField, data.mappingManufacturerTitlePage, data.mappingManufacturerCMSManufacturerIdResultAfterSearch,
                                             data.mappingManufacturerCMSManufacturerIdColumnName, data.mappingManufacturerResetButton)

        #search by Mapping Status select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingManufacturerSearchButton, data.mappingManufacturerMappingStatusSelectDropdown,
                                             data.mappingManufacturerTitlePage, data.mappingManufacturerMappingStatusResultOnPage,
                                             data.mappingManufacturerResetButton)





        #open Catalog Management -> Mapping -> Mapping Category

        self.openMappingCategory()
    def openMappingCategory(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Mapping Category button
        driver.find_element_by_xpath(data.mappingMappingCategoryButton).click()
        driver.implicitly_wait(3)


        self.searchOnMappingCategory()
    def searchOnMappingCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Mapping Category')

        #search by Import Provider select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingCategorySearchButton, data.mappingCategoryImportProviderSelectDropDown,
                                             data.mappingCategoryTitlePage, data.mappingCategoryResultOnPage,
                                             data.mappingCategoryResetButton)

        #search by Provider Category
        searchMethods.searchFunctionForField(driver, data.mappingCategoryProviderCategoryDataSource, data.mappingCategorySearchButton,
                                             data.mappingCategoryProviderCategoryField, data.mappingCategoryTitlePage, data.mappingCategoryProviderCategoryResultAfterSearch,
                                             data.mappingCategoryProviderCategoryColumnName, data.mappingCategoryResetButton)

        #search by CMS Category
        searchMethods.searchFunctionForField(driver, data.mappingCategoryCMSCategoryDataSource, data.mappingCategorySearchButton,
                                             data.mappingCategoryProviderCategoryField, data.mappingCategoryTitlePage, data.mappingCategoryCMSCategoryResultAfterSearch,
                                             data.mappingCategoryCMSCategoryColumnName, data.mappingCategoryResetButton)

        #search by Mapping Status select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingCategorySearchButton, data.mappingCategoryMappingStatusSelectDropDown,
                                             data.mappingCategoryTitlePage, data.mappingCategoryMappingStatusResultOnPage,
                                             data.mappingCategoryResetButton)





         #open Catalog Management -> Mapping -> Mapping Family

        self.openMappingFamilyCategory()
    def openMappingFamilyCategory(self):
        driver = self.driver

         #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Mapping Family button
        driver.find_element_by_xpath(data.mappingMappingFamilyButton).click()
        driver.implicitly_wait(3)


        self.searchOnMappingFamilyCategory()
    def searchOnMappingFamilyCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Mapping Family (page name must be refactoring)')

        #search by Import Provider select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingFamilySearchButton, data.mappingFamilyImportProviderSelectDropDown,
                                             data.mappingFamilyTitlePage, data.mappingFamilyImportProviderResultOnPage,
                                             data.mappingFamilyResetButton)

        #search by Content Family
        searchMethods.searchFunctionForField(driver, data.mappingFamilyContentFamilyDataSource, data.mappingFamilySearchButton,
                                             data.mappingFamilyContentFamilyField, data.mappingFamilyTitlePage, data.mappingFamilyContentFamilyResultAfterSearch,
                                             data.mappingFamilyContentFamilyColumnName, data.mappingFamilyResetButton)

        #search by CMS Family
        searchMethods.searchFunctionForField(driver, data.mappingFamilyCMSFamilyDataSource, data.mappingFamilySearchButton,
                                             data.mappingFamilyCMSFamilyField, data.mappingFamilyTitlePage, data.mappingFamilyCMSFamilyResultAfterSearch,
                                             data.mappingFamilyCMSFamilyColumnName, data.mappingFamilyResetButton)

        #search by Mapping Status select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingFamilySearchButton, data.mappingFamilyMappingStatusSelectDropDown,
                                             data.mappingFamilyTitlePage, data.mappingFamilyMappingStatusResultOnPage,
                                             data.mappingFamilyResetButton)





        #open Catalog Management -> Mapping -> Mapping Language Content Provider

        self.openMappingLanguageContentProviderCategory()
    def openMappingLanguageContentProviderCategory(self):
        driver = self.driver

         #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Mapping Family button
        driver.find_element_by_xpath(data.mappingLanguageContentProviderButton).click()
        driver.implicitly_wait(3)

        self.searchOnMappingLanguageContentProviderCategory()
    def searchOnMappingLanguageContentProviderCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Mapping Language Content Provider')

        #search by Import Provider
        searchMethods.searchBySelectDropDown(driver, data.mappingLanguageContentProviderSearchButton, data.mappingLanguageContentProviderImportProviderSelectDropDown,
                                             data.mappingLanguageContentProviderTitlePage, data.mappingLanguageContentProviderImportProviderResultOnPage,
                                             data.mappingLanguageContentProviderResetButton)

        #search by Provider Language
        searchMethods.searchFunctionForField(driver, data.mappingLanguageContentProviderProviderLanguageDataSource, data.mappingLanguageContentProviderSearchButton,
                                             data.mappingLanguageContentProviderProviderLanguageField, data.mappingLanguageContentProviderTitlePage, data.mappingLanguageContentProviderProviderLanguageResultAfterSearch,
                                             data.mappingLanguageContentProviderProviderLanguageColumnName, data.mappingLanguageContentProviderResetButton)

        #search by CMS Language
        searchMethods.searchFunctionForField(driver, data.mappingLanguageContentProviderCMSLanguageDataSource, data.mappingLanguageContentProviderSearchButton,
                                             data.mappingLanguageContentProviderCMSLanguageField, data.mappingLanguageContentProviderTitlePage, data.mappingLanguageContentProviderCMSLanguageResultAfterSearch,
                                             data.mappingLanguageContentProviderCMSLanguageColumnName, data.mappingLanguageContentProviderResetButton)

        #search by Mapping Status
        searchMethods.searchBySelectDropDown(driver, data.mappingLanguageContentProviderSearchButton, data.mappingLanguageContentProviderMappingStatusSelectDropDown,
                                             data.mappingLanguageContentProviderTitlePage, data.mappingLanguageContentProviderMappingStatusResultOnPage,
                                             data.mappingLanguageContentProviderResetButton)





    #open Catalog Management -> Mapping -> Mapping Feature

        self.openMappingFeatureCategory()
    def openMappingFeatureCategory(self):
        driver = self.driver

         #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Mapping Feature button
        driver.find_element_by_xpath(data.mappingFeatureButton).click()
        driver.implicitly_wait(3)

        self.searchOnMappingFeatureCategory()
    def searchOnMappingFeatureCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Mapping Language Content Provider')

        #search by Import Provider select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mappingFeatureSearchButton, data.mappingFeatureImportProviderSelectDropDown,
                                             data.mappingFeatureTitlePage, data.mappingFeatureImportProviderResultOnPage,
                                             data.mappingFeatureResetButton)

        #search by Provider Category
        searchMethods.searchFunctionForField(driver, data.mappingFeatureProviderFeatureDataSource, data.mappingFeatureSearchButton,
                                             data.mappingFeatureProviderFeatureField, data.mappingFeatureTitlePage, data.mappingFeatureProviderFeatureResultAfterSearch,
                                             data.mappingFeatureProviderFeatureColumnName, data.mappingFeatureResetButton)

        #search by Provider Feature Measure
        searchMethods.searchFunctionForField(driver, data.mappingFeatureProviderFeatureMeasureDataSource, data.mappingFeatureSearchButton,
                                             data.mappingFeatureProviderFeatureMeasureField, data.mappingFeatureTitlePage, data.mappingFeatureProviderFeatureMeasureResultAfterSearch,
                                             data.mappingFeatureProviderFeatureMeasureColumnName, data.mappingFeatureResetButton)

        #search by Icecat Feature
        searchMethods.searchFunctionForField(driver, data.mappingFeatureIcecatFeatureDataSource, data.mappingFeatureSearchButton,
                                             data.mappingFeatureIcecatFeatureField, data.mappingFeatureTitlePage, data.mappingFeatureIcecatFeatureResultAfterSearch,
                                             data.mappingFeatureIcecatFeatureColumnName, data.mappingFeatureResetButton)

        #search by Icecat Feature Measure
        searchMethods.searchFunctionForField(driver, data.mappingFeatureIcecatFeatureMeasureDataSource, data.mappingFeatureSearchButton,
                                             data.mappingFeatureIcecatFeatureMeasureField, data.mappingFeatureTitlePage, data.mappingFeatureIcecatFeatureMeasureResultAfterSearch,
                                             data.mappingFeatureIcecatFeatureMeasureColumnName, data.mappingFeatureResetButton)

        #search by Mapping Status
        searchMethods.searchBySelectDropDown(driver, data.mappingFeatureSearchButton, data.mappingFeatureMappingStatusSelectDropDown,
                                             data.mappingFeatureTitlePage, data.mappingFeatureMappingStatusResultOnPage,
                                             data.mappingFeatureResetButton)




        #open Catalog Management -> Mapping -> Unit Conversion Rules

        self.openUnitConversionRulesCategory()
    def openUnitConversionRulesCategory(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Mappings Button
        driver.find_element_by_xpath(data.mappingsButton).click()

        #click on Unit Conversion Rules button
        driver.find_element_by_xpath(data.unitConversionRulesButton).click()
        driver.implicitly_wait(3)

        self.searchOnUnitConversionRulesCategory()
    def searchOnUnitConversionRulesCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Mapping -> Unit Conversion Rules')

        #search by Icecat Measure
        searchMethods.searchFunctionForField(driver, data.unitConversionRulesIcecatMeasureDataSource, data.unitConversionRulesSearchButton,
                                             data.unitConversionRulesIcecatMeasureField, data.unitConversionRulesTitlePage, data.unitConversionRulesIcecatMeasureResultAfterSearch,
                                             data.unitConversionRulesIcecatMeasureColumnName, data.unitConversionRulesResetButton)

        #search by CMS Measure
        searchMethods.searchFunctionForField(driver, data.unitConversionRulesCMSMeasureDataSource, data.unitConversionRulesSearchButton,
                                             data.unitConversionRulesCMSMeasureField, data.unitConversionRulesTitlePage, data.unitConversionRulesCMSMeasureResultAfterSearch,
                                             data.unitConversionRulesCMSMeasureColumnName, data.unitConversionRulesResetButton)

        #search by Rule (first)
        searchMethods.searchFunctionForField(driver, data.unitConversionRulesDataSourceFirst, data.unitConversionRulesSearchButton,
                                             data.unitConversionRulesField, data.unitConversionRulesTitlePage, data.unitConversionRulesResultAfterSearch,
                                             data.unitConversionRulesCMSMeasureColumnNameByRule1, data.unitConversionRulesResetButton)

        #search by Rule (second)
        searchMethods.searchFunctionForField(driver, data.unitConversionRulesDataSourceSecond, data.unitConversionRulesSearchButton,
                                             data.unitConversionRulesField, data.unitConversionRulesTitlePage, data.unitConversionRulesResultAfterSearchSecond,
                                             data.unitConversionRulesCMSMeasureColumnNameByRule2, data.unitConversionRulesResetButton)





        #open Catalog Management -> Price Rules Management -> Price Rules

        self.openPriceRulesCategory()
    def openPriceRulesCategory(self):
        driver = self.driver

        #click on Catalog Management button
        driver.find_element_by_xpath(data.catalogManagementButton).click()

        #click on Price Rules Management button
        driver.find_element_by_xpath(data.priceRulesManagementButton).click()

        #click on Price Rules button
        driver.find_element_by_xpath(data.priceRulesButton).click()
        driver.implicitly_wait(3)

        self.searchOnPriceRulesCategory()
    def searchOnPriceRulesCategory(self):
        driver = self.driver

        print
        print('Catalog Management -> Price Rules Management -> Price Rules')

        #search by Category select2 dropdown
        searchMethods.searchBySelectTwo(driver, data.priceRulesTitlePage, data.priceRulesSearchButton, data.priceRulesCategoryColumnName,
                                        data.priceRulesCategoryDataSource, data.priceRulesCategorySelect2,
                                        data.priceRulesCategorySelect2Field, data.priceRulesCategoryNotification,
                                        data.priceRulesCategoryResultAfterSearch, data.priceRulesResetButton)

        #search by Manufacturer select2 dropdown
        searchMethods.searchBySelectTwo(driver, data.priceRulesTitlePage, data.priceRulesSearchButton, data.priceRulesManufacturerColumnName,
                                        data.priceRulesManufacturerDataSource, data.priceRulesManufacturerSelect2,
                                        data.priceRulesManufacturerSelect2Field, data.priceRulesManufacturerNotification,
                                        data.priceRulesManufacturerResultAfterSearch, data.priceRulesResetButton)

        #search by Product MPN
        searchMethods.searchFunctionForField(driver, data.priceRulesProductMPNDataSource, data.priceRulesSearchButton,
                                             data.priceRulesProductMPNField, data.priceRulesTitlePage, data.priceRulesProductMPNResultAfterSearch,
                                             data.priceRulesProductMPNColumnName, data.priceRulesResetButton)

        #search by Supplier select dropdown
        searchMethods.searchBySelectDropDown(driver, data.priceRulesSearchButton, data.priceRulesSupplierSelectDropDown,
                                             data.priceRulesTitlePage, data.priceRulesSupplierResultOnPage,
                                             data.priceRulesResetButton)

        #search by Group ID
        searchMethods.searchBySelectDropDown(driver, data.priceRulesSearchButton, data.priceRulesGroupIDSelectDropDown,
                                             data.priceRulesTitlePage, data.priceRulesGroupIdResultOnPage,
                                             data.priceRulesResetButton)





    #open Customers -> Customers Management

        self.openCustomersManagement()
    def openCustomersManagement(self):
        driver = self.driver

        #click on Customers button
        driver.find_element_by_xpath(data.customersButton).click()

        #click on Customers Management button
        driver.find_element_by_xpath(data.customersManagementButton).click()

        self.searchOnCustomersManagementCategory()
    def searchOnCustomersManagementCategory(self):
        driver = self.driver

        print
        print('Customers -> Customers Management')

        #search by Customer ID
        searchMethods.searchFunctionForField(driver, data.customersManagementCustomerIdDataSource, data.customersManagementSearchButton,
                                             data.customersManagementCustomerIdField, data.customersManagementTitlePage, data.customersManagementCustomerIdResultAfterSearch,
                                             data.customersManagementCustomerIdColumnName, data.customersManagementResetButton)

        #search by First Name
        searchMethods.searchFunctionForField(driver, data.customersManagementFirstNameDataSource, data.customersManagementSearchButton,
                                             data.customersManagementFirstNameField, data.customersManagementTitlePage, data.customersManagementFirstNameResultAfterSearch,
                                             data.customersManagementFirstNameColumnName, data.customersManagementResetButton)

        #search by Last Name
        searchMethods.searchFunctionForField(driver, data.customersManagementLastNameDataSource, data.customersManagementSearchButton,
                                             data.customersManagementLastNameField, data.customersManagementTitlePage, data.customersManagementLastNameResultAfterSearch,
                                             data.customersManagementLastNameColumnName, data.customersManagementResetButton)

        #search by Phone
        searchMethods.searchFunctionForField(driver, data.customersManagementPhoneDataSource, data.customersManagementSearchButton,
                                             data.customersManagementPhoneField, data.customersManagementTitlePage, data.customersManagementPhoneResultAfterSearch,
                                             data.customersManagementPhoneColumnName, data.customersManagementResetButton)

        #search by Email
        searchMethods.searchFunctionForField(driver, data.customersManagementEmailDataSource, data.customersManagementSearchButton,
                                             data.customersManagementEmailField, data.customersManagementTitlePage, data.customersManagementEmailResultAfterSearch,
                                             data.customersManagementEmailColumnName, data.customersManagementResetButton)

        #search by Country
        searchMethods.searchFunctionForField(driver, data.customersManagementCountryDataSource, data.customersManagementSearchButton,
                                             data.customersManagementCountryField, data.customersManagementTitlePage, data.customersManagementCountryResultAfterSearch,
                                             data.customersManagementCountryColumnName, data.customersManagementResetButton)

        #search by  Company
        searchMethods.searchFunctionForField(driver, data.customersManagementCompanyDataSource, data.customersManagementSearchButton,
                                             data.customersManagementCompanyField, data.customersManagementTitlePage, data.customersManagementCompanyResultAfterSearch,
                                             data.customersManagementCompanyColumnName, data.customersManagementResetButton)

        #search by Job Title
        searchMethods.searchFunctionForField(driver, data.customersManagementJobTitleDataSource, data.customersManagementSearchButton,
                                             data.customersManagementJobTitleField, data.customersManagementTitlePage, data.customersManagementJobTitleResultAfterSearch,
                                             data.customersManagementJobTitleColumnName, data.customersManagementResetButton)

        #search by Type select dropdown
        searchMethods.searchBySelectDropDown(driver, data.customersManagementSearchButton, data.customersManagementTypeSelectDropDown,
                                             data.customersManagementTitlePage, data.customersManagementTypeResultOnPage,
                                            data.customersManagementResetButton)

        #search by Status select dropdown
        searchMethods.searchBySelectDropDown(driver, data.customersManagementSearchButton, data.customersManagementStatusSelectDropDown,
                                             data.customersManagementTitlePage, data.customersManagementTypeResultOnPage,
                                             data.customersManagementResetButton)





        #FO Settings -> Search Management -> Category Search Management

        self.openCategorySearchManagementCategory()
    def openCategorySearchManagementCategory(self):
        driver = self.driver

        #click on FO Settings button
        driver.find_element_by_xpath(data.foSettingsButton).click()

        #click on Search Management button
        driver.find_element_by_xpath(data.searchManagementButton).click()

        #click on Category Search Management
        driver.find_element_by_xpath(data.categorySearchManagementButton).click()
        driver.implicitly_wait(3)

        self.searchOnCategorySearchManagementCategory()
    def searchOnCategorySearchManagementCategory(self):
        driver = self.driver

        searchMethods.searchFunctionForField(driver, data.categorySearchManagementDataSource, data.categorySearchManagementSearchButton,
                                             data.categorySearchManagementField, data.categorySearchManagementTitlePage, data.categorySearchManagementResultAfterSearch,
                                             data.categorySearchManagementColumnName, data.categorySearchManagementResetButton)





        #FO Settings -> Synonyms

        self.openSynonymsCategory()
    def openSynonymsCategory(self):
        driver = self.driver

        #click on FO Settings button
        driver.find_element_by_xpath(data.foSettingsButton).click()

        #click on Synonyms button
        driver.find_element_by_xpath(data.synonymsButton).click()
        driver.implicitly_wait(3)

        self.searchOnSynonymsCategory()
    def searchOnSynonymsCategory(self):
        driver = self.driver

        print
        print('FO Settings -> Synonyms')

        #search by Rule
        searchMethods.searchFunctionForField(driver, data.synonymsRuleDataSource, data.synonymsSearchButton,
                                             data.synonymsRuleField, data.synonymsTitlePage, data.synonymsRuleResultAfterSearch,
                                             data.synonymsRuleColumnName, data.synonymsResetButton)






        #Imports -> History And Statuses

        self.openHistoryAndStatusesCategory()
    def openHistoryAndStatusesCategory(self):
        driver = self.driver

        #click on Imports button
        driver.find_element_by_xpath(data.importsButton).click()

        #click on History And Statuses button
        driver.find_element_by_xpath(data.historyAndStatusesButton).click()
        driver.implicitly_wait(3)

        self.searchOnHistoryAndStatusesCategory()
    def searchOnHistoryAndStatusesCategory(self):
        driver = self.driver

        print
        print('Imports -> History And Statuses')

        #search by Import Name
        searchMethods.searchFunctionForField(driver, data.historyAndStatusesImportNameDataSource, data.historyAndStatusesSearchButton,
                                             data.historyAndStatusesField, data.historyAndStatusesTitlePage, data.historyAndStatusesImportNameResultAfterSearch,
                                             data.historyAndStatusesColumnName, data.historyAndStatusesResetButton)

        #search by Type
        searchMethods.searchBySelectDropDownWithoutNumberQuantity(driver, data.historyAndStatusesSearchButton, data.historyAndStatusesTypeSelectDropDown,
                                                                  data.historyAndStatusesTitlePage, data.historyAndStatusesResultAfterSearch,
                                                                  data.historyAndStatusesResetButton)

        #search by Last Start Time
        searchMethods.searchByCreatedAtField(driver, data.historyAndStatusesLastStartTimeDataSource, data.historyAndStatusesSearchButton,
                                             data.historyAndStatusesLastStartTimeField, data.historyAndStatusesLastStartTimeResultAfterSearch,
                                             data.historyAndStatusesTitlePage, data.historyAndStatusesLastStartTimeColumnName, data.historyAndStatusesResetButton)

        #search by Last Finish Time
        searchMethods.searchByCreatedAtField(driver, data.historyAndStatusesLastFinishTimeDataSource, data.historyAndStatusesSearchButton,
                                             data.historyAndStatusesLastFinishTimeField, data.historyAndStatusesLastFinishTimeResultAfterSearch,
                                             data.historyAndStatusesTitlePage, data.historyAndStatusesLastFinishTimeColumnName, data.historyAndStatusesResetButton)


        #search by Last Status
        #refactoring!!!
        #refactoring





    #open Administration -> Manage Admins
        self.openManageAdminsCategory()
    def openManageAdminsCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Manage Admins
        driver.find_element_by_xpath(data.manageAdminsButton).click()
        driver.implicitly_wait(3)

        self.searchOnManageAdminsCategory()
    def searchOnManageAdminsCategory(self):
        driver = self.driver

        print
        print('Administration -> Manage Admins')

        #search for ID
        searchMethods.searchFunctionForField(driver, data.manageAdminsIdDataSource, data.manageAdminsSearchButton,
                                             data.manageAdminsIdField, data.manageAdminsTitlePage, data.manageAdminsIdResultAfterSearch,
                                             data.manageAdminsIdColumnName, data.manageAdminsResetButton)

        #search for Username
        searchMethods.searchFunctionForField(driver, data.manageAdminsUsernameDataSource, data.manageAdminsSearchButton,
                                             data.manageAdminsUsernameField, data.manageAdminsTitlePage, data.manageAdminsUserNameResultAfterSearch,
                                             data.manageAdminsUsernameColumnName, data.manageAdminsResetButton)

        #search by Email
        searchMethods.searchFunctionForField(driver, data.manageAdminsEmailDataSource, data.manageAdminsSearchButton,
                                             data.manageAdminsEmailField, data.manageAdminsTitlePage, data.manageAdminsEmailResultAfterSearch,
                                             data.manageAdminsEmailColumnName, data.manageAdminsResetButton)

        #search by Registration Date

        searchMethods.searchByCreatedAtField(driver, data.manageAdminsRegistrationDateDataSource, data.manageAdminsSearchButton,
                                             data.manageAdminsRegistrationDateField, data.manageAdminsRegistrationDateResultAfterSearch,
                                             data.manageAdminsTitlePage, data.manageAdminsRegistrationDateColumnName, data.manageAdminsResetButton)
        driver.find_element_by_xpath(data.manageAdminsSearchButton).click()
        driver.find_element_by_xpath(data.manageAdminsResetButton).click()

        #search by Last Visit
        searchMethods.searchByCreatedAtField(driver, data.manageAdminsLastVisitDataSource, data.manageAdminsSearchButton,
                                             data.manageAdminsLastVisitField, data.manageAdminsLastVisitResultAfterSearch,
                                             data.manageAdminsTitlePage, data.manageAdminsLastVisitColumnName, data.manageAdminsResetButton)
        driver.find_element_by_xpath(data.manageAdminsSearchButton).click()
        driver.find_element_by_xpath(data.manageAdminsResetButton).click()

        #search by Superuser
        searchMethods.searchBySelectDropDown(driver, data.manageAdminsSearchButton, data.manageAdminsSuperuserSelectDropDown,
                                             data.manageAdminsTitlePage, data.manageAdminsSuperuserResultAfterSearch, data.manageAdminsResetButton)







    #open Administration -> Payment Methods
        self.openPaymentMethodsCategory()
    def openPaymentMethodsCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Payment Method button
        driver.find_element_by_xpath(data.paymentMethodButton).click()
        driver.implicitly_wait(3)

        self.searchOnPaymentMethodsCategory()
    def searchOnPaymentMethodsCategory(self):
        driver = self.driver

        #search by Code
        searchMethods.searchFunctionForField(driver, data.paymentMethodCodeDataSource, data.paymentMethodSearchButton,
                                             data.paymentMethodCodeField, data.paymentMethodPageTitle, data.paymentMethodCodeResultAfterSearch,
                                             data.paymentMethodCodeColumnName, data.paymentMethodResetButton)






    #open Administration -> Shipping Method
        self.openShippingMethodCategory()
    def openShippingMethodCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Payment Method button
        driver.find_element_by_xpath(data.shippingMethodButton).click()
        driver.implicitly_wait(3)

        self.searchOnShippingMethodCategory()
    def searchOnShippingMethodCategory(self):
        driver = self.driver

        #search by Code
        searchMethods.searchFunctionForField(driver, data.shippingMethodCodeDataSource, data.shippingMethodSearchButton,
                                             data.shippingMethodCodeField, data.shippingMethodPageTitle, data.shippingMethodCodeResultAfterSearch,
                                             data.shippingMethodCodeColumnName, data.shippingMethodResetButton)

        #search by Name
        searchMethods.searchFunctionForField(driver, data.shippingMethodNameDataSource, data.shippingMethodSearchButton,
                                             data.shippingMethodNameField, data.shippingMethodPageTitle, data.shippingMethodNameResultAfterSearch,
                                             data.shippingMethodNameColumnName, data.shippingMethodResetButton)

        #search by Rate
        searchMethods.searchFunctionForField(driver, data.shippingMethodRateDataSource, data.shippingMethodSearchButton,
                                             data.shippingMethodRateField, data.shippingMethodPageTitle, data.shippingMethodRateResultAfterSearch,
                                             data.shippingMethodRateColumnName, data.shippingMethodResetButton)

        #search by Rate Type select dropdown
        searchMethods.searchBySelectDropDown(driver, data.shippingMethodSearchButton, data.shippingMethodRateTypeSelectDropDown,
                                             data.shippingMethodPageTitle, data.shippingMethodRateTypeResultOnPage, data.shippingMethodResetButton)


        #search by Rating
        searchMethods.searchFunctionForField(driver, data.shippingMethodRatingDataSource, data.shippingMethodSearchButton,
                                             data.shippingMethodRatingField, data.shippingMethodPageTitle, data.shippingMethodRatingResultAfterSearch,
                                             data.shippingMethodRatingColumnName, data.shippingMethodResetButton)

        #search by Active select dropdown
        searchMethods.searchBySelectDropDown(driver, data.shippingMethodSearchButton, data.shippingMethodActiveSelectDropDown,
                                             data.shippingMethodPageTitle, data.shippingMethodActiveResultOnPage, data.shippingMethodResetButton)





    #open Administration -> Language -> Management

        self.openLanguageManagementCategory()
    def openLanguageManagementCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Language button
        driver.find_element_by_xpath(data.languageButton).click()

        #click on Management button
        driver.find_element_by_xpath(data.languageManagementButton).click()
        driver.implicitly_wait(3)

        self.searchOnLanguageManagementCategory()
    def searchOnLanguageManagementCategory(self):
        driver = self.driver

        #search by Language ID
        searchMethods.searchFunctionForField(driver, data.languageManagementLanguageIdDataSource, data.languageManagementSearchButton,
                                             data.languageManagementLanguageIdField, data.languageManagementPageTitle, data.languageManagementLanguageIdResultAfterSearch,
                                             data.languageManagementLanguageIdColumnName, data.languageManagementResetButton)

        #search by Language Name
        searchMethods.searchFunctionForField(driver, data.languageManagementLanguageNameDataSource, data.languageManagementSearchButton,
                                             data.languageManagementLanguageNameField, data.languageManagementPageTitle, data.languageManagementLanguageNameResultAfterSearch,
                                             data.languageManagementLanguageNameColumnName, data.languageManagementResetButton)

        #search by Language Code
        searchMethods.searchFunctionForField(driver, data.languageManagementLanguageCodeDataSource, data.languageManagementSearchButton,
                                             data.languageManagementLanguageCodeField, data.languageManagementPageTitle, data.languageManagementLanguageCodeResultAfterSearch,
                                             data.languageManagementLanguageCodeColumnName, data.languageManagementResetButton)

        #search by Active select dropdown
        searchMethods.searchBySelectDropDown(driver, data.languageManagementSearchButton, data.languageManagementLanguageActiveSelectDropDown,
                                             data.languageManagementPageTitle, data.languageManagementLanguageResultOnPage, data.languageManagementResetButton)

        #search by Sort
        searchMethods.searchFunctionForField(driver, data.languageManagementSortDataSource, data.languageManagementSearchButton,
                                             data.languageManagementSortField, data.languageManagementPageTitle, data.languageManagementSortResultAfterSearch,
                                             data.languageManagementSortColumnName, data.languageManagementResetButton)






    #open Administration -> Languages -> Dictionaries
        self.openLanguageDictionariesCategory()
    def openLanguageDictionariesCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Language button
        driver.find_element_by_xpath(data.languageButton).click()

        #click on Dictionaries button
        driver.find_element_by_xpath(data.languageDictionariesButton).click()
        driver.implicitly_wait(3)

        self.searchOnLanguageDictionaryCategory()
    def searchOnLanguageDictionaryCategory(self):
        driver = self.driver

        #seach by Message
        searchMethods.searchFunctionForField(driver, data.languageDictionariesMessageDataSource, data.languageDictionariesSearchButton,
                                             data.languageDictionariesMessageField, data.languageDictionariesPageTitle, data.languageDictionariesMessageResultAfterSearch,
                                             data.languageDictionariesMessageColumnName, data.languageDictionariesResetButton)

        #search by Category select dropdown
        searchMethods.searchBySelectDropDown(driver, data.languageDictionariesSearchButton, data.languageDictionariesCategorySelectDropDown,
                                             data.languageDictionariesPageTitle, data.languageDictionariesCategoryResultOnPage, data.languageDictionariesResetButton)





    #open Administration -> Mail Template
        self.openMailTemplateCategory()
    def openMailTemplateCategory(self):
        driver = self.driver

        #click on Administration button
        driver.find_element_by_xpath(data.administrationButton).click()

        #click on Mail Template button
        driver.find_element_by_xpath(data.mailTemplateButton).click()
        driver.implicitly_wait(3)

        self.searchOnMailTemplateCategory()
    def searchOnMailTemplateCategory(self):
        driver  = self.driver

        #search by ID
        searchMethods.searchFunctionForField(driver, data.mailTemplateIdDataSource, data.mailTemplateSearchButton,
                                             data.mailTemplateIdField, data.mailTemplatePageTitle, data.mailTemplateIdResultAfterSearch,
                                             data.mailTemplateIdColumnName, data.mailTemplateResetButton)

        #search by Key
        searchMethods.searchFunctionForField(driver, data.mailTemplateKeyDataSource, data.mailTemplateSearchButton,
                                             data.mailTemplateKeyField, data.mailTemplatePageTitle, data.mailTemplateKeyResultAfterSearch,
                                             data.mailTemplateKeyColumnName, data.mailTemplateResetButton)

        #search by Category select dropdown
        searchMethods.searchBySelectDropDown(driver, data.mailTemplateSearchButton, data.mailTemplateCategorySelectDropDown,
                                             data.mailTemplatePageTitle, data.mailTemplateCategoryResultOnPage, data.mailTemplateResetButton)




    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
