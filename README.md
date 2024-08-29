# bil2_django

**bil2_django** is a comprehensive web application built with Django, designed specifically for a car company. This project showcases a robust integration of backend and frontend technologies, including web scraping, Docker, and modern UI frameworks.

## Features

- **Django Backend:** Manages server-side logic, database interactions, and web scraping.
- **Web Scraping:** Automates data extraction from car-related websites.
- **Frontend:** Utilizes Bootstrap, custom CSS, and JavaScript for a responsive UI.
- **Docker:** Facilitates containerized deployment for seamless application scaling.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)

### Installation & Running

#### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t car .
   docker run -p 8080:80 -e ENV_VARIABLE=value car

### using Django server
* make virtual env. and activate it
* change working directory to where the `manage.py` file is 
* Install the requirments:`pip install requirments.txt`
* run project: `python manage.py runserver`

### Project Structure

* apps/: Contains Django applications managing different features.
* core/: Settings and configurations for the Django project.
* staticfiles/: Static assets like CSS, JavaScript, and images.
* Dockerfile: Docker image build instructions.
* docker-compose.yml: Docker Compose configuration for multi-container setups.
* nginx.conf: NGINX configuration for deploying the application.

### Screenshots
Here are some snapshots of the application:

- **Home Page**

<img width="1438" alt="image" src="https://github.com/user-attachments/assets/ed44cd31-12e3-445a-965e-956a60a5cf76">

<img width="1434" alt="image" src="https://github.com/user-attachments/assets/9353e730-c782-4892-9e08-d1824ff47e7e">

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/6c065ffc-08ac-48d7-a2a4-5706ac35034f">
<img width="1435" alt="image" src="https://github.com/user-attachments/assets/4c45aa70-887a-49c5-8773-b38fdfe4ab19">

<img width="1436" alt="image" src="https://github.com/user-attachments/assets/01e34630-a035-4e1a-b886-7dcda0ede7b3">

<img width="1437" alt="Screenshot 2024-08-29 at 13 27 08" src="https://github.com/user-attachments/assets/cb06e112-195d-47e4-9acf-468392f55091">

<img width="1437" alt="Screenshot 2024-08-29 at 13 28 13" src="https://github.com/user-attachments/assets/23ec4cef-18ce-4537-80d0-12c7154456c0">


- **Car Listings**
  * Buy car
    <img width="1439" alt="image" src="https://github.com/user-attachments/assets/64333e8a-88d3-4ee5-94c2-9e35dce322d5">

  * Sell car
    <img width="1439" alt="image" src="https://github.com/user-attachments/assets/37844a7b-92d3-4b99-a4da-3610139383d4">
    <img width="1440" alt="image" src="https://github.com/user-attachments/assets/49c7fb2f-d647-46a9-b073-98787947d014">

  * and more

