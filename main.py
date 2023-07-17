import os
from selenium import webdriver
from time import sleep
from dotenv import load_dotenv
# ------- 追加部分 -------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------- 追加部分 -------

load_dotenv()


def main():
    driver = webdriver.Chrome('C:\\Users\\bunta\\chromedriver_win32\\chromedriver')
    login_url = os.getenv('LOGIN_URL')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    teacher_url = os.getenv('TEACHER_URL')

    driver.get(login_url)
    driver.save_screenshot('test.png')

    # 入力
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)

    # ログイン
    driver.find_element_by_id('login_submit').click()
    driver.get(teacher_url)
    driver.save_screenshot('test3_teacher.png')

    trainer_details = driver.find_elements_by_css_selector('a.trainer_detail')

    trainer_details[6].click()

    # 最大の読み込み時間を設定 今回は最大30秒待機できるようにする
    wait = WebDriverWait(driver=driver, timeout=30)
    # トレーナー詳細の上のタブが出るまで待機
    wait.until(EC.visibility_of_element_located((By.ID, 'tabs')))
    driver.save_screenshot('trainer_details.png')
    # 「レッスン予約」をクリック
    driver.find_element_by_css_selector("#tabs > ul > li:nth-child(2)").click()
    # スケジュール表が表示されるまで待機
    wait.until(EC.visibility_of_element_located((By.ID, 'trainerScheduleSearchResult')))
    driver.save_screenshot('trainer_details2.png')

    # 朝の時間帯ボタンをクリック
    time_zones = driver.find_elements_by_css_selector('#trainer_time_period_list td')
    number_of_available = []

    for time_zone in time_zones:
        time_zone.click()
        # スケジュール表が表示されるまで待機
        sleep(0.5)
        wait.until(EC.presence_of_element_located((By.ID, 'trainerScheduleSearchResult')))
        # id=trainerScheduleSearchResultの中の〇（i要素）の要素をすべて取得し配列に入れる
        a = driver.find_elements_by_css_selector('#trainerScheduleSearchResult i')

        number_of_available.append(len(a))
        print(len(a))

    print(number_of_available)
    driver.quit()


if __name__ == '__main__':
    main()
