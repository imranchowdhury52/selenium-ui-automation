from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    dashboard_header = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb")

    def is_dashboard_visible(self):
        try:
            return self.driver.find_element(*self.dashboard_header).is_displayed()
            
        except:
            return False