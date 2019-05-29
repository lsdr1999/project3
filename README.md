# Project 3

This project contains a website called "pizzaAPI".

Users are able to register and sign in (i.e. with username `pietzza` and password `1234`). When registered and logged in users are able to order food from the menu (pizza, pasta, salads, etcetera). Users can leave the page/log out and, when they return, find the order to still be present in their cart. They are also able to delete certain items from the cart (this is my personal touch, together with a more extensive styling of the website).
Admins are able to view all orders (sign in with username `admin` and password `adminadmin`).  
The website comes with next-level styling, with moving text and a 'pizza'-cursor. Have fun ordering food!

# Manual
Log in with an username and password if you already have an account. If this is not the case, register with your full name, emailadress, etcetera. When you have been registered you can log in.
When logged in you will be taken to the main page (index), here you will see a short overview of the food we have in stock. In the navbar select 'Menu' -> 'Full Menu' to get started. You will now be taken to the menu. If you already know what you want you can select a menu item from the dropdown list for instance 'Dinner Platters'. You are able to choose everything from the menu, add an item to your cart by selecting the price. You will then be taken to a new space where you can confirm you choice. If you selected a pizza with a certain amount of toppings don't forget to add them!
If you made your choice proceed to the checkout. Here you can, again, see an overview of your cart. Here it is also possible to remove items, if so: you will be taken to a new space where you can confirm you choice. When you are ready to checkout simply select checkout and your order will be placed. To view your order go to 'Order'. If you are done ordering, log out via 'Log out'.

As an admin you are able to view the new placed orders, log in with the right credentials and you will be taken to the main page (manage). Here you can view all orders that have been placed by customers. You can also view the menu and, if you are hungry, order a pizza for yourself (which you will probably need to make yourself... too bad...).

# Overview of all relevant files in the /orders folder:
## /static/orders/
This folder contains the following files:
- script.js (which contains the javascript that makes this project work as it should).
- styles.scss, styles.css (which make the project look whole lot better).

## /templates
This folder contains the following files:
- layout.html (the layout for all pages, i.e. for including the navbar, 'pizza'-cursor and background)
- login.html (login page).
- register.html (register page).
- index.html (the main page for users).
- manage.html (the main page for admins).
- menu.html (the full menu page).
- cart.html (the inbetween page where you must confirm any changes to the cart)
- order.html (the order page).

## admin.py and models.py
This is where all models are created and activated to create a database/dataset.

## urls.py
This is where all urls are created.

## views.py
This is the main python file, which consists of all the important python code to get everything working.

# Overview of all relevant files in the /project3 folder:
## requirements.txt
The required downloads are shown in this file.
