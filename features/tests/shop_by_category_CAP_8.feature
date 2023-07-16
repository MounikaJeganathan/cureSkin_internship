# Created by venka at 7/13/2023
Feature: User can shop by category Face

  Scenario: User is shopping from shop by category
    Given Open cure skin main page
    When Click to "Shop by category" - select Face
    Then Verify face header is shown
    Then Verify first product name has the word Face in it