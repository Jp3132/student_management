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
    git clone https://github.com/Jp3132/student_management.git
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

## Challenges Encountered
- **Database Integration:** Initially faced issues with database migrations. Solved by ensuring all models were correctly defined and running `makemigrations` before `migrate`.
- **User Authentication:** Implementing secure user authentication was challenging. Used Django's built-in authentication system to streamline the process.
- **Responsive Design:** Ensuring the application was mobile-friendly required extensive CSS adjustments and testing across different devices.

## Feature Implementation
- **Add New Students:**
    - **Code Snippet:**
        ```python
        def add_student(request):
            if request.method == 'POST':
                form = StudentForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('student_list')
            else:
                form = StudentForm()
            return render(request, 'add_student.html', {'form': form})
        ```
    

- **Update Student Information:**
    - **Code Snippet:**
        ```python
        def update_student(request, pk):
            student = get_object_or_404(Student, pk=pk)
            if request.method == 'POST':
                form = StudentForm(request.POST, instance=student)
                if form.is_valid():
                    form.save()
                    return redirect('student_detail', pk=student.pk)
            else:
                form = StudentForm(instance=student)
            return render(request, 'update_student.html', {'form': form})
        ```
    

- **View Detailed Student Profiles:**
    - **Code Snippet:**
        ```python
        def student_detail(request, pk):
            student = get_object_or_404(Student, pk=pk)
            return render(request, 'student_detail.html', {'student': student})
        ```
   

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

