import random
import re
import time

from locators.interactions_locators import InteractionsPageLocators, SelectablePageLocators, DroppablePageLocators, \
    DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = InteractionsPageLocators()

    def get_sortable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text

class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def simple_drop(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def acceptable_drop(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPTABLE)
        self.action_drag_and_drop_to_element(not_acceptable, drop_div)
        text_not_acceptable = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        text_acceptable = drop_div.text
        return text_not_acceptable, text_acceptable

    def prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_inner = not_greedy_inner_box.text
        text_not_greedy = self.element_is_visible(self.locators.NOT_GREEDY_DROPBOX_TEXT).text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_inner = greedy_inner_box.text
        text_greedy = self.element_is_visible(self.locators.GREEDY_DROPBOX_TEXT).text
        return text_not_greedy, text_not_greedy_inner, text_greedy, text_greedy_inner

    def will_revert_draggable(self, type_drag):
        drags = {"will":
                         {'revert': self.locators.WILL_REVERT},

        "not_will": {'revert': self.locators.NOT_REVERT},
                     }
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        will_revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_DRAGGABLE)
        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(2)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    def get_before_and_after_postition(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0,50), random.randint(0,50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position


    def simple_drag(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        before_postion, after_position = self.get_before_and_after_postition(drag_div)
        return before_postion, after_position

