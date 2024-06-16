from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Automation:

    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
    
    def _click_element(self, xpath):
        self._wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()

    def _find_element(self, xpath):
        return self._wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def _find_all_elements_by_class(self, class_name):
        return self._wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))

    def _type_text(self, xpath, text):
        self._driver.find_element(By.XPATH, xpath).send_keys(text)
