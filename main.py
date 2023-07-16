from selenium import webdriver
from time import sleep


def print_hi(name):
    driver = webdriver.Chrome('C:\\Users\\bunta\\chromedriver_win32\\chromedriver')
    login_url = 'https://www.bizmates.jp/MyBizmates/'
    driver.get(login_url)
    driver.save_screenshot('test.png')

    # email入力
    input_email = driver.find_element_by_id('email')
    input_email.send_keys('xxxx')
    input_pass = driver.find_element_by_id('password')
    input_pass.send_keys('xxxx')

    driver.find_element_by_id('login_submit').click()

    driver.save_screenshot('test2.png')

    teacher_url = 'https://www.bizmates.jp/MyBizmates/student/schedule'
    driver.get(teacher_url)
    driver.save_screenshot('test3.png')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
