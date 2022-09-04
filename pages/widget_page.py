from locators.widget_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': {'title': self.locators.SECTION_FIRST,
                               'content': self.locators.SECTION_TEXT_FIRST},
                     'second': {'title': self.locators.SECTION_SECOND,
                                'content': self.locators.SECTION_TEXT_SECOND},
                     'third': {'title': self.locators.SECTION_THIRD,
                               'content': self.locators.SECTION_TEXT_THIRD}
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        self.go_to_element(section_title)
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]