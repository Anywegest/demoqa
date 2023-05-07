from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.prov = WebElement(driver, "div.col-12.mt-4.col-md-6")
        self.text_elements = WebElement(driver, 'div.playgound-header > div')
        self.icon_elements = WebElement(driver, '#app > header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        super().__init__(driver, self.base_url)



#    def equal_url(self):
 #       if self.get_url() == 'https://demoqe.com/elements':
  #      # if 'https://demoqe.com/elements' == self.base_url:
   #         return True
    #    return False
