# Manual Testing

[Main README.md](README.md)


## Epic 1 - Core Functionality 

### User Stories

* [Easy navigation of site](https://github.com/RebeccaKen/Restaurant-site/issues/12): As a user I can easily navigate through the website so that I can find the content I need.

* [Important information on home page](https://github.com/RebeccaKen/Restaurant-site/issues/10): As a user, I can see important information about the diner on the website's home page so that I don’t have to search the website for that information.

* [Visible navigation bar and fixed footer](https://github.com/RebeccaKen/Restaurant-site/issues/13): As a user I can find a navigation bar and footer so that I can see what content there is on the website.

The homepage instantly provides the user with all information need to be able to navigate through the website & understand the ethos of the restaurant.

The navbar is easy to use and it is clear to the user which page they are currently on.

The footer is fixed and provides opening times and the restaurant's social media icons. 

- Navbar: 
  
![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302827/Navbar_z2dc0r.png)

- Footer:
![](https://res.cloudinary.com/djbdldshh/image/upload/v1682384869/footer.png_jvabvp.png)

* [Submit contact form](https://github.com/RebeccaKen/Restaurant-site/issues/14): As a user I can send a contact form to the restaurant so that I can receive additional information.

Upon submitting the contact form, a message stating: "Thank you for your Feedback" appears, to confirm the submission of the contact form. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302816/Feedback_form_d4fube.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302818/Feedback-thank-you_mldxal.png)


## Epic 2 - Reservations functionality 

* [Make a reservation request](https://github.com/RebeccaKen/Restaurant-site/issues/3): As a user, I want to be able to make a reservation request for a table for a specific date/time so that I will know if I have a table when I arrive.

* [Reservation party number](https://github.com/RebeccaKen/Restaurant-site/issues/4): As a user, I want to be able to select the number of people in my party when booking so that I know there will be an available room at the table for all my party’s members.

* [Reservation confirmation](https://github.com/RebeccaKen/Restaurant-site/issues/2): As a user, I want to see a notification on the page so that I know my reservation is submitted.

* [Customer can edit/delete reservation](https://github.com/RebeccaKen/Restaurant-site/issues/6): As a user, I can log in and I can edit/delete an existing reservation request so that I can make changes online if my plans change.

From the reservations page, a authenticated user can add their details, (name, phone number, email, date, time, number of guests and notes) and submit the form, a message will appear that states: 'Thank you for your reservation' that confirms the reservation has been submitted. 

The authenicated user can also edit & delete their reservation. Once they have edited or deleted their reservation, they are taken to the 'reservations page' to view their edited reservation or see that their reservation has been deleted. The authenicated user can only see their own reservations, for security purposes. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1683043702/Screenshot_2023-05-02_at_17-07-55_Mr._D_z_Route_66_Diner_ohvqi6.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1683043787/Screenshot_2023-05-02_at_17-09-21_Mr._D_z_Route_66_Diner_dygcha.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302830/Reservation-delete_vvlkrz.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302833/Reservation-list_t6ng0y.png)

## Epic 3 - Authenticated User Experience

* [Clear Login status](https://github.com/RebeccaKen/Restaurant-site/issues/9):As a user, I can see a clear visual indication of my login status so that I can choose to be logged in or out. 

* [Customer can register an account](https://github.com/RebeccaKen/Restaurant-site/issues/8): As a user, I want to register for an account so that I can have my information saved and manage my reservations.

A authenicated user can see their log in status on the right side of the menu. The menu will show links for pages that only authorised users can visit & use, they are: 'My Reservations' & 'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'. This change in the navigation bar ensures users are directed to pages they can use and also prompts the user to sign up for an account. Furthermore, it makes it clear what the logged-in status is to the user.

When the user have logged in, a message appears under the navigation bar that states: 'Successfully signed in as *name*'. This also gives the user a clear indication of their login status. The user also have the option to logout. When a user has logged out, the navigation bar reverts to show the options 'Register' or 'Login'. A message will also appear that states: 'You are now signed out'.

When an unauthorised user would like to sign up to have an account, they can click on the 'Register' page. The page presents three field that must be filled, they are: 'Name', 'Password' and 'Password (again)'. The 'Email' field is optional. Once a the user has signed up, a message will appear below the naviagtion bar on the homepage that states: 'Successfully signed in as *name*'. The navigation bar will also reflect their new status. The user will now see 'My Reservations' & 'Logout' in the right-hand size of the navigation bar. 


![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302835/Reservation-sign-in_uxrpr5.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682303793/sign-up_otztff.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302837/Sign-out_mnszdy.png)

## Epic 4 - Menus can be viewed

* [Menu can be viewed](https://github.com/RebeccaKen/Restaurant-site/issues/1): As a user, I can browse the restaurants' menu so I can decide what to order. 

Any user, authenicated or not, can view the menus under the 'Menu' heading. The menus page features all the restaurant's menus along with a image for each one. The menu items feature a title, description, price and a list of allergens. 

![](https://res.cloudinary.com/djbdldshh/image/upload/v1682302825/Menu_ojvjab.png)


## Epic 5 - Superuser Access 

* [Superuser can access backend](https://github.com/RebeccaKen/Restaurant-site/issues/15)

* [Superuser can use all CRUD functionality on menu](https://github.com/RebeccaKen/Restaurant-site/issues/16)

Using a specified login the site owner can access the admin backend

![](https://res.cloudinary.com/djbdldshh/image/upload/v1683046758/Screenshot_2023-05-02_at_17-56-16_Site_administration_Django_site_admin_d3knpb.png)

Once in this admin backend, the superuser is able to access the menu items model, add new items or edit/delete existing one.

![](https://res.cloudinary.com/djbdldshh/image/upload/v1683046911/Screenshot_2023-05-02_at_18-00-07_Select_menu_item_to_change_Django_site_admin_mimdxm.png)

![](https://res.cloudinary.com/djbdldshh/image/upload/v1683046989/Screenshot_2023-05-02_at_18-02-27_Sausage_fries_Change_menu_item_Django_site_admin_wuj6zm.png)