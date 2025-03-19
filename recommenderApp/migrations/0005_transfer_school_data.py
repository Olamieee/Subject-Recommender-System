# your_app/migrations/XXXX_transfer_school_data.py
from django.db import migrations

def transfer_school_data(apps, schema_editor):
    # Get the old models with CharFields for school
    TeacherProfile = apps.get_model('your_app_name', 'TeacherProfile')
    StudentProfile = apps.get_model('your_app_name', 'StudentProfile')
    School = apps.get_model('your_app_name', 'School')
    
    # For each teacher, find or create the corresponding school and update the reference
    for teacher in TeacherProfile.objects.all():
        school_name = teacher.school_name  # Assuming this is the old field name
        school, created = School.objects.get_or_create(name=school_name)
        teacher.school = school  # This is the new field
        teacher.save()
    
    # Do the same for students
    for student in StudentProfile.objects.all():
        school_name = student.school  # Assuming this is the old field name
        school, created = School.objects.get_or_create(name=school_name)
        student.school = school  # This is the new field
        student.save()

class Migration(migrations.Migration):
    dependencies = [
        ('recommenderApp', '0004_school_remove_teacherprofile_school_name_and_more'),
    ]

    operations = [
        migrations.RunPython(transfer_school_data),
    ]