# Student Management System

## Overview
The Student Management System is a web application designed to manage student data efficiently. It provides functionalities for adding, updating, and deleting student records, as well as viewing detailed information about each student.

## Features
- Add new students
- Update existing student information
- View detailed student profiles
- Search and filter student data

## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Python, Django
- **Database:** SQLite (default), can be configured to use other databases
- **Version Control:** GitHub

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com//student_management.git
    cd student_management
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:8000
    ```

## Usage
- Navigate to the homepage to view the list of students.
- Use the navigation bar to add new students or search for existing ones.
- Click on a student's name to view detailed information and perform update or delete operations.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
