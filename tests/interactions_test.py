from pages.interactions_page import SortablePage, SelectablePage, DroppablePage, DraggablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "drag and drop has not been done"
            assert grid_before != grid_after, "drag and drop has not been done"


    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no active element"
            assert len(item_grid) > 0, "no active element"

    class TestDroppablePage:

        def test_simple_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result_text = droppable_page.simple_drop()
            assert result_text == "Dropped!", "the element has not been dropped"

        def test_acceptable_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_acceptable_text, acceptable_text = droppable_page.acceptable_drop()
            assert not_acceptable_text == "Drop here", "the element has not been dropped"
            assert acceptable_text == "Dropped!", "the element has not been dropped"

        def test_prevent_propogation_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_not_greedy, text_not_greedy_inner, text_greedy, text_greedy_inner = droppable_page.prevent_propogation()
            assert text_not_greedy == "Dropped!", "the text has not been changed"
            assert text_not_greedy_inner == "Dropped!", "the text has not been changed"
            assert text_greedy == "Outer droppable", "the text has been changed"
            assert text_greedy_inner == "Dropped!", "the text has not been changed"

        def test_revert_drop(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.will_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.will_revert_draggable('not_will')
            assert will_after_move != will_after_revert, "the element has not reverted"
            assert not_will_after_move == not_will_after_revert, "the element has reverted"


    class TestDraggablePage:

        def test_simple_drag(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag()
            assert before != after, "the position has not been changed"

