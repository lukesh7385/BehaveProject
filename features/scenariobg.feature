Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser
    When I open Application
    And Enter valid username and password
    And Click on  login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced search user
    When navigate to advanced search page
    Then advanced search page should display

