
Feature: Amazon BestSellers Test

  Scenario: Verify Amazon BestSellers has 5 links
    Given Open amazon bestsellers page
    Then verify 5 links are displayed
