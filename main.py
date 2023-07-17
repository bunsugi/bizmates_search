import os
from selenium import webdriver
from time import sleep
from dotenv import load_dotenv

load_dotenv()


def main():
    driver = webdriver.Chrome('C:\\Users\\bunta\\chromedriver_win32\\chromedriver')
    login_url = os.getenv('LOGIN_URL')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    print(os.getenv('LOGIN_URL'))
    print(os.getenv('EMAIL'))
    print(os.getenv('PASSWORD'))

    driver.get(login_url)
    driver.save_screenshot('test.png')

    # 入力
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)

    # ログイン
    driver.find_element_by_id('login_submit').click()

    driver.save_screenshot('test2_after_submit.png')

    teacher_url = 'https://www.bizmates.jp/MyBizmates/student/schedule'
    driver.get(teacher_url)
    driver.save_screenshot('test3.png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
