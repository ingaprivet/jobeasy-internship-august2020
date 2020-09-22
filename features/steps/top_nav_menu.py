from behave import given, when, then


@given('Open Home page')
def open_home_page(context):
    context.driver.get('https://gettop.us//')


@given('GetTop logo is displayed')
def logo_present(context):
    context.app_internship.top_menu.logo_present()


@when('Click on GetTop logo')
def go_to_page(context):
    context.app_internship.top_menu.go_to_page()


@then('https://gettop.us/ page is displayed')
def verify_page_displayed(context):
    context.app_internship.top_menu.verify_page_displayed()


@when('Select a Mac product from header-nav-main and open correct product page')
def select_product_opens_page(context):
    context.app_internship.top_menu.select_product_opens_page()


@when('Hoover over header-nav-main item and display correct menu options')
def hover_and_display(context):
    context.app_internship.top_menu.hover_and_display()


@when('Clicking on Account icon')
def go_to_login_form(context):
    context.app_internship.top_menu.go_to_login_form()


@then('Login form opens')
def verify_login_form(context):
    context.app_internship.top_menu.verify_login_form()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app_internship.cart_func.click_cart_icon()


@then('Verify {search_text} text present')
def verify_found_results_text(context, search_text):
    context.app_internship.cart_func.verify_found_results_text(search_text)


# @given('Open a Product page')
# def open_amazon(context):
#    context.driver.get('https://gettop.us/product/airpods/')

@given('Open Product {product_id} page')
def open_prod_page(context, product_id):
    context.app_internship.prod_page.open_prod_page(product_id)

@when('Click on Add to Cart button')
def click_add_button(context):
    context.app_internship.cart_func.click_add_button()


@then('Verify top nav menu displays correct Product price')
def verify_correct_prod_price_displayed(context):
    context.app_internship.cart_func.verify_correct_prod_price_displayed()


@then('Verify top nav menu displays correct amount of items')
def verify_correct_items_amount_displayed(context):
    context.app_internship.cart_func.verify_correct_items_amount_displayed()


@when('Hover over cart icon')
def hover_cart_icon(context):
    context.app_internship.cart_func.hover_cart_icon()


@then('Click on Remove button')
def click_remove_from_cart(context):
    context.app_internship.cart_func.click_remove_from_cart()


@then('Verify {no_prod_cart} message is displayed')
# No products in the cart.
def verify_product_removed(context, no_prod_cart):
    context.app_internship.cart_func.verify_product_removed(no_prod_cart)


@then('Click View Cart button')
def click_view_cart_button(context):
    context.app_internship.cart_func.click_view_cart_button()


@then('Verify correct page is displayed')
def verify_page_displayed(context):
    context.app_internship.cart_func.verify_page()
    #context.app_internship.top_menu.verify_page_displayed()


@then('Click on Checkout button')
def click_checkout_button(context):
    context.app_internship.cart_func.click_checkout_button()


@then('Verify correct products shown')
def verify_cart_correct_products(context):
    context.app_internship.cart_func.verify_cart_correct_products()
    #context.app_internship.top_menu.verify_page_displayed()


@then('Verify correct subtotal shown')
def verify_cart_correct_subtotal(context):
    context.app_internship.cart_func.verify_cart_correct_subtotal()
