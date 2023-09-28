
Feature: Amazon Window Handling Case


  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Verify Amazon app page is opened
    And User can close new window and switch back to original
