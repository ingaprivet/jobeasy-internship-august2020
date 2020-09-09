from pages_internship.base_page import Page_Internship
from pages_internship.top_menu import TopNavMenu_Internship
from pages_internship.search_return_page import SearchResultsInternship
from pages_internship.prod_page import Product_Internship
from pages_internship.top_banner import TopBanner
from pages_internship.cart_func import CartServices

# from pages_internship.sign_in_services import SignInServices
# from pages_internship.hamburger_menu_services import HamburgerMenuServices



class Application_Internship:
    print(f'in Application_Internship')

    def __init__(self, driver):
        self.driver = driver
        self.page = Page_Internship(self.driver)
        self.top_banner = TopBanner(self.driver)
        self.top_menu = TopNavMenu_Internship(self.driver)
        self.search_return_page = SearchResultsInternship(self.driver)
        self.prod_page = Product_Internship(self.driver)
        self.cart_func = CartServices(self.driver)


        # self.sign_in_services = SignInServices(self.driver)
        # self.hamburger_menu_services = HamburgerMenuServices(self.driver)
