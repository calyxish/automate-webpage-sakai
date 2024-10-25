import time
import getpass 
from selenium import webdriver
from selenium.webdriver.common.by import By


# Function to login into sakai
def login_into_sakai(preferred_browser, student_id, password):
    """
    info need preferred_browser, student_id, and password to log into sakai.
    """
    # url
    preferred_browser.get("https://sakai.ug.edu.gh/portal/xlogin")

    # Enter student_id
    student_id_element = preferred_browser.find_element(By.ID, 'eid')
    student_id_element.send_keys(student_id)

    # Enter password
    student_id_password = preferred_browser.find_element(By.ID, 'pw')
    student_id_password.send_keys(password)

    # Submit the form
    submit_button = preferred_browser.find_element(By.ID, 'submit')
    submit_button.click()


while True:
    """
    Prompt the user to enter their credentials
    make it more interactive
    """
    # student_id = input("Enter your ID:\n") enter my ug student id
    # password = getpass.getpass("Enter your password (hidden):\n") enter my ug student password

    # If you prefer to open sakai without entering your 
    # credentials over and over again. 
    student_id = "22032451"
    password = "48318"


    preferred_browser = webdriver.Chrome()

    # Perform login
    login_into_sakai(preferred_browser, student_id, password)

    # Keep the browser open the time i prefer to stay on Sakai
    time.sleep(10)  # 5min = 60 x 5 = (300) [time in seconds]
    preferred_browser.quit()

    # Prompt to retry login or end the loop
    retry_again = input("Do you want to log in again? (yes/no): ").strip().lower()
    if retry_again != 'yes':
        print("Thank for trying my App.")
        break




