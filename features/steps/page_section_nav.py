from behave import given, when, then


@when('Browse Our Categories text is shown')
def verify_current_section(context):
    context.app_internship.page_section.verify_current_section()


@when('{cat_quantity} Product Categories are shown')
def category_shown_quantity(context, cat_quantity):
    context.app_internship.page_section.category_shown_quantity(cat_quantity)


@then('User can Click on Product Category and Product category page is displayed')
def hover_and_show(context):
    context.app_internship.page_section.hover_and_show()


@when('Latest Products on Sale text is shown')
def verify_current_section(context):
    context.app_internship.page_section.verify_current_section()
