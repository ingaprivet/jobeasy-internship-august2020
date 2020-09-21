# By IngaB
from behave import given, when, then


@when('Hover over Wishlist icon and click')
def hover_click_wishlist_icon(context):
    context.app_internship.wishlist_page.hover_click_wishlist_icon()


@when('Open Wishlist page')
def open_wishlist_page(context):
    context.app_internship.wishlist_page.open_wishlist_page()


@then('Open Wishlist page')
def open_wishlist_page(context):
    context.app_internship.wishlist_page.open_wishlist_page()


@then('Verify Wishlist page opened')
def verify_wishlist_page_opened(context):
    context.app_internship.wishlist_page.verify_wishlist_page_opened()


@then('Verify {empty_message} message shown when empty Wishlist')
def veify_wishlist_empty_message(context, empty_message):
    context.app_internship.wishlist_page.veify_wishlist_empty_message(empty_message)


@then('Verify {product_added} added to Wishlist')
def verify_product_added_wishlist(context, product_added):
    context.app_internship.wishlist_page.verify_product_added_wishlist(product_added)


@then('Verify {product_removed_message} is shown upon removal of Product from Wishlist')
def verify_product_removed_wishlist(context, product_removed_message):
    context.app_internship.wishlist_page.verify_product_removed_wishlist(product_removed_message)


@then('Click on x to remove Product from Wishlist')
def click_remove_wishlist(context):
    context.app_internship.wishlist_page.click_remove_wishlist()


@when('Click on Wishlist item')
def click_wishlist_item(context):
    context.app_internship.wishlist_page.click_wishlist_item()


@then('Verify {wishlist_item} Product page is shown')
def open_product_page(context, wishlist_item):
    context.app_internship.wishlist_page.open_product_page(wishlist_item)


@then('Verify User can see social logos to share wishlist items')
def social_network_logos_shown(context):
    context.app_internship.prod_page.social_network_logos_shown()
