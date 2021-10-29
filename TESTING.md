# Urban Attiva eCommerce Website Testing

---

## Contents 

1.  [Code Validation](#code-validation)
2.  [Browser Compatibility](#browser-compatibility)
3.  [Responsiveness](#responsiveness)
4.  [Lighthouse Reports](#lighthouse-reports)
5.  [User Story Testing](#user-story-testing)
6.  [Defensive Design Testing](#defensive-design-testing)
7.  [Defects and Issues](#defects-and-issues)

---

### CSS Code Validation

The HTML code was validated using the [W3C CSS validation service](https://jigsaw.w3.org/css-validator/).

![CSS Validator](testing-files/velo-route-css-validation.png)

### HTML Code Validation

The HTML code was validated using the [W3C Markup validation service](https://validator.w3.org/).

No significant errors and all resolved.

This was a manual process to copy and paste the code from each page and review to highlight any errors that were not syntax errors as a result of using Flask and Jinja templates. The only errors found related to a few stray tags and some very minor duplication of attributes and an error stating that validation is not allowed on text area field inputs so this was removed.

### jQuery Code Validation

The jQuery code was validated using the [JSHint validation service](https://jshint.com/).

![JSHint Validator](testing-files/urban-attiva-jshint-validation.png)

### Python Code Validation

The Python code was validated using the [PEP 8 Online Validation Service](http://pep8online.com/).

![PEP 8 Validator](testing-files/urban-attiva-pep8-validation.png)

---

## Browser Compatibility

Browser compatibility was good across Safari, Opera, Edge, Firefox and Chrome browsers.

![Browser compatibility](testing-files/urban-attiva-browser-compatibility-testing.png)

---

## Responsiveness

Resonsiveness was good across all device sizes. Responsiveness of the site has been tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

The site has been tested on the following devices:

-   Desktop: 1024px, > 1200px. 
-   Mobile and Tablet: Galaxy S5/S6/S7, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone x, iPad, iPad Pro, Kindle Fire and Nexus 9

![Responsiveness testing](testing-files/urban-attiva-responsiveness-testing.png)

--- 

## Lighthouse Reports

Lighthouse reports were run for all pages of the website. A significant improvement was seen following code validation and user story testing that resulted in issues being addressed such as a lack of a meta tag and missing alt attributes. The second run was not as high as the 95% mark that I initially set for all performance measures. In some cases 95% was exceeded and in others the performance was not optimal but there were no alarmingly low scores. This is something i would address at a future stage. As a result I have marked these as failed in the user story testing summary.

--- 

## User Story Testing

The user stories below have all been tested through two test cycles. The full test results for all user stories are detailed in the attached [testing report](testing-files/urban-attiva-user-story-testing-final.pdf).

### Website Owner

-   As the website owner, I want branding to be clear and consistent across the website so that the user has a consistent experience.
-   As the website owner, I want the website to be search engine optimised so that users can easily find our website.
-   As the website owner, I want the website to be accessible to all users so that all users can use our website.
-   As the website owner, I want the website to be conformant to web development best practices so that I know the development quality meets required standards.
-   As the website owner, I want the  website to be compatible with different browsers so that users have a consistent experience no matter which browser they use.
-   As the website owner, I want the website to be secure so that only authorised users can access store management functionality.

### Shoppers

-   As a shopper, I want to understand what the store sells and to be able to navigate the website easily so that I can so that I can decide if I want to purchase any products.
-   As a shopper, I want to be able to access the website on all types of device so that I can use the device that is most convenient to me at the time.
-   As a shopper, I want to search products by name or description so that I can find specific products that I'd like to purchase.
-   As a shopper, I want to see products matching that I have searched for and the number of results returned so that I can see whether the product I searched for is available.
-   As a shopper, I want to view and sort multiple categories of products simultaneously so that I can find the products by price, name, rating or category across parent categories e.g. 'nutrition' or 'cycling'.
-   As a shopper, I want to view and sort specific categories of product so that I can find products by specific category e.g. 'running shoes' and sort by price, name or rating.
-   As a shopper, I want to view and sort the full list of available products so that I can find products by price, name, rating or category from the full list of products.
-   As a shopper, I want to view individual product details so that I can see the price, description, product rating, product image and available sizes of products.
-   As a shopper, I want to be able to select the quantity and size of product so that I can purchase the product quantity I want and in the correct size.
-   As a shopper, I want to view products that have been added to my shopping bag so that I can see the items I have selected and the total cost of the items in my shopping cart.
-   As a shopper, I want to adjust the quantity of items in my shopping bag so that I can make changes to the contents of my shopping cart before checkout.
-   As a shopper, I want to purchase an item without registering so that I can quickly purchase items without the need to register.
-   As a shopper, I want to enter my payment information so that I can quickly check out and pay for my items.
-   As a shopper, I want to view an order confirmation after checkout so that I can verify that I haven't made any mistakes when entering my information.
-   As a shopper, I want to receive an order confirmation after checkout so that I can keep a proof of purchase.
-   As a shopper, I want to read item reviews from verified shoppers so that I can see how other shoppers rate the products.
-   As a shopper, I want to see updates in relation to the company or interesting material so that I can find out more about the company, related topics or events.
-   As a shopper, I want to search blog posts so that I can find blog posts of interest to me.
-   As a shopper, I want to register for an account so that I can have a personal account and be able to view my profile.

### Registered Users

-   As a registered user, I want to receive a confirmation email after registering so that I can verify that my account was successfully registered.
-   As a registered user, I want to have a personal user profile so that I can view my account information, order history and order confirmations.
-   As a registered user, I want to log in and log out once I have registered so that I can access my personal account information.
-   As a registered user, I want to add a product review so that I can provide a review of the product that I have purchased.
-   As a registered user, I want to recover my password if I have forgotten it so that I can reaccess my account.
-   As a registered user, I want to leave comments on blog posts so that I can express my views on the blog content.

### Administrator

-   As an administrator, I want to add a blog post so that I can publish blog posts for users to read.
-   As an administrator, I want to add a product so that I can add new items to the store.
-   As an administrator, I want to delete a product so that I can remove items that are no longer sold.
-   As an administrator, I want to delete reviews so that I can remove inappropriate reviews.
-   As an administrator, I want to edit / update a blog post so that I can amend the content of blog posts.
-   As an administrator, I want to edit / update a product so that I can change product prices, descriptions, images and other product attributes.

---

## Defensive Design Testing

1. Tested in user story testing - When deleting routes, cycling tips or categories on the site a modal will appear where the user has to confirm that they want to delete the item. Once they have confirmed then the item will be deleted.
2. Validation has been included on all form fields as listed below:

Product form:

-   Username validated to ensure that it is of length 5 - 15 characters and consists only of numbers and letters. The username is also checked to ensure it does not already exist in the database and a user is notified via a flash message if this is the case.
-   First name and last name fields cannot begin with a space, with a required length between 2 - 20 and letters.
-   Email address field is validated to ensure a valid email address in the correct format is entered.
-   Password is validated to ensure it is between 8 - 15 characters and contains at least one number and one capital and one lowercase letter.

Product review form:

-   Category, difficulty and country are dropdown fields with data populated from the database.
-   Route name is validated to ensure it cannot start with a blank space and must consist only of letters with no special characters.
-   The route image is validated to ensure it is a valid URL and has a recognised jpg, jpeg, gif or png extension.
-   The route description is validated to ensure that it is of length between 10 - 300 characters consisting of letters, numbers and standard punctuation.
-   The route distance is validated to ensure it is a number between 1 and 6 numbers in length, so a maximum of 99999.
-   The route link is validated to ensure it is a valid URL.
-   The same validation is in place when a user comes to edit a route.

Blog form:

-   The category is populated form the database.
-   The cycling tip name is validated for a maximum of 30 characters which must be letters and spaces.
-   The cycling tip image is validated to ensure it is a valid URL and has a recognised jpg, jpeg, gif or png extension.
-   The cycling tip description is validated to ensure that it is of length between 10 - 300 characters consisting of letters, numbers and standard punctuation.
-   The cycling tip link is validated to ensure it is a valid URL.

Blog comment form:

-   The category input is validated to ensure the user only inputs letter, spaces and no special characters.

---

## Defects and Issues

### Resolved

1.  Defect Ref DEF001: It was discovered during testing that users could delete the quantity of a product form the quantity field prior to adding to the cart which resulted in a 500 error. Solved by adding 'or' 1 in the add to cart view quantity variable. This is not an ideal solution but the user can then adjust the quantity in their cart prior to submitting the order. Would need a more satisfactory solution if developed further.
2.  Defect Ref DEF002: It was noticed during testing that the validation was not working on the cart quantity field allowing the user to type negative, decimals or delete the quantity value resulting in a 500 error. Implemented a HTML5 constraint and added (Max 50) to the Quantity label <a href="https://stackoverflow.com/questions/30948387/number-only-input-box-with-range-restriction/30948674"></a> as with Defect Ref XXX, this is not the most elegant solution but avoids 500 errors for the user.
3.  

### Unresolved

- No specific bugs as such but would like to improve on the lighthouse reports performance metrics. After the first round of testing and fixing the performance was good but not above the 95% across the board I was hoping for. IMprovements to be made in this area.

---

[Link to README.md file](README.md).