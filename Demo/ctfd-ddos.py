import random
import string
import sys
import time

from selenium import webdriver

sleep_time = 1


def create_account(name, email_id, team_password):
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('http://127.0.0.1:8000/register')
    time.sleep(sleep_time)

    team_name = browser.find_element_by_name('name')
    email = browser.find_element_by_name('email')
    password = browser.find_element_by_name('password')

    team_name.send_keys(name)
    email.send_keys(email_id)
    password.send_keys(team_password)

    submit_button = browser.find_element_by_id('submit')
    submit_button.click()

    time.sleep(sleep_time)

    browser.close()


def random_string(length=10):
    return ''.join([random.choice(
        string.ascii_letters + string.digits) for n in range(length)])


def random_line(file):
    line = next(file)
    for num, aline in enumerate(file):
        if random.randrange(num + 2):
            continue
        line = aline
    return line


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            names_file = open("first-names.txt")
            name = random_line(names_file).strip()
            email_id = name + '@' + 'gmail.com'
            random_password = random_string(14)

            create_account(name, email_id, random_password)
