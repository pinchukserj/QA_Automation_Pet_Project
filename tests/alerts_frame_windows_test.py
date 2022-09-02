from pages.alerts_frame_windows_page import BrowserWindowsPage


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