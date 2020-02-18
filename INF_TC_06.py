import time
from appium.webdriver.common.touch_action import TouchAction

def test_load_from_database(self):
    load_from_database_button= self.driver.find_element_by_id('com.mtd.usa.cubcadet:id/load_from_database')
    load_from_database_button.click()
    #time.sleep(5)
    select_title = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ABC']")
    select_title.click()
    time.sleep(5)


''' actions = TouchAction(self.driver)
    element = self.driver.find_element_by_class_name('android.widget.ScrollView')
    self.driver.swipe(475, 900, 475, 200, 400)
    actions.tap(element).perform()
    time.sleep(5)
'''
