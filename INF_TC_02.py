import time

# click on navigation symbol by using symbol xpath and on clicking that Menubar screen should be displayed
def test_open_navigation(self):
    navigation_symbol = self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
    navigation_symbol.click()
    # screen stays for 5 seconds
    time.sleep(3)
