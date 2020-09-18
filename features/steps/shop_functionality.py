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
