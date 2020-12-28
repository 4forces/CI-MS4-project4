# Upbeat Engineering - Searching for electronic engineering components? Look no further.

<img  src="static/img/readme/title-pic.PNG"  width="800"  style="margin:0">


## Overview

If you are someone who has interest in tinkering with mechatronics, want to make robots that can help you do things in life, yet know not where to get components.

Upbeat Engineering is here to help you. We offer sales of electronic components at affordable prices. We know that building electronics sometimes depends on inspiration and the 'feel' which may be lost if there is a delay or absence of the right parts. So we offer ourself as a swift source of components. Your order will reach you no later than 3 workind days, right here in Singapore.

We are also looking to expand our services to product design and engineering kits for the youth education.
This project is deployed on Heroku [here](https://i-ms4-upbeatengineering.herokuapp.com/).


### Objective

Upbeat Engineering is a based on a true concept from the developer's relative, a mechatronics enthusiast looking to expand his network of similar minded hobbyist by sharing his hardware and electronic parts (with a small fee). He knows by experience that building robots and devices do not move in a linear manner, resulting in spare parts and unused components, and sometimes a deterence to inspiration.

Parts and orders usually comes from overseas, with waiting time and a higher price. The purpose of Upbeat Engineering is to help like minded enthusiasts have a shorter lead time to getting what they need, so they can quickly get back on track with building.
  
---


## UX and UI

For this project, the frontend html was done first before proceeding to integrate with Django. The reason for this is to have an overview of the look and layout first before commencing work on the backend.

This website was conceptualized in discussion with a family member of the developer, who wished to do an online business related for sales of electronic engineering components and engineering design and solutions. 

The look of was based off this [site](https://hackaday.com/blog/), which is the family member indicated his preference. Based on this site's look, inspiration was sourced from [Pinterest](https://www.pinterest.com/), with the eventual decision to reference and adopt the theme of this [page](https://www.behance.net/gallery/62918019/GamingGear-E-commerce-Website).

The colour palette used is as follows:
<img  src="static/image/readme/color-swatch.png"  width="800"  style="margin:0">

Similar to the [reference site](https://www.behance.net/gallery/62918019/GamingGear-E-commerce-Website) mentioned above, the fonts of Gotham and [Cabin](https://fonts.google.com/specimen/Cabin) were adopted for this site. However, since Gotham is a paid font, [Raleway](https://fonts.google.com/specimen/Raleway) is used as a replacement, as listed on [this site](https://fontsplugin.com/google-fonts-gotham/).

Effort was made to source for suitable background images that relate to electronics and circuit boards, which are in-line with the theme of this page. Image sources came from [Pinterest](https://www.pinterest.com/), [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/).


### User stories

As a potential buyer:

1. I want to be able to search by the component product name
2. I want to be able to search by component product type (sensor, motor, connectors, etc)
3. I want to see a more detailed component product description
4. I want to be able to see the list of items in a 'shopping cart'. I should be able to increase/decreae the quantity of items in my shopping cart, or remove the item, just like a physical shopping cart. 

As the shop owner:

1. I want to be able to add new products to my shop. 
2. I want to be able to remove old products from my shop.
3. I want toe be able to change the various product details (such as name, description, supplier, etc) when needed


### Wireframes and ER Diagrams

<details>
<summary>Desktop Wireframes (Click <a href=>here</a> for diagram only view)</summary>

<p align="center">
    <img height="350" src="https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/wireframe-desktop.png" alt="Desktop wireframe">
</p>

</details>

<details>
<summary>Mobile Wireframes</summary>

<p align="center">
    <img height="350" src="https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/wireframe-mobile.png" alt="Desktop wireframe">
</p>

</details>

<details>
<summary>ER Diagrams</summary>

<p align="center">
    <img height="350" src="https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/erd2-rs2.png" alt="Desktop wireframe">
</p>

</details>

The frontend individual webpages was done first before integration into Django backend. The reason for this was to have an overall view of the layout, appearance and 'feel' of the page flow.  


## Features

This site has 7 main features:

-  [Landing page](#)
-  [Products List](#)
-  [View Product](#)
-  [Shopping Cart](#)
-  [Add Product*](#)
-  [Update Product*](#)
-  [Delete Product*](#)

**Admin only*


### Landing Page

Upon visiting this site, the user is greeted with a landing page. This page has a carousel with various images of electonics hobbyist workshops and component. 

Clicking on the "Shop Now" button in the carousel brings the user to the [xxxxxproduct listings](#) on the shop. 

Following is a short write up "About Us" which gives the background of this shop and the intent of the shop owners. 

On the navbar, there are the following links: 
- Logo: Leads back to the landing page
- Shop: Brings user to the products list page
- Login: Login screen for user
- Register: Registration page for user

Upon user login, the following links will appear:
- Logout: Logout page. This replaces login link.
- Cart: Shopping cart that shows products user wishes to purchase. 

Upon admin login, the navbar will display the following additional link:
- Add product: Leads the admin to the "add product" form.

**Notes on Feature Development:**

The images from for the carousel, mostly selected from [Unsplash](https://unsplash.com/) is based on the shop owner being an electronic engineering hobbyist, and aims to invoke a sense of interest in tinkering in engineering electronics.

Code Institute's walkthough of [Boutique Ado project](https://github.com/ckz8780/boutique_ado_v1) on the LMS was referenced to for the initial setting up steps on Django.

The navbar was made initially transparent. This was done by following the Steps on this [Stackoverflow post](https://stackoverflow.com/questions/16392952/css-to-make-bootstrap-navbar-transparent). 

Along the way, it was decided that a semi-transparent background will be better for the UX, since page elements will overlap with the contents inside a transparent navbar. AN attempt was made to do a 'frosted-glass background' by following [this site](https://codepen.io/GreggOD/pen/xLbboZ). However, this was eventually replaced with a simpler method by using the 'Backdrop-filter' CSS property. 

More on backdrop-filter can be found on [CSS-Tricks](https://css-tricks.com/the-backdrop-filter-css-property/) and [Mozilla.org](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter). It is noted that this property may have some compatibilty issues with certain browsers.

Towards the end of the development process, there was a need to differentiate the features access between a superuser and a "normal login" user (for example a customer) on the navbar and throughout the site. 

This was accomplished via 2 portions: adding a  `@user_passes_test(lambda u: u.is_superuser)` for superuser and `@login_required` for normal login user before the respective `def` fuction in `views.py`, followed by if-else loops in the `template.html` with conditions: `{% if user.is_authenticated %}` and/or `{% if user.is_superuser %}`

References to superuser only access was found on Stackoverflow [here](https://stackoverflow.com/questions/12003736/django-login-required-decorator-for-a-superuser) and [here](https://stackoverflow.com/questions/56897625/want-to-authenticate-only-superuser). Normal user - `@login required` was covered by the lecturer.


#### Products List Page

On this page, the user can see all the products sold. Each  product's image thumbnail, name, price and category are arranged into cards for the user to preview. The user may only add the product to cart upon login. The user can also click on the product thumbnail to view it in detail. The user may also search for specific products by using the search function, which allows search by key words and/or category.

**Notes on Feature Development:** 

The display layout for the products list page and [xxxxxview product page](#) was largely referenced from [Banggood Online Store](https://sea.banggood.com/search/single-pin.html?from=nav) and [Cytron.io](https://sg.cytron.io/p-encoder-sensor-module?src=search.instant), due to the similar nature of products sold. 

At the initial stage, Bootstrap code from [this site](https://getbootstrap.com/docs/4.5/examples/carousel/) was referenced for the individual item layout. Along the way, through discussion with classmates, decision was made to use [Bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/) instead. [W3Schools](https://www.w3schools.com/bootstrap4/bootstrap_cards.asp) was referred to frequently for tutorial on Bootstrap cards usage. 

There was some issues with changing the background colour of the cards. A solution was found on [Stackoverflow](https://stackoverflow.com/questions/42430987/how-to-change-the-opacity-of-a-card-block-in-bootstrap-4). A way was also found to [fit the images nicely into the card](https://stackoverflow.com/questions/3029422/how-do-i-auto-resize-an-image-to-fit-a-div-container).


#### View Product Page

This pages shows further information on the product, such as quantity in stock, part number and description.

The user may search for the desired product via typing in the product name, and selecting one of the six product types: Power, Sensors, Connectors, Signal Converters, Motors and Others.

The user may also add the product to the shopping cart from this page.


#### Shopping Cart and checkout

The shopping cart shows the list of products the user intends to purchase. The product name, unit price, quantity of purchase and costs sub-total  are shown. A thumbnail of the product is shown as well. 

The user can increase or decrease the quantity by clicking on the "-" and "+" buttons. The "Sub-Total" updates according to the quantity. If the user changes his mind, he may also click on the "thrash" icon to remove it from the cart.

The total costs at the bottom right is also updated accordingly.

Once the user has finished shopping, he can click on the "Checkout" button to proceed with checkout on Stripe.

**Notes on Feature Development:** 

During the initial stage of development, the cart contents could not be displayed. To investigate, the `cart` contents stored in session storage was printed to console via `print(cart)`, these were then passed to a [python dictionary beautifier](https://codebeautify.org/python-formatter-beautifier). It was eventually discovered that this issue was due to pointing to the wrong dictionary keys. A sample of the code below:

```python
def view_cart(request)
  cart = request.session.get('shopping_cart', {})
  print(cart)
```

There were also rounding errors for the values of 'sub-total' and 'total'. An explanation and possible [solution](https://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency) to handle this error was to use `DecimalField` instead of `FloatField`. 
However, this causes Stripe to give an "Integer Error". Upon consulting [Stripe documentation](https://stripe.com/docs/currencies), it became clear that Stripe works with integer values only. Hence after discussion with the lecturer, a workaround is to use `IntegerField` for the cost price, and divide by 100 to properly display in dollars. 

The division by 100 was done in the `template.html` by [using mathfilters](https://stackoverflow.com/questions/5848967/django-how-to-do-calculation-inside-the-template-html-page), with adjustments to [display 2 decimal places]((https://stackoverflow.com/questions/12903686/how-can-i-get-a-decimal-field-to-show-more-decimal-places-in-a-template). The installation steps for mathfilters can be found [here](https://pypi.org/project/django-mathfilters/).

At the final step, after checkout and payment, Stripe Webhooks failed due to `HTTP status code 401 (Unauthorized)`. After looking at the [stripe documentation](https://stripe.com/docs/error-handling) and piecing the facts together, it was deduced this occured due to port 8080 being set as private in Gitpod. This issue was resolved after changing the setting to "Make Public".


#### Add Product (Admin only)

An admin can access this page to add new products to the shop for sale. The following fields have to be populated: Name, Cost, Unit, Quantity, Category, Part Number, Description, Supplier and Cover (image upload). This function is accessed from the [xxxxView Product Page](#). 

**Notes on development:** 

Significant time and effort was spent troubleshooting the [Cloudinary](https://cloudinary.com/) image upload function via HTML template pages. Initially, when this was done, the image identifier link failed to be captured - means to say the image field is actually empty. The "Uploading..."  and "Done!" messages did not work as well. What was puzzling was that everything worked fine when image upload is done via Django backend. 

Due to sparse information on troubleshooting Cloudinary issues, this developer resorted to scrutinising the JavaScript and the image upload HTML `<form>` elements for code discrepancies. Thorough comparision was done with the JavaScript and HTML in the [Django Cloudinary Sample](https://github.com/cloudinary/cloudinary-django-sample/blob/master/photo_album/templates/upload.html#L87), with the help of an [Online JS Beautifier](https://beautifier.io/). 

Eventually, with the help of [this article](https://medium.com/@szczerbeansky/django-web-app-and-images-cloudinary-straightforward-study-ae8b5bb03e37), one of the cause for errors was identified - the missing `enctype="multipart/form-data"` for the `<form>` element. 

With the help of [TextCompare.org](https://www.textcompare.org/javascript/), another cause was identified, where the "#id" and ".class" of the HTML and JavaScript did not match, leading to the "Uploading...", etc messages failing to update. 

Through discussions with classmates (some who also faced the same issue), the final and most important cause was finally resolved: `fields = ('cover')` was missing from the Forms Model! Classmates who did not face this issue used `fields = ('__all__')`, hence circumventing it altogether. A sample of the corrected `ProductForm` model is appended: 

```python
class ProductForm(forms.ModelForm):
    cover = CloudinaryJsFileField()

    class Meta:
        model = Product
        fields = ('name', 'cost', 'unit', 'quantity',
                  'category', 'part_number', 'description',
                  'supplier', 'cover')
        # fields = ('cover') was missing the whole time!
```

Much time was spent scrutinising and attempting to debug the frontend code as this developer wrongly assumed that there was no issue with the backend code (due to successful upload with Django backend).

Sometimes, the answer is just right under our nose. It is when one is able to not hold on too strongly to one's close-minded fixations, that there is space for the solution to make its way to one's mind. This was a valuable lesson learnt not just in coding, but also to life. 


#### Update Product (Admin only)

If the admin wishes to update the product details, he can do so. This function is accessed from the [xxxxView Product Page](#). 


## Delete Product (Admin only)

The admin may also choose to remove the product if needed. This function is also accessed from the [xxxxView Product Page](#). 


**Notes on development for Add/Update/Delete Product:** 
  
Django messages were used to provide feedback and inform the user upon the completion of these functions. These site were referred to for understanding the Django messages framework and working with Django messages:

- [The messages framework](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/)
- [Message Levels and Tags](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)

Django messages was used in conjunction with [Toastr](https://github.com/CodeSeven/toastr). This was done with help from [this article](https://stackoverflow.com/questions/45004245/how-to-use-toastr-in-django-for-success-or-fail-message) in Stackoverflow. Point to note that the JavaScript syntax for toastr in Django templates differs slightly from that used in Flask templates. 


### Features Left to Implement
 

 1. Feedback to user, either in the form of pop-ups, redirecting to a new page, or Django Messages upon the following events:
    - Checkout successful
    - Purchase completion: e.g. "Thank your for your purchase"
    - Checkout cancelled

2. HTTP 404 and HTTP 500 pages, in the event of invalid page or server errors

3. Displaying "Welcome \<Username\>!" at the navbar after user login

4. Adding CSS and layout for the following pages: 
   - Reset password
   - Verify email 
   - Confirm email  

5. Adding notes for the requirements of the username and password at the user registration page, for example: 
   - Minimum length of username and password
   - Accepted/Unaccepted characters (e.g. *&!%)

6. Update Username and Registered Email pages

7. Instructions to user on filling of forms for adding/updating product, for example:
    - Input product cost in cents
    - Character limits for each field

8. Customise form fields display for uniqueness. Currently the standard display is used.

7. Update the quantity in stock when purchases are made

8. Admin CRUD functions for product Supplier and Category

## Technologies Used

1.  [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) to display contents in browser

2.  [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) page styling customisatoin

3.  [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for DOM manipulation and user element interaction

4.  [bootstrap](https://getbootstrap.com/) for the frontend development

5.  [Fontawesome](https://www.bootstrapcdn.com/fontawesome/) iconsets for buttons

6.  [Gitpod](https://www.gitpod.io/) online cloud develop environment

7.  [Python](https://www.python.org/) as the backend development language

8.  [Django](https://www.djangoproject.com/) web framework

9.  [SQLite3](https://www.sqlite.org/index.html) database used for development phase with Django

10.  [Heroku](https://www.heroku.com/) for cloud platform deplpyment

11.  [PostgreSQL](https://www.postgresql.org/) database after deployment to Heroku

12.  [Cloudinary](https://cloudinary.com/) for storing online images

13.  [toastr](https://github.com/CodeSeven/toastr) for flash messages

14.  [ERDplus](https://erdplus.com/) to draw ER Diagrams and Relationship Schema

15.  [Balsamiq](https://balsamiq.com/wireframes/desktop/) for wireframes
 
---
 

## Testing


Manual testing was done on all links and Pages.

Test cases are for Shopper (User) and Admin (Superuser).

User type | Username | Password
-|-|-
Shopper (User) | testtest | rotiprata123
Admin (Superuser) | admin | rotiprata123


### Testing for Shopper (User)

<details>
<summary>Test Steps</summary>

No. | Test Case | Expected Result(s) | Results
-|-|-|-
1 | Click on the "Upbeat Engineering" icon at the top left of the page | User will be brought to the *Landing Page* | Pass
2 | Click on the "Login" button on the Navbar | User will be brought to the *Sign In* page | Pass
3 | Type in the login and passsword as above, and click "Sign In" | User will be brought back to the *Landing Page* | Pass
4 | Click on "Click here to shop!" button in the carousel, or the "Shop" link on the navbar | User will be brought to the *Product List* page | Pass
5 | Search by text input only: Input desired search field in Search bar (for e.g. "converter"), and leave "Category' alone | Products fitting the search Criteria will be displayed | Pass
6 | Search by category only: Select "Power" for "Category' | Products of Category "Power" will be displayed | Pass
7 | Search by both text input and category: Input desired search field in Search bar (for e.g. "converter"). Select "Power" for "Category' | Products with words "converter" under Category "Power" will be displayed | Pass
8 | Click on an item image | User will be brought to the *View Product Page* | Pass
8 | Click on "Add to cart button" button, or "Submit" on the navbar | User will be brought to the *Update or Remove items Page* | Pass
8 | Click on "Submit New Item" button, or "Submit" on the navbar | User will be brought to the *Update or Remove items Page* | Pass
8 | Click on "Submit New Item" button, or "Submit" on the navbar | User will be brought to the *Update or Remove items Page* | Pass
  
</details>

### Browse Items Page

  

No. | Test Case | Expected Result(s)

-|-|-

1 | Mouse-over any item-box | Item-box will be expanded slightly

2 | Click on item-box | User will be redirected to *Item Details page*

  

### Search Items Page

  

No. | Test Case | Expected Result(s) | Remarks

-|-|-|-

1 | Click on "Search" button | All submitted items listed | -

2 | Type in an item name (For e.g. "chair" or "bottle") | The item(s) containing the word "chair" or "bottle will displayed | Search by item name only

3 | Select one of the 5 item types from the dropdown list (For e.g. "Toys and Playthings") | All items with type "Toys and Playthings" will be displayed | Search by item type only

4 | Type in an item name and select an item type (For e.g. type "jumpers", select "clothes") | All items with "jumpers" in their name and type: "clothes" will be displayed | Search by both item name and type

5 | Type in a random text, for e.g "abc" into the search box and click search | "No item found" will be shown | -

6 | Mouse-over any item-box in search results| Item-box expand animation will be observed | -

7 | Click on item-box in search results | User will be redirected to *Item Details page* | -

  

### Submit Item Page

  

No. | Test Case | Expected Result(s)

-|-|-

1 | Key in all fields and select radio buttons and click "Submit" | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item "\<item name>" added** will appear.

2 | Leave any field empty and click "Submit" | User will be prompted to provide compulsory fields

3 | Leave out '@' from the email in "Contact" field | User will be prompted to provide a proper email

  

### Update or Remove items Page

  

No. | Test Case | Expected Result(s)

-|-|-

1 | Click on "Edit" button | User will be redirected to "Edit Item" page, allowing user to view and make changes to previously entered fields.

2 | From the "Edit Item" page, click on "Submit" button | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item \<item name> updated** will appear.

3 | From the "Update or Remove Items" page, click on "Delete" button | User will be brought to confirmation to "Delete Item" page with dialog box asking user **Are you sure you want to delete "\<item name>"?**

4 | In the confirmation to "Delete Item" page, click "Cancel" | User will be brought back to "Update or Remove Items" Page

5 | In the confirmation to "Delete Item" page, click "Confirm" | (i) User will be brought to "Update or Remove Items" Page, (ii) Flash message **Item deleted** will appear.

  
  

### Issues and bugs

  

- Text with no spaces exceeds the container width in item boxes (screenshot [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/text-exceeds-container.PNG))

- Repeat of commit messages due to infamiliarity using the *git rebase* function (screenshot [here](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/rebase-repeat-commits2.PNG))

- Line 184 of `app.py` gives the following error `f-string is missing placeholderscornflakes(F541)`

- Issues with sticky footer:

- Setting `position:absolute` shows a floating footer for "long" pages ([screenshot](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/footer.PNG))

- Removing it results in floating footer for short pages ([screenshot](https://github.com/4forces/CI-MS3-project3/tree/master/static/img/readme/footer2.PNG))

  

---

  

## Deployment

  

### Github

  

**(a) Downloading this Project**

  

To download the project code, please do the following:

  

1. At the [project page](https://github.com/4forces/CI-MS3-project3), click on the "Code" button, and select "Download ZIP"

2. This ZIP file can be unzipped to access all project code and related files

  

**(b) Clone the Project**

  

To clone this project, please do the following:

  

1. At the [project page](https://github.com/4forces/CI-MS3-project3), click on the "Code" button

2. Click on the "copy icon" to copy the project link to clipboard

2. This URL can be pasted it in your IDE terminal to clone in your computer

  

**(c) Creating the Repository**

1. Login to GitHub

2. Go to [CI Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

3. Type in a unique name under "Repository name", and an optional description of the to-be-created repository

4. Select the option of making the repository "Public"

6. Click on the "Create Repository from template" button

7. User will be re-directed to the newly created repository page

  

**(d) Deploying to GitHub Pages**

1. On the menu-bar, click on "Settings" (Beside the gear icon)

2. Scroll down to "GitHub Pages" section

3. Under "Source", select "Branch: master"

4. Click "Save", and the website will be deployed

5. Scroll down to "GitHub Pages" section again, where the deployed link can be retrieved

6. The project can be accessed via the deployed link.

  

### Heroku

  

1. Sign up for a Heroku account

2. After forking, downloading or cloning from the master branch this project from [github](https://github.com/4forces/CI-MS3-project3),

install all the requirements with `pip3 install -r requirements.txt` in the terminal

3. Login to Heroku by typing in the terminal `heroku login -i`

4. Create a new app (replace <app_name> with a name of your own (Note: name must be unique)

5. Check that new remote has been added by typing `git remote -v` into the terminal

6. Install gunicorn with `pip3 install gunicorn`

7. Create a file named `Procfile` (without any extension, with the first P uppercase)

8. Open the "Procfile" add the following line `web gunicorn <your python file name without .py>:app `

9. Create requirements file with the command `pip3 freeze --local > requirements.txt` in terminal

10. Commit all additions by typing following in terminal:

-  `git add .`

-  `git commit -m "<Commit Message>"`

- Replace `<Commit Message>` with a suitable description

11. Git push to Heroku by using `git push heroku master` command

12. Add the following in Heroku Config Vars

- MongoDB URI

- Secret key for Flask

- Database Name: giftkids

13. Set the debug mode to false on Heroku

  

## Credits

  

### Gitpod Setup

  

- Code Institute's [Gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

  

### Images and Graphics

- Images were mostly sourced from [Unplash](https://unsplash.com/), and a bit from [Pexels](https://www.pexels.com/)

- Background image graphics obtained from [freepik](https://www.freepik.com/premium-vector/toys-doodle-set_6551728.htm#page=1&query=toys&position=41)

- README title picture from [Am I Responsive](http://ami.responsivedesign.is/#)

  
  

### Secret Key

-  [RandomKeygen](https://randomkeygen.com/) to generate the secret key

  
  

### Site Theme and Appearance

-  [Pinterest](https://www.pinterest.com/), which led to [Jadusona](https://demo.hasthemes.com/shopify/jadusona-cm.html)

-  [Code Institute Slack community](https://code-institute-room.slack.com) for recommending the following Chrome Extensions:

-  [Color palette](http://palette.site/) to extract reference site color theme

-  [Color pickr eyedropper](https://vidsbee.com/ColorPick/) to identify site colours

  

### Logo and favicion

1.  [Free Logo Design](https://www.freelogodesign.org/) to generate site logo

2.  [favicon.io](https://favicon.io/favicon-converter/) to convert logo to favicon

  
  

### Readme Writing and Markdown

The [CI Slack community](https://code-institute-room.slack.com), which gave many pointers and tips on various useful sites on:

  

**Markdown:**

  

-  [Adam Pritchard's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

-  [commonmark.org](https://commonmark.org/help/)

-  [Github Guides - Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)

-  [Line breaks in markdown](https://gist.github.com/shaunlebron/746476e6e7a4d698b373)

  

**Writing of the Readme:**

  

-  [CI Readme template](https://github.com/Code-Institute-Solutions/readme-template)

-  [Anna Gilhespy's *Portrait Artist* Readme](https://github.com/AJGreaves/portrait-artist/blob/master/README.md)

  

### Syntax Clarifications

  

- Documentations for [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/)

  

### Deployment to Heroku

  

- Lecturer [Mr. KX Chor's](https://github.com/kunxin-chor) for his detailed step-by-step guidance

  

---

  

## Acknowledgements

  

- The wonderful CI community at Slack for numerous useful tips, inspiration and motivation :sparkling_heart:

- Our Lecturer Mr. Paul Chor for much patience & dedication in teaching and sharing his deep knowledge with us :clap:

- My classmates (Collin, Eddy, Frances, JY and Rui Shan) in the spirit of sticking together - Encouraging, striving, struggling :satisfied:

  

**For education purposes only**