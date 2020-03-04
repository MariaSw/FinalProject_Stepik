#базовая страница, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером

from selenium.common.exceptions import NoSuchElementException

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
