import time

# In this testcase we are checking the DashBoard screen.
# On executing this, Dashboard Screen should be opened and Latest settings Reel Speed, Max Walking Speed Should be displayed, Default Moisture type should be Medium.
def test_open_app(self):
    self.driver.implicitly_wait(30)
    # Click on "Stop Searching" button by using resource id
    stop_searching_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/btn_search_mowers')
    stop_searching_button.click()
    self.driver.implicitly_wait(30)
    # screen stays for 5 seconds
    time.sleep(3)

    # Click on "Find Infinicut" button by using resource id
    find_infinicut_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/btn_search_mowers')
    find_infinicut_button.click()
    # screen stays for 10 seconds
    #time.sleep(10)

    # we are choosing one specific mower from avilable mowers using its xpath
    select_mower = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Infini A9']")
    select_mower.click()
    # screen stays for 15 seconds
    time.sleep(10)
