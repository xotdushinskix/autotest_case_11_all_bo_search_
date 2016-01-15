logInEmailField = '//*[@id="UserLogin_username"]'
logInPasswordField = '//*[@id="UserLogin_password"]'


logInEmail = 'admin'
logInPassword = 'admin'


logInButton = '//*[@id="login-form"]//div[6]/input'



#by Orders management page
ordersButton = '//*[@id="top"]/nav/ul/li[1]/div/a'
ordersManagementButton = '//*[@id="top"]/nav/ul/li[1]//li//a'
ordersManagementPageTitle = '//*[@id="content"]/h3'

ordersResetButton = '//*[@id="reset-button-order-grid"]'
ordersSearchButton = '//*[@id="order-grid"]//td[2]/button'
ordersEmptyField = '//*[@id="order-grid"]/div[1]/div'

#data by first name
ordersFirstNameDataSource = '//*[@id="order-grid"]//td[4]'
ordersFirstNameResultAfterSearch = '//*[@id="order-grid"]//tr[1]/td[4]'
ordersFirstNameColumnName = '//*[@id="order-grid_c3"]'
ordersFirstNameField = '//*[@id="MdOrder_billing_first_name"]'

#data by last name
ordersLastNameDataSource = '//*[@id="order-grid"]//td[5]'
ordersLastNameResultAfterSearch = '//*[@id="order-grid"]//tr[1]/td[5]'
ordersLastNameColumnName = '//*[@id="order-grid_c4"]'
ordersLastNameField = '//*[@id="MdOrder_billing_last_name"]'

#data by company
ordersCompanyDataSource = '//*[@id="order-grid"]//td[6]'
ordersCompanyResultAfterSearch = '//*[@id="order-grid"]//tr[1]/td[6]'
ordersCompanyColumnName = '//*[@id="order-grid_c5"]'
ordersCompanyField = '//*[@id="MdOrder_billing_company"]'

#data by created at
ordersCreatedAtDataSource = '//*[@id="order-grid"]//td[3]'
ordersCreatedAtResultAfterSearch = '//*[@id="order-grid"]//tr[1]/td[3]'
ordersCreatedAtColumnName = '//*[@id="order-grid_c2"]'
ordersCreatedAtField = '//*[@id="MdOrder_dateCreatedSearch"]'

ordersSelectDropDownResultOnPage = '//*[@id="order-grid"]//td/div/span'

#data by shipping method
ordersShippingMethodSelectDropDown = '//*[@id="MdOrder_shipping_method_code"]'

#data by payment method
ordersPaymentMethodSelectDropDown = '//*[@id="MdOrder_payment_method_code"]'

#data by status
ordersStatusSelectDropDown = '//*[@id="MdOrder_status"]'






#Catalog Management button
catalogManagementButton = '//*[@id="top"]//nav/ul/li[2]/div/a'

#by Products page
productsButton = '//*[@id="top"]/nav/ul/li[2]/div/ul/li[1]//a'

productsSearchButton = '//*[@id="product-grid"]//td[2]/button'
productsEmptyField = '//*[@id="product-grid"]/div[1]/div'
productsResetButton = '//div[10]/button'

productsManagementPageTitle = '//*[@id="product-index-page"]//h3'

#data by product id
productsProdIdDataSource = '//*[@id="product-grid"]//td[3]/a/span'
productsProdIdResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[3]//span'
productsProdIdColumnName = '//*[@id="product-grid_c2"]'
productsProdIdField = '//*[@id="EsProduct_product_id"]'

#data by title
productsTitleDataSource = '//*[@id="product-grid"]//tr/td[4]'
productsTitleResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[4]'
productsTitleColumnName = '//*[@id="product-grid_c3"]'
productsTitleField = '//*[@id="EsProduct_title"]'

#data by MPN
productsMPNDataSource = '//*[@id="product-grid"]//tr/td[5]'
productsMPNResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[5]'
productsMPNColumnName = '//*[@id="product-grid_c4"]'
productsMPNField = '//*[@id="EsProduct_mpn"]'

#data by family name
productsFamilyDataSource = '//*[@id="product-grid"]//tr/td[6]'
productsFamilyResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[6]'
productsFamilyColumnName = '//*[@id="product-grid_c5"]'
productsFamilyField = '//*[@id="EsProduct_family_name"]'

#data by series name
productsSeriesDataSource = '//*[@id="product-grid"]//tr/td[7]'
productsSeriesResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[7]'
productsSeriesColumnName = '//*[@id="product-grid_c6"]'
productsSeriesField = '//*[@id="EsProduct_series_name"]'

productsSelectDropDownResultOnPage = '//*[@id="product-grid"]//td[1]//span'

#data by published dropdown select
productsPublishedSelectDropDown = '//*[@id="EsProduct_visibility"]'

#data by stock dropdown select
productsStockSelectDropDown = '//*[@id="EsProduct_stock"]'

#data by manufacturer select2
productsManufacturerDataSource = '//*[@id="product-grid"]//tr/td[9]'
productsManufacturerResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[9]'
productsManufacturerColumnName = '//*[@id="product-grid_c8"]'
productsManufacturerSelect2 = '//*[@id="s2id_EsProduct_manufacturer_id"]'
productsManufacturerSelect2Field = '//*[@id="select2-drop"]//div/input'
productsManufacturerNotification = '//*[@id="select2-drop"]//ul/li/div'

#data by manufacturer select2
productsCategoryDataSource = '//*[@id="product-grid"]//tr/td[10]'
productsCategoryResultAfterSearch = '//*[@id="product-grid"]//tr[1]/td[10]'
productsCategoryColumnName = '//*[@id="product-grid_c9"]'
productsCategorySelect2 = '//*[@id="s2id_EsProduct_category_id"]'
productsCategorySelect2Field = '//*[@id="select2-drop"]/div/input'
productsCategoryNotification = '//*[@id="select2-drop"]/ul/li[1]/div/span'



#manufacturers
manufacturersButton = '//*[@id="top"]//li[2]/div/ul/li[3]//a'


manufacturersSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
manufacturersResetButton = '//*[@id="reset-button-featuregroup-grid"]'

manufacturersPageTitle = '//*[@id="manufacturer_index_page"]//h3'

#data by Manufacturer ID
manufacturersManufacturerIDDataSource = '//*[@id="featuregroup-grid"]//tr/td/a/span'
manufacturersManufacturerIDResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td/a/span'
manufacturersManufacturerIDColumnName = '//*[@id="featuregroup-grid_c0"]'
manufacturersManufacturerIDField = '//*[@id="Manufacturer_manufacturer_id"]'

#data by Name
manufacturersNameDataSource = '//*[@id="featuregroup-grid"]/table[2]//td[2]'
manufacturersNameResultAfterSearch = '//*[@id="featuregroup-grid"]/table[2]//tr[1]/td[2]'
manufacturersNameColumnName = '//*[@id="featuregroup-grid_c1"]'
manufacturersNameField = '//*[@id="Manufacturer_name_search"]'

#data by Update
manufacturersUpdateDataSource = '//*[@id="featuregroup-grid"]//table/tbody/tr/td[3]'
manufacturersUpdateResultAfterSearch = '//*[@id="featuregroup-grid"]/table[2]//tr[1]/td[3]'
manufacturersUpdateColumnName = '//*[@id="featuregroup-grid_c2"]'
manufacturersUpdateField = '//*[@id="Manufacturer_update"]'



#features!

featuresButton = '//*[@id="top"]//li[2]/div/ul/li[5]/div/a'

#feature groups
featuresGroupsButton = '//*[@id="top"]//div//li[5]/div/ul/li[1]/div/a'

#Features -> Groups -> CMS Groups Management
featureGroupsCMSGroupsManagement = '//*[@id="top"]//div//li[1]//li[1]//a'

#data by CMS Groups Management
cmsGroupsManagementSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
cmsGroupsManagementResetButton = '//*[@id="reset-button-featuregroup-grid"]'
cmsGroupsManagementTitlePage = '//*[@id="content"]/h3'

cmsGroupsManagementNameDataSource = '//*[@id="featuregroup-grid"]/table[2]/tbody/tr/td[2]'
cmsGroupsManagementNameResultAfterSearch = '//*[@id="featuregroup-grid"]/table[2]/tbody/tr[1]/td[2]'
cmsGroupsManagementNameColumnName = '//*[@id="featuregroup-grid_c1"]'
cmsGroupsManagementNameField = '//*[@id="FeatureGroup_name_search"]'

#Features -> Groups -> Icecat Groups List
icecatGroupsListButton = '//*[@id="top"]//li[1]//li[2]//a'

icecatGroupsListSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
icecatGroupsListResetButton = '//*[@id="reset-button-featuregroup-grid"]'
icecatGroupsListTitlePage = '//*[@id="content"]//h3'

#data by ID
icecatGroupsListIDDataSource = '//*[@id="featuregroup-grid"]//td[1]/span'
icecatGroupsListIDResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td[1]/span'
icecatGroupsListIDColumnName = '//*[@id="featuregroup-grid_c0"]'
icecatGroupsListIDField = '//*[@id="ICategoryFeatureGroup_category_feature_group_id"]'

#data by category field
icecatGroupsListCategoryDataSource = '//*[@id="featuregroup-grid"]//table[2]/tbody/tr/td[2]'
icecatGroupsListCategoryResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]/tbody/tr[1]/td[2]'
icecatGroupsListCategoryColumnName = '//*[@id="featuregroup-grid_c1"]'
icecatGroupsListCategoryField = '//*[@id="ICategoryFeatureGroup_category_search"]'

#data by group name
icecatGroupsListGroupNameDataSource = '//*[@id="featuregroup-grid"]//tr/td[3]'
icecatGroupsListGroupNameResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td[3]'
icecatGroupsListGroupNameColumnName = '//*[@id="featuregroup-grid_c2"]'
icecatGroupsListGroupNameField = '//*[@id="ICategoryFeatureGroup_name_search"]'



#Feature -> Measure
measureButton = '//*[@id="top"]//li[5]/div/ul/li[2]/div/a'

cmsMeasureManagementButton = '//*[@id="top"]//div//li[2]//li[1]//a'

cmsMeasureManagementTitlePage = '//*[@id="content"]//h3'
cmsMeasureManagementSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
cmsMeasureManagementResetButton = '//*[@id="reset-button-featuregroup-grid"]'

#search by Name
cmsMeasureManagementNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[2]'
cmsMeasureManagementNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[2]'
cmsMeasureManagementNameColumnName = '//*[@id="featuregroup-grid_c1"]'
cmsMeasureManagementNameField = '//*[@id="Measure_name_search"]'

#search by Sign
cmsMeasureManagementSignDataSource = '//*[@id="featuregroup-grid"]//td[3]'
cmsMeasureManagementSignResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td[3]'
cmsMeasureManagementSignColumnName = '//*[@id="featuregroup-grid_c2"]'
cmsMeasureManagementSignField = '//*[@id="Measure_sign_search"]'

#Icecat Measure List
icecatMeasureListButton = '//*[@id="top"]//div//li[2]//li[2]//a'

icecatMeasureListSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
icecatMeasureListResetButton = '//*[@id="reset-button-featuregroup-grid"]'
icecatMeasureListTitlePage = '//*[@id="content"]//h3'

#data by Measure ID
icecatMeasureListMeasureIdDataSource = '//*[@id="featuregroup-grid"]//tr/td/span'
icecatMeasureListMeasureIdResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td/span'
icecatMeasureListMeasureIdColumnName = '//*[@id="featuregroup-grid_c0"]'
icecatMeasureListMeasureIdField = '//*[@id="IMeasure_measure_id"]'

#data by Name
icecatMeasureListNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[2]'
icecatMeasureListNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[2]'
icecatMeasureListNameColumnName = '//*[@id="featuregroup-grid_c1"]'
icecatMeasureListNameField = '//*[@id="IMeasure_name_search"]'

#data by Sign Name
icecatMeasureListSignNameDataSource = '//*[@id="featuregroup-grid"]//td[3]'
icecatMeasureListSignNameResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td[3]'
icecatMeasureListSignNameColumnName = '//*[@id="featuregroup-grid_c2"]'
icecatMeasureListSignNameField = '//*[@id="IMeasure_sign_search"]'



#Features -> Features
featuresFeaturesButton = '//*[@id="top"]//li[5]//li[3]/div/a'

#CMS Features Management
cmsFeaturesManagementButton = '//*[@id="top"]//li[5]//li[3]//li[1]//a'

cmsFeaturesManagementSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
cmsFeaturesManagementResetButton = '//*[@id="reset-button-featuregroup-grid"]'
cmsFeaturesManagementTitlePage = '//*[@id="content"]/h3'

#data by Name
cmsFeaturesManagementNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[2]'
cmsFeaturesManagementNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[2]'
cmsFeaturesManagementNameColumnName = '//*[@id="featuregroup-grid_c1"]'
cmsFeaturesManagementNameField = '//*[@id="Feature_name_search"]'

#data by Measure Name
cmsFeaturesManagementMeasureNameDataSource = '//*[@id="featuregroup-grid"]//td[4]'
cmsFeaturesManagementMeasureNameResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td[4]'
cmsFeaturesManagementMeasureNameColumnName = '//*[@id="featuregroup-grid_c3"]'
cmsFeaturesManagementMeasureNameField = '//*[@id="Feature_measure_search"]'



#Icecat Features Management
icecatFeatureListButton = '//*[@id="top"]//li[3]//li[2]//a'

icecatFeatureListSearchButton = '//*[@id="featuregroup-grid"]//td[2]/button'
icecatFeatureListResetButton = '//*[@id="reset-button-featuregroup-grid"]'
icecatFeatureListTitlePage = '//*[@id="content"]//h3'

#data by Feature ID
icecatFeatureListFeatureIdDataSource = '//*[@id="featuregroup-grid"]//td/span'
icecatFeatureListFeatureIdResultAfterSearch = '//*[@id="featuregroup-grid"]//tr[1]/td/span'
icecatFeatureListFeatureIdColumnName = '//*[@id="featuregroup-grid_c0"]'
icecatFeatureListFeatureIdField = '//*[@id="IFeature_feature_id"]'

#data by Name
icecatFeatureListNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[2]'
icecatFeatureListNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[2]'
icecatFeatureListNameColumnName = '//*[@id="featuregroup-grid_c1"]'
icecatFeatureListNameField = '//*[@id="IFeature_name_search"]'

#data by Measure Name
icecatFeatureListMeasureNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[3]'
icecatFeatureListMeasureNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[3]'
icecatFeatureListMeasureNameColumnName = '//*[@id="featuregroup-grid_c2"]'
icecatFeatureListMeasureNameField = '//*[@id="IFeature_measure_search"]'

#data by Sign Name
icecatFeatureListSignNameDataSource = '//*[@id="featuregroup-grid"]//table[2]//td[4]'
icecatFeatureListSignNameResultAfterSearch = '//*[@id="featuregroup-grid"]//table[2]//tr[1]/td[4]'
icecatFeatureListSignNameColumnName = '//*[@id="featuregroup-grid_c3"]'
icecatFeatureListSignNameField = '//*[@id="IFeature_sign_search"]'




#Catalog Management -> Mappings

mappingsButton = '//*[@id="top"]//li[2]/div/ul/li[6]/div/a'


#1.1 Mappings -> Mapping Manufacturer
mappingManufacturerButton = '//*[@id="top"]//div//li[6]//li[1]//a'

mappingManufacturerSearchButton = '//*[@id="mappings-grid"]//td[2]/button'
mappingManufacturerResetButton = '//*[@id="reset-button-mappings-grid"]'
mappingManufacturerTitlePage = '//*[@id="content"]//h3'

#data by Import Provider
mappingManufacturerImportProviderSelectDropDown = '//*[@id="MappingManufacturer_import_id"]'
mappingManufacturerImportProviderResultOnPage = '//*[@id="mappings-grid"]//td[1]//span'

#data by Distributor Manufacturer
mappingManufacturerDistributorManufacturerDataSource = '//*[@id="mappings-grid"]//tr[2]/td[3]'
mappingManufacturerDistributorManufacturerResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[3]'
mappingManufacturerDistributorManufacturerColumnName = '//*[@id="mappings-grid_c2"]'
mappingManufacturerDistributorManufacturerField = '//*[@id="MappingManufacturer_source_name"]'

#data by CMS Manufacturer ID
mappingManufacturerCMSManufacturerIdDataSource = '//*[@id="mappings-grid"]//tr[2]/td[5]'
mappingManufacturerCMSManufacturerIdResultAfterSearch = '//*[@id="mappings-grid"]//tr/td[5]'
mappingManufacturerCMSManufacturerIdColumnName = '//*[@id="mappings-grid_c4"]'
mappingManufacturerCMSManufacturerIdField = '//*[@id="MappingManufacturer_manufacturer_name"]'

#data by Mapping Status
mappingManufacturerMappingStatusSelectDropdown = '//*[@id="MappingManufacturer_isMapped"]'
mappingManufacturerMappingStatusResultOnPage = '//*[@id="mappings-grid"]//td/div/span'



#1.2 Mappings -> Mapping Category
mappingMappingCategoryButton = '//*[@id="top"]//div//li[6]//li[2]//a'

mappingCategorySearchButton = '//*[@id="mappings-grid"]//td[2]/button'
mappingCategoryResetButton = '//*[@id="reset-button-mappings-grid"]'
mappingCategoryTitlePage = '//*[@id="content"]//h3'

#data by Import Provider
mappingCategoryImportProviderSelectDropDown = '//*[@id="MappingCategory_import_id"]'
mappingCategoryResultOnPage = '//*[@id="mappings-grid"]//td/div/span'

#data by Provider Category
mappingCategoryProviderCategoryDataSource = '//*[@id="mappings-grid"]//tr/td[3]'
mappingCategoryProviderCategoryResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[3]'
mappingCategoryProviderCategoryColumnName = '//*[@id="mappings-grid_c2"]'
mappingCategoryProviderCategoryField = '//*[@id="MappingCategory_source_name"]'

#data by CMS Category
mappingCategoryCMSCategoryDataSource = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingCategoryCMSCategoryResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingCategoryCMSCategoryColumnName = '//*[@id="mappings-grid_c4"]'
mappingCategoryCMSCategoryField = '//*[@id="MappingCategory_category_name"]'

#data by Mapping Status select dropdown
mappingCategoryMappingStatusSelectDropDown = '//*[@id="MappingCategory_isMapped"]'
mappingCategoryMappingStatusResultOnPage = '//*[@id="mappings-grid"]//td/div/span'



#1.3 Mappings -> Mapping Family
mappingMappingFamilyButton = '//*[@id="top"]//div//li[6]//li[3]//a'

mappingFamilySearchButton = '//*[@id="mappings-grid"]//td[2]/button'
mappingFamilyResetButton = '//*[@id="reset-button-mappings-grid"]'
mappingFamilyTitlePage = '//*[@id="content"]//h3'

#data by Import Provider select dropdown
mappingFamilyImportProviderSelectDropDown = '//*[@id="MappingFamily_import_id"]'
mappingFamilyImportProviderResultOnPage = '//*[@id="mappings-grid"]//td/div/span'

#data by Content Family
mappingFamilyContentFamilyDataSource = '//*[@id="mappings-grid"]//td[3]'
mappingFamilyContentFamilyResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[3]'
mappingFamilyContentFamilyColumnName = '//*[@id="mappings-grid_c2"]'
mappingFamilyContentFamilyField = '//*[@id="MappingFamily_source_name"]'

#data by CMS Family
mappingFamilyCMSFamilyDataSource = '//*[@id="mappings-grid"]//td[5]'
mappingFamilyCMSFamilyResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingFamilyCMSFamilyColumnName = '//*[@id="mappings-grid_c4"]'
mappingFamilyCMSFamilyField = '//*[@id="MappingFamily_family_name"]'

#data by Mapping Status
mappingFamilyMappingStatusSelectDropDown = '//*[@id="MappingFamily_isMapped"]'
mappingFamilyMappingStatusResultOnPage = '//*[@id="mappings-grid"]//td/div/span'



#1.4 Mappings -> Mapping Language Content Provider
mappingLanguageContentProviderButton = '//*[@id="top"]//div//div//li[4]//a'

mappingLanguageContentProviderSearchButton = '//*[@id="mappings-grid"]//td[2]/button'
mappingLanguageContentProviderResetButton = '//*[@id="reset-button-mappings-grid"]'
mappingLanguageContentProviderTitlePage = '//*[@id="content"]//h3'

#data by Import Provider select dropdown
mappingLanguageContentProviderImportProviderSelectDropDown = '//*[@id="MappingLanguageContentProvider_import_id"]'
mappingLanguageContentProviderImportProviderResultOnPage = '//*[@id="mappings-grid"]//td/div/span'

#data by Provider Language
mappingLanguageContentProviderProviderLanguageDataSource = '//*[@id="mappings-grid"]//td[3]'
mappingLanguageContentProviderProviderLanguageResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[3]'
mappingLanguageContentProviderProviderLanguageColumnName = '//*[@id="mappings-grid_c2"]'
mappingLanguageContentProviderProviderLanguageField = '//*[@id="MappingLanguageContentProvider_source_name"]'

#data by CMS Language
mappingLanguageContentProviderCMSLanguageDataSource = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingLanguageContentProviderCMSLanguageResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingLanguageContentProviderCMSLanguageColumnName = '//*[@id="mappings-grid_c5"]'
mappingLanguageContentProviderCMSLanguageField = '//*[@id="MappingLanguageContentProvider_language_name"]'

#data by Mapping Status select dropdown
mappingLanguageContentProviderMappingStatusSelectDropDown = '//*[@id="MappingLanguageContentProvider_isMapped"]'
mappingLanguageContentProviderMappingStatusResultOnPage = '//*[@id="mappings-grid"]//td/div/span'



#1.4 Mappings -> Mapping Feature
mappingFeatureButton = '//*[@id="top"]//div//div//li[5]//a'

mappingFeatureSearchButton = '//*[@id="mappings-grid"]//td[2]/button'
mappingFeatureResetButton = '//*[@id="reset-button-mappings-grid"]'
mappingFeatureTitlePage = '//*[@id="content"]//h3'

#data by Import Provider select dropdown
mappingFeatureImportProviderSelectDropDown = '//*[@id="MappingFeature_import_id"]'
mappingFeatureImportProviderResultOnPage = '//*[@id="mappings-grid"]//td/div/span'

#data by Provider Feature
mappingFeatureProviderFeatureDataSource = '//*[@id="content"]//table[2]//td[2]'
mappingFeatureProviderFeatureResultAfterSearch = '//*[@id="content"]//table[2]//tr[1]/td[2]'
mappingFeatureProviderFeatureColumnName = '//*[@id="mappings-grid_c1"]'
mappingFeatureProviderFeatureField = '//*[@id="MappingFeature_source_name"]'

#data by Provider Feature Measure
mappingFeatureProviderFeatureMeasureDataSource = '//*[@id="mappings-grid"]//td[3]'
mappingFeatureProviderFeatureMeasureResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[3]'
mappingFeatureProviderFeatureMeasureColumnName = '//*[@id="mappings-grid_c2"]'
mappingFeatureProviderFeatureMeasureField = '//*[@id="MappingFeature_source_measure"]'

#data by Icecat Feature
mappingFeatureIcecatFeatureDataSource = '//*[@id="mappings-grid"]//td[4]'
mappingFeatureIcecatFeatureResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[4]'
mappingFeatureIcecatFeatureColumnName = '//*[@id="mappings-grid_c3"]'
mappingFeatureIcecatFeatureField = '//*[@id="MappingFeature_icecat_feature_name"]'

#data by Icecat Feature Measure
mappingFeatureIcecatFeatureMeasureDataSource = '//*[@id="mappings-grid"]//td[5]'
mappingFeatureIcecatFeatureMeasureResultAfterSearch = '//*[@id="mappings-grid"]//tr[1]/td[5]'
mappingFeatureIcecatFeatureMeasureColumnName = '//*[@id="mappings-grid_c4"]'
mappingFeatureIcecatFeatureMeasureField = '//*[@id="MappingFeature_icecat_feature_measure"]'

#data by Mapping Status
mappingFeatureMappingStatusSelectDropDown = '//*[@id="MappingFeature_isMapped"]'
mappingFeatureMappingStatusResultOnPage = '//*[@id="mappings-grid"]//td/div/span'




#1.5 Mappings -> Unit Conversion Rules
unitConversionRulesButton = '//*[@id="top"]//div//li[6]//li[6]//a'

unitConversionRulesSearchButton = '//*[@id="yw1"]//td[2]/button'
unitConversionRulesResetButton = '//*[@id="reset-button-yw1"]'
unitConversionRulesTitlePage = '//*[@id="content"]//h3'

#data by Icecat Measure
unitConversionRulesIcecatMeasureDataSource = '//*[@id="yw1"]//table[2]//td[1]'
unitConversionRulesIcecatMeasureResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[1]'
unitConversionRulesIcecatMeasureColumnName = '//*[@id="yw1_c0"]'
unitConversionRulesIcecatMeasureField = '//*[@id="UnitRule_icecat_measure_name_sign"]'

#data by CMS Measure
unitConversionRulesCMSMeasureDataSource = '//*[@id="yw1"]//table[2]//td[3]'
unitConversionRulesCMSMeasureResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[3]'
unitConversionRulesCMSMeasureColumnName = '//*[@id="yw1_c2"]'
unitConversionRulesCMSMeasureField = '//*[@id="UnitRule_measure_name_sign"]'

#data by Rule (1)
unitConversionRulesDataSourceFirst = '//*[@id="yw1"]//table[2]//td[1]'
unitConversionRulesResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[1]'
unitConversionRulesCMSMeasureColumnNameByRule1 = '//*[@id="yw1_c0"]'
unitConversionRulesField = '//*[@id="UnitRule_cross_search"]'

#data by Rule (2)
unitConversionRulesDataSourceSecond = '//*[@id="yw1"]//table[2]//td[3]'
unitConversionRulesResultAfterSearchSecond = '//*[@id="yw1"]//table[2]//tr[1]/td[3]'
unitConversionRulesCMSMeasureColumnNameByRule2 = '//*[@id="yw1_c2"]'





#Catalog Management -> Price Rules Management

priceRulesManagementButton = '//*[@id="top"]//li[2]//li[7]/div/a'


#Price Rules Management -> Price Rules
priceRulesButton = '//*[@id="top"]//li[2]//li[7]//li[2]//a'

priceRulesSearchButton = '//*[@id="yw1"]//td[2]/button'
priceRulesResetButton = '//*[@id="reset-button-yw1"]'
priceRulesTitlePage = '//*[@id="content"]//h3'

#data by Category select2
priceRulesCategoryDataSource = '//*[@id="yw1"]//table[2]//td[10]'
priceRulesCategoryResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[10]'
priceRulesCategoryColumnName = '//*[@id="yw1_c9"]'
priceRulesCategorySelect2 = '//*[@id="s2id_PriceRules_searchCategory"]//a'
priceRulesCategorySelect2Field = '//*[@id="select2-drop"]//div/input'
priceRulesCategoryNotification = '//*[@id="select2-drop"]/ul/li[1]/div'

#data by Manufacturer select2
priceRulesManufacturerDataSource = '//*[@id="yw1"]//table[2]//td[11]'
priceRulesManufacturerResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[11]'
priceRulesManufacturerColumnName = '//*[@id="yw1_c10"]'
priceRulesManufacturerSelect2 = '//*[@id="s2id_PriceRules_searchManufacturer"]//a'
priceRulesManufacturerSelect2Field = '//*[@id="select2-drop"]//div/input'
priceRulesManufacturerNotification = '//*[@id="select2-drop"]//ul/li[1]/div'

#data by Product MPN
priceRulesProductMPNDataSource = '//*[@id="yw1"]//table[2]//td[11]'
priceRulesProductMPNResultAfterSearch = '//*[@id="yw1"]//table[2]//tr[1]/td[14]'
priceRulesProductMPNColumnName = '//*[@id="yw1_c13"]'
priceRulesProductMPNField = '//*[@id="PriceRules_mpn"]'

#data by Supplier select dropdown
priceRulesSupplierSelectDropDown = '//*[@id="PriceRules_supplier"]'
priceRulesSupplierResultOnPage = '//*[@id="yw1"]//td/div/span'

#data by Group ID select dropdown
priceRulesGroupIDSelectDropDown = '//*[@id="PriceRules_group_id"]'
priceRulesGroupIdResultOnPage = '//*[@id="yw1"]//td/div/span'





#Customers -> Customers Management

customersButton = '//*[@id="top"]//nav/ul/li[3]/div/a'

customersManagementButton = '//*[@id="top"]//nav/ul/li[3]//li//a'

customersManagementSearchButton = '//*[@id="customer-grid"]//td[2]/button'
customersManagementResetButton = '//*[@id="reset-button-customer-grid"]'
customersManagementTitlePage = '//*[@id="content"]//h3'

#data by Customer ID
customersManagementCustomerIdDataSource = '//*[@id="customer-grid"]//td/a/span'
customersManagementCustomerIdResultAfterSearch = '//*[@id="customer-grid"]//tr[1]/td[1]//a/span'
customersManagementCustomerIdColumnName = '//*[@id="customer-grid_c0"]'
customersManagementCustomerIdField = '//*[@id="Customer_customer_id"]'

#data by First Name
customersManagementFirstNameDataSource = '//*[@id="customer-grid"]//table[2]//td[2]'
customersManagementFirstNameResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[2]'
customersManagementFirstNameColumnName = '//*[@id="customer-grid_c1"]'
customersManagementFirstNameField = '//*[@id="Customer_first_name"]'

#data by Last Name
customersManagementLastNameDataSource = '//*[@id="customer-grid"]//table[2]//td[3]'
customersManagementLastNameResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[3]'
customersManagementLastNameColumnName = '//*[@id="customer-grid_c2"]'
customersManagementLastNameField = '//*[@id="Customer_last_name"]'

#data by Phone
customersManagementPhoneDataSource = '//*[@id="customer-grid"]//table[2]//td[4]'
customersManagementPhoneResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[4]'
customersManagementPhoneColumnName = '//*[@id="customer-grid_c3"]'
customersManagementPhoneField = '//*[@id="Customer_phone"]'

#data by Email
customersManagementEmailDataSource = '//*[@id="customer-grid"]//table[2]//td[5]'
customersManagementEmailResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[5]'
customersManagementEmailColumnName = '//*[@id="customer-grid_c4"]'
customersManagementEmailField = '//*[@id="Customer_email"]'

#data by Country
customersManagementCountryDataSource = '//*[@id="customer-grid"]//table[2]//td[6]'
customersManagementCountryResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[6]'
customersManagementCountryColumnName = '//*[@id="customer-grid_c5"]'
customersManagementCountryField = '//*[@id="Customer_country"]'

#data by Company
customersManagementCompanyDataSource = '//*[@id="customer-grid"]//table[2]//td[7]'
customersManagementCompanyResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[7]'
customersManagementCompanyColumnName = '//*[@id="customer-grid_c6"]'
customersManagementCompanyField = '//*[@id="Customer_company"]'

#data by Job Title
customersManagementJobTitleDataSource = '//*[@id="customer-grid"]//table[2]//td[8]'
customersManagementJobTitleResultAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[8]'
customersManagementJobTitleColumnName = '//*[@id="customer-grid_c7"]'
customersManagementJobTitleField = '//*[@id="Customer_job_title"]'

#data by Type
customersManagementTypeSelectDropDown = '//*[@id="Customer_type"]'
customersManagementTypeResultOnPage = '//*[@id="customer-grid"]//td/div/span'

#data by Status
customersManagementStatusSelectDropDown = '//*[@id="Customer_status"]'
customersManagementStatusResultOnPage = '//*[@id="customer-grid"]//td/div/span'





#FO Settings -> Search Management -> Category Search Management
foSettingsButton = '//*[@id="top"]//nav/ul/li[4]/div/a'
searchManagementButton = '//*[@id="top"]//li[4]//li[3]/div/a'
categorySearchManagementButton = '//*[@id="top"]//li[4]//li[3]//li//a'

categorySearchManagementSearchButton = '//*[@id="yw2"]//table[1]//td[2]/button'
categorySearchManagementResetButton = '//*[@id="reset-button-yw2"]'
categorySearchManagementTitlePage = '//*[@id="content"]//h3'

#data by Category
categorySearchManagementDataSource = '//*[@id="yw2"]//table[2]//td[1]'
categorySearchManagementResultAfterSearch = '//*[@id="yw2"]//table[2]//tr[1]/td[1]'
categorySearchManagementColumnName = '//*[@id="yw2_c0"]'
categorySearchManagementField = '//*[@id="Category_name_search"]'




#FO Settings -> Synonyms
synonymsButton = '//*[@id="top"]//li[4]//li[4]//a'

synonymsSearchButton = '//*[@id="synonyms-grid"]//table[1]//button'
synonymsResetButton = '//*[@id="reset-button-synonyms-grid"]'
synonymsTitlePage = '//*[@id="content"]//h3'

#data by Rule
synonymsRuleDataSource = '//*[@id="synonyms-grid"]//table[2]//td[2]'
synonymsRuleResultAfterSearch = '//*[@id="Synonym_rule"]'
synonymsRuleColumnName = '//*[@id="synonyms-grid_c1"]'
synonymsRuleField = '//*[@id="Synonym_rule"]'




#Imports -> History And Statuses
importsButton = '//*[@id="top"]//nav/ul/li[5]/div/a'
historyAndStatusesButton = '//*[@id="top"]//nav/ul/li[5]//ul/li//a'

historyAndStatusesSearchButton = '//*[@id="imports-grid"]//td[2]/button'
historyAndStatusesResetButton = '//*[@id="reset-button-imports-grid"]'
historyAndStatusesTitlePage = '//*[@id="imports_index_page"]//h3'

#data by Import Name
historyAndStatusesImportNameDataSource = '//*[@id="imports-grid"]//table[2]//td[1]'
historyAndStatusesImportNameResultAfterSearch = '//*[@id="imports-grid"]//table[2]//tr[1]/td[1]'
historyAndStatusesColumnName = '//*[@id="imports-grid_c0"]'
historyAndStatusesField = '//*[@id="Imports_import_name"]'

#data by Type
historyAndStatusesTypeSelectDropDown = '//*[@id="Imports_type"]'
historyAndStatusesResultAfterSearch = '//*[@id="imports-grid"]//table[2]//tr[1]/td[2]'

#data by Last Start Time
historyAndStatusesLastStartTimeDataSource = '//*[@id="imports-grid"]//table[2]//td[3]'
historyAndStatusesLastStartTimeResultAfterSearch = '//*[@id="imports-grid"]//table[2]//tr[1]/td[3]'
historyAndStatusesLastStartTimeColumnName = '//*[@id="imports-grid_c2"]'
historyAndStatusesLastStartTimeField = '//*[@id="Imports_last_start_time"]'

#data by Last Finish Time
historyAndStatusesLastFinishTimeDataSource = '//*[@id="imports-grid"]//table[2]//td[4]'
historyAndStatusesLastFinishTimeResultAfterSearch = '//*[@id="imports-grid"]//table[2]//tr[1]/td[4]'
historyAndStatusesLastFinishTimeColumnName = '//*[@id="imports-grid_c3"]'
historyAndStatusesLastFinishTimeField = '//*[@id="Imports_last_finish_time"]'

#data by Last Status
#refactoring
#!!!!!
#!!!!!




#Administration -> Manage Admins
administrationButton = '//*[@id="top"]//nav/ul/li[6]/div/a'

manageAdminsButton = '//*[@id="top"]//nav/ul/li[6]/div/ul/li[2]//a'

manageAdminsSearchButton = '//*[@id="user-grid"]//td[2]/button'
manageAdminsResetButton = '//*[@id="reset-button-user-grid"]'
manageAdminsTitlePage = '//*[@id="content"]//h3'

#data by ID
manageAdminsIdDataSource = '//*[@id="user-grid"]//td[1]/a/span'
manageAdminsIdResultAfterSearch = '//*[@id="user-grid"]//tr[1]/td[1]/a/span'
manageAdminsIdColumnName = '//*[@id="user-grid_c0"]'
manageAdminsIdField = '//*[@id="User_id"]'

#data by Username
manageAdminsUsernameDataSource = '//*[@id="user-grid"]//table[2]//td[2]'
manageAdminsUserNameResultAfterSearch = '//*[@id="user-grid"]//table[2]//tr[1]/td[2]'
manageAdminsUsernameColumnName = '//*[@id="user-grid_c1"]'
manageAdminsUsernameField = '//*[@id="User_username"]'

#data by Email
manageAdminsEmailDataSource = '//*[@id="user-grid"]//table[2]//td[3]'
manageAdminsEmailResultAfterSearch = '//*[@id="user-grid"]//table[2]//tr[1]/td[3]'
manageAdminsEmailColumnName = '//*[@id="user-grid_c2"]'
manageAdminsEmailField = '//*[@id="User_email"]'

#data by Registration Date
manageAdminsRegistrationDateDataSource = '//*[@id="user-grid"]//table[2]//td[4]'
manageAdminsRegistrationDateResultAfterSearch = '//*[@id="user-grid"]//table[2]//tr[1]/td[4]'
manageAdminsRegistrationDateColumnName = '//*[@id="user-grid_c3"]'
manageAdminsRegistrationDateField = '//*[@id="User_create_at"]'

#data by Last Visit
manageAdminsLastVisitDataSource = '//*[@id="user-grid"]//table[2]//td[5]'
manageAdminsLastVisitResultAfterSearch = '//*[@id="user-grid"]//table[2]//tr[1]/td[5]'
manageAdminsLastVisitColumnName = '//*[@id="user-grid_c4"]'
manageAdminsLastVisitField = '//*[@id="User_lastvisit_at"]'

#data by Superuser
manageAdminsSuperuserSelectDropDown = '//*[@id="User_superuser"]'
manageAdminsSuperuserResultAfterSearch = '//*[@id="user-grid"]//td/div/span'




#Administration -> Payment Method
paymentMethodButton = '//*[@id="top"]//nav/ul/li[6]//li[5]//a'

paymentMethodSearchButton = '//*[@id="payment-method-grid"]//td[2]/button'
paymentMethodResetButton = '//*[@id="reset-button-payment-method-grid"]'
paymentMethodPageTitle = '//*[@id="content"]//h3'

#data by Code
paymentMethodCodeDataSource = '//*[@id="payment-method-grid"]//tr/td[2]/input' #'//*[@id="payment-method-grid"]//table[2]//td[2]'
paymentMethodCodeResultAfterSearch = '//*[@id="payment-method-grid"]//table[2]//tr[1]/td[2]'
paymentMethodCodeColumnName = '//*[@id="payment-method-grid_c1"]'
paymentMethodCodeField = '//*[@id="PaymentMethod_code"]'





#Administration -> Shipping Method
shippingMethodButton = '//*[@id="top"]//nav/ul/li[6]//li[6]//a'

shippingMethodSearchButton = '//*[@id="shipping-method-grid"]//td[2]/button'
shippingMethodResetButton = '//*[@id="reset-button-shipping-method-grid"]'
shippingMethodPageTitle = '//*[@id="shippingMethods"]//h3'

#data by Code
shippingMethodCodeDataSource = '//*[@id="shipping-method-grid"]//table[2]//td[2]'
shippingMethodCodeResultAfterSearch = '//*[@id="shipping-method-grid"]//table[2]//tr[1]/td[2]'
shippingMethodCodeColumnName = '//*[@id="shipping-method-grid_c1"]'
shippingMethodCodeField = '//*[@id="ShippingMethod_code"]'

#data by Name
shippingMethodNameDataSource = '//*[@id="shipping-method-grid"]//table[2]//td[3]'
shippingMethodNameResultAfterSearch = '//*[@id="shipping-method-grid"]//table[2]//tr[1]/td[3]'
shippingMethodNameColumnName = '//*[@id="shipping-method-grid_c2"]'
shippingMethodNameField = '//*[@id="ShippingMethod_name"]'

#data by Rate
shippingMethodRateDataSource = '//*[@id="shipping-method-grid"]//table[2]//td[4]'
shippingMethodRateResultAfterSearch = '//*[@id="shipping-method-grid"]//table[2]//tr[1]/td[4]'
shippingMethodRateColumnName = '//*[@id="shipping-method-grid_c3"]'
shippingMethodRateField = '//*[@id="ShippingMethod_rate"]'

#data by Rate Type
shippingMethodRateTypeSelectDropDown = '//*[@id="ShippingMethod_rate_type"]'
shippingMethodRateTypeResultOnPage = '//*[@id="shipping-method-grid"]//td[1]//span'

#search by Rating
shippingMethodRatingDataSource = '//*[@id="shipping-method-grid"]//table[2]//td[6]'
shippingMethodRatingResultAfterSearch = '//*[@id="shipping-method-grid"]//table[2]//tr[1]/td[6]'
shippingMethodRatingColumnName = '//*[@id="shipping-method-grid_c5"]'
shippingMethodRatingField = '//*[@id="ShippingMethod_rating"]'

#search by Active select dropdown
shippingMethodActiveSelectDropDown = '//*[@id="ShippingMethod_active"]'
shippingMethodActiveResultOnPage = '//*[@id="shipping-method-grid"]//td[1]//span'





#Administration -> Language -> Management
languageButton = '//*[@id="top"]//li[6]//li[9]/div/a'

languageManagementButton = '//*[@id="top"]//li[6]//li[9]//li[1]//a'

languageManagementSearchButton = '//*[@id="grid"]//table[1]//td[2]/button'
languageManagementResetButton = '//*[@id="reset-button-grid"]'
languageManagementPageTitle = '//*[@id="content"]//ol/li[5]/span'               #refactoring this!!!!

#data by Language ID
languageManagementLanguageIdDataSource = '//*[@id="grid"]//td[1]/a/span'
languageManagementLanguageIdResultAfterSearch = '//*[@id="grid"]//tr[1]/td[1]/a/span'
languageManagementLanguageIdColumnName = '//*[@id="grid_c0"]'
languageManagementLanguageIdField = '//*[@id="Languages_language_id"]'

#data by Language Name
languageManagementLanguageNameDataSource = '//*[@id="Languages_name"]'
languageManagementLanguageNameResultAfterSearch = '//*[@id="Languages_name"]'
languageManagementLanguageNameColumnName = '//*[@id="grid_c1"]'
languageManagementLanguageNameField = '//*[@id="Languages_name"]'

#data by Language Code
languageManagementLanguageCodeDataSource = '//*[@id="Languages_code"]'
languageManagementLanguageCodeResultAfterSearch = '//*[@id="Languages_code"]'
languageManagementLanguageCodeColumnName = '//*[@id="grid_c2"]'
languageManagementLanguageCodeField = '//*[@id="Languages_code"]'

#data by Active select dropdown
languageManagementLanguageActiveSelectDropDown = '//*[@id="Languages_active"]'
languageManagementLanguageResultOnPage = '//*[@id="grid"]//td[1]/div/span'

#data by Sort
languageManagementSortDataSource = '//*[@id="Languages_sort"]'
languageManagementSortResultAfterSearch = '//*[@id="Languages_sort"]'
languageManagementSortColumnName = '//*[@id="grid_c4"]'
languageManagementSortField = '//*[@id="Languages_sort"]'





#Administration -> Language -> Dictionaries
languageDictionariesButton = '//*[@id="top"]//li[6]//li[9]//li[2]//a'

languageDictionariesSearchButton = '//*[@id="grid"]//tr/td[2]/button'
languageDictionariesResetButton = '//*[@id="reset-button-grid"]'
languageDictionariesPageTitle = '//*[@id="content"]//h2'

#data by Message
languageDictionariesMessageDataSource = '//*[@id="SourceMessage_message"]'
languageDictionariesMessageResultAfterSearch = '//*[@id="SourceMessage_message"]'
languageDictionariesMessageColumnName = '//*[@id="grid_c0"]'
languageDictionariesMessageField = '//*[@id="SourceMessage_message"]'

#data by Category select dropdown
languageDictionariesCategorySelectDropDown = '//*[@id="SourceMessage_category"]'
languageDictionariesCategoryResultOnPage = '//*[@id="grid"]//td[1]//span'





#Administration -> Mail Template
mailTemplateButton = '//*[@id="top"]//li[6]//li[10]//a'

mailTemplateSearchButton = '//*[@id="grid"]//td[2]/button'
mailTemplateResetButton = '//*[@id="reset-button-grid"]'
mailTemplatePageTitle = '//*[@id="content"]//h3'

#data by ID
mailTemplateIdDataSource = '//*[@id="grid"]//td[1]/a/span'
mailTemplateIdResultAfterSearch = '//*[@id="grid"]//tr[1]/td[1]/a/span'
mailTemplateIdColumnName = '//*[@id="grid_c0"]'
mailTemplateIdField = '//*[@id="MailTemplate_id"]'

#search by Key
mailTemplateKeyDataSource = '//*[@id="grid"]//table[2]//td[2]'
mailTemplateKeyResultAfterSearch = '//*[@id="grid"]//table[2]//tr[1]/td[2]'
mailTemplateKeyColumnName = '//*[@id="grid_c1"]'
mailTemplateKeyField = '//*[@id="MailTemplate_key"]'

#search by Category select dropdown
mailTemplateCategorySelectDropDown = '//*[@id="MailTemplate_category"]'
mailTemplateCategoryResultOnPage = '//*[@id="grid"]//td[1]/div/span'