# Search Based User Recommendation
Simple Application Implementing User recommendation based on their search on an ecommerce website.

# Description:
This Project contains 3 apps (User, Product, Recommendation). Product app contains all the product available on an ecommerce website, User app contains all the User registered on ecommerce website and Recommendation application contains the user making any search to the products available on the ecommerce website.

Whenever registered user makes any search on the products available on the website, his ID and the Productid he searched for product will be captured in Recommendation Model. In this App, Search results are captured, if any products contain search string (product size and product shape). If user types anything in the search bar and if that string is present in product size or in product shape those products will be displayed to user and these results will be captured in Recommendation table.

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
 
3) write py manage.py makemigration (it will generate t-SQL for  all the required database tables in the server)
C:\Users\BizAct-110\Desktop\Recommendation\recommend> py manage.py makemigrations

4) Type py manage.py migrate (it will run the sql generated in the above step. i.e it will create the tables in the database.)
 C:\Users\BizAct-110\Desktop\Recommendation\recommend> py manage.py migrate
 
5) You can also create useruser to see all the details in the admin panel.
C:\Users\BizAct-110\Desktop\Recommendation\recommend> py manage.py createsuperuser

6)  You can run ProductPopulate.py (to populate the Product database. In current setup it will populate 35000 Products into Products table. You can change this number)
C:\Users\BizAct-110\Desktop\Recommendation\recommend> py ProductPopulate.py

7) You can run UserPopulate.py (to populate User database. In current setup it will populate 5 User into Users table. You can change this number) 
C:\Users\BizAct-110\Desktop\Recommendation\recommend> py UserPopulate.py


8) type command py manage.py runserver
C:\Users\BizAct-110\Desktop\Recommendation\recommend> py manage.py runserver

# Results

## Product Dashboard showing  the Implementation of Insert, Update, Seach and Pagination 

![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/ProductDashboard.PNG)

## Product Insertion form:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/InsertProduct.PNG)

## Product Update form:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/UpdateProduct.PNG)

## User Dashboard:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/UserDashboard.PNG)

## User Insert Form:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/InsertUser.PNG)

## User Update Form:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/UpdateUser.PNG)

## User Recommendation Dashboard:-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/RecommendationDashboard.PNG)

## User Login :-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/Login.PNG)

## User Logout Redirection :-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/LogOutRedirection.PNG)

## User SignUp :-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/SignUpform.PNG)


## Registered Users :-
![Image Not Available](https://github.com/shivendra04/Recommend/blob/master/Result/RegisterdUers.PNG)



# Author:

Shivendra Verma

Shivajnv2011@gmail.com

BlogProject: http://djangoblog1.pythonanywhere.com/



