# By IngaB
from behave import given, when, then


@given('Open Shop page')
def open_shop_page(context):
    context.app_internship.shop_func.open_shop_page()


@then('User can see recently viewed items and open them')
def recently_viewed_items_shown(context):
    context.app_internship.shop_func.recently_viewed_items_shown()


@then('Verify User is taken to correct page')
def item_page_shown(context):
    context.app_internship.shop_func.item_page_shown()


@then('User sees {cat_01}, {cat_02}, {cat_03}, {cat_04} under Browse')
def verify_categories_block(context, cat_01, cat_02, cat_03, cat_04):
    context.app_internship.shop_func.verify_categories_blick(cat_01, cat_02, cat_03, cat_04)


@then('Verify click on Product Category opens Product category page')
def click_open_category_page(context):
    context.app_internship.shop_func.click_open_category_page()


@then('User can open & close Quick View by clicking on closing X')
def open_close_quick_view(context):
    context.app_internship.category_page.open_close_quick_view()


@when('User clicks Quick View & add product to cart')
def open_quick_view_add_cart(context):
    context.app_internship.category_page.open_quick_view_add_cart()


@then('Verify Product quantity in cart')
def verify_correct_items_amount_displayed(context):
    context.app_internship.category_page.verify_correct_items_amount_displayed()


@when('User clicks trough multiple product pages by clicking 1, 2')
def open_next_page_number(context):
    context.app_internship.shop_func.open_next_page_number()


@when('User clicks trough multiple product pages by clicking > and <')
def open_next_page_arrow(context):
    context.app_internship.shop_func.open_next_page_arrow()


@then('Verify correct {page_number} number is shown')
def verify_correct_page_number_shown(context, page_number):
    context.app_internship.shop_func.verify_correct_page_number_shown(page_number)


@then('User click on Home link')
def go_home(context):
    context.app_internship.shop_func.go_home()


@then('Verify Home page is displayed')
def verify_page_displayed(context):
    context.app_internship.top_menu.verify_page_displayed()


@when('User can use price Filter slider')
def use_price_filter(context):
    context.app_internship.shop_func.use_price_filter()


@then('User can click Filter button')
def click_filter_button(context):
    context.app_internship.shop_func.click_filter_button()


@then('Verify filtered by price items are shown')
def filtered_price_items_shown(context):
    context.app_internship.shop_func.filtered_price_items_shown()


@then('User can reset price filter after they were applied')
def price_filter_reset(context):
    context.app_internship.shop_func.price_filter_reset()


@then('Verify {no_math_message} shown if no products match selected filters')
def verify_no_match_message(context, no_math_message):
    context.app_internship.shop_func.verify_no_match_message(no_math_message)
