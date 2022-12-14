import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators, SliderPageLocators, \
    ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):

        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
            input_multi.click()
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.DELETE_ONE_VALUE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 6))
        progress_bar_button.click()

        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text

        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {'what': {'title': self.locators.TAB_WHAT,
                               'content': self.locators.CONTENT_WHAT},
                     'origin': {'title': self.locators.TAB_ORIGIN,
                                'content': self.locators.CONTENT_ORIGIN},
                     'use': {'title': self.locators.TAB_USE,
                               'content': self.locators.CONTENT_USE},
                     'more': {'title': self.locators.TAB_MORE,
                               'content': self.locators.CONTENT_MORE},
                     }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tooltips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        time.sleep(1)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS_TEXT)
        text = tooltip_text.text
        return text

    def check_tooltip(self):
        tooltip_text_button = self.get_text_from_tooltips(self.locators.BUTTON_HOVER, self.locators.BUTTON_TOOLTIP)
        tooltip_text_input = self.get_text_from_tooltips(self.locators.INPUT_HOVER, self.locators.INPUT_TOOLTIP)
        tooltip_text_contrary = self.get_text_from_tooltips(self.locators.CONTRARY_LINK, self.locators.CONTRARY_TOOLTIP)
        tooltip_text_section = self.get_text_from_tooltips(self.locators.SECTION_LINK, self.locators.SECTION_TOOLTIP)
        return tooltip_text_button, tooltip_text_input, tooltip_text_contrary, tooltip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_items_list = self.elements_are_present(self.locators.MENU_LIST)
        data = []
        for item in menu_items_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data

