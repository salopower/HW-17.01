import pytest
from selenium import webdriver
from tests.site_fields_XPATH import *
from selenium.webdriver.common.by import By

driver = webdriver.Edge()


@pytest.fixture()
def oped_edge_link():
    driver.get('https://demoqa.com/text-box')
    yield driver
    driver.quit()


def test_text_boxes_xpath(oped_edge_link):
    full_name_field = (By.XPATH, FULL_NAME_FIELD)
    email_field = (By.XPATH, EMAIL_FIELD)
    current_address_field = (By.XPATH, CURRENT_ADDRESS_FIELD)
    permanent_address_field = (By.XPATH, PERMANENT_ADDRESS_FIELD)
    submit_button = (By.XPATH, SUBMIT_BUTTON_FIELD)

    driver.find_element(*full_name_field).send_keys("John Doe")
    driver.find_element(*email_field).send_keys("johndoe@example.com")
    driver.find_element(*current_address_field).send_keys("123 Main St")
    driver.find_element(*permanent_address_field).send_keys("456 Park Ave")
    driver.find_element(*submit_button).click()

    name_value = driver.find_element(*full_name_field).get_attribute("value")
    email_value = driver.find_element(*email_field).get_attribute("value")
    curr_addr_value = driver.find_element(*current_address_field).get_attribute('value')
    perm_addr_value = driver.find_element(*permanent_address_field).get_attribute('value')

    result_name = driver.find_element(By.XPATH, NAME_RESULT_FIELD).text.split(':')[1]
    result_email = driver.find_element(By.XPATH, EMAIL_RESULT_FIELD).text.split(':')[1]
    result_curr_addr = driver.find_element(By.XPATH, CURRENT_ADDRESS_RESULT_FIELD).text.split(':')[1]
    result_perm_addr = driver.find_element(By.XPATH, PERMANENT_ADDRESS_RESULT_FIELD).text.split(':')[1]

    assert name_value == result_name
    assert email_value == result_email
    assert curr_addr_value == result_curr_addr
    assert perm_addr_value == result_perm_addr


def test_invalid_email_xpath(oped_edge_link):
    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON_FIELD)
    email.send_keys('john.smith')
    submit.click()

    email_error = driver.find_element(By.XPATH, ERROR_EMAIL_FIELD)
    assert email_error.is_displayed()


def test_invalid_email_css(oped_edge_link):
    email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    submit = driver.find_element(By.CSS_SELECTOR, 'button[id="submit"]')
    email.send_keys('john.smith')
    submit.click()

    email_error = driver.find_element(By.CSS_SELECTOR, 'input[class="mr-sm-2 field-error form-control"]')
    assert email_error.is_displayed()
