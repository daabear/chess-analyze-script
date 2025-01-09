from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://chess.wintrcat.uk/")

dropdown = Select(driver.find_element(By.ID, 'load-type-dropdown'))
dropdown.select_by_value('chesscom')

textarea = driver.find_element(By.ID, 'chess-site-username')
textarea .send_keys('daolqp')

time.sleep(5)

driver.quit()
