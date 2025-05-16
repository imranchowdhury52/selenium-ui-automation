from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()
