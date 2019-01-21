This file contains important informations how to setup environment for django API and how to use particular endpoints.

Before cloning repository create virtual environment by using command:
python -m venv name_of_your_environment
Activate virtual environment and install libraries from requirements.txt file.
Clone this repository.

As the database is not attached, you have to manually create sqlite object.
From within main directory type: 
python manage.py makemigrations
python manage.py migrate
 
Its needed to create superuser manually, type:
python manage.py createsuperuser

and follow the instructions, remember credentials to log into Browsable API. 
Not registered user has read only permissions.

To run local server type:
python manage.py runserver

1.Create exam by entering "/exams/create" endpoint

'id' field will be added automatically.

2. To list all sent exams go to "/exams" endpoint. You can update the data of exam by entering "/exams/" endpoint 
with exams id suffix. 

3. To assign points to exam task enter "exams/tasks/<int:pk>" endpoint, where pk is automatically added id
of the task. You can add new task from any "exams/tasks/<int:pk>" endpoint.

4. To upload exam sheet go to "exams/files/upload" endpoint. To retreive exam sheet just send GET
to "exams/files/download" endpoint. To edit or upload go to "exams/files/update/<int:pk>" endpoint.

#####################################
Future development: authentication