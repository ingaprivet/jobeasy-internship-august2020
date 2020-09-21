Feature: Test Scenarios for Shop functionality

@smoke
Scenario:   TMTN - 21 / TMTN - 23
  Given Open Shop page
    When User can use price Filter slider
    Then User can click Filter button
    Then Verify filtered by price items are shown
    Then User can reset price filter after they were applied
    Then Verify no price filter shown on page


@smoke
Scenario:   TMTN - 21 / TMTN - 24
  Given Open Shop page
   Then User can sort products by price high to low
   And  User can sort products by price low to high
   And  User can sort products by popularity
   And  User can sort products by rating




