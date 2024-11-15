from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: dict[str, str]
    subjects: ()
    hobbies: dict[str, int]
    upload_file_name: str
    current_address: str
    state: str
    city: str


student_1 = User(
    first_name='Alexander',
    last_name='Ivanov',
    email='maily-mail@sb.ru',
    gender='Male',
    phone_number='9645120774',
    date_of_birth={"day": '12', "month": 'April', "year": '1997'},
    subjects=('Maths', 'English'),
    hobbies={'Sports': 1, 'Reading': 2},
    upload_file_name='SI.jpg',
    current_address='Moscow, Red Square, h. 1',
    state='Haryana',
    city='Karnal'
)
