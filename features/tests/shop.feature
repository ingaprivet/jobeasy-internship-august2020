Feature: Test Scenarios for Shop functionality

@smoke
Scenario:   TMTN - 21 / TMTN - 27
  Given Open a Product airpods-pro page
  And Open a Product iphone-11 page
  And Open Shop page
  Then User can see recently viewed items and open them
  And Verify User is taken to correct page


@smoke
Scenario:   TMTN - 21 / TMTN - 26
  Given Open Shop page
  #Then User sees Accessories, IPad, IPhone, MacBook under Browse
  Then Verify click on Product Category opens Product category page


@smoke
Scenario:   TMTN - 21 / TMTN - 25
  Given Open Shop page
  Then User can open & close Quick View by clicking on closing X

@smoke
Scenario:   TMTN - 21 / TMTN - 25
    Given Open Shop page
    When User clicks Quick View & add product to cart
    Then Verify correct Product quantity in cart


@smoke
Scenario:   TMTN - 21 / TMTN - 25
    Given Open Shop page
    When User clicks trough multiple product pages by clicking 1, 2
    #fix next step to check for any page number / pass from prev step
    Then Verify correct Page 2 number is shown


@smoke
Scenario:   TMTN - 21 / TMTN - 25
    Given Open Shop page
    When User clicks trough multiple product pages by clicking > and <
    #fix next step to check for any page number / pass from prev step
    Then Verify correct Page 2 number is shown

@smoke
Scenario:   TMTN - 21 / TMTN - 24
  Given Open Shop page
   Then User can sort products by price high to low
   And  User can sort products by price low to high
   And  User can sort products by popularity
   And  User can sort products by rating

@smoke
Scenario:   TMTN - 21 / TMTN - 23
  Given Open Shop page
    When User can use price Filter slider
    Then User can click Filter button
    Then Verify filtered by price items are shown
    Then User can reset price filter after they were applied
    Then Verify no price filter shown on page

@smoke
Scenario:   TMTN - 21 / TMTN - 23
  Given Open Shop page
    Then Verify No products were found matching your selection shown if no products match selected filters

@smoke
Scenario:   TMTN - 21 / TMTN - 22
    Given Open Shop page
    Then User click on Home link
    And Verify Home page is displayed







