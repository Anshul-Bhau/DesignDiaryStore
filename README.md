# DesignDiary

Welcome to **DesignDiary**, a personal store website store for handmade accessories and crochet collections. This project is built using Django for the backend and utilizes a MySQL database for data management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Django Backend**: Robust backend built with Django framework.
- **MySQL Database**: Data management with MySQL for storing information of different articles.
- **Responsive Design**: Mobile-friendly interface that adapts to different screen sizes for better user experience.
- **Admin Panel**: Easy-to-use admin panel for managing articles, categories, and user interactions.


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/rudee-Sb/designdiary.git
    cd designdiary
    ```

2. Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
   - Create a new database in MySQL.
   - Update the `DATABASES` setting in `settings.py` with your database credentials.

5. Run migrations:
    ```
    python manage.py migrate
    ```

6. Create a superuser (for accessing the admin panel):
    ```
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000` to view the website.

## Usage

Once the server is running, you can interact with the website as a user or access the admin panel at `http://127.0.0.1:8000/admin` using the superuser credentials created earlier.

## Admin Panel

The admin panel allows you to manage articles, categories, and user interactions effectively. You can add new products, edit existing ones, or remove items from your inventory.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under a custom license. Please refer to the [LICENSE](LICENSE) file in this repository for details on how you may use this project.

---

### Contributors
- [Anshul Bhau](https://github.com/Anshul-Bhau)
- [Rudra Bhau](https://github.com/rudee-Sb)
