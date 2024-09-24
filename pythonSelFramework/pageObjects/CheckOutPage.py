from subprocess import check_output

from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkOutButton = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    # self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")
    #find_elements(By.CSS_SELECTOR,".card-footer button")[i]

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCheckOutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage