Feature: Login functionality

  Scenario: Login with valid credentials
    Given I navigated to Login Page
    When I enter valid address and valid password into the fields
    And I click on Login button
    Then I should get logged in