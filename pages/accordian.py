from components.components import WebElement

class Accordian:
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        self.sec = WebElement(driver, '#section1Content > p')
        self.lem = WebElement(driver, '#section1Heading')
        self.tion = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.ment = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.mol = WebElement(driver, '#section3Content > p')
        self.driver = driver

    def visit(self):
        return self.driver.get(self.base_url)


