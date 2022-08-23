import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_per_addr = text_box_page.check_filled_form()
            time.sleep(3)
            assert full_name == output_name, "full name does not match"
            assert email == output_email, "email does not match"
            assert current_address == output_curr_addr, "current address does not match"
            assert permanent_address == output_per_addr, "permanent address does not match"

    class TestCheckBox:
        def test_checkbox(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Input checkboxes and output result does not match"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == "Yes", '"Yes" have not been selected'
            assert output_impressive == "Impressive", '"Impressive" have not been selected'
            assert output_no == "No", '"No" have not been selected'


class TestWebTable:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()

        print(new_person)
        print(table_result)
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, "The person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, "age has not been changed"

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == 'No rows found', "Person has not been deleted"

    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50,
                         100], "The number of rows in the table has not been changed or has changed incorrectly"


class TestButtonsPage:

    def test_different_click_on_the_buttons(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_button("double")
        right = button_page.click_on_different_button("right")
        click = button_page.click_on_different_button("click")
        assert double == "You have done a double click", "Double click button was not pressed"
        assert right == "You have done a right click", "Right click button was not pressed"
        assert click == "You have done a dynamic click", "Click button was not pressed"

class TestLinksPage:
    def test_check_link(self, driver):
        link_page = LinksPage(driver, 'https://demoqa.com/links')
        link_page.open()
        href_link, current_url = link_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken or url is incorrect"

    def test_check_broken_link(self, driver):
        link_page = LinksPage(driver, 'https://demoqa.com/links')
        link_page.open()
        response_code = link_page.check_broken_link('https://demoqa.com/bad-request')
        assert response_code == 400, "status code is incorrect"

class TestUploadAndDownload:
    def test_upload_file(self, driver):
        upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_and_download_page.open()
        file_name, result = upload_and_download_page.upload_file()
        assert file_name == result, "file name and result path does not match"

    def test_download_file(self):
        pass