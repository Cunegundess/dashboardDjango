<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Summary</summary>
  <ol>
    <li>
      <a href="#About-the-Project">About the Project</a>
        <ul>
          <li><a href="#Installation">Installation</a></li>
          <li><a href="#Configuration">Configuration</a></li>
          <li><a href="#Features">Features</a></li>
          <li><a href="#Technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#Contact">Contact</a></li>
  </ol>
</details>
</br>

<!-- Sobre o Projeto -->

<a id="About-the-Project"></a>
# About the Project

</br>

dashboardDjango is a web application built with Django that provides a dashboard for data visualization and management. It allows users to create, manage multiple dashboard and visualize data in a user-friendly manner.

</br>

<a id="Installation"></a>
## Installation
- - -

To install and run this project, follow these steps:

1.  Clone the repository:
   
    `git clone https://github.com/Cunegundess/dashboardDjango.git`
   
2.  Navigate to the project directory:

    `cd dashboardDjango`

3.  Create a virtual environment:

    `python -m venv venv`

4.  Activate the virtual enviroment:

    - For Windows:
    
      `venv/Scripts/activate`

    - For macOS/Linux:
    
      `source venv/bin/activate`

5.  Install the dependencies:

    `pip install -r requirements.txt`

6.  Set up the database:
    
    `python manage.py migrate`

7.  Start the development server:
   
    `python manage.py runserver`

8.  Open your web browser and visit http://localhost:8000 to access the application.

</br>

<a id="Configuration"></a>
## Configuration
-----
The application comes with a default configuration, but you may need to customize it based on your needs. Here are the main configuration files:

- settings.py: Contains the general settings for the Django project, such as database configuration and secret key.
- dashboardDjango/settings.py: Contains the application-specific settings, such as widget types and data sources.
- dashboardDjango/urls.py: Handles the URL routing for the application.

Make sure to review these files and modify them accordingly before deploying the project to a production environment.

</br>

<a id="Features"></a>
## Features
--------
- User Authentication: User registration and login functionality.
- Dashboard Creation: Users can create multiple dashboards.
- Data Visualization: Data visualization for effective representation.
- Responsive Design: The application is responsive and works well on different devices.

</br>

<a id="Technologies"></a>
# Technologies

dashboardDjango makes use of several open-source libraries and frameworks, including:

- ![Django](https://img.shields.io/badge/Django-3.2-green?style=for-the-badge&logo=django&logoColor=white)

- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple?style=for-the-badge&logo=bootstrap&logoColor=white)

- ![jQuery](https://img.shields.io/badge/jQuery-3.x-blue?style=for-the-badge&logo=jquery&logoColor=white)
  
We would like to express our gratitude to the developers of these fantastic tools and the open-source community for their contributions.

</br>

<a id="Contact"></a>
# Contact

Lucas Cunegundes - [LinkedIn](https://www.linkedin.com/in/lucas-cunegundes) - lucascsantana6@gmail.com