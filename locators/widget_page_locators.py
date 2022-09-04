from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_TEXT_FIRST = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_TEXT_SECOND = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_TEXT_THIRD = (By.CSS_SELECTOR, "div[id='section3Content'] p")
