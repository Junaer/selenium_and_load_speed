import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path
import time
import urllib.request

Base_url = "https://www.facebook.com/"
driver = webdriver.Firefox(executable_path=r'/home/evgen/cod/dj/selenium_and_load_speed/geckodriver')
driver.get(Base_url)

class selenium_download():
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def selenium_run_for_git(self):
        driver.get(url='https://git-scm.com/')
        download_page = driver.find_element(by=By.XPATH, value='//*[@id="nav-downloads"]/a/h3')
        download_page.click()
        win_page = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/a')
        win_page.click()
        download_git = driver.find_element(by=By.XPATH, value='//*[@id="main"]/p[3]/strong/a')
        start = time.perf_counter()
        download_git.click()
        while True:
            download_folder = os.path.expanduser(self.path)
            filenames = glob.glob(download_folder + self.name)
            if len(filenames) > 0 and not any('.crdownload' in self.name for self.name in filenames):
                break
            for self.name in filenames:
                if self.name.endswith('.crdownload'):
                    continue
                if self.name.endswith('.xls'):
                    print('')
                    print('Download complete.')
                    print('')
                    break
                else:
                    break
        run_time = time.perf_counter() - start
        print(run_time)
        return round(run_time, 2)

    def selenium_run_for_7zip(self):
        driver.get(url='https://www.7-zip.org')
        download_7zip = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td[1]/a')
        start = time.perf_counter()
        download_7zip.click()
        while True:
            download_folder = os.path.expanduser(self.path)
            filenames = glob.glob(download_folder + self.name)
            if len(filenames) > 0 and not any('.crdownload' in self.name for self.name in filenames):
                break
            for self.name in filenames:
                if self.name.endswith('.crdownload'):
                    continue
                if self.name.endswith('.xls'):
                    print('')
                    print('Download complete.')
                    print('')
                    break
                else:
                    break
        run_time = time.perf_counter() - start
        print(run_time)
        return round(run_time, 2)
        # download_7zip = driver.find_element(by=By.XPATH, value='//*[@id="sidebar"]/nav/ul/li[1]/a')
        # start = time.perf_counter()
        # download_7zip.click()
        # run_time = time.perf_counter() - start
        # driver.switch_to.window(driver.window_handles[0])
        # driver.close()
        # return round(run_time, 2)

    def get_avg_speed(self, func):
        time_download = func
        full_path = f'{self.path}{self.name}'
        size = os.path.getsize(self.name)
        avg_speed = size / time_download
        round_avg_speed = round(avg_speed)
        return print(f"Вес файла {size} байт'а. Cредняя скорость скачивания {round_avg_speed} байт'а в секунду или {round_avg_speed/1000000} мегабайт'а в секунду")




# if __name__ == '__main__':
#     # download_git = selenium_download('/home/gogelgans/Загрузки/', 'Git-2.36.1-64-bit.exe')
#     # download_git.get_avg_speed(download_git.selenium_run_for_git())
#     download_7zip = selenium_download('/home/gogelgans/Загрузки/', '')
#     download_7zip.selenium_run_for_7zip()


