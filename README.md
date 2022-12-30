![ATU Logo](images/ATU_Logo.png)

# Data Representation

Author: Ruth Keady 

g00321445@atu.ie
***

## Overview
This repository contains my project submission for the Data Representation module 2022. As there was flexibility for this project I chose to create a webpage that contains an online digital portfolio (an interactive CV) where future techincal students can showcase their skillset to future employers. The idea behind this business idea is that the credentials within this application would be authenticated. This idea arose from a conversation with a friend who mentioned that within their working environment a situation arose where a team member was hired and within a few weeks it became obvious that this individual had falsified their CV or exagerated skillsets. I found out that this is not an uncommon issue, infact in a study 63% of people admitted to lieing on their CV. As this negatively imapcts teams, organisations, and takes opertunities away from people who have accredited skillsets, I thought to myself - how can this process be improved. At the moment this webpage is a concept, there is no code installed to validate the entries but I hope to take this further to do so. At present I believe the submission overs most of what was asked of this project. 

### Problem statement 
Description:
Write a program that demonstrates that you understand creating and consuming
RESTful APIs.

### Structure 
The purpose of this project is to demonstrate that I have achieved the learning outcomes of the module, which are:
- Create a basic Flask Server
- Rest API with ability to perform CRUD operations
- Create a Database with 2 tables
- Webpage  interface 

### DataBases:
1. Login to MySql on your local desktop
2. In a seperate terminal navigate to te downloaded files and run 'python databaseCreate.py'   
3. In the terminal with mySQL open Type Show Databases;>use datarepresentation;>show tables;. You should be able to see jobs and edcuation tables. Use the command 'Select * from <table>' to see the records within each table. 

## Table of Contents

- FOLDERS:
- DATABASE COMMANDS - python scripts to create and update the database content. 
- STATICPAGES - contains html web pages and image folder to support the web interface. 
- README - information on how to run the project. 
- Requirements - what needs to be installed to run the project. 
- SERVER.py - the python script used to start the server. 


## Requirements To Run This Project 
In order to run this project on your device please complete the following steps:
- Step 1. Within this repository select the green code button. From the dropdown select download ZIP at the bottom. Unzip the folder on your computer. 
- Step 2. Using your terminal, navigate to the location that the downloaded files were saved.Enter 'python server.py'. Suggest to run the project from a virtual environment. 

### Requirements

To run this project from your local device the following will need to be installed as prerequsites:
  -  Anaconda or a Python environment. [Python Installation Guide](https://docs.anaconda.com/anaconda/install/index.html)
  - Flask [Flask Installation Guide](https://flask.palletsprojects.com/en/2.0.x/installation/)
  - SQL database management system. (mySQL was used to create this project on a MAC OS) [MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)
  - The requirements.txt file contained within this repository. From the terminal enter: `pip install -r requirements.txt` in the repo directory.

Alternatively, if you do not wish to install all these packages and files to your local device you can run them in a virtual environment. While in the folder with the repo in your CLI, do the following:

1. Type `python3 -m venv venv` to create a virtual environment (VM).
2. Then `source venv/bin/activate` for MAC or `.\venv\Script\activate.bat` for Windows to open the environment.
3. Then `pip install -r requirements.txt` to install the necessary packages
4. Then enter `python server.py` or 'python3 server.py' depending on what python package you have installed to run the program. 

To exit the VM type deactivate.

## Run API
1. Once the commands above are entered a link to the url will be created : http://127.0.0.1:5000. Open the link and typr /home.html to open the home page. 
2. Navigate through the webpages. 

## Conclusion
I enjoyed this project, i think it works well however I fear I spent too much time on the webpages as opose to the API interface. I would like to have third party API interface and authentication however I coudld not find a use case for this within the piece of work. 

## Credits
1. Main source for webpage design - https://www.youtube.com/watch?v=oYRda7UtuhA&t=3458s
2. Lecture content
