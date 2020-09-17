# By IngaB
from behave import given, when, then


@given('Open a Category {category_name} page')
def open_category_page(context, category_name):
    context.app_internship.category_page.open_category_page(category_name)


@when('Showing all 3 results message is present')
def results_message_present(context):
    context.app_internship.category_page.results_message_present()


@then('Verify {items_result} items are shown on the page')
def verify_items_presented(context, items_result):
    context.app_internship.category_page.verify_items_presented(items_result)


@then('Verify all items have category, name and price')
def verify_item_attributes_shown(context):
    context.app_internship.category_page.verify_item_attributes_shown()


@then('User can open and close Quick View by clicking on closing X')
def open_close_quick_view(context):
    context.app_internship.category_page.open_close_quick_view()


@then('User can click Quick View and add product to cart')
def open_quick_view_add_cart(context):
    context.app_internship.category_page.open_quick_view_add_cart()


@then('Verify Product quantity in cart')
def verify_correct_items_amount_displayed(context):
    context.app_internship.category_page.verify_correct_items_amount_displayed()
