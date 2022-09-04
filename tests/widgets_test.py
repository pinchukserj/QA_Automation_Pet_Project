from pages.widget_page import AccordianPage


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