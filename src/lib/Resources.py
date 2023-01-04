class LoginModuleResources:
    username = "//input[@id='name']"
    password = "//input[@id='password']"
    submit_button = "//button[@id='submitSigninLogin']"
    popup = "//*[@id='popUpMessage']"


class TeamModuleResources:
    Team_Module = "//*[@id='teamsbuttonfordisablenavbar']"
    Create_New_Team = "//a[normalize-space()='Create Team']"
    Team_Name = "//*[@id='team_username']"
    Team_Name_Popup = "//*[@id='usernameteam']"
    Primary_Manager = "//select[@name='primary_manager']"
    Secondary_Manager = "//select[@name='secondary-manager']"
    Description = "//*[@id='desc']"
    Create_Team_Btn = "//*[@id='create-team-button']"
    Create_Team_Popup = "//*[@id='popUpMessage']"
    Search_Team = "//*[@id='searchText']"
    Three_Dots = "//div[normalize-space()='...']"
    Edit_Team = "(//a[normalize-space()='Edit Team'])[1]"
    Edit_Name = "//*[@id='campaign']"
    Save_Button = "//*[@id='edit-team-save-button']"
    Assign_User_Btn = "//*[@class='icon-box01']"
    Select_User = "//select[@name='assigner-User']"
    Assign_Button = "//*[@id='assign-user-model']"
    View_Team = "//*[@class='icon-box012']"
    Assign_From_Details = "//div[@class='create-new-campaign-btn mobile-hide']//a[@data-bs-target='#AddAgent'][contains(text(),'Assign')]"
    Select_User2 = "//select[@name='assigner_ids_User']"
    Assign_Button_D = "//*[@id='AssignTeam']"


