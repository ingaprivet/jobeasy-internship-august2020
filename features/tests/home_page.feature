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


#"Browse Our Categories" text is shown
#4 correct categories are shown
#Upon clicking on each category, correct page opens

