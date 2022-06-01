import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path
import time
import urllib.request

driver = webdriver.Chrome('/home/gogelgans/Документы/work/homework/selenium_and_load_speed/chromedriver')

def selenium_run_for_git(path, name):
    driver.get(url='https://git-scm.com/')
    download_page = driver.find_element(by=By.XPATH, value='//*[@id="nav-downloads"]/a/h3')
    download_page.click()
    win_page = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/a')
    win_page.click()
    download_git = driver.find_element(by=By.XPATH, value='//*[@id="main"]/p[3]/strong/a')
    start = time.perf_counter()
    download_git.click()
    while True:
        download_folder = os.path.expanduser(path)
        filenames = glob.glob(download_folder + name)
        if len(filenames) > 0 and not any('.crdownload' in name for name in filenames):
            break
        for name in filenames:
            if name.endswith('.crdownload'):
                continue
            if name.endswith('.xls'):
                print('')
                print('Download complete.')
                print('')
                break
            else:
                break
    run_time = time.perf_counter() - start
    print(run_time)
    return round(run_time, 2), path, name

def selenium_run_for_7zip():
    driver.get(url='https://www.google.ru/')
    search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys('скачать zip 7', Keys.ENTER)
    link_7zip = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div[1]/div/a/div')
    link_7zip.click()
    # download_7zip = driver.find_element(by=By.XPATH, value='//*[@id="sidebar"]/nav/ul/li[1]/a')
    # start = time.perf_counter()
    # download_7zip.click()
    # run_time = time.perf_counter() - start
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    # return round(run_time, 2)


# def download_file_and_check_time(name, url):
#     name = name
#     url = url
#     start = time.perf_counter()
#     urllib.request.urlretrieve(url, filename=name)
#     run_time = time.perf_counter() - start
#     return round(run_time, 2)

def get_avg_speed(name, path, url):
    time_download = download_file_and_check_time(name=name, url=url)
    size = os.path.getsize(path)
    avg_speed = size / time_download
    round_avg_speed = round(avg_speed)
    return print(f"Вес файла {size} байт'а. Cредняя скорость скачивания {round_avg_speed} байт'а в секунду")


if __name__ == '__main__':
    selenium_run_for_git('/home/gogelgans/Загрузки/', 'Git-2.36.1-64-bit.exe')


