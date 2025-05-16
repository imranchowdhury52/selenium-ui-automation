from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_successful_login():
    driver = get_driver()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    assert dashboard_page.is_dashboard_visible()

    driver.quit()
