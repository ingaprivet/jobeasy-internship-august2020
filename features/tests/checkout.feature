Feature: Test Scenarios for Checkout functionality

@smoke
Scenario: User sees correct error message if clicking 'Pace Order' when a required field not populated  TMTN - 28 / TMTN - 29
    Given Open a Product airpods-pro page
    When Click on Add to Cart button
    Then Verify correct items quantity is shown in the cart
    And Click on Checkout button
    And Verify correct page is displayed
    When Click Place Order when required field not populated
    Then Verify Billing First name is a required field. message is on page
    Then User can fill out Checkout form
    #User can select any country from country drop down


@smoke
Scenario:   User can go back to Cart by clicking 'Shopping Cart' TMTN - 28 / TMTN - 29
    Given Open a Product airpods-pro page
    When Click on Add to Cart button
    Then Verify correct items quantity is shown in the cart
    And Click on Checkout button
    And Verify correct page is displayed
    And User can go back to Cart by clicking Shopping Cart
    And Verify correct page is displayed


