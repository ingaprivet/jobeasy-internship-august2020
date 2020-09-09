from behave import given, when, then


@when('Browse Our Categories text is shown')
def verify_current_section(context):
    context.app_internship.page_section.verify_current_section()


@when('Latest Products on Sale text is shown')
def verify_current_section(context):
    context.app_internship.page_section.verify_current_section()
