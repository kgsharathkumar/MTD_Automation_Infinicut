import time

# click on navigation symbol by using symbol xpath and on clicking that Menubar screen should be displayed
def test_find_infinicut(self):
    find_infinicut_button = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Find Infinicut']")
    find_infinicut_button.click()
    # screen stays for 5 seconds
    time.sleep(15)
