Feature: Login and Navigate to Pages

  Scenario: Login validation using CSV data
    Given I open the browser
    When I enter login credentials from "test_data.csv"
    Then I should see the correct success message
