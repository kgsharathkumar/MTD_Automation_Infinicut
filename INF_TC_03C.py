import time

def test_return_button_onscreen(self):
    # click on "Return" button using resource id
    # On clicking return button it redirects to Dashboard screen with updated settings of factory configuration screen
    return_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/factory_return')
    return_button.click()

    # wait for 5 seconds
    #time.sleep(5)