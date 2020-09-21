# By IngaB
from behave import given, when, then


@then('User can select {country} from country drop down')
def click_country_dropdown(context, country):
    context.app_internship.checkout_page.click_country_dropdown(country)


@then('User can go back to Cart by clicking Shopping Cart icon')
def go_back(context):
    context.app_internship.checkout_page.go_back()


@then('Click Place Order when First name field not populated')
def place_order(context):
    context.app_internship.checkout_page.place_order()


@then('Verify {info_missing} message is on page')
def verify_info_missing_message(context, info_missing):
    context.app_internship.checkout_page.verify_info_missing_message(info_missing)


@then('User can fill out Checkout form')
def fill_out_form(context):
    context.app_internship.checkout_page.fill_out_form()

