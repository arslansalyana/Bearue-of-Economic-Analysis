# bea.py

import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time

# def get_download_folder_path():
#     return input("Enter the download folder path: ")

def get_download_folder_path():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return input("Enter the download folder path: ")


def main():
    # Get the download folder path from the user
    # download_folder_path = get_download_folder_path()
    download_folder_path = get_download_folder_path()

    # Initialize the Chrome driver with the automatically installed ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")

    # Set the download folder
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })

    # Initialize the Chrome driver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Navigate to the desired website
    driver.get(
        "https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey&_gl=1*vnhlse*_ga*NDY1MjM0MzM3LjE3MDE3NjU2NjM.*_ga_J4698JNNFT*MTcwNTMxNzA2My4yNC4xLjE3MDUzMTcwODMuNDAuMC4w")

    # You can add additional waiting or actions as needed
    time.sleep(2)

    # Wait for the content to load before clicking on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME'
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]')))

    # Click on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME' using XPath
    section1_table112_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]"
    section_link_table112 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, section1_table112_xpath)))
    section_link_table112.click()

    # Wait for the content to load after clicking on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME'
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[2]')))

    # Introduce a short delay before clicking on table 1.1.2
    time.sleep(2)

    # Click on the next table 1.1.2 using XPath
    table_112 = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[2]'
    table112_click = driver.find_element(By.XPATH, table_112)
    table112_click.click()

    # Wait for the content to load after clicking on table 1.1.2
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'ModifyTableBtn')))

    # Click on the 'ModifyTableBtn' button using its ID for table 1.1.2
    modify_table112_btn = driver.find_element(By.ID, 'ModifyTableBtn')
    modify_table112_btn.click()

    # Wait for the box to appear after the modify button click for 1.1.3
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    # Introduce a short delay before interacting with the dropdown
    time.sleep(2)

    # Find the dropdown menu and wait for it to be clickable
    dropdown112_xpath = '/html/body/div[5]/div/div/div[2]/div/div[1]/div/select'
    dropdown_112 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, dropdown112_xpath)))

    # Select the option with text content '1947-A & Q'
    select = Select(dropdown_112)
    select.select_by_visible_text('1947-A & Q')

    #   Introduce a short delay before clicking on the 'Refresh Table 1.1.2' button
    time.sleep(2)

    # Click on the 'Refresh Table' button
    refresh_table112_btn_xpath = '/html/body/div[5]/div/div/div[3]/button[1]'
    refresh_table112_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, refresh_table112_btn_xpath)))
    refresh_table112_btn.click()

    # Wait for the toolbox to appear after clicking the 'Refresh Table 1.1.2' button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'toolBox')))

    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.ID, 'pleasewait-modal')))

    # Introduce a short delay before interacting with the toolbox
    time.sleep(2)

    # Find the 'DownloadTableBtn' button in the toolbox and click it
    download_table112_btn_id = 'DownloadTableBtn'
    download_table112_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, download_table112_btn_id)))
    download_table112_btn.click()

    # Wait for the download modal to appear
    download112_modal_xpath = '/html/body/div[7]/div/div/div[2]/div'
    download_modal = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, download112_modal_xpath)))

    # Introduce a short delay before interacting with the list group
    time.sleep(2)

    # Click on the second option in the list group (2nd anchor tag)
    option112_xpath = '/html/body/div[7]/div/div/div[2]/div/a[2]'
    option112 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, option112_xpath)))
    option112.click()

    # ////********..........********/////
    # the above lines of code download the table 1.1.2
    # ////********..........********/////

    # Go back to the previous two pages
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, 'pleasewait-modal')))
    driver.execute_script("window.history.go(-2)")  # Go back two pages

    # ////********..........********/////
    # Now code for table 1.1.3
    # ////********..........********/////

    # Wait for the content to load before clicking on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME'
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]')))

    # Click on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME' using XPath
    section1_table113_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]"
    section_link_table113 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, section1_table113_xpath)))
    section_link_table113.click()

    # Wait for the content to load after the first click
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[3]')))

    # Introduce a short delay before clicking on the next link
    time.sleep(2)

    # Click on the table 1.1.3 using XPath
    table_113 = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[3]'
    table113_click = driver.find_element(By.XPATH, table_113)
    table113_click.click()

    # Wait for the content to load after clicking on table 1.1.3
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'ModifyTableBtn')))

    # Click on the 'ModifyTableBtn' button using its ID for table 1.1.3
    modify_table113_btn = driver.find_element(By.ID, 'ModifyTableBtn')
    modify_table113_btn.click()

    # Wait for the box to appear after the modify button click for 1.1.3
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    # Introduce a short delay before interacting with the dropdown
    time.sleep(2)

    # Find the dropdown menu and wait for it to be clickable
    dropdown113_xpath = '/html/body/div[5]/div/div/div[2]/div/div[1]/div/select'
    dropdown_113 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, dropdown113_xpath)))

    # Select the option with text content '1947-A & Q'
    select = Select(dropdown_113)
    select.select_by_visible_text('1947-A & Q')

    # Introduce a short delay before clicking on the 'Refresh Table 1.1.3' button
    time.sleep(2)

    # Click on the 'Refresh Table' button
    refresh_table113_btn_xpath = '/html/body/div[5]/div/div/div[3]/button[1]'
    refresh_table113_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, refresh_table113_btn_xpath)))
    refresh_table113_btn.click()

    # Wait for the toolbox to appear after clicking the 'Refresh Table 1.1.2' button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'toolBox')))

    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.ID, 'pleasewait-modal')))

    # Introduce a short delay before interacting with the toolbox
    time.sleep(2)

    # Find the 'DownloadTableBtn' button in the toolbox and click it
    download_table113_btn_id = 'DownloadTableBtn'
    download_table113_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, download_table113_btn_id)))
    download_table113_btn.click()

    # Wait for the download modal to appear
    download113_modal_xpath = '/html/body/div[7]/div/div/div[2]/div'
    download113_modal = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, download113_modal_xpath)))

    # Introduce a short delay before interacting with the list group
    time.sleep(2)

    # Click on the second option in the list group (2nd anchor tag)
    option113_xpath = '/html/body/div[7]/div/div/div[2]/div/a[2]'
    option113 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, option113_xpath)))
    option113.click()

    # ////********..........********/////
    # the above lines of code download the table 1.1.3
    # ////********..........********/////

    # Go back to the previous two pages
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, 'pleasewait-modal')))
    driver.execute_script("window.history.go(-2)")  # Go back two pages

    # ////********..........********/////
    # Now code for table 1.1.5
    # ////********..........********/////

    # Wait for the content to load before clicking on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME'
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]')))

    # Click on 'SECTION 1 - DOMESTIC PRODUCT AND INCOME' using XPath
    section1_table115_xpath = "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]"
    section_link_table115 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, section1_table115_xpath)))
    section_link_table115.click()

    # Wait for the content to load after the first click
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[5]')))

    # Introduce a short delay before clicking on the next link
    time.sleep(2)

    # Click on the table 1.1.5 using XPath
    table_115 = '/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span[5]'
    table115_click = driver.find_element(By.XPATH, table_115)
    table115_click.click()

    # Wait for the content to load after clicking on table 1.1.5
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'ModifyTableBtn')))

    # Click on the 'ModifyTableBtn' button using its ID for table 1.1.5
    modify_table115_btn = driver.find_element(By.ID, 'ModifyTableBtn')
    modify_table115_btn.click()

    # Wait for the box to appear after the modify button click for 1.1.5
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    # Introduce a short delay before interacting with the dropdown
    time.sleep(2)

    # Find the dropdown menu and wait for it to be clickable
    dropdown115_xpath = '/html/body/div[5]/div/div/div[2]/div/div[1]/div/select'
    dropdown_115 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, dropdown115_xpath)))

    # Select the option with text content '1947-A & Q'
    select = Select(dropdown_115)
    select.select_by_visible_text('1947-A & Q')

    # Introduce a short delay before clicking on the 'Refresh Table 1.1.5' button
    time.sleep(2)

    # Click on the 'Refresh Table' button
    refresh_table115_btn_xpath = '/html/body/div[5]/div/div/div[3]/button[1]'
    refresh_table115_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, refresh_table115_btn_xpath)))
    refresh_table115_btn.click()

    # Wait for the toolbox to appear after clicking the 'Refresh Table 1.1.5' button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'toolBox')))

    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.ID, 'pleasewait-modal')))

    # Introduce a short delay before interacting with the toolbox
    time.sleep(2)

    # Find the 'DownloadTableBtn' button in the toolbox and click it
    download_table115_btn_id = 'DownloadTableBtn'
    download_table115_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, download_table115_btn_id)))
    download_table115_btn.click()

    # Wait for the download modal to appear
    download115_modal_xpath = '/html/body/div[7]/div/div/div[2]/div'
    download115_modal = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, download115_modal_xpath)))

    # Introduce a short delay before interacting with the list group
    time.sleep(2)

    # Click on the second option in the list group (2nd anchor tag)
    option115_xpath = '/html/body/div[7]/div/div/div[2]/div/a[2]'
    option115 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, option115_xpath)))
    option115.click()

    # ////********..........********/////
    # the above lines of code download the table 1.1.5
    # ////********..........********/////

    # ////********..........********/////
    # Now code for State GDP Summary - Annual
    # ////********..........********/////

    # Navigate to the desired website
    driver.get(
        "https://apps.bea.gov/itable/?ReqID=70&step=1&acrdn=1&_gl=1*1xauxsa*_ga*MTE4MzYyODI0My4xNzAxMTk2MDM5*_ga_J4698JNNFT*MTcwMTk3MjM2Ni41LjEuMTcwMTk3Mzk2MS4wLjAuMA..#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyOSwyNSwzMSwyNiwyNywzMF0sImRhdGEiOltbIlRhYmxlSWQiLCI1MzIiXSxbIk1ham9yX0FyZWEiLCIwIl0sWyJTdGF0ZSIsWyIwIl1dLFsiQXJlYSIsWyJYWCJdXSxbIlN0YXRpc3RpYyIsWyItMSJdXSxbIlVuaXRfb2ZfbWVhc3VyZSIsIkxldmVscyJdLFsiWWVhciIsWyItMSJdXSxbIlllYXJCZWdpbiIsIi0xIl0sWyJZZWFyX0VuZCIsIi0xIl1dfQ==")

    # Introduce a short delay before interacting with the toolbox
    time.sleep(5)

    # Find the 'DownloadTableBtn' button in the toolbox and click it
    gdp_id = 'DownloadTableBtn'
    download_gdp = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, gdp_id)))
    download_gdp.click()

    # Introduce a short delay before interacting with the list group
    time.sleep(5)

    # Click on the second option in the list group (2nd anchor tag)
    csv_xpath = '/html/body/div[7]/div/div/div[2]/div/a[2]'
    try:
        click_on_csv = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, csv_xpath)))
        driver.execute_script("arguments[0].click();", click_on_csv)
        print("Clicked on CSV element successfully.")

    except Exception as e:
        print(f"Error clicking on CSV element: {e}")

    # ////********..........********/////
    # the above lines of code downloads State GDP Summary - Annual
    # ////********..........********/////

    # ////********..........********/////
    # Now code for Value added by industry- Annual
    # ////********..........********/////

    driver.get(
        "https://apps.bea.gov/iTable/?reqid=150&step=2&isuri=1&categories=gdpxind&_gl=1*qmhnu9*_ga*NDY1MjM0MzM3LjE3MDE3NjU2NjM.*_ga_J4698JNNFT*MTcwNTMyMDM3My4yNS4wLjE3MDUzMjAzNzMuNjAuMC4w#eyJhcHBpZCI6MTUwLCJzdGVwcyI6WzEsMiwzXSwiZGF0YSI6W1siY2F0ZWdvcmllcyIsIkdkcHhJbmQiXSxbIlRhYmxlX0xpc3QiLCIxIl1dfQ==")

    # Wait for the content to load after clicking on table value added by industry- Annual
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'ModifyTableBtn')))

    # Click on the 'ModifyTableBtn' button using its ID for value added by industry- Annual
    modify_ValInd = driver.find_element(By.ID, 'ModifyTableBtn')
    modify_ValInd.click()

    # Wait for the box to appear
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    # Introduce a short delay before interacting with the dropdown
    time.sleep(5)  # Adjust the sleep time as needed

    # Find the dropdown menu and wait for it to be clickable
    dropdown_year2017_xpath = '/html/body/div[5]/div/div/div[2]/div/div[2]/div/select'
    year_2017 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_year2017_xpath)))

    # Select the option with text content 2017-A
    select = Select(year_2017)
    select.select_by_visible_text('2017-A')

    # Introduce a short delay before clicking on the 'Refresh' button
    time.sleep(5)

    # Find the div for the Annual option and wait for it to be clickable
    annual_div_xpath = '/html/body/div[5]/div/div/div[2]/div/div[5]/div/div[1]/label'
    annual_div = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, annual_div_xpath)))

    # Click on the div to select the 'Annual' option
    annual_div.click()

    # Introduce a short delay before clicking on the 'Refresh Table value added by industry- Annual' button
    time.sleep(5)

    # Click on the 'Refresh Table' button
    refresh_valIndusAnn_xpath = '/html/body/div[5]/div/div/div[3]/button[1]'
    refresh_valIndusAnn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, refresh_valIndusAnn_xpath)))
    refresh_valIndusAnn.click()

    # Wait for the toolbox to appear after clicking the 'Refresh value added by industry- Annual' button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'toolBox')))

    time.sleep(5)  # Adjust the sleep time as needed

    # Find the 'DownloadTableBtn' button in the toolbox and click it
    download_valIndus_id = 'DownloadTableBtn'
    download_valIndus = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, download_valIndus_id)))
    download_valIndus.click()

    # Wait for the download modal to appear
    csvValIndu_xpath = '/html/body/div[7]/div/div/div[2]/div'
    downCsvVal = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, csvValIndu_xpath)))
    downCsvVal.click()

    # Introduce a short delay before interacting with the list group
    time.sleep(5)

    # Click on the second option in the list group (2nd anchor tag)
    try:
        option2_xpath = '/html/body/div[7]/div/div/div[2]/div/a[2]'
        optionValIndus = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, option2_xpath)))
        optionValIndus.click()
    except:
        pass

# if __name__ == "__main__":
#     main()
if __name__ == "__main__":
    main()
