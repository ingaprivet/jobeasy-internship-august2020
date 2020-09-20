Feature: Test Scenarios for Product Page functionality

@smoke
Scenario: User can zoom in product image TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  When Verify User can zoom in Product image
  Then Verify User can scroll thru Product images
  And Verify User can close Product images by clicking x


@smoke
Scenario: User can see product description block TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  Then Verify image, name, price, description are shown for a Product

@smoke
Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  When Hover over heart icon and click
  Then Verify Product is added to wishlist

@smoke
Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  When Click on HOME link
  Then User is taken to Home page

@smoke
Scenario: Category link takes user to correct category page TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  When Click on Accesories Product category link
  Then Accesories Product category page is shown

@smoke
Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn  TMTN - 13 / TMTN - 14
  Given Open a Product airpods-pro page
  When Social network logos are present
  Then Each click on a social network link opens a new login window


@smoke
Scenario: User can add product to cart /  TMTN - 13 / TMTN - 15

  Given Open a Product airpods-pro page
  When Click on Add to Cart button
  Then Verify correct items quantity is shown in the cart

@smoke
Scenario: User can add product to cart click + button to modify amount of cart item and verify correct amount of items shown / TMTN - 13 / TMTN - 15

  Given Open a Product airpods-pro page
  When Click plus button
  And Click on Add to Cart button
  Then Verify correct items quantity is shown in the cart

@smoke
Scenario: User can add product to cart click + button to modify amount of cart item and verify correct amount of items shown / TMTN - 13 / TMTN - 15

  Given Open a Product airpods-pro page
  When Click plus button
  And Click minus button
  And Click on Add to Cart button
  Then Verify correct items quantity is shown in the cart

@smoke
Scenario: User can add product to cart click + button to modify amount of cart item and verify correct amount of items shown / TMTN - 13 / TMTN - 15

  Given Open a Product airpods-pro page
  When Type in 5 quantity of items to be added to cart
  And Click on Add to Cart button
  Then Verify correct items quantity is shown in the cart

@smoke
Scenario: User sees " ... have been added to your cart" confirmation upon adding items to cart  / TMTN - 13 / TMTN - 15

  Given Open a Product airpods-pro page
  When Click on Add to Cart button
  Then Verify been added to your cart confirmation message is shown


@smoke
Scenario: If product is out of stock, Add to Cart is not shown / TMTN - 13 / TMTN - 15
  Given Open a Product land-tee page
  When  Product is Out of stock user sees message
  Then Add to Cart button is not shown


@smoke
Scenario: If product is out of stock, Checkout is not shown / TMTN - 13 / TMTN - 15
  Given Open a Product land-tee page
  When  Product is Out of stock user sees message
  Then Checkout button is not shown


@smoke
Scenario: User can see "You may also like." block on product page / TMTN - 13 / TMTN - 16
  Given Open a Product land-tee page
  When Block text You may also like is shown
  Then Suggested products are shown and clickable
  And  User is taken to correct pages upon click on Suggested products


@smoke
Scenario: User can see product description block TMTN - 13 / TMTN - 17
  Given Open a Product airpods-pro page
  Then Verify Description block for a Product is shown

@smoke
Scenario: User can submit a review and see correct  amount of product reviews displayed TMTN - 13 / TMTN - 18
  Given Open a Product airpods-pro page
  When Verify Review block for a Product is shown
  #Then Verify Product review text can be submitted
  #And Verify correct quantity of product reviews is shown











