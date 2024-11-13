*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle
    Set Password  kalleville
    Set Password Confirmation  kalleville
    Submit Credentials
    Registration Should Fail With Message  Password must contain at least one character that is not a letter

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  ville123
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Main Page
    Submit Logout
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  jarkko
    Set Password  jarkko123
    Set Password Confirmation  jarkko123
    Submit Credentials
    Go To Main Page
    Submit Logout
    Set Username  jarkko
    Set Password  jarkko123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  ja
    Set Password  jarkko123
    Set Password Confirmation  jarkko123
    Submit Credentials
    Go To Login Page
    Set Username  ja
    Set Password  jarkko123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Submit Logout
    Click Button  Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page