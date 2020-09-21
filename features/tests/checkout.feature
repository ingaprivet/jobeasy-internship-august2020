Feature: Test Scenarios for Checkout functionality

@smoke
Scenario: User sees correct error message if clicking 'Pace Order' when a required field not populated  TMTN - 28 / TMTN - 29
    Given Open a Product airpods-pro page
    When Click on Add to Cart button
    Then Verify correct items quantity is shown in the cart
    And Click on Checkout button
    And Verify correct page is displayed
    And User can select BY from country drop down
    And User can fill out Checkout form
    And Click Place Order when First name field not populated
    And Verify Billing First name is a required field. message is on page
    And User can go back to Cart by clicking Shopping Cart icon
    And Verify correct page is displayed




