# Expense Tracker App

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>

The purpose of this expense tracker application is to enables users to manage their personal finances by keeping record of their spending and viewing the information in a way that is helpful for decision-making.

This expense tracker app assists users to manage their day-to-day expenses, keep track of their total expenses and view expense overview summary of their expenses by different categories and views. Users can register to create an account and then login to get started with using the app.

In particular, once logged in, users can:

- Record expenses
- View a detailed list of all expense transactions
- View an overview summary of their expenses which include: total expenses incurred to date, expenses by category, expenses by month and expenses by day
  
## Installation <a name="installation"><a> 

There are two different ways to run the application: using Docker or a virtual environment.

Open your local Integrated Development Environment (IDE) such as VSCode.

On your IDE, open the terminal.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run -d -p 8000:8000 bonolor/expense-tracker-app
```

3. Open your web browser to view the expense tracker app, which can be done by entering "http://localhost:8000" or "http://127.0.0.1:8000/" on your browser.

Note: If you stop running the docker container following the "**Stop Running**" instructions below, the next time you would like to run the application again, you can enter the following command:

```
docker start <container id>
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run -d -p 8000:8000 bonolor/expense-tracker-app
```

4. Select the "8000" port link next to "Open Port".

**Stop Running**

To stop running the application both when using Docker Playground and Docker on your desktop, obtain the container id by running the following command:

```
docker ps -a
```

Stop running the container to stop running the app:

```
docker stop <container id>
```

### Virtual Environment

1. Download the folder in the repository named the following: TrackerProjectSite.
 
3. Move and save the downloaded folder to the desired parent directory location.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the TrackerProjectSite folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the TrackerProjectSite directory (if you are not already in the directory):
  
  ```
  cd TrackerProjectSite
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

   ```
  pip install --upgrade pip
  ```
  
 11. Once all packages are installed, add a file named _.env_ in the the parent TrackerProjectSite directory.

 12. Enter the following command in the terminal to generate a secret key:
 
 ```
 python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
 ```
 
 13. In the .env file created above, insert the key and debug mode in the file:
 
 SECRET_KEY=Key-generated-above  
 DEBUG=False  
  
  
 14. Make migrations:
 
  ```
 python manage.py migrate
  ```
 
 15. Enter the following command  to run the server and hence the expense tracker application:
  
  ```
  python manage.py runserver
  ```
  
  Open your web browser to view the expense tracker app, which can be done by entering "http://localhost:8000" or "http://127.0.0.1:8000/" on browser or following your preferred method for opening on browser based on your IDE.

  
## Usage <a name="usage"><a>
  
  ### Home
  
  Once you run the application successfully and open your web browser, the page will open to the following screen:
 
  <img width="700" alt="Screenshot 2023-05-02 at 19 53 59" src="https://user-images.githubusercontent.com/127111801/235745933-86a30cec-f87f-4a77-89fc-65f314961e15.png">
  
   ### Sign Up
  
  Create an account on the sign up page using any desired credentials per the field labels.
  
  The following are example credentials you can also use if this is your first time creating an account:
  
  **First Name:** *ProjectUser1*  
  **Email:** *projectuser1@gmailf.com*  
  **Username:** *ProjectUser1*  
  **Password:** *ShacjR97#*  
  **Confirm Password:** *ShacjR97#* 
  
  This displays as:
  
  <img width="700" alt="Screenshot 2023-05-02 at 20 09 01" src="https://user-images.githubusercontent.com/127111801/235751821-b644e0e1-27be-4252-8bef-3f2986eef6fc.png">

  Once you register, you will automatically log in and be directed to the following screen:
  
  <img width="700" alt="Screenshot 2023-05-02 at 20 09 51" src="https://user-images.githubusercontent.com/127111801/235752231-81bf0ec8-95b6-44ba-8059-d0b6f5f2a45b.png">

  ### Login
  
  If you log out after signing up, you can log in either using the credentials you created when you registered or using the following credentials:
  
   **Username:** _ProjectUser1_  
   **Password:** _ShacjR97#_  
  
 <img width="700" alt="Screenshot 2023-05-02 at 20 39 21" src="https://user-images.githubusercontent.com/127111801/235756105-64997ecf-dfa4-4001-bf56-14d4ddb37eab.png">
  
  ### Record Expense
  
  Record your expenses:
  
  <img width="700" alt="Screenshot 2023-05-02 at 20 12 08" src="https://user-images.githubusercontent.com/127111801/235750214-b19976d9-f691-4d6f-a1ef-20f353163d78.png">

  ### Expense Detail
  
  View a detailed list of all the expense transactions to date:
  
  <img width="700" alt="Screenshot 2023-05-02 at 20 13 26" src="https://user-images.githubusercontent.com/127111801/235750512-a2a63ce2-9b1e-4c4d-ab91-417a55a7a34b.png">

  ### Expense Overview
  
  View an overview summary of your expenses:
  
  <img width="700" alt="Screenshot 2023-05-02 at 20 16 01" src="https://user-images.githubusercontent.com/127111801/235750941-ffd03d01-363d-44c9-afa7-7e3b6efb761a.png">
  
   ### Logout
   
   
   <img width="700" alt="Screenshot 2023-05-02 at 22 36 59" src="https://user-images.githubusercontent.com/127111801/235780598-5815bddf-027f-4925-94f6-5c85deebf5f0.png">
   
  
## Credit and Contribution <a name="credit_and_contribution"><a> 

This project has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.

  
  
