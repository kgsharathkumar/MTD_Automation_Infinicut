import time

from appium.webdriver.common.touch_action import TouchAction

def test_calculate_foc_screen(self):
    # Swipe down the screen to find required button
    actions = TouchAction(self.driver)
    element = self.driver.find_element_by_class_name('android.widget.ScrollView')
    self.driver.swipe(475, 900, 475, 200, 400)
    actions.tap(element).perform()
    #time.sleep(5)
    # Click on "Calculate FOC" button by its resource id
    calculate_foc_button = self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/calculate_foc')
    calculate_foc_button.click()
    #time.sleep(5)

