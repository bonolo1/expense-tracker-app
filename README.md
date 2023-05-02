# Expense Tracker App

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>

This expense tracker app assists users to manage their day-to-day expenses, keep track of their total expenses and view expense overview summary of their expenses by different categories and views. Users can register to create an account and then login to get started with using the app.

In particular, once logged in, users can:

- Record expenses
- View a detailed list of all expense transactions
- View an overview summary of their expenses which include: total expenses incurred to date, expenses by category, expenses by month and expenses by day
  
## Installation <a name="installation"><a> 

There are two different ways to run the applications: using Docker or a virtual environment.

1. Open your local Integrated Development Environment (IDE) such as VSCode
2. On your IDE, open the terminal.

### Docker

You can either use docker on your desktop or using Docker Playground. Descriptions for using both options are included.

**Run using Desktop**

If don't already have Docker installed on your desktop

Install Docker on your desktop


1. Enter the following command in the terminal to run the app's container on Docker hub:

**Run using Docker Playground**

Go to docker playground and enter "Start" at the following link: https://labs.play-with-docker.com/

In the terminal, enter the following

```
docker run -d -p 8000:8000 bonolor/expense-tracker-app
```

Select the "8000" port link next to "Open Port".

**Stop Running**

To stop running, obtain the container id:

```
docker ps -a
```

Stop running the container

```
docker stop <container id>
```


2. Open your browser and enter either


### Virtual Environment

1. Download the folder in the repository named the following: TrackerProjectSite.
 
3. Move and save the downloaded folder to the desired parent directory location.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the TrackerProjectSite folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal:
   
  ```
  python -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the TrackerProjectSite directory:
  
  ```
  cd TrackerProjectSite
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. Once all packages are installed, enter the following command to run the server and hence the expense tracker application:
  
  ```
  python manage.py runserver
  ```
  
  Open your web browser to view the expense tracker app, which can be done by entering "http://localhost:8000" or "http://127.0.0.1:8000/" on browser or following your preferred method for opening on browser based on your IDE.

  
## Usage <a name="usage"><a>
  
## Credit and Contribution <a name="credit_and_contribution"><a> 

This project has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.

  
  
