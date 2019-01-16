This file contains important informations how to setup environment for django API and how to use paarticular endpoints.

Before cloning repository create virtual environment by using command:
python -m venv name_of_your_environment
Activate virtual environment and install libraries from requirements.txt file.
Clone this repository.

As the database is not attached, you have to manually create sqlite object.
From within main directory type: 
python manage.py makemigrations
python manage.py migrate
 
Its needed create manually 'Owner' entry either from admin panel or using django shell.
To run local server type:
python manage.py runserver

1.Create exam by entering "/exams/create" endpoint on post json with needed fields. 
example:
{
  "owner": 1,
  "grade":5,
  "students_name": "ola"
}

'id' field will be added automatically.

2. To list all sent exams go to "/exams" endpoint. You can update the data of exam by entering "/exams/" endpoint 
with exams id suffix. 

3. To assign points to exam task enter "exams/tasks/<int:pk>" endpoint, where pk is automatically added id
of the task. You can add new task from any exams/tasks/* endpoint.
example:
{
  "exam": 1,
  "task_number": 2,
  "number_of_points": 10
}

4. To upload exam sheet use external client (e.g. Postman). You have to send POST on "exams/files/<int:exam_id>" endpoint 
with selected file and header "Content-Disposition" "attachment; filename=sample.pdf". To retreive exam sheet just send GET
to the same endpoint.

#####################################
Future development: authentication