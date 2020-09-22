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


@when('Footer shows {footer_cat01}, {footer_cat02}, {footer_cat03} categories')
def verify_footer_section(context, footer_cat01, footer_cat02, footer_cat03):
    context.app_internship.page_section.verify_footer_section(footer_cat01, footer_cat02, footer_cat03)


@then('{footer_copy} shown in footer')
def verify_copy(context, footer_copy):
    context.app_internship.page_section.verify_copy(footer_copy)


@when('Click on Footer top link')
def hover_click_top_link(context):
    context.app_internship.page_section.hover_click_top_link()


@then('Verify Top of Home Page shown')
# use GetTop logo to identify Top of Home Page
def logo_present(context):
    context.app_internship.top_menu.logo_present()


@then('Footer has working links to all product categories')
def hover_click_top_links(context):
    context.app_internship.page_section.hover_click_top_links()

@then ('All products in the footer have price, name, star-rating')
def product_attributes_shown(context):
    context.app_internship.page_section.product_attributes_shown()
