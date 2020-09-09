from behave import given, when, then


@when('Click on right and left arrows')
def click_arrows(context):
    context.app_internship.top_banner.click_arrows()


@when('Click bottom dots')
def click_bottom_dots(context):
    context.app_internship.top_banner.click_bottom_dots()


@when('Click on Product01 banner')
def click_banner_product01(context):
    context.app_internship.top_banner.click_banner_product01()


@when('Click on Product02 banner')
def click_banner_product02(context):
    context.app_internship.top_banner.click_banner_product02()


@then('Top banners are shown')
def verify_page(context):
    context.app_internship.top_banner.verify_page()


@then('Product01 category page is displayed')
def verify_page(context):
    context.app_internship.top_banner.verify_page()


@then('Product02 category page is displayed')
def verify_page(context):
    context.app_internship.top_banner.verify_page()
