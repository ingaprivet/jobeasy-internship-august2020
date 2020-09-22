from pages_internship.base_page import PageServices
from pages_internship.top_menu import TopNavMenuServices
from pages_internship.search_return_page import SearchResultServices
from pages_internship.prod_page import ProductServices
from pages_internship.top_banner import TopBannerServices
from pages_internship.cart_func import CartServices
from pages_internship.page_section import PageSectionServices
from pages_internship.category_page import CategoryServices
from pages_internship.shop_func import ShopServices
from pages_internship.checkout_page import CheckoutServices
from pages_internship.wishlist_page import WishlistServices


class Application_Internship:
    #print(f'in Application_Internship')

    def __init__(self, driver):
        self.driver = driver
        self.page = PageServices(self.driver)
        self.top_banner = TopBannerServices(self.driver)
        self.top_menu = TopNavMenuServices(self.driver)
        self.search_return_page = SearchResultServices(self.driver)
        self.prod_page = ProductServices(self.driver)
        self.cart_func = CartServices(self.driver)
        self.page_section = PageSectionServices(self.driver)
        self.category_page = CategoryServices(self.driver)
        self.shop_func = ShopServices(self.driver)
        self.checkout_page = CheckoutServices(self.driver)
        self.wishlist_page = WishlistServices(self.driver)



