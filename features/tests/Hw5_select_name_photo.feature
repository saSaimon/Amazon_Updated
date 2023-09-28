
Feature: Amazon Search Result has Product name and product image
  Scenario: User can search any product and verify the product name and image
    Given Open amazon main page
    When Search for shirt
    Then Verify that every product has a name and image
