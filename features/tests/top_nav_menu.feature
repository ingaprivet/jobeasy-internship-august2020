# Created by ingabukhvalova at 9/1/20
Feature: Tests scenarios for Top Nav Menu

@smoke
Scenario: GetTop logo takes to the https://gettop.us/ page
  Given Open Home page
  And GetTop logo is displayed
  When Click on GetTop logo
  Then https://gettop.us/ page is displayed

@smoke
Scenario: User can search for an existing product and sees correct results
  Given Open Home page
  When Hoover over magni icon
  And Verify search tooltip is displayed
  Then Search for Watch Series 5
  And Product results for Watch Series 5 are shown
  When Hoover over magni icon
  And Verify search tooltip is displayed
  Then Search for Rose Wine
  And Display No products were found matching your selection message

@smoke
Scenario:User can hover over header-nav-main icons and see menu options or select one of header-nav-main product and correct page opens
  Given Open Home page
  When Select a Mac product from header-nav-main and open correct product page
  When Hoover over header-nav-main item and display correct menu options

@smoke
Scenario: Test for Account icon functionality
  Given Open Home page
  When Clicking on Account icon
  Then Login form opens

@smoke
Scenario: User verifies that his Shopping Cart is empty
  Given Open Home page
  When Click on Cart icon
  #check next message to be change for No products in the cart.
  Then Verify Your cart is currently empty. text present

@smoke
Scenario: User can add a product to the cart and verify the price in top nav menu is correct
  Given Open a Product page
  When Click on Add to Cart button
  Then Verify top nav menu displays correct Product price
  And Verify top nav menu displays correct amount of items

@smoke
Scenario: User can add products to cart and verify correct products and subtotal shown
  Given Open a Product page
  When Click on Add to Cart button
  And Click on Add to Cart button
  Then Verify correct subtotal shown
  And  Verify correct products shown

@smoke
Scenario: User can add a product to the cart, hover over a cart icon, click "View Cart" and verify a cart page is displayed
  Given Open a Product page
  When Click on Add to Cart button
  And Hover over cart icon
  Then Click View Cart button
  And Verify correct page is displayed

@smoke
Scenario: User can add products to  cart, hover over cart icon, click on "Checkout" and verify checkout page is displayed
  Given Open a Product page
  When Click on Add to Cart button
  And Hover over cart icon
  Then Click on Checkout button
  And Verify correct page is displayed

@smoke
Scenario: User can add a product to the cart, hover over cart icon and verify a product can be removed
  Given Open a Product page
  When Click on Add to Cart button
  And Hover over cart icon
  Then Click on Remove button
  And Verify No products in the cart. message is displayed












