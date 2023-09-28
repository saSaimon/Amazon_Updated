
Feature: Amazon Best Sellers Links Test

  Scenario: User sees Amazon Best Sellers Links icon

    Given Open amazon main page
    When Change the location
    And Click Amazon Best Sellers
    Then Verify Best Sellers 5 links are visible
