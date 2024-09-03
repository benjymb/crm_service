<a id="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">CRM Service</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#set-up-and-usage">Set-up and usage</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a project made for the Agile Monkeys recruitment process.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![DjangoRF][DjangoRF]][DjangoRF-url]
* [![DjangoOAuthToolkit][Django-OAuthToolkit]][DjangoOAuthToolkit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This app requires:  
* python and pip
* Linux or Mac

### Set-up and usage

1. Clone the repo
   ```sh
   git clone https://github.com/benjymb/crm_service.git
   ```
2. Create a new virtual environment called venv
   ```sh
   python3 -m venv venv 
   ```
4. Install dependencies
   ```sh
   . venv/bin/activate
   pip install -r requirements.txt
   ```
5. Create database 
   ```sh
   python manage.py migrate
   ```
6. Run app
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/benjymb

[Python]: https://img.shields.io/badge/Python-3.10-35495E?style=for-the-badge&logo=python&logoColor=4FC08D
[Python-url]: https://python.org/
[Django]: https://img.shields.io/badge/Django-5.1-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[Django-url]: https://django.org/
[DjangoRF]: https://img.shields.io/badge/Django&Rest&Framework-3.15.2-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[DjangoRF-url]: https://www.django-rest-framework.org/
[DjangoOAuthToolkit]: https://img.shields.io/badge/Django&Rest&Framework-3.15.2-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[DjangoOAuthToolkit-url]: https://github.com/jazzband/django-oauth-toolkit

