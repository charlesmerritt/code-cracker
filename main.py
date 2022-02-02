from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://cryptobin.co/w177y163")

    # Opens and saves the passwords to a list
    with open('list.txt') as f:
        lines = f.readlines()
        # Removes the new line character in every password
        lines = [line.removesuffix('\n') for line in lines]

    with open('main.js') as f:
        script = ''.join(f.readlines())
        # Adds a line to execute the function with a placeholder for the future password
        script += 'return enterpass(arguments[0])'

    count = len(lines)
    for i, line in enumerate(lines):
        print(f"Trying password #{i}: {line}\n"
              f'Progress: {round((i / count) * 100, 2)}%')

        # Checks if the password decrypted the paste
        if driver.execute_script(script, line):
            print(f"The password is {line}")
            break