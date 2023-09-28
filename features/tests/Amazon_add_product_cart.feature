
Feature: Amazon Add Product to cart test

  Scenario: User can add product to cart

    Given Open amazon page
    When Input Key chain into Amazon search field
    And click on Amazon search icon
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 Item
