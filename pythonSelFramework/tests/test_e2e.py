
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkOutPage =HomePage.shopItems()
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        confirmPage = checkOutPage.getCheckOutButton(self.driver)
        confirmPage.checkOutBtn().click()
        confirmPage.getDropdown().send_keys("Ind")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmPage.getdropdownList().click()
        confirmPage.getCheckbox().click()
        confirmPage.getPurchaseButton().click()
        textMatch = confirmPage.getMessage().text
        assert ("Success! Thank you!" in textMatch)

