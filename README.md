# Log-Analysis

### Project Overview
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  
#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database.
  
  3. Create view article_view using:
  ```
    create view article_view as select title,author,count(*) as views from articles,log where 
    log.path like concat('%',articles.slug) group by articles.title,articles.author 
    order by views desc;
  ```
  | Column  | Type    |
  | :-------| :-------|
  | title   | text    |
  | author  | text    |
  | views   | Integer |
  
  4. Create vier error_log_view using:
  ```
    create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
    then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
    order by "Percent Error" desc;
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | date          | date    |
  | Percent Error | float   |
  
#### Running the queries:
  1. From the vagrant directory inside the virtual machine,run logs.py using:
  ```
    $ python3 logs.py
  ```
  
#### FAQ's: [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/b2ff9cba-210e-463e-9321-2605f65491a9)
