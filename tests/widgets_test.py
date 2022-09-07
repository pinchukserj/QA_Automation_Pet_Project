import time

from pages.widget_page import AccordianPage, AutoCompletePage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title_first, content_first = accordian_page.check_accordian('first')
            title_second, content_second = accordian_page.check_accordian('second')
            title_third, content_third = accordian_page.check_accordian('third')
            assert title_first == "What is Lorem Ipsum?" and content_first > 0, "Accordian does not exists"
            assert title_second == "Where does it come from?" and content_second > 0, "Accordian does not exists"
            assert title_third == "Why do we use it?" and content_third > 0, "Accordian does not exists"

    class TestAutoComplete:
        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, "colors does not match"

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before - count_value_after == 1, "color has not been deleted"

        def test_fill_single_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, "the color has not been selected"

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after, "slider does not work"

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.change_progress_bar_value()
            assert value_before != value_after, "progress bar has not been changed"

