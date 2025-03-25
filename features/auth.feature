Feature: User Authentication on Magento Software Testing Board

  Scenario: Successful Account Creation
    Given I am on the Magento homepage
    When I navigate to the sign-up page
    And I fill in the sign-up form with valid details
    And I submit the sign-up form
    Then I should be redirected to the My Account page

  Scenario: Successful Sign-In
    Given I am logged out and on the Magento homepage
    When I navigate to the sign-in page
    And I enter my credentials
    And I submit the sign-in form
    Then I should be logged in successfully