from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver


    checkOutButton = (By.XPATH,"//button[@class='btn btn-success']")
    dropdown = (By.ID,"country")
    dropdownList = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    confirmMessage = (By.CSS_SELECTOR,"[class*='alert-success']")
    def checkOutBtn(self):
        return self.driver.find_element(*ConfirmPage.checkOutButton)

    def getDropdown(self):
        return self.driver.find_element(*ConfirmPage.dropdown)

    def getdropdownList(self):
        return self.driver.find_element(*ConfirmPage.dropdownList)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getMessage(self):
        return self.driver.find_element(*ConfirmPage.confirmMessage)