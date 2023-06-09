from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.login_page import BasePage
import pytest
import time



# step 4.3.2 and 4.3.3
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.name_and_price()
    time.sleep(5)

# -----------



# step 4.3.4
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="names assert error")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_links(browser, link):

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.name_and_price()
    time.sleep(1)

# ------------



# step 4.3.6
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.step6
class Test_Negative_Check():

    # падает
    @pytest.mark.xfail 
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser): 
        page = ProductPage(browser, link, 0)   
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    # ждет 4 сек и проходит
    def test_guest_cant_see_success_message(self, browser): 

        page = ProductPage(browser, link, 0)   
        page.open()
        page.should_not_be_success_message()

    # ждет 4 сек и падает
    @pytest.mark.xfail 
    def test_message_disappeared_after_adding_product_to_basket(self, browser): 

        page = ProductPage(browser, link, 0)   
        page.open()
        page.add_to_basket()
        page.should_be_success_message()

# ------------



# step 4.3.8
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_should_see_login_link_on_product_page(browser):

    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# -----------



# step 4.3.10
@pytest.mark.step10
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"

    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()

    page.is_basket_empty()
    page.basket_empty_text_present()

# -----------


# step 4.3.13
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):

        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()
        

    def test_user_cant_see_success_message(self, browser):

        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.name_and_price()
