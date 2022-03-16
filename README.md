<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

body{
    background-color: black;
    font-family: Poppins, sans-serif;
    font-weight: 400;
    letter-spacing: 1px;
}

p {
  line-height: 32px;
  margin-bottom: 20px;
  }

</style>

<center><img src="static/readme-images/ow-logo.png" alt="Outdoor World Logo" width="50%"></center>

----

    This is the README file for my Code Institute MS4 project site, Outdoor World - The online outdoor equipment store.

    Outdoor World is an online store selling outdoor clothing and equipment for a range of activities. The store also has a blog feature for the store owners to help promote products, also allowing readers to comment on their posts for customer interaction.

    This project is the 4th project as part of the Code Institute Full Stack Development course. The projects are set in order to demonstrate my understanding of what we have learnt during the previous units.
    The task set for this project is to build a full-stack site based around business logic used to control a centrally-owned dataset and set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

<br>

<center><img src="static/readme-images/ow-mockups.png" alt="Website Mockup" width="80%">

[CLICK HERE TO VISIT THE LIVE SITE](https://ts-outdoorworld.herokuapp.com/) </center>

----
<br>

# Table Of Content:

- <a href="#project_goals">Project Goals</a>
- <a href="#ux">User Experience (UX)</a>
    - <a href="#ux-user_stories">User Stories</a>
    - <a href="#ux-design">Design</a>
        - <a href="#ux-design-color">Color</a>
        - <a href="#ux-design-typography">Typography</a>
        - <a href="#ux-design-images">Images</a>
        - <a href="#ux-design-structure">Structure & Mockup Designs</a></a>
        - <a href="#ux-design-amendments">Amendments To Mockup Designs During Development</a></a>
- <a href="#features">Features</a>
    - <a href="#features-current">Current Features</a>
    - <a href="#features-future">Possible Future Features</a>
- <a href="#database">Database</a>
- <a href="#key-components">Key Components</a>
    - <a href="#key-components-languages">Languages</a>
    - <a href="#key-components-frameworks">Frameworks & Libraries</a>
    - <a href="#key-components-others">Others</a>
- <a href="#testing">Testing</a>
    - <a href="#testing-html">HTML</a>
    - <a href="#testing-css">CSS</a>
    - <a href="#testing-javascript">Javascript</a>
    - <a href="#testing-pep8">PEP8 Compliance</a>
    - <a href="#testing-lighthouse">Overall Website Performance & Compatibility </a>
    - <a href="#testing-responsive-design">Responsive Design</a>
    - <a href="#testing-browser-compatibility">Browser Compatibilty</a>
    - <a href="#testing-links">Link Testing</a>
    - <a href="#testing-user-stories">User Story Testing</a>
    - <a href="#testing-problems-during-development">Problems During Development</a>
    - <a href="#testing-bugs">Known Bugs</a>
- <a href="#deployment">Deployment</a>
    - <a href="#deployment-heroku">Deployment With Heroku</a>
    - <a href="#deployment-forking">Forking</a>
    - <a href="#deployment-cloning">Cloning Project</a>
- <a href="#credits">Credits</a>
    - <a href="#credits-content">Content</a>
    - <a href="#credits-media">Media</a>
    - <a href="#credits-code">Code</a>
    - <a href="#credits-acknowledgments">Acknowledgements</a>

----

# <span id="project_goals">Project Goals</span>

*   Design, develop and implement a full stack web application using HTML, CSS, JavaScript, Python and Django

*   Identify and apply necessary security features

*   Design a website that uses HTML, CSS, Javascript, Python & Django


# <span id="ux">User Experience (UX)</span>

    This section is designed to generate possible scenarios of the typical end user that would use this website. 
    This will help ensure end user requirements are designed into the website.


## <span id="ux-user_stories"><b>User Stories</b></span>

|ID|User Type|I want to be able to...|So that I can...|
|---|---|---|---|
|<strong>A. Viewing & Navigation</strong>|
|A1|All Users | See that they have landed on the correct site they intended to visit.| To reassure users they have arrived at the correct store.|
|A |All Users | Understand the purpose and reason for the store.| To keep the interest of the users.|
|A |All Users | Be able to view the website correctly on any device.|Browse the store fully without missing out on content or having a negative experience|
|A |All Users | Find the business's social links| To engage with the business's social media pages and share the website with friends.|
|A |Shopper | See all the products available| To find suitable products to purchase|
|A |Shopper | Easily navigate categories of different products| To display a narrower selection of products they are interested in buying|
|A |Shopper | See the value of the items in the basket| To see how much they have spent|
|A |Shopper | Filter or See clearly any special offers that the site may have| To make savings on purchases|
|A |Site User | Easily locate the login link.| Returning users are able to have access to their accounts without navigating multiple pages.|

|<strong>B. Registration & User Accounts</strong>|
|B1|Site User| Register for an account|To store information about purchases, addresses and payment |
|B2|Site User| Login/Logout of their account| Access account information and be able to logout to prevent other users viewing this information.   |
|B3|Site User| See  a list of previous orders made|To view previously purchased items |
|B4|Site User| Personal user account| To store addresses/payment information|
|B5|Site User| Login using social accounts| Quick and convenient way to login|

|<strong>C. Sorting & Searching</strong>|
|<strong>D. Purchasing & Checkout</strong>|


    - The website administrator must be able to find the administrator tools when logged into the site.

    - The website administrator must not be able to delete the main administrator account from the database.

    - The website administrator must be able to create, remove, update and delete products.

    - The website administrator must be the only users to have access to the restricted websites and non-administrators must not be able to access restricted sites by direct URL inputs.

## <span id="ux-design"><b>Design</b></span>

* ### <span id="ux-design-color"><b>Color</b></span>

    When choosing the most suitable color scheme for the site, I decided to list the main points of what I wanted to try to create from the design.

    Here are the key points to consider when choosing the colors:

    * Eye Catching
    * Comfortable
    * Color Compatibility
    * Use colors commonly associated with Adventure/Outdoor Activities

    I chose to develop both the logo and the main site theme at the same time to ensure that they could work well together. 
    The colors were going to be an important part of the design in order to create a brand that could be applied throughout the company should it be required in the future.

    To choose a compatible color scheme, I decided to use [Adobe Color](https://color.adobe.com/) to find colors that would work well together. 
    I began by searching the [Adobe Color](https://color.adobe.com/) site using keywords such as Outdoor, Mountains, Climing, Scrambling and Hiking. The site then found a large selection of different color schemes, and I chose a color scheme I felt would represent the brand for the site well.
    
    [Adobe Color](https://color.adobe.com/) also helps ensure that the colors are compatible together.

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ CONTRAST SCORING @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    <img src="" alt="Color Palette" width="50%">

* ### <span id="ux-design-typography"><b>Typography</b></span>

    When choosing which font to use as part of my design, I felt it was important for it to be easy to read but less uniform than fonts commonly found on other sites. I wanted the font to be appropriate so that I could use it for the logo text and the main site text. This would then help maintain a nice continuity within the design and help create the store's brand.

    I have used Google to source the fonts and these are loaded within the head of the page.

    The logo font is [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue)

    <img src="" alt="Image of the Bebas Neue Font @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" width="30%">

    This is the font @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    The secondary font is [Montserrat](https://fonts.google.com/specimen/Montserrat)

    <img src="" alt="Image of the @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Font" width="30%">

    This font is used as the font for all key information of the product descriptions and checkout information etc. making sure the large blocks of text are easy to read.

* ### <span id="ux-design-images"><b>Images</b></span>

    There is very little base images on the site, the majority of the images are the product images.
    The images for each of the products to the site are outsourced and the staff/administrator must provide a url to the image or they can use the image upload function that will store and reference the image from a remote storage solution by Amazon S3.

* ### <span id="ux-design-structure"><b>Structure & Mockup Designs</b></span>


    <h3> Homepage </h3>
    <img src="" alt="Wireframe image for the Homepage" width="100%">
    
    <br>
    <h3> Registration Page </h3>
    <img src="" alt="Wireframe image for the Registration page" width="100%">

    <br>
    <h3> Login Page </h3>
    <img src="" alt="Wireframe image for the Login page" width="100%">

<br>

* ### <span id="ux-design-amendments"><b>Amendments To Mockup Designs During Development</b></span>



## <span id="features"><b>Features</b></span>

* ### <span id="features-current"><b>Current Features</b></span>

    * #### <b>User Access Structure</b>

    * #### <b>Navigation Menu Based On User Level</b>

        <img src="" alt="Wireframe image for the navigation bars based on user access." width="100%">

    * #### <b>Dynamically Created Navigation Menu Dropdown</b>

    * #### <b>User Account</b>

* ### <span id="features-future"><b>Possible Future Features</b></span>

    * #### Loyalty Scheme
        Returning customers can use their Outdoor World accounts to store and build loyalty points from regular purchases. These points could then be redeemed against money off vouchers. 

        This would be a good way for the store to retain and attract repeat business, in turn impoving sales.

    * #### Local Activity Section
        In order to offer the customers with opportunities to use the equipment they buy in the store. It would be good to offer adventures and tours that the store operates on the site. Customers could then register and pay for the courses online.

        This could create a good customer and business relationship, also helping to boost sales from any recommendations that instructors could make during the activities.

    * #### Hire Shop
        As the store is located within a watersport center, it would be great to manage all the equipment hires.
    
        Customers could be able to book and pay for the equipment online, the system would then generate an email with a unique code that the customer could present in-store to collect the hire equipment.

    * #### Product Reviews

        Customers could leave reviews for products they have purchased in the store.
        This can improve the shopping experience for others when browsing products and hopefully help promote sales for products receiving good reviews.

## <span id="database"><b>Database</b></span>

<img src="" alt="Wireframe image for the database plans." width="50%">

## <span id="key-components"><b>Key Components</b></span>

* ### <span id="key-components-languages"><b>Languages</b></span>

    * #### [HTML5](https://en.wikipedia.org/wiki/HTML5)
    * #### [CSS3](https://en.wikipedia.org/wiki/CSS)
    * #### [JavaScript](https://www.javascript.com/)
    * #### [Python](https://www.python.org/)

* ### <span id="key-components-frameworks"><b>Frameworks & Libraries</b></span>

    * #### [jQuery](https://jqueryui.com/)
    * #### [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    * #### [FontAwesome](https://fontawesome.com/)
    * #### [Google Fonts](https://fonts.google.com/)

* ### <span id="key-components-others"><b>Others</b></span>

    * #### [GitHub](https://github.com/) - Repository Hosting
    * #### [GitPod](https://www.gitpod.io/) - Development Environment
    * #### [Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html) - Used to create the logo and favicon
    * #### [Website Mockup Generator](https://websitemockupgenerator.com/) - To create the opening image for the README.
    * #### [TinyPNG](https://tinypng.com/) - Used to reduce image file sizes
    * #### [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Performance and Accessibility Reporting
    * #### [Balsamiq](https://balsamiq.com/) - Used to build the wireframes
    * #### [Heroku](https://www.heroku.com/) - Live site deployment
    * #### [Am I Responsive](http://ami.responsivedesign.is/) - To check responsive design
    * #### [W3 Validator](https://validator.w3.org/) - To check my HTML code


## <span id="testing"><b>Testing</b></span>

* ### <span id="testing-html"><b>HTML</b></span>

    To test my HTML code, I used the [W3 Validator](https://validator.w3.org/)

    

    Here is the pass report for the homepage:

    <img src="readme-images/html_validation_report.png" alt="HTML Validation Report" width="80%">

<br>

* ### <span id="testing-css"><b>CSS</b></span>

    To test my CSS code, I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

<br>

* ### <span id="testing-javascript"><b>Javascript</b></span>

    To test my Javascript code, I used the [JSHint Validator](https://jshint.com/)

<br>

* ### <span id="testing-pep8"><b>PEP8 Compliance</b></span>

    To test my PEP8 compliance, I used [PEP8 Online Check](http://pep8online.com).

<br>

* ### <span id="testing-lighthouse"><b>Overall Website Performance & Compatibility</b></span>

    To test my websites performance and compatibility, I used [Lighthouse](https://developers.google.com/web/tools/lighthouse)

<br>

* ### <span id="testing-responsive-design"><b>Responsive Design</b></span>

    In order to test the design on as many devices as possible, I came across a website called [Responsive Test Tool](http://responsivetesttool.com/)
    It enabled me to test my design on a large range of devices.

* ### <span id="testing-browser-compatibility"><b>Browser Compatibility</b></span>

    To test my site's compatibility, I found a website called [Browserling](https://www.browserling.com/)

    Using this tool I was able to test a range of browsers, some of which I wouldn't otherwise have access to.
    Unfortunately the site has a limited free version, and an upgrade to a premium plan would be required to access every device they offer, however I'm confident that the site is very compatible on the most popular browsers.

    <img src="" alt="chrome browser test" width="40%">
    <img src="" alt="firefox browser test" width="40%">
    <img src="" alt="internet explorer browser test" width="40%">
    <img src="" alt="opera browser test" width="40%">

* ### <span id="testing-links"><b>Link Testing</b></span>

     [Dead Link Checker](https://www.deadlinkchecker.com/)

    Here are the results from the [Dead Link Checker](https://www.deadlinkchecker.com/):

    <img src="" alt="Dead Link Reports" width="80%">

<br>

* ### <span id="testing-user-stories"><b>User Story Testing</b></span>


<br>

* ### <span id="testing-problems-during-development"><b>Problems During Development</b></span>

- When a user uploaded an image using a URL, the front end image would always appear as a broken image.
I belive this was because it was trying to refer to a generated URL that is created for an image that is uploaded.

To correct this issue, I created an ELIF statement within the IF function that was already written. 
The function would then check if an image had been uploaded, if not then check for a image URL and if neither had been uploaded then it would place a generic 'no image' placeholder for the project.

- I was receiving the following error everytime I was trying to edit a blog post:

"django.urls.exceptions.NoReverseMatch: Reverse for 'edit_product' with arguments '('',)' not found. 1 pattern(s) tried: ['products/edit/"  

After reading through my code in detail, I noticed I had forgotten to include the post.id within the form action.

<br>

* ### <span id="testing-bugs"><b>Known Bugs</b></span>

<br>

## <span id="deployment"><b>Deployment</b></span>

* ### <span id="deployment-heroku"><b>Deployment With Heroku</b></span>

   
* ### <span id="deployment-forking"><b>Forking</b></span>

    To fork this repository, you will need to carry out the following steps;

    - On [Github](https://www.github.com), navigate to the repository you wish to fork.

    - In the top right corner click <b>Fork</b>

        <img src="" alt="image showing the location of the fork button on Github" width="80%">

* ### <span id="deployment-cloning"><b>Cloning Project</b></span>

    In order to display the website with all its features, you will need to clone the repository to your GitHub account or locally. 

    Cloning will enable you to copy all of the site's files at that time, into your own working environment to apply any changes or test the site.

    - On GitHub, navigate to the repository location
    - On the right hand side of the page you will see a green button labelled 'Code'. Click This
    - A menu will appear with different ways of cloning the repository.

        <img src="" alt="Github website showing where to find the 'code' button." width="80%">

    <b>To Clone the repository By HTTPS</b>
    - From the previous step, click on the clipboard button (located after the address) under the 'HTTPS' tab.
    - Open terminal and change directory to the area you wish to load the repository into.
    - Once you're in the required directory, enter the command 'git clone' and paste the URL that you added to the clipboard in the previous step. - Press Enter

        <img src="" alt="Github website showing where to click to copy the address to the clipboard" width="80%">

    <b>To Clone the repository to GitHub Desktop</b>
    - Follow steps 1,2 and 3 above.
    - Click 'Open with GitHub Desktop
    - Follow the prompts within the GitHub Desktop popups to complete the clone.

        <img src="" alt="Github website showing where to click to open with Github Desktop" width="80%">

    <b>How to download a Zip file of the repository</b>
    - Follow steps 1,2 and 3 above.
    - Select the option 'Download Zip'

        <img src="" alt="Github website showing the Download Zip link." width="80%">

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Once you have cloned the repository, you will need to carry out these additional steps:
        a. Create an env.py file containing your own variables
        b. Create a MongoDB database and replicate the databases from <a href="#database">here</a>.
        c. Install all the packages listed within the requirements.txt file using the following command within your environment:

            pip install -r requirements.txt

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## <span id="credits"><b>Credits</b></span>

* ### <span id="credits-content"><b>Content</b></span>



* ### <span id="credits-media"><b>Media</b></span>

    *   No Image Icon - <a href="https://www.freeiconspng.com/img/23494">No Save Icon Format</a>


* ### <span id="credits-code"><b>Code</b></span>



* ### <span id="credits-acknowledgments"><b>Acknowledgements</b></span>

    - Thank you to everyone on Slack for help and advice
    - Thanks to all the tutors who have supported me during the project.
    - Thanks to Code Intitute for the walk through project which I used and referenced during the development.
    - Thank you to my mentor [Caleb Mbakwe](https://www.linkedin.com/in/calebmbakwe/) for his great guidance