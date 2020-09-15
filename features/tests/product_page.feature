Feature: Test Scenarios for Product Page functionality

@smoke
Scenario: User can see product description block TMTN - 13 / TMTN - 17

  Given Open a Product airpods-pro page
  Then Verify Description block for a Product is shown


@smoke
Scenario: User can submit a review and see correct  amount of product reviews displayed TMTN - 13 / TMTN - 18

  Given Open a Product airpods-pro page
  Then Verify Review block for a Product is shown
  #Then User can submit a review'
  #Then Verify correct quantity of product reviews are shown

#li#tab-title-reviews.reviews_tab]