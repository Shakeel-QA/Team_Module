import time, csv
from selenium.webdriver.common.keys import Keys
from uuid import uuid1
from typing import List
import pyautogui
import random
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from lib.Resources import LoginModuleResources, TeamModuleResources
from lib.Pag import LoginPage, Click, SendKeys, get_selection_list
import datetime

def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="") as f:
        f.writelines(data)

USER_NAME = "Shakeel_QA_Admin"
PASS_WORD = "AA@@1122"

THREE_CHARACTERS = "ABC"
SPECIAL_CHARACTERS = "#$@$@#$#$$"
TEAM_NAME = "Shakeel_J_P"
DESCRIPTION = "Shakeel is testing from selenium"
# SEARCH_TEAM = TEAM_NAME
EDIT_NAME = "QA_PTA"


def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    login = LoginPage(driver)
    login.enter_username(LoginModuleResources.username, USER_NAME)
    login.enter_password(LoginModuleResources.password, PASS_WORD)
    login.submit_btn(LoginModuleResources.submit_button)
    url = (driver.current_url)
    time.sleep(0.5)
    today = date.today()

    make_csv("team Report.csv",f"Test Case,Scenario, Result{today}, URL\n", new=True)
    make_csv('team Report.csv',f'Login Credential,Username:{USER_NAME},Password:{PASS_WORD}\n', new=False)
    make_csv('team Report.csv',f'Login Module,Login With Correct Username and Password,Login Successfully,{url}\n', new=False)
    time.sleep(1)

    Team_Module = Click(driver)
    Team_Module.Click_button(TeamModuleResources.Team_Module)
    time.sleep(0.5)

    Creat_New_Team = Click(driver)
    Creat_New_Team.Click_button(TeamModuleResources.Create_New_Team)
    time.sleep(0.5)

    Teamname = SendKeys(driver)
    Teamname.send_keys(TeamModuleResources.Team_Name, THREE_CHARACTERS)
    url_s = (driver.current_url)
    time.sleep(1)

    pop_nam = driver.find_element(By.XPATH, "//*[@id='usernameteam']").text
    make_csv(
        "team Report.csv",
        f"Team Module,Check Team Name Less then 5 Characters,{pop_nam},{url_s}\n",
        new=False,
    )
    time.sleep(0.5)

    Clear_name = driver.find_element(By.XPATH, "//*[@id='team_username']").clear()

    Team_name1 = SendKeys(driver)
    Team_name1.send_keys(TeamModuleResources.Team_Name, SPECIAL_CHARACTERS)
    time.sleep(1)

    pop_nam2 = driver.find_element(By.XPATH, "//*[@id='usernameteam']").text
    make_csv(
        "team Report.csv",
        f"Team Module,Check Team Name With Special Characters,{pop_nam2},{url_s}\n",
        new=False,
    )
    time.sleep(0.5)

    Clear_name1 = driver.find_element(By.XPATH, "//*[@id='team_username']").clear()

    Team_name1 = SendKeys(driver)
    Team_name1.send_keys(TeamModuleResources.Team_Name, TEAM_NAME)
    time.sleep(1)

    pop_nam2 = driver.find_element(By.XPATH, "//*[@id='usernameteam']").text
    make_csv(
        "team Report.csv",
        f"Team Module,Check Team Name Above 5 Characters,Username Accpeted,{url_s}\n",
        new=False,
    )
    time.sleep(3)

    # Find all of the options in the dropdown menu
    options = driver.find_elements('xpath',"//select[@name='primary_manager']")
    random_option = random.choice(options)
    random_option.click()


    options_lists_Primary = get_selection_list(driver, TeamModuleResources.Primary_Manager)
    time.sleep(1)

    Primary_Manager = driver.find_element(
        By.XPATH, f"//option[@value='{options_lists_Primary}']"
    ).text
    make_csv(
        "team Report.csv",
        f"Team Module,Select Primary Manager(User Selected ),{Primary_Manager},{url_s}\n",
        new=False,
    )
    time.sleep(2)

    options_lists_Secondary = get_selection_list(driver, TeamModuleResources.Secondary_Manager)
    time.sleep(2)

    Secondary_Manager = driver.find_element(
        By.XPATH, f"//option[@value='{options_lists_Secondary}']"
    ).text
    make_csv(
        "team Report.csv",
        f"Team Module,Select Secondary Manager(User Selected ),{Secondary_Manager},{url_s}\n",
        new=False,
    )
    time.sleep(1)

    Description = SendKeys(driver)
    Description.send_keys(TeamModuleResources.Description , DESCRIPTION)
    time.sleep(1)
    make_csv(
        "team Report.csv",
        f"Team Module,Add Description,Description Added,{url_s}\n",
        new=False,
    )
    time.sleep(1)

    Create_Buttonn = Click(driver)
    Team_Module.Click_button(TeamModuleResources.Create_Team_Btn)
    time.sleep(0.5)
    pop_Team_Creates = driver.find_element(By.ID,"popUpMessage").text  
    make_csv('team Report.csv',f'Team Module,Click on Create Button,{pop_Team_Creates},{url_s}\n', new=False)
    make_csv('team Report.csv',f'Team Module,Created Team Name,{TEAM_NAME},{url_s}\n', new=False)
    time.sleep(1)
    
    Search_Team = SendKeys(driver)
    Search_Team.send_keys(TeamModuleResources.Search_Team , TEAM_NAME)
    time.sleep(1)

    Three_Dots = Click(driver)
    Three_Dots.Click_button(TeamModuleResources.Three_Dots)
    time.sleep(1)

    Edit_Button = Click(driver)
    Edit_Button.Click_button(TeamModuleResources.Edit_Team)
    url_t = (driver.current_url)
    time.sleep(1)

    Clear_Team_Name = driver.find_element(By.XPATH, "//*[@id='campaign']").clear()

    Search_Team_Name = SendKeys(driver)
    Search_Team_Name.send_keys(TeamModuleResources.Edit_Name, EDIT_NAME)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)

    Save_Button = Click(driver)
    Save_Button.Click_button(TeamModuleResources.Save_Button)
    time.sleep(1)
    
    pop_Team_Edit = driver.find_element(By.ID,"popUpMessage").text 
    make_csv('team Report.csv',f'Team Module,Edit Team and Change Name,{pop_Team_Edit},{url_t}\n', new=False)
    make_csv('team Report.csv',f'Team Module,Edited Team Name,{EDIT_NAME},{url_s}\n', new=False)
    time.sleep(1)

    Search_Teams = SendKeys(driver)
    Search_Teams.send_keys(TeamModuleResources.Search_Team , EDIT_NAME)
    time.sleep(1)

    Three_Dots1 = Click(driver)
    Three_Dots1.Click_button(TeamModuleResources.Three_Dots)
    time.sleep(1)

    Assign_User = Click(driver)
    Assign_User.Click_button(TeamModuleResources.Assign_User_Btn)
    url_f = (driver.current_url)
    time.sleep(1)

    options_lists2 = get_selection_list(driver, TeamModuleResources.Select_User)
    time.sleep(1)

    User_Assign = driver.find_element(
        By.XPATH, f"//option[@value='{options_lists2}']"
    ).text
    make_csv(
        "team Report.csv",
        f"Team Module,Select User (User Selected ),{User_Assign},{url_t}\n",
        new=False,
    )
    time.sleep(1)

    Asign_Btn = Click(driver)
    Asign_Btn.Click_button(TeamModuleResources.Assign_Button)
    time.sleep(0.5)

    pop_Team_Assign = driver.find_element(By.ID,"popUpMessage").text 
    make_csv('team Report.csv',f'Team Module,Assign User to Team,{pop_Team_Assign},{url_f}\n', new=False)
    time.sleep(1)

    Search_Team_Details = SendKeys(driver)
    Search_Team_Details.send_keys(TeamModuleResources.Search_Team , EDIT_NAME)
    time.sleep(1)

    Three_Dots2 = Click(driver)
    Three_Dots2.Click_button(TeamModuleResources.Three_Dots)
    time.sleep(1)

    Team_Details = Click(driver)
    Team_Details.Click_button(TeamModuleResources.View_Team)
    url_d = (driver.current_url)
    time.sleep(2)

    scroll_down = driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)
    make_csv('team Report.csv',f'Team Module,Click View Team Button,View Team Button is Working,{url_d} \n', new=False)
    time.sleep(2)

    # scroll_up = driver.execute_script("window.scrollTo(3000, 0);")

    Assign_User_Second = Click(driver)
    Assign_User_Second.Click_button(TeamModuleResources.Assign_From_Details)
    url_f = (driver.current_url)
    time.sleep(1)

    options_lists_Assign = get_selection_list(driver, TeamModuleResources.Select_User2)
    time.sleep(1)

    User_Assigning = driver.find_element(
        By.XPATH, f"//option[@value='{options_lists_Assign}']"
    ).text
    make_csv(
        "team Report.csv",
        f"Team Module,Select User (User Selected ),{User_Assigning},{url_d}\n",
        new=False,
    )
    time.sleep(1)

    Asign_Btn_Second = Click(driver)
    Asign_Btn_Second.Click_button(TeamModuleResources.Assign_Button_D)
    time.sleep(0.5)

    pop_Team_Assigning = driver.find_element(By.ID,"popUpMessage").text 
    make_csv('team Report.csv',f'Team Module,Assign User to Team,{pop_Team_Assigning},{url_f}\n', new=False)
    time.sleep(5)

    


if __name__ == "__main__":
    main()
