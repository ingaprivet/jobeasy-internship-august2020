# By IngaB
from behave import given, when, then


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
