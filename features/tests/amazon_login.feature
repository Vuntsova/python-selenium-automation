# Created by emiliya at 11/13/20
Feature: Test Scenario for Amazon Login

  Scenario: Find Product on Amazon
    Given Open the Amazon Page
    When Input Dress
    And Click on Amazon search button
    Then Search result Dress


  Scenario: User Can Login if already not
    Given Open the Amazon Page
    When Check If Logged In
    And Hover over Account & List
    And Click the Sign In button
    And Enter Email Address in the input field
    And Click Continue Button
    And Enter Password in the input field
    And Click Sign In button
    Then Verification Code Is Required
