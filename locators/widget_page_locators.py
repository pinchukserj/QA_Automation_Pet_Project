from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_TEXT_FIRST = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECTION_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_TEXT_SECOND = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    SECTION_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_TEXT_THIRD = (By.CSS_SELECTOR, "div[id='section3Content'] p")

class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    DELETE_ONE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")

class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")

class ProgressBarPageLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

class TabsPageLocators:
    TAB_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    CONTENT_WHAT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TAB_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    CONTENT_ORIGIN = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TAB_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    CONTENT_USE = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TAB_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    CONTENT_MORE = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")