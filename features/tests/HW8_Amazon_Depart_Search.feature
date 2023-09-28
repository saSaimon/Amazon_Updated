
Feature: Amazon Department Search Test

  Scenario: User can select and search in Amazon Department
    Given Open Amazon page
    When Change the location
    When Select department by alias Electronics
    And Search for Speaker
    Then Verify electronics department is selected
#    Then Verify Electronics after Search

  Scenario: User can hover to New Arrivals tab and see details
    Given Open Amazon product B074TBCSC8 page
    When Change the location
    When Hover over New Arrivals tab
    Then Verify verifies that the user sees the details
