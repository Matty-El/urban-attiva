[<img src="static/images/urban-attiva-logo.png" width="250">](https://velo-route.herokuapp.com/)

# VeloRoute Website

![Urban Attiva](readme-files/urban-attiva-presented.png)

Working with the company director, this website has been developed as the first iteration of an eCommerce store for Urban Attiva. The website provides shoppers with the ability to browse and purchase products, add product reviews and to read the company blog to find out what is new with Urban Attiva and to leave comments on blog articles.

The client requested a simple, attractive and modern website that is responsive and easy to navigate, allows potential customers to sign up for email updates on company news, provides links to the company social media accounts and links to enable the customer to purchase products.

The site was developed using knowledge gained from the Code Institute HTML Essentials, CSS Essentials, User Centric Frontend Development, Interactive Frontend Development, Backend Development and Full STack Frameworks modules.

View the live website [here.](https://urban-attiva.herokuapp.com/)

---

## Contents

1.  [User Experience Design](#user-experience-design)
2.  [Data Model](#data-model)
3.  [Features](#features)
4.  [Technologies Used](#technologies-used)
5.  [Testing](#testing)
6.  [Deployment](#deployment)
7.  [Credits](#credits)

---

## User Experience Design

### Strategy

The key business goals for developing the website are:

-   To sell both own brand and established brand sports products to generate revenue for the company.
-   To promote the Urban Attiva brand through the blog and utilisation of an Urban Attiva style template.

### Scope

#### User Stories

#### Website Owner

-   As the website owner, I want branding to be clear and consistent across the website so that the user has a consistent experience.
-   As the website owner, I want the website to be search engine optimised so that users can easily find our website.
-   As the website owner, I want the website to be accessible to all users so that all users can use our website.
-   As the website owner, I want the website to be conformant to web development best practices so that I know the development quality meets required standards.
-   As the website owner, I want the  website to be compatible with different browsers so that users have a consistent experience no matter which browser they use.
-   As the website owner, I want the website to be secure so that only authorised users can access store management functionality.

#### Users

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

#### Registered Users

-   As a registered user, I want to receive a confirmation email after registering so that I can verify that my account was successfully registered.
-   As a registered user, I want to have a personal user profile so that I can view my account information, order history and order confirmations.
-   As a registered user, I want to log in and log out once I have registered so that I can access my personal account information.
-   As a registered user, I want to add a product review so that I can provide a review of the product that I have purchased.
-   As a registered user, I want to recover my password if I have forgotten it so that I can reaccess my account.
-   As a registered user, I want to leave comments on blog posts so that I can express my views on the blog content.

#### Administrator

-   As an administrator, I want to add a blog post so that I can publish blog posts for users to read.
-   As an administrator, I want to add a product so that I can add new items to the store.
-   As an administrator, I want to delete a product so that I can remove items that are no longer sold.
-   As an administrator, I want to delete reviews so that I can remove inappropriate reviews.
-   As an administrator, I want to edit / update a blog post so that I can amend the content of blog posts.
-   As an administrator, I want to edit / update a product so that I can change product prices, descriptions, images and other product attributes.

### Structure

The Urban Attiva website has been designed to provide an attractive, intuitive and easy to navigate website. The site has been developed to enable visitors to register, log in, search for products to add to their shopping cart, to check out securely and access their account information.

The website has the following key elements:

-   A simple landing page design with a main navigation menu with links for the home page, shop, blog and user account. 
-   The home page has a hero image with header and a prominant shop now button, images with links to the product categories, and a footer with links to further information and social media. A dropdown search field allows users to search for  products by entering their own search criteria.
-   The shop dropdown menu provides access to the main product categories and the product pages enable sorting within categories with a link through to individual product details.
-   Shopping cart and checkout functionality.
-   A blog page listing recent blog posts.
-   An account dropdown menu with links to register and log in. Once logged in a user has access to their profile and administration users can access the product and blog management functionality.

### Skeleton

#### Wireframes

The wireframes were developed using [Balsamiq](https://balsamiq.com/).

-   Small device [wireframes](design/velo-route-small-device.png).
-   Medium device [wireframes](design/velo-route-medium-device.png).
-   Large device [wireframes](design/velo-route-large-device.png).

The following changes were made after the initial design.

-   Functionality to enable users to leave product reviews.
-   User registered discount functionality.


### Surface

The Urban Attiva website features a clean and simple design with #263238 used for dark backgrounds and text and #FAFAFA for light backgrounds and text to provide good contrast. Colour is added to the site through the use of images and buttons as detailed in the colour scheme below.

#### Branding

A simple Urban Attiva logo has been developed aligned to the branding for an existing sister company.

![Urban Attiva Logo](static/images/velo-route-logo-crop.png)

#### Colours

![Colour scheme](design/velo-route-colour-palette.png)

A simple colour palette using #263238 for navigation and footer backgrounds and #FAFAFA for text to provide a good contrast whilst avoiding the potential eyestrain of using pure black and white.

All icons with the exception of the social media icons use colour #607D8B. Social media icons in footer are the same colour as the footer text #FAFAFA.

Colours have been used for flash messages and action buttons. #4DD0E1 has been used for the flash messages background, #EF6C00 for the call to action button on the home page, #0097A7 for action buttons throughout the site and #D50000 for all delete buttons.

Images are used to add some additional colour to the website.

#### Typography

Roboto font has been utilised for all text across the website. This is a simple and modern font available from the Google Fonts library which is unobtrusive and easy to read. Font Awesome icons have been utilised for icons throughout the site.

### Defensive Design

The website has been developed incorporating the following defensive design aspects.

#### Error Handling

-   Error pages for 403, 404 and 500 errors which will be displayed to the user if any of these errors occur.

#### Confirm on Delete

-   All areas of the website where users can delete data incorporate modals to prompt the user if they really want to permanently delete the data.

#### Segregation of Duties**

-   The standard users of the website can only create, update and delete routes and can only update and delete routes they have added to Veloroute.

-   The admin user can view and edit any routes that have been added and have full functionality to create, edit and delete routes and cycling tips.

-   A further role of IT user has been added who can only create, update and delete categories as an understanding of the data model is required prior to any changes to these categories. 

#### Data Input Validation

Django-allauth is utilised for all authentication, registration, account management functionality.

Data validation is on custom forms is incorporated on all data input fields with the following validation applied to:

Product management form:

-   Username validated to ensure that it is of length 5 - 15 characters and consists only of numbers and letters. The username is also checked to ensure it does not already exist in the database and a user is notified via a flash message if this is the case.
-   First name and last name fields cannot begin with a space, with a required length between 2 - 20 and letters.
-   Email address field is validated to ensure a valid email address in the correct format is entered.
-   Password is validated to ensure it is between 8 - 15 characters and contains at least one number and one capital and one lowercase letter.

Blog management form:

-   Category, difficulty and country are dropdown fields with data populated from the database.
-   Route name is validated to ensure it cannot start with a blank space and must consist only of letters with no special characters.
-   The route image is validated to ensure it is a valid URL and has a recognised jpg, jpeg, gif or png extension.
-   The route description is validated to ensure that it is of length between 10 - 300 characters consisting of letters, numbers and standard punctuation.
-   The route distance is validated to ensure it is a number between 1 and 6 numbers in length, so a maximum of 99999.
-   The route link is validated to ensure it is a valid URL.
-   The same validation is in place when a user comes to edit a route.

Product review form:

-   The category is populated form the database.
-   The cycling tip name is validated for a maximum of 30 characters which must be letters and spaces.
-   The cycling tip image is validated to ensure it is a valid URL and has a recognised jpg, jpeg, gif or png extension.
-   The cycling tip description is validated to ensure that it is of length between 10 - 300 characters consisting of letters, numbers and standard punctuation.
-   The cycling tip link is validated to ensure it is a valid URL.

Blog comment form:

-   The category input is validated to ensure the user only inputs letter, spaces and no special characters.

---

## Data Model

The MongoDB VeloRoute database has seven collections as detailed in the attached diagram.

![Urban Attiva Data Model](readme-files/velo-route-data-model.png)

---

## Features

### Existing Features

#### Sections

#### Home Page

-   Urban Attiva logo with a link to the home page.
-   A navigation menu that allows the user to navigate the website by clicking the navigation links. The navigation menu collapses to a burger icon with aa exapnding sidenav menu on smaller devices. 
-   Section one of the home page includes a hero image, header text and a shop now button.
-   Section two of the home page images for each of the core product categories which when clicked link through to the product pages pre filtered by category.
-   Section three of the home page includes some customer reviews.
-   Section four of the home page cconatins some information highlighting free shipping thresholds, secure payments and registered user discounts.

#### Shop Navigation

-   The shop navigation menu enables users to link to the product page with products displayed filtered by core product categories and sub categories.
-   The product page provides the shopper with the ability to sort the product listing by price, rating, name or category.
-   Clicking on a product images navigates the user to the product details page where information about the product is displayed. The user can add a product to their shopping cart from the prodcut detail page and select the quentity and chosen size.

#### Shopping Cart

-   Once the user has selectd products and added them to their shopping cart the cart 
-   Cycling Tips are added by the admin user and cannot be edited by other users. Admin users can edit or delete cycling tips and the delete button is linked to a modal to confirm if the user definitely wants to delete the cycling tip.

#### Log In Page

-   The log in page provides a simple form for the user to log in to VeloRoute with the details they provided on registration.
-   The user is directed to their profile page when they log in.

#### Join Us Page

-   The Join Us page has a simple form for the user to provide their details so that the user can be registered. All inputs are validated.
-   Upon registration the user's details are stored in a MongoDB database with the password hashed for additional security.

#### Profile Page

-   The profile page displays the logged in user's profile details and the routes they have added which are displayed with the most recently added routes listed first.
-   The displayed routes can be edited by selecting the edit button or they can be deleted. There is a cancel button if the user decides that they do not wish to edit the route which returns the user to their profile page. The delete button is linked to a modal that displays a message to ask if the use definitely wants to delete the route.

#### Add Routes Page

-   The Add Routes page allows users who are logged in to the site to add new routes.
-   There is a simple input form that has dropdown select options for choosing a route category, country and difficulty level and input fields for users to add a route name, route image, route description, route distance and a link to the route on the users favourite GPS activity platform, e.g. Strava.

#### Add Cycling Tip Page

-   The Add Cycling Tips page allows admin users to add new cycling tips to the VeloRoute website.
-   There is a simple input form that has a dropdown select option for choosing a cycling tip category and input fields for the admin user to add a cycling tip name, an image, a cycling tip description and a link to further information related to the cycling tip.

#### Manage Categories Page

-   The Manage Categories page allows administration users to add, edit and delete the categories used for the dropdown select options on the Add Route and Add Cycling Tips pages.
-   The categories are displayed as simple cards categorised by each category type with buttons for adding, editing and deleting the categories.

#### Footer Section

-   This section has information about the VeloRoute team, copyright wording and links to Facebook, Twitter, Instagram and Pinterest social media sites.

_Note: The social media links currently link to the social media websites and not VeloRoute specific pages_

#### Future features

-   The ability for users to add ratings to the routes that have been added to VeloRoute.
-   Additional country categorisation to include states, regions, counties etc.
-   Addition of a separate cycling tips page to link from each of the cycling tips to provide a more detailed overview and instructions.
-   A newsletter for users to sign up to updates relating to VeloRoute.

---

## Technologies Used

The following technologies have been used to complete the UX design, capture user stories and defects and assign for development and to develop the Urban Paws website.

### Languages

-   [HTML5](https://en.wikipedia.org/wiki/HTML5) - used for the structure and content of the Trail Running UK website.
-   [CSS3](https://en.wikipedia.org/wiki/CSS) - used to style the Trail Running UK website.
-   [jQuery](https://jquery.com/)- used for scripts for the why trail running and races sections of the Trail Running UK website and for the newsletter.
-   [Python](https://www.python.org/) - used to style the Trail Running UK website.

### Frameworks - Libraries - Other

-   [Materialize](https://getbootstrap.com/) - utilised for the front-end design framework.
-   [MongoDB](https://www.mongodb.com/) - used as the database for the project.
-   [GitHub](https://github.com/) - for hosting the website repository.
-   [GitPod](https://gitpod.io/) - used as the development environment for the website.
-   [Google Fonts](https://fonts.google.com/) - used to source the Roboto font used throughout the website.
-   [Font Awesome](https://fontawesome.com/) - used to source icons for use throughout website.
-   [Balsamiq](https://balsamiq.com/) - utilised for the development of the website wireframes.
-   [Canva](https://canva.com/) - used for the design of the VeloRoute website logo.
-   [Coolors](https://coolors.co/) - used for creating the colour palette image.

### Testing Tools Used

-   [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used to edit changes prior to implementing the code changes, to diagnose problems and for performance, accessibility, best practice and search engine optimisation testing.
-   [Autoprefixer](https://autoprefixer.github.io/) - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
-   [Markup validation service](https://validator.w3.org/) - for the validation of HTML5 code.
-   [CSS validation service](https://jigsaw.w3.org/css-validator/) - for the validation of the CSS3 code.
-   [JShint](https://jshint.com/) - used to check for errors in the JavaScript code. 
-   [PEP8](http://pep8online.com/) - used to check for errors in the Python code.

---

## Testing

Full details of testing are contained in the [testing document](TESTING.md).

### Deployment

#### Requirements

To be able to deploy this project you will need the following:

- Python3 installed
- A Github account 
- A MongoDB account 
- A Heroku account

#### To clone the project locally

To clone this project from GitHub.

1.  Open the project repository on GitHub and click the **Code** dropdown button.
2.  Select the **HTTPS** tab and copy the URL.
3.  Open your terminal (Mac OS, Linux) or Git-Bash terminal (Windows).
4.  Change the current working directory to the location where you want the cloned directory to be created.
5.  Type **git clone**, enter a space and then paste the URL copied from GitHub.
6.  Press **Enter** and the local clone will be created in the specified directory.

#### Working with the local copy

1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: **pip3 install -r requirements.txt**.
2. Create a database in MongoDB  
    - Signup or login to your MongoDB account.
    - Create a cluster and a database.
    - Create seven collections in the database: **categories, cycling_tips, cycling_tip_categories, difficulty_levels, routes, users, countries.**
    - Add the data to the collections. See the VeloRoute [Data Model](#data-model) for details on how the data has been modelled for this project.
3. Create the environment variables 
    - Create a .gitignore file in the root directory of the project.
    - Add the env.py file in the .gitignore.
    - Create the file env.py. This  will contain all the environment variables.

    ```
    Import os
    os.environ.setdefault("IP", "Added by developer")
    os.environ.setdefault("PORT", "Added by developer")
    os.environ.setdefault("SECRET_KEY", "Added by developer")
    os.environ.setdefault("MONGO_URI", "Added by developer")
    os.environ.setdefault("MONGO_DBNAME", "Added by developer")
    ```
4. Run the app: Open your terminal window in your IDE. Type python3 app.py to run the app.

#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: **pip3 freeze -- local > requirements.txt.** (The file is needed for Heroku to know which files to install.)
    - In terminal window of your IDE type: **python app.py > Procfile** (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select your region. 
3. Deployment method 'Github'
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search for your Github repository to connect to it.
        - When your repository appears click on **connect** to connect your repository to Heroku. 
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars**.
        - Enter the variables contained in your env.py file. it is about: **IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME**
4. Push the requirements.txt and Procfile to repository. 
     ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"

    $ git add Procfile 
    $ git commit -m "Add Procfile"
    ```
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to **Automatic deployments**. Click on **Enable Automatic Deploys**. By **Manual deploy** click on **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app will open and the live link is available from the address bar. 

---

## Challenges

Two significant challenges were encountered late on in the project:

1.  The Materialize grid system presented an issue where the cards that were utilised flexed perfectly within the Materialize columns to become a uniform width but the image element within the card-image div did not flex perfectly proportionately to the width. As a reult the cards were very slightly different heights resulting in gaps in the rows of cards as they flexed to fill the parent container. I thought that if a container can be utilized as a parent to the image and the image constrained within that container as it flexed then maybe I could achieve a uniform height for all card images. After lots of searching on Google I came across <a href="https://css-tricks.com/scaled-proportional-blocks-with-css-and-javascript/"></a> which seemed to describe what i was thinking. After adapting the code I achieved the desired result. Images with a uniform height and cards aligned.

2.  The second challenge was when the realisation hit me that if my admin user has access to change or delete categories that have been set up in the system that could break the functionality related to other aspects of the site. To resolve this I created an IT user and assigned the ability to create , update and delete categories to this user as this user will understand the data model and can assess any required change before implementing the change and can consult the developer as required. 

---

## Credits

### Content

All text content included in this project is my own.

### Media

All images are my own, have been licensed from Adobe Stock or are freely available on Unsplash. Credits are listed below.

**Hero Image**

-   The hero image is licensed from Adobe Stock.

**Routes Images**

-   The Brossac, Chatignac and Berneuil route photo is my own.
  
-   Wokingham CC Sunday ride route: Photo by <a href="">Martin Magnemyr</a> on Unsplash
  
-   Beauty of the Peak District ride: Photo by <a href="">Minkus</a> on Unsplash

-   Epic French Pyrenees route: Photo by <a href="">Yury Kirillov</a> on Unsplash
  
-   Coast to Alicante route: Photo by <a href="">Polina Rytova</a> on Unsplash
  
-   Mountain trails route: Photo by <a href="">Jan Kopřiva</a> on Unsplash

**Cycling Tips Images**

-   Clean and maintain your bike cycling tip: Photo by <a href="">Dan Burton</a> on Unsplash
  
-   The M Check cycling tip: Photo by <a href="">Robert Bye</a> on Unsplash

-   Coffee and cake cycling tip: Photo by <a href="">Nathan Dumlao</a> on Unsplash
  
-   Clean your chain cycling tip: Photo is licensed from Adobe Stock

### Acknowledgements

-   [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) for mentor guidance and support.
