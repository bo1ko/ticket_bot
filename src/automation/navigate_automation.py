import time

from .automation import Automation


class NavigateAutomation(Automation):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def _get_number_from_string(self, string):
        return int("".join(filter(str.isdigit, string)))

    def navigate(self, first_date):
        # page: https://eq.hsc.gov.ua/step0
        # button - Записатись
        self._click_element('/html/body/main/div/div/div[1]/div[2]/div/button[1]')
        time.sleep(1)

        # page: https://eq.hsc.gov.ua/site/step
        # button - Практичний іспит
        self._click_element('/html/body/main/div/div/div[2]/div/div/div/div/a[5]')
        time.sleep(1)

        # page: https://eq.hsc.gov.ua/site/step_pe?
        # button - Практичний іспит (сервісного центру)
        self._click_element('/html/body/main/div/div[1]/div[2]/div/div/div/div/button[1]')
        time.sleep(1)

        # modal menu - Так
        self._click_element('//*[@id="ModalCenterServiceCenter"]/div/div/div[2]/button[1]')
        time.sleep(1)

        # modal menu - Так
        self._click_element('//*[@id="ModalCenterServiceCenter1"]/div/div/div[2]/a[1]')
        time.sleep(1)

        # page: https://eq.hsc.gov.ua/site/step_cs?
        # button - Практичний іспит на категорію B (механіка)
        self._click_element('/html/body/main/div/div/div[2]/div/div/div/div/a[4]')
        time.sleep(1)

        # date list
        date_list = self._find_all_elements_by_class('qtime')
        for date in date_list:
            if self._get_number_from_string(date.text) == first_date:
                date.click()
                break
