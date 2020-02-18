import time

from appium.webdriver.common.touch_action import TouchAction
def test_save_to_database(self):
    # Click on "Save To Database" Button using its resource id
    # On Clicking that button A Screen with Setup name and tiltle should be opened
    save_to_database_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/save_to_database')
    save_to_database_button.click()
    # Screen stays for 5 seconds
    #time.sleep(5)


'''    actions = TouchAction(self.driver)
    element = self.driver.find_element_by_class_name('android.widget.ScrollView')
    self.driver.swipe(475, 900, 475, 200, 400)
    actions.tap(element).perform()
    time.sleep(5)
'''


