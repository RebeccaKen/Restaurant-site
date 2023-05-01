# Mr D'z Route 66 Diner

![Image of deployed website](https://res.cloudinary.com/djbdldshh/image/upload/v1682384287/Am_I_Responsive_lkiian.png)

[Link to live website](https://restaurant-site-app.herokuapp.com/)

This is a full stack project created with Django, Python, Bootstrap, JavaScript, Html and CSS. This website was constructed to act as a website for the fictional Diner style restaurant ‘Mr D’z Route 66 Diner’. This website allows guests to make reservations & view the menu online.  

## User Experience (UX)

### Planning

The development of ideas for this website grew with UX principles in mind. I began to think about strategy and the demographic that would make up the patrons visiting the website. I planned the implantation of features that would best suit the demographic. 

Given that ‘Mr D’z Route 66 Diner’ is located along route 66, the vast majority of the diner’s patrons would be travelling so it is assumed that they will be visiting the website via their mobile phones. Creating a website that should be responsive and clearly visible on mobile screens was critical to the success of the website. 

### Demographic 

- Family groups
- Solo travellers
- Frequent customers (truckers, travelling sales people, etc...)
- Travellers using route 66 
- Customers who enjoy fast, convenient food

### What users will expect:

- A menu that is has descriptions of the food available and specifies any allergens
- An informative website that is simple to navigate 
- A reservation system so they can request a table
- A system that allows customers to manage their booking
- A contact form to contact the diner staff

### User Stories 

1. As a superuser, I can create, remove, update or delete menu items from the database so that I can ensure the menu items are accurate and that the menu is fully up-to-date.
2. As a superuser I can log in so that I can and access the backend of the website.
3. As a user I can send a contact form to the restaurant so that I can receive additional information.
4. As a user I can find a navigation bar and footer so that I can see what content there is on the website.
5. As a user I can easily navigate through the website so that I can find the content I need.
6. As a user I want to see icons for the restaurant's social media pages so that I can follow the diner on different platforms.
7. As a user, I can see important information about the diner on the website's home page so that I don’t have to search the website for that information.
8. As a user, I can see a clear visual indication of my login status so that I can choose to be logged in or out.
9. As a user, I want to register for an account so that I can have my information saved and manage my reservations.
10. As a user, I can log in and I can edit/delete an existing reservation request so that I can make changes online if my plans change.
11. As a user, I want to be able to select the number of people in my party when booking so that I know there will be an available room at the table for all my party’s members.
12. As a user, I want to be able to make a reservation request for a table for a specific date/time so that I will know if I have a table when I arrive.
13. As a user, I want to receive see a notification confirming my reservation has been submitted so that I know my reservation has been submitted. 
14. As a user, I can browse the restaurants' menu so I can decide what to order.

## Scope

In order to achieve the desired user & business goals, the following features will be included in this release:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with brief information about the restaurant.
- Menus page with descriptions, pricing and alergens listed.
- Reservations page, with a booking form that sends to the restaurant admin. 
- Manage reservations page, where logged-in users can edit/delete existing reservations they have.
- Update details page, for logged in users to update their details which in turn updates the customer model.
- Register/login feature using Django allauth


## Databases 

The Menus, Reservations and feedback apps require databases to store information so I have built 5 custom models.

### Menus

Menu & MenuItem are the model names for the menus app, these are two standalone models that provide all of the information required to display the items as part of the restaurant's menu. Each item has a name, description, price & allergens.

### Reservation

There are 2 models in this app, Customer & Reservation. The combination of these models allow for customer details to be stored, reservation enquiries to be made & managed.For each reservation, there will be a customer assigned to it. The customer is assigned during the enquiry process. This works for users that are logged in. 


### Feedback

The Feedback model allows customer, who and both logged in and not logged in, to send feedback to the admin where it is stored in a database. Each Feedback form requires a customers name or it cannot be submitted. A feedback form has a name, email, comments section and a rating dropdown menu. 
    

## Wireframes

Please note the actual website differs slightly from the original wireframes.

[Wireframes](Wireframes.md)

## Testing
[Testing](testing.md)

### Colour palette 

The colour palette I chose for this website is fun, electric and reflects the energetic atmosphere at Mr. D'z Route 66 Diner. I wanted the user to get the impression from the website that Mr.D'z Route 66 Diner was a lively establishment, so I choose a colour palette that both compliments and clashes in equal turns. The pastel pink as a background colour works nicely to give the website a fresh colour wash without over-powering any of the images, fonts or features on the website. I choose a bright red for the submit buttons to clash with that pastel pink without sacrificing the buttons' visibility. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682294209/Coolers_Palette_nw9nhn.jpg)

### Logo

I created a logo to enhance the branding of the diner. I created the logo using Canva. I have added a navy blue background to the image of the logo below so the first line ('Mr.D'z') would be visiable. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682294312/Navy_Blue_Pink_Text_Logo_wqowsz.jpg)

I added the logo to the main image of the homepage, so that it would be clear to the user without over-powering the main image. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302985/Screenshot_2023-04-24_at_03-22-26_Mr._D_z_Route_66_Diner_xoekj5.png)

## Features

### Home Icon

I wanted to create a small icon that would act as a clickable button that would bring the user back to the 'Home' page of the site. I used Canva to create the icon. I choose to use an illustration of a hamburger as the hamburger is an iconic food often associated with diner, it also acts as a nod to the nav bar, which collapses on mobile screens to a hamburger icon. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302579/Artistic_Textured_Ink_Brush_Stroke_Brand_Logo_bkneln.png)

### Navigation Bar

The navigation bar has links to all the active pages for the user and are clearly labelled. If the user is logged in then the right side of the menu shows links for pages that only authorised users can visit & use, they are: 'My Reservations' & 'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'. This change in the navigation bar ensures users are directed to pages they can use and also prompting the user to sign up for an account. Furthermore, it makes it clear what the logged-in status is to the user.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302767/Screenshot_2023-04-24_at_03-18-58_Mr._D_z_Route_66_Diner_ivic6h.png)

The navigation bar is fully responsive and collapses on mobile screens to a hamburger icon, this easily allows the user to continue to use the navigation links without the need to press back on the browser.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302814/Dropdown_menu_zo0mp0.png)

### Main image

This main image of the website is an exterior image of Mr.D'z Route 66 Diner with the logo embedded in it. The main image is featured on the homepage of the website so the user can see the exterior of the restaurant straight away when they visit the site. This will allow the user to know what the restaurant looks like, which would be of benefit as the customer base are travelling down Route 66 and will need to know what the restaurant looks like in order to find it. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302823/Main-with-logo_wwo02c.png)

### About Us 

The about us section of the homepage gives the website user a brief history of Mr.D'z Route 66 Diner, a summary of the Restaurant ethos and corresponding image. This section in fully responsive and when viewed on mobile screen, the about us section will stack on top of the image. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682384582/About-us_section_x7i6mm.png)


### Footer 

The footer displays some of the restaurants key information and has links to social accounts. It is split into two sections, the opening times ('Open 24/7') and the social media icons beneath. 


![](https://res.cloudinary.com/djbdldshh/image/upload/v1682384869/footer.png_jvabvp.png)


### Contact Us 

All users are able to submit a contact form from the 'Contact' page, this sends the form to the admin side of the site where the admin can view the feedback. Having a way to communicate with the website owner/restaurant manager is a helpful tool for the user and helps the rastaurant to learn from the customer's experience and improve their service accordingly.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302816/Feedback_form_d4fube.png)

When the user submits a feedback form, a red 'thank you' message appears. This allows the user to know that their form has been submitted and their feedback is appreciated. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302818/Feedback-thank-you_mldxal.png)

### Menu 

The menus page features all the restaurant's menus along with a image for each one. The menu items feature a title, description, price and a list of allergens. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302825/Menu_ojvjab.png)

### Reservations 

### Sign in 

In order to make a reservation, the user is directed to sign-in to their account. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302835/Reservation-sign-in_uxrpr5.png)

### Reservation form 

Once they have signed in, the user gains access to a reservatioon form that allows them to submit their name, email, phone number, reservation time, reservation date and the number of guests in their party. The user can also fill in the notes area to specify any special requests i.e. 'We will need a high-chair'. The name, phone number and email fields are also required fields, so a reservation cannot be submitted without them. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302829/Reservation-_create_krlmsc.png)

### Reservation list 

When the user has submitted their reservtaion form, they are taken to the 'My Reservations' page. This page allows the user to view all their current reservations. This page can also be accessed by a logged-in user when they access the 'My Reservations' heading in the navigation bar. The reservations on the 'My Reservations' page has two violet buttons: 'Edit' & 'Delete'. When the user's mouse hovers over the buttons, they turn red. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302833/Reservation-list_t6ng0y.png)

### Reservation Edit 

When the user clicks into the 'Edit' button on the 'My Reservation' page, they are presented with their current reservation in a form. There, the user can edit their reservation and submit the changes. Once the edited reservation has been submitted, the user is brought back to the homepage. A green message appears at the top of the page stating 'Your reservation has been edited!' so the user understands their edited reservation is submitted. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302831/Reservation-edit_lc2hhw.png)

### Reservation Delete 

When a user clicks on the 'Delete' button, they are presented with a question 'Are you sure you want to delete this reservation?' and two buttons, 'Delete' & 'Confirm'. If the user clicks 'Cancel' they will be brought back to the 'My Reservations' page where they will be able to see their reservation is not deleted. If they click 'Delete' they will be taken to the 'My Reservations' page where they can see that their reservation has been removed from the page. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302830/Reservation-delete_vvlkrz.png)

### Login 

The sign in page is located under the heading 'Login'. This page allows the user to sign in to their account by filling in the 'Username' & 'Password' fields. There is also a 'Remember me' button so the user can save their 'Username' & 'Password' for their convenience. When the user have logged in, a message appears under the navigation bar that states: 'Successfully signed in as *name*'. When the user is logged in, the right side of the menu shows links for pages that only authorised users can visit & use, they are: 'My Reservations' & 'Logout'. Both the message and the changes in the navigation page give the user a clear indication of their login status. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302835/Reservation-sign-in_uxrpr5.png)

### Logout 

The sign out page is located under the heading 'Logout'. When the user clicks the 'Logout' heading, they are taken to a page that states: 'Are you sure you want to sign out?' When the user clicks 'Sign out' they are taken back to the homepage, where the user will see a message appear beneath the navigation bar that states: 'You are now signed out'. The navigation bar will also revert to it's original, non-signed in state. The right side of the menu shows links for pages that unauthorised users can visit & use, they are: 'Reservations', 'Register' and 'Login'. Both the message and the changes in the navigation page give the user a clear indication of their login status. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302837/Sign-out_mnszdy.png)

### Register

When an unauthorised user would like to sign up to have an account, and book reservations, they can click on the 'Register' page. The page presents three field that must be filled, they are: 'Name', 'Password' and 'Password (again)'. The 'Email' field is optional. Once a the user has signed up, a message will appear below the naviagtion bar on the homepage that states: 'Successfully signed in as *name*'. The navigation bar will also reflect their new status. The user will now see 'My Reservations' & 'Logout' in the right-hand size of the navigation bar. 
![](https://res.cloudinary.com/djbdldshh/image/upload/v1682303793/sign-up_otztff.png)


## Deployment


The master branch of this repository has been used for the deployed version of this application.
Using Github & Gitpod

To deploy my Django application, I had to use the Code Institute Python Essentials Template.

- Click the Use This Template button.
- Add a repository name and brief description.
- Click the Create Repository from Template to create your repository.
- To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one.       
- Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    -git add .: adds all modified files to a staging area
    -git commit -m "A message explaining your commit": commits all changes to a local repository.
    git push: pushes all your committed changes to your Github repository.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial and Django Blog cheatsheat

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed. A Procfile is also required that specifies the commands that are executed by the app on startup.

- Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
- Click the New dropdown and select Create New App.
- Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
- Select the region you are working in.

### Heroku Settings You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

- In the Settings tab, click on Reveal Config Vars and set the following variables:
        SECRET_KEY - to be set to your chosen key
        CLOUDINARY_URL - to be set to your Cloudinary API environment variable
- In the resources tab you must install 'Heroku Postgres'

### Heroku Deployment In the Deploy tab:

-Connect your Heroku account to your Github Repository following these steps:
        Click on the Deploy tab and choose Github-Connect to Github.
        Enter the GitHub repository name and click on Search.
        Choose the correct repository for your application and click on Connect.
    
- You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
- Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should see the below View button, click this to open your application.



### Technology Used 


- Bootstrap
- Django
- Python
- Cloudinary
- Font Awesome
- Google Dev Tools
- Github
- Gitpod 
- Grammerly
- png2jpg
- Heroku
- PostgreSQL
- Canva
  

### Credits 

- Unsplash 
- Am I Responsive?

### Testing 

I have used a combination of manual and automated testing to ensure the website's functionality meets the desired intent.

### Code Validation

All of my code has been validated using an online validator specific to the language, all code now passes with zero errors.


* W3C CSS Validation Service - Used to validate all CSS code written and used in this webpage.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682975449/Screenshot_2023-05-01_at_17-30-00_W3C_CSS_Validator_results_for_TextArea_CSS_level_3_SVG_kzvyoj.png)


* JSHint - Used to validate JS code


* CI PYTHON LINTER - Used to validate Python code 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682975447/Screenshot_2023-04-28_at_18-50-17_CI_Python_Linter_o42ahe.png)

* SYNK - Used to test code security 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682975445/Screenshot_2023-05-01_at_17-27-58_Python_Code_Checker_Powered_By_Snyk_Code_Snyk_u0ymn7.png)

* WAVE - Used to test the accessibility of the website.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682977938/Screenshot_2023-05-01_at_22-51-56_WAVE_Report_of_Mr._D_z_Route_66_Diner_od347d.png)

