

  Feature: Login functionality

  Scenario Outline: Login with different credentials
    Given I open the application
    When I enter username "<username>"
    And I enter password "<password>"
    And I click on login button
    Then I should see the message "<message>"

    Examples:
      | username   | password   | message                |
      | Ali        | 12345      | Login successful       |
      | Ahmet      | 123        | Invalid credentials    |
      | Haci       | admin123   | Login successful       |
