
Feature: Verify that logged out user sees Sign In when clicking on Returns and Orders

  Scenario: User who is looged out can see sign in page
  Given Open https://www.amazon.com
    When Click Orders
    Then Verify Sign in page opened: Sign In header is visible, email input field is present


