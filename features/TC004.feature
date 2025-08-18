Feature: Google Search

  Scenario: Search for OpenAI on Google
    Given I open the Google home page
    When I search for "OpenAI"
    Then I should see results related to "OpenAI"
