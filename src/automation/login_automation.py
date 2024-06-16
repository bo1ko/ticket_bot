import pathlib
import time

from .automation import Automation
from pynput.keyboard import Key, Controller


class LoginAutomation(Automation):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self._keyboard_controller = Controller()
        self._file_path = f'{pathlib.Path(__file__).parent.parent.resolve()}\\key\\key.jks'
    
    
    def login(self, password):
        # page: https://eq.hsc.gov.ua/
        # checkbox
        self._click_element('/html/body/main/div/div/div/div/div/div/div[2]/input')
        time.sleep(1)

        # submit button
        self._click_element('/html/body/main/div/div/div/div/div/div/div[2]/div[2]/a')
        time.sleep(1)
        
        # page: id.gov.ua
        # button - Файловий носій
        self._click_element('//*[@id="root"]/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/a')
        time.sleep(1)
        
        # page: id.gov.ua/euid-auth-js
        # button - Перетягніть сюди файл ключа 
        self._click_element('//*[@id="PKeyFileName"]/p/span')
        time.sleep(1)
        
        # upload jks file
        self._keyboard_controller = Controller()
        self._keyboard_controller.type(self._file_path)
        self._keyboard_controller.press(Key.enter)
        time.sleep(1)
        
        # input password
        self._type_text('/html/body/div/div/div[1]/div[2]/div/div[1]/form/div[3]/div/div[2]/div/input', password)
        time.sleep(1)
        
        # next button
        self._click_element('//*[@id="id-app-login-sign-form-file-key-sign-button"]')
        time.sleep(1)

        # accept button
        self._click_element('//*[@id="btnAcceptUserDataAgreement"]')
        time.sleep(1)
