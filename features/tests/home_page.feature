Feature: Test Scenarios for Home Page functionality


@smoke
Scenario: User can click right and left arrows to see top banners
  Given Open Home page
  When Click on right and left arrows
  Then Top banners are shown

@smoke
Scenario:User can click bottom dots to see top banners
  Given Open Home page
  When Click bottom dots
  Then Top banners are shown

@smoke
Scenario: User can click on product banner and is taken to correct category page
  Given Open Home page
  When Click on Product01 banner
  Then Product01 category page is displayed
  Given Open Home page
  When Click on Product02 banner
  Then Product02 category page is displayed

@smoke
Scenario: User can browse Product Categories
  Given Open Home page
  When Browse Our Categories text is shown
  And  4 Product Categories are shown
  Then User can Click on Product Category and Product category page is displayed

@smoke
Scenario: Footer functionality
  Given Open Home page
  When Footer shows Best Selling, Latest, Top Rated categories
  Then All products in the footer have price, name, star-rating
  Then Copyright 2020 shown in footer
  And Footer has working links to all product categories
  When Click on Footer top link
  Then Verify Top of Home Page shown

