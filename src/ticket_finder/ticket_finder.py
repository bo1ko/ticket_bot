import time

from ..automation.automation import Automation
from ..automation.navigate_automation import NavigateAutomation
from selenium_recaptcha_solver import RecaptchaSolver

class Ticket(Automation):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def _change_page(self, last_date):
        self._click_element('//div[contains(@onclick, "next()")]')

        if int(''.join(filter(str.isdigit, self._find_element('//*[@id="slider"]').text))) == last_date:
            self._driver.refresh()

    def get_ticket(self, maximum_time, last_date, minimal_time=8, first_date=None):
        STATUS_LIST = ["hsc_.png", "hsc_i.png"]
        RECAPTCHA_URL = 'https://eq.hsc.gov.ua/site/recaptcha'
        

        while True:
            try:
                if self._driver.current_url == RECAPTCHA_URL:
                    solver = RecaptchaSolver(self._driver)
                    recaptcha_iframe = self._find_element('//iframe[@title="reCAPTCHA"]')
                    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
                    
                    self._click_element('//*[@id="captchaform"]/button')

                    NavigateAutomation(self._driver, self._wait).navigate(first_date)
                else:
                    point = self._find_element('//img[contains(@style, "z-index: 315;")]')
                    
                    if point.get_attribute('src').split('/')[-1] in STATUS_LIST:
                        point.click()
                        self._find_element('//*[@id="map"]/div[1]/div[6]/div/div[1]')
                        ticket_time = int(self._find_element('//*[@id="id_chtime"]').text.slit(":")[0])
                        time.sleep(0.5)

                        if minimal_time >= ticket_time or ticket_time <= maximum_time:
                            self._click_element('//*[@id="submit"]')
                            self._click_element('/html/body/main/div/div/div[2]/div/div/div/div[5]/a') 

                            time.sleep(10)             
                            return print(f'Ticket: {ticket_time}')
                        else:
                            self._change_page(last_date)
                    else:
                        self._change_page(last_date)
                    
                    time.sleep(1)
            except:
                self._driver.refresh()
