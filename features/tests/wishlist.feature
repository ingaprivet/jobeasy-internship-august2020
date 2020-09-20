Feature: Test Scenarios for Wishlist functionality

@smoke
Scenario:   "No products added to the wishlist" shown if no product were added to the list TMTN - 30 / TMTN - 31
  When Open Wishlist page
  Then  Verify No products added to the wishlist message shown when empty Wishlist

@smoke
Scenario:   Add and remove products to/from Wishlist, verify user sees correct products and messages TMTN - 30 / TMTN - 32
  Given Open a Product airpods-pro page
  When Hover over Wishlist icon and click
  Then Open Wishlist page
  And Verify Wishlist page opened
  And Verify AirPods Pro added to Wishlist
  Then Click on x to remove Product from Wishlist
  Then Verify Product successfully removed. is shown upon removal of Product from Wishlist
  #User can see social logos to share wishlist items

@smoke
Scenario:   Add product to Wishlist, verify user can click on Wishlist item and is taken to correct product page TMTN - 30 / TMTN - 32
  Given Open a Product airpods-pro page
  When Hover over Wishlist icon and click
  Then Open Wishlist page
  And Verify Wishlist page opened
  And Verify AirPods Pro added to Wishlist
  When Click on Wishlist item
  Then Verify AirPods Pro Product page is shown







