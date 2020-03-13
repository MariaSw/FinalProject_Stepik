#базовая страница, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():
    #конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #открывать нужную страницу в браузере
    def open(self):
        #внутри класса
        self.browser.get(self.url)
        #за пределами класса это будет вызываться так
        #BasePage.browser.get(BasePage.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def URL_contains(self, what):
        return what in self.browser.current_url

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def elements_equal(self, howexp, whatexp, howact, whatact):
        exp = self.browser.find_element(howexp, whatexp).text
        act = self.browser.find_element(howact, whatact).text
        return exp==act
    #myoption


