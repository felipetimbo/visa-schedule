import time
import utils
import numpy as np
# import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

class VisaSchedule():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = ''
        self.password = ''   
        self.start = '2023-02-23'    
        self.end = '2023-06-01'    

    def run(self):
        driver = self.driver
        driver.get('https://ais.usvisa-info.com/pt-br/niv/users/sign_in')
        userneme_elem = driver.find_element(By.XPATH, '//*[@id="user_email"]')
        userneme_elem.send_keys(self.username)
        password_elem = driver.find_element(By.XPATH, '//*[@id="user_password"]')
        password_elem.send_keys(self.password)
        checkbox_elem = driver.find_element(By.XPATH, '//*[@id="policy_confirmed"]')
        driver.execute_script("arguments[0].click();", checkbox_elem)

        # login
        driver.find_element(By.XPATH, '//*[@id="sign_in_form"]/p[1]/input').click()
        time.sleep(5)

        # reschedule
        driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a').click()
        time.sleep(5)

        # driver.find_element(By.XPATH, '//*[@id="b6xsbj-accordion-label"]/h5/span').click()
        # driver.find_element(By.XPATH, '//*[@id="b6xsbj-accordion"]/div/div[2]/p[2]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/a').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/div/div/div[2]/p[2]/a').click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/input').click()
        time.sleep(5)

        

        # calendar_elem.send_keys('2023-03-03')
        # calendar_elem.clear()

        # value = ele.get_attribute('id')

        # start = datetime.datetime.strptime(self.start, "%Y-%m-%d")
        # end = datetime.datetime.strptime(self.end, "%Y-%m-%d")
        # dates = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

        dates = [ 
                    # "2023-03-01", "2023-04-01", "2023-05-01"
                    # "2023-06-01", "2023-07-01", "2023-08-01"
                    # "2023-09-01", "2023-10-01", "2023-11-01"
                    "2023-12-01", "2024-01-01", "2024-02-01" 
                ]

        date_not_found = True

        while date_not_found:

            calendar_elem = driver.find_element(By.XPATH, '//*[@id="appointments_consulate_appointment_date"]')
            driver.execute_script("arguments[0].removeAttribute('readonly')", calendar_elem)

            for date in dates:
                utils.log_msg('trying month %s/%s ' % (date[5:6], date[0:4] ))

                calendar_elem.send_keys(date)

                for i in range(1, 7):
                    for j in range(1, 7):
                        try:
                            date_available = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[%s]/td[%s]/a' % (str(i), str(j)))
                            date_available.click()

                            hour_elem = driver.find_element(By.XPATH, '//*[@id="appointments_consulate_appointment_time"]')

                            selection = Select(hour_elem)
                            selection.select_by_index(1)   
                            date_not_found = False
                            utils.log_msg('date found: %s' % str(hour_elem.text[:5]))
                            break
                        except NoSuchElementException:
                            mini_seconds_to_sleep = np.random.randint(10)
                            time.sleep(mini_seconds_to_sleep * 0.1)
                        
                    if not date_not_found:
                        break

                if not date_not_found:
                    break  

                calendar_elem.clear()   

            if not date_not_found:
                break 

            seconds_to_sleep = np.random.randint(30)
            utils.log_msg('sleeping for %s seconds...' % str(seconds_to_sleep))
            time.sleep(seconds_to_sleep)
            driver.refresh()

        driver.find_element(By.XPATH, '//*[@id="appointments_submit"]').click()
        time.sleep(2)

        # driver.find_element(By.XPATH, '/html/body/div[6]/div/div/a[2]').click()
        utils.log_msg('FINISHED!')

if __name__ == "__main__":
    visa = VisaSchedule()
    visa.run()
