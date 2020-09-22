Feature: Test Scenarios for Category functionality

@smoke
Scenario: TMTN-19 / TMTN-20
  Given Open a Category Iphone page
  When Showing all 3 results message is present
  Then Verify 3 items are shown on the page
  And Verify all items have category, name and price
  And Only items of correct category iPhone are shown

@smoke
Scenario: TMTN-19 / TMTN-20
  Given Open a Category Iphone page
  Then User can open and close Quick View by clicking on closing X

@smoke
Scenario: TMTN-19 / TMTN-20
  Given Open a Category Iphone page
  Then User can click Quick View and add product to cart
  And Verify Product quantity in cart




