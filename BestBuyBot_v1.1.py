import time
from selenium import webdriver  # importing selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client


driver = webdriver.Chrome()

################################ SIGN IN ##################################
# driver.get(
#     'https://www.bestbuy.com/identity/signin?token=tid%3Ad1f04895-5a33-11ec-bb2b-06572c31469d')

# email = driver.find_element(By.ID, 'fld-e')
# email.send_keys("EMAIL")
# password = driver.find_element(By.ID, 'fld-p1')
# password.send_keys('PASSWORD')
# driver.find_element(By.ID, 'cia-remember-me').click()
# driver.find_element(By.CLASS_NAME, 'c-button').click()

################################ TEST ##################################
# # uncomment next line and insert a new link to test a product with a good yellow "add to cart" button
# driver.get(
#     'https://www.bestbuy.com/site/l-o-l-surprise-l-o-l-surprise-movie-magic-doll-asst-in-pdq/6462708.p?skuId=6462708')

################################ SCALP ##################################
# # website to scalp from (12/07/2021 PS5 link)
driver.get(
    'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')


foundButton = False  # saying "if the button I am looking for is false"

while not foundButton:  # if the button is not found

    addToCartButton = addButton = driver.find_element(
        By.CLASS_NAME, 'add-to-cart-button')

    # if the button has btn-disabled in its class name
    if('c-button-disabled' in addToCartButton.get_attribute('class')):

        time.sleep(2)  # wait some time for the button to appear (3 seconds)
        driver.refresh()  # refresh the page
    else:
        foundButton = True

addToCartButton.click()

################################ CHECK OUT PAGE ##################################

driver.get('https://www.bestbuy.com/cart')

time.sleep(3)
driver.find_element(
    By.XPATH, "//input[contains(@id,'fulfillment-shipping')]").click()

time.sleep(3)
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'btn-primary'))
    )
    element.click()

except:
    print('couldnt find "continue" button')

# ################################ LOG IN as guest ##################################

try:

    continueAsGuest = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'guest'))
    )
    continueAsGuest.click()

except:
    print('couldnt find "check out as guest" button')

try:
    fName = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@id,'.firstName')]")))
 # please input your first name where it says "FIRST_NAME"
    fName.send_keys('FIRST_NAME')

    lName = driver.find_element(
        By.XPATH, "//input[contains(@id,'.lastName')]")
 # please input your last name where it says "LAST_NAME"
    lName.send_keys('LAST_NAME')

    street = driver.find_element(
        By.XPATH, "//input[contains(@id,'.street')]")
# please input your street adress where it says "STREET_ADDRESS"
    street.send_keys('STREET_ADDRESS')

    city = driver.find_element(
        By.XPATH, "//input[contains(@id,'.city')]")
# please input your city where it says "CITY"
    city.send_keys('CITY')

    zipcode = driver.find_element(
        By.XPATH, "//input[contains(@id,'.zipcode')]")
# please input your zipcode where it says "ZIPCODE"
    zipcode.send_keys('ZIPCODE')

# please input your state TWO LETTER ABBREVIATION where it says "STATE"
    driver.find_element(
        By.XPATH, "//select[contains(@id,'.state')]/option[text()='STATE']").click()

    email = driver.find_element(
        By.XPATH, "//input[contains(@id,'emailAddress')]")
# please input your email address where it says "EMAIL"
    email.send_keys('EMAIL')

    phone = driver.find_element(
        By.XPATH, "//input[contains(@id,'phone')]")
# please input your phone number where it says "PHONE_NUMBER" no spaces EX:(5555555555)
    phone.send_keys('PHONE_NUMBER')

    time.sleep(5)
    driver.find_element(
        By.CLASS_NAME, 'btn-secondary').click()

    time.sleep(5)
    driver.find_element(
        By.CLASS_NAME, 'btn-block').click()
except:
    print('error filling out information')

#############################  TEXT MESSAGE ALERT OPTION ###################################

    time.sleep(5)
try:
    # Copy and paste your TWILIO Account SID where it says "ACCOUNT_SID" and Auth token where it says "AUTH_TOKEN"
    client = Client("ACCOUNT_SID", "AUTH_TOKEN")

    # enter number to text where it says "+NUMBER_TO_TEXT" in following format +15556667777 do not forget to include country code
    # enter YOUR twilio number where it says "+TWILIO_NUMBER" in following format +15556667777 do not forget to include country code

    client.messages.create(to=["+NUMBER_TO_TEXT"],
                           from_="+TWILIO_NUMBER",
                           body="The item was added to your cart, please go input CC info")
except:
    print('error sending text message on payment page')
