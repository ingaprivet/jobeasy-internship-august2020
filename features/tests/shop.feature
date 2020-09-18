Feature: Test Scenarios for Shop functionality

@smoke
Scenario: User can zoom in product image TMTN - 21 / TMTN - 27
  Given Open a Product airpods-pro page
  And Open a Product iphone-11 page
  And Open Shop page
  Then User can see recently viewed items and open them
  And Verify User is taken to correct page