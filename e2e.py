from selenium import webdriver
from selenium.webdriver.common.by import By
# import os



def test_scores_service():
        my_driver = webdriver.Chrome(executable_path='F:/devops\chromedriver.exe')
        my_driver.get("http://127.0.0.1:5000")
        input()
        result_element = my_driver.find_element(By.ID, "Score")
        score = int(result_element.text)
        if 1 <= score <= 1000:
            print(True)
            return True
        else:
            print(False)
            return False


# test_scores_service()

def main_function():
    test_scores_service()
    if False:
        return -1
        exit()
    else:
        return 0
        pass
main_function()

