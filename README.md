# Phase 3 Project - Library Book Search and Request

## About

This CLI program mimcs some of the features of a library system. It allows users 
to create a library account and search for a directory of 2000 books. Users can
request the book from the search results, delete their book requests, and 
update their personal info.

***

## How to install

1. clone this repository
2. open the program
3. run `pipenv install` and then `pipenv shell`
4. cd into the directory `cd lib/db`
5. run `cli.py`
   

## How to use
The initial menu will have the option to sign up or login to an existing account.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/ee9b09fd-8db8-4b12-a6bb-ab4861163248)

Existing patron information can be found in the `library.db`. 

![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/a739ca4d-3c09-4688-94e9-101c48d7691a)

Enter the library card number and the last 4 digits of the phone number to enter.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/a6e92c58-6b82-45c6-b164-015afba93812)

In the main menu, the library patron have 3 choices: search books, update info, and view books requests.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/a9bde1d4-1ebb-4d3a-946b-4228c30985e0)


### SEARCH

Patron will have the option from the list of 2000 books from either: title, genre, author name, or ISBN-10.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/fae9016f-76e9-4783-8c3c-d5063170ad31)

The program will list all the search results.

![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/18056800-ad22-4301-8764-dafd669a227f)

Selecting the book will show the book's information and have the option to request the book.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/46d9e033-2692-400e-ab04-bc412b7b03d3)



### VIEW REQUESTS

This option will be available if the patron has books requested. The menu will show a list of books requested.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/9eb40f4c-08ca-430e-9bcb-ae7dd443c54d)

Patron can choose from one of the books in the list. Here the patron can see the book information and
provides option to delete the request.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/d1dc4c42-799f-43ee-9024-48cb24f240f0)



### UPDATE INFO

The library patron will choose from the three options to update: first name, last name, or phone number.
![image](https://github.com/wwlwong/p3-cli-project/assets/102167991/3cddbab6-eeae-49a7-9544-19f1addb45e0)





## Resources

- books dataset were obtained from this kaggle dataset
  https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata
   
