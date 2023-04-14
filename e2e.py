from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_scores_service():
    service = Service('C:/Users\snirm\Desktop\DevOps\chromedriver.exe')
    service.start()
    my_driver = webdriver.Chrome(service=service)
    my_driver.get("http://127.0.0.1:5000")
    result_element = my_driver.find_element(By.ID, "Score")
    score = int(result_element.text)
    if 1 <= score <= 1000:
        print(True)
        return True
    else:
        print(False)
        return False


def main_function():
    test_scores_service()
    if False:
        return -1
        exit()
    else:
        return 0
        pass


main_function()
