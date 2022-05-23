from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path
import time
import urllib.request
from progress.bar import IncrementalBar

driver = webdriver.Chrome()

def selenium_run_for_git():
    driver.get(url='https://git-scm.com/')
    time.sleep(1)
    download_page = driver.find_element(by=By.XPATH, value='//*[@id="nav-downloads"]/a/h3')
    download_page.click()
    time.sleep(2)
    win_page = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/a')
    win_page.click()
    time.sleep(2)

def selenium_run_for_7zip():
    driver.get(url='https://www.google.ru/')
    time.sleep(1)
    search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys('скачать zip 7', Keys.ENTER)
    time.sleep(2)
    link_7zip = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div[1]/div/a/div')
    link_7zip.click()
    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()


def download_file_and_check_time(name, url):
    name = name
    url = url
    start = time.perf_counter()
    urllib.request.urlretrieve(url, filename=name)
    run_time = time.perf_counter() - start
    return round(run_time, 2)

def get_avg_speed(name, path, url):
    time_download = download_file_and_check_time(name=name, url=url)
    size = os.path.getsize(path)
    avg_speed = size / time_download
    round_avg_speed = round(avg_speed)
    return print(f"Вес файла {size} байт'а. Cредняя скорость скачивания {round_avg_speed} байт'а в секунду")


if __name__ == '__main__':
    func_list = [selenium_run_for_git(), get_avg_speed('Git-2.36.1-64-bit.exe', 'C:\\git\\Git-2.36.1-64-bit.exe','https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe'),
                 selenium_run_for_7zip(),get_avg_speed('7z2107-x64.exe', 'C:\\git\\7z2107-x64.exe', 'https://www.7-zip.org/a/7z2107-x64.exe')]
    count = 0
    bar = IncrementalBar('Осталось: ', max=len(func_list))
    for func in func_list:
        func
        bar.next()
        count += 1
    bar.finish()

