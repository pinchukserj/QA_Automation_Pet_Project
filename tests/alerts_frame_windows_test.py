import time

from conftest import driver
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab_text = new_tab_page.check_new_tab()
            assert new_tab_text == "This is a sample page", "new tab has not been opened or text is not matched"

        def test_new_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_window_text = new_tab_page.check_new_window()
            assert new_window_text == "This is a sample page", "new window has not been opened or text is not matched"

    class TestAlerts:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "alert did not show up"

        def test_see_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "alert did not appear after 5 sec"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "alert has not been confirmed"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert alert_text == f"You entered {text}", "alert did not show up"

    class TestFrame:
        def test_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "the frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "the frame does not exist"

    class TestNestedFrames:
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame", "Frame does not exist"
            assert child_text == "Child Iframe", "Frame does not exist"

    class TestModalDialogs:
        def test_small_modal_dialog(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            title_small, body_small = modal_dialogs_page.check_small_dialog()
            assert title_small == "Small Modal", "Title of small modal is incorrect"
            assert body_small == "This is a small modal. It has very less content", "Text of small modal is incorrect"

        def test_large_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            title_large, body_large = modal_dialogs_page.check_large_dialog()
            assert title_large == "Large Modal", "Title of large modal is incorrect"
            assert len(body_large) == 574, "Text of large modal is incorrect"

