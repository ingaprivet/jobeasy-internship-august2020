# By IngaB
from behave import given, when, then


@given('Open a Product {product_id} page')
def open_prod_page(context, product_id):
    context.app_internship.prod_page.open_prod_page(product_id)


@when('Click plus button')
def click_plus_button(context):
    context.app_internship.prod_page.click_plus_button()


@when('Click minus button')
def click_plus_button(context):
    context.app_internship.prod_page.click_minus_button()


@then('Verify correct items quantity is shown in the cart')
def verify_correct_items_amount_displayed(context):
    context.app_internship.cart_func.verify_correct_items_amount_displayed()


@when('Hoover over magni icon')
def hover_magni_icon(context):
    context.app_internship.prod_page.hover_magni_icon()


@when('Verify search tooltip is displayed')
def verify_search_tooltip(context):
    context.app_internship.prod_page.verify_search_tooltip()


@then('Search for {search_word}')
def search_word_func(context, search_word):
    context.app_internship.prod_page.search_word_func(search_word)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app_internship.search_return_page.verify_found_results_text(search_word)


@then('Display {empty_result} message')
def verify_no_results_text(context, empty_result):
    context.app_internship.search_return_page.verify_no_results_text(empty_result)


@when('Type in {quantity_items} quantity of items to be added to cart')
def verify_intered_quantity_of_items(context, quantity_items):
    context.app_internship.cart_func.input_quantity(quantity_items)


@then('Verify {item_added_message} confirmation message is shown')
def verify_item_added_message_shown(context, item_added_message):
    context.app_internship.prod_page.verify_item_added_message_shown(item_added_message)


@when('Product is {out_of_stock_message} user sees message')
def verify_outofstock_message_shown(context, out_of_stock_message):
    context.app_internship.prod_page.verify_outofstock_message_shown(out_of_stock_message)


@then('Add to Cart button is not shown')
def verify_add_button_available(context):
    context.app_internship.prod_page.verify_add_button_available()


@then('Checkout button is not shown')
def verify_checkout_button_available(context):
    context.app_internship.prod_page.verify_checkout_button_available()


@when('Block text {umaylike_widget_text} is shown')
def verify_umaylike_widget_text(context, umaylike_widget_text):
    context.app_internship.prod_page.verify_umaylike_widget_text(umaylike_widget_text)


@then('Suggested products are shown and clickable')
def verify_suggested_products_shown(context):
    context.app_internship.prod_page.verify_suggested_products_shown()


@then('User is taken to correct pages upon click on Suggested products')
def verify_correct_page_shown(context):
    context.app_internship.prod_page.verify_correct_page_shown()


@when('Verify {product_page_block} for a Product is shown')
def verify_product_page_section(context, product_page_block):
    context.app_internship.page_section.verify_product_page_section(product_page_block)


@then('Verify {product_page_block} for a Product is shown')
def verify_product_page_section(context, product_page_block):
    context.app_internship.page_section.verify_product_page_section(product_page_block)


@then('Verify {product_review_text} can be submitted')
def verify_product_review_submission(context, product_review_text):
    context.app_internship.prod_page.verify_product_review_submission(product_review_text)


@then('Verify {product_image}, {product_name}, {product_price}, {product_description} are shown for a Product')
def verify_product_attributes_shown(context, product_image, product_name, product_price, product_description):
    context.app_internship.prod_page.verify_product_attributes_shown(product_image, product_name, product_price,
                                                                     product_description)
