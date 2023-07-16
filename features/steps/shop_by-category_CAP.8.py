from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open cure skin main page')
def open_main_page(context):
    context.app.main_page_cure.open_main_page_cure()


@when('Click to "Shop by category" - select Face')
def shop_category(context):
    context.app.header_cure.click_shop_category()
    context.app.shop_category_page.click_face()


@then('Verify {expected_text} header is shown')
def verify_face(context, expected_text):
    context.app.shopping_face_category.verify_title(expected_text)


@then('Verify first product name has the word {expected_result} in it')
def verify_product_name(context, expected_result):
    context.app.shopping_face_category.verify_product_name(expected_result)
