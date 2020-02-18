import time
# Click on Factory Configuration Screen option in MenuBar
# On Clicking that, Factory Configuration Screen should be Opened and Default Reel Width is 22, Number of blades is 11,
# Infinicut model is Pro Rotary Battery and Return Button should be displayed.

def test_find_infinicut_screen(self):
    find_infinicut_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Find Infinicut']")
    find_infinicut_button.click()


def test_dashboard_screen(self):
    dashboard_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Dashboard']")
    dashboard_button.click()
    time.sleep(5)

def test_infinicut_status_screen(self):
    infinicut_status_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Infinicut Status']")
    infinicut_status_button.click()
    time.sleep(5)


def test_deck_settings_screen(self):
    deck_settings_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Deck Settings']")
    deck_settings_button.click()
    time.sleep(5)

def test_cassette_settings_screen(self):
    casette_settings_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Cassette Settings']")
    casette_settings_button.click()

def test_drive_settings_screen(self):
    drive_settings_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Drive Settings']")
    drive_settings_button.click()

def test_diagnostics_screen(self):
    diagnostics_screen_button = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Diagnostics Screen']")
    diagnostics_screen_button.click()

def test_factory_configuration_screen(self):
    factory_configuration = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Factory Configuration Screen']")
    factory_configuration.click()
    # screen stays for 5 seconds
    time.sleep(3)