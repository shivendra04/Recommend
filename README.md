# Search Based User Recommendation
Simple Application Implementing User recommendation based on their search on an ecommerce website.

# Description:
This Project contains 3 apps (User, Product, Recommendation). Product app contains all the product available on an ecommerce website, User app contains all the User registered on ecommerce website and Recommendation application contains the user making any search to the products available on the ecommerce website.

Whenever registered user makes any search on the products available on the website, his ID and the Productid he searched for product will be captured in Recommendation Model. In this App, Search results are captured, if any products contain search string (product size and product shape). If user types anything in the search bar and if that string is present in product size of in product shape those products will be displayed to user.

This project also implements Update, Insert, Create User and Products in the Database. Which means Product details can be altered once it inserted in the database and same for user as well.

Currently recommendation App is populating based on the Registered users, not from the User App which I created. When we view user’s data, is not the one who are registered user but added randomly from UserPopulate.py file. We can Add new users and modify existing user also. Still need to link the registered user with the user dashboard.

Pagination is also implemented in product dashboard to show only 15 products in 1 page.
This project can be used to recommend product to user on the same website or any other website bases on his search history captured in Recommendation model.

# Getting Started:
## Dependencies:-
Django 3.0.6

Python 3.8.0

MySql 8.0.11

Windows 10 (created on windows 10)

Active Internet connection to load bootstrap used in the templates.

## Installing:-
1) git clone https://github.com/shivendra04/Recommend.git
2) Change the connection used in the project in the setting.py to your connection or use default Inbuilt Database (SQLite3) provided by Django
## Executing Program:-
1) Create the database in your system and change the connection details in the settings.py or uncomment the default the setting and comment out the current database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'userrecommend',
        'HOST':'localhost',
        'POST':'3306',
        'USER':'root',
        'PASSWORD':'root',
    }
}

2) Open command prompt and navigate to Recommend\recommend>
 C:\Users\BizAct-110\Desktop\Recommendation\recommend>


