from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://chess.wintrcat.uk/")

dropdown_btn = driver.find_element(By.ID, 'load-type-dropdown')
dropdown_btn.click()

# Use arrow keys to select chesscom to trigger verify/arrow button
dropdown_btn.send_keys(Keys.ARROW_DOWN)
dropdown_btn.send_keys(Keys.RETURN)

# Input username into textarea
textarea = driver.find_element(By.ID, 'chess-site-username')
textarea.clear()
textarea.send_keys('daolqp')

# Click the arrow button that appears
username_verify_btn = driver.find_element(By.CLASS_NAME, 'usernameVerifyBtnIcon')
username_verify_btn.click()

# Click latest game
games_listings = WebDriverWait(driver, 2).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'game-listing'))
)
if games_listings:
    games_listings[0].click()

analyze_btn = driver.find_element(By.ID, 'review-button')
analyze_btn.click()

time.sleep(30)

# Click reCAPTCHA
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

time.sleep(10)

driver.quit()
