from pages.base_page import BasePage

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqe.com/elements'
        super().__init__(driver, self.base_url)

#    def equal_url(self):
 #       if self.get_url11111() == 'https://demoqe.com/elements':
  #      # if 'https://demoqe.com/elements' == self.base_url:
   #         return True
    #    return False
