from faker import Faker
#first install using pip install faker command
import random
from .models import *
#seed is used to fill the database
fake=Faker()

def afunction(n=10)->None:
    for _ in range(n):
        dms=["humanity", "sociology", "psychology", "science", "pharmacy", "physics", "botany"]
        department_obj=Department.objects.create(department=random.choice(dms))
        student_ids=Student_id.objects.create(student_id=f"ST-00{random.randint(1,20)}")
        student_name=fake.name()
        student_age=random.randint(20,30)
        student_address=fake.address()
        student_email=fake.email()

        Student.objects.create(
            department=department_obj,
            student_id=student_ids,
            student_name=student_name,
            student_age=student_age,
            student_address=student_address,
            student_email=student_email
            )



