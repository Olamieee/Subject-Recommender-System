from django.test import TestCase
from django.contrib.auth.models import User
from .models import TeacherProfile, StudentProfile, Prediction
from django.urls import reverse
from django.test import Client


class ProfileModelTest(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username="teacher1", email="teacher1@example.com", password="testpass")
        self.user2 = User.objects.create_user(username="student1", email="student1@example.com", password="testpass")

    def test_create_teacher_profile(self):
        """Test if a TeacherProfile is created successfully"""
        teacher = TeacherProfile.objects.create(
            user=self.user1,
            full_name="John Doe",
            email="teacher1@example.com",
            school_name="ABC High School",
            subject_specialization="Mathematics"
        )
        self.assertEqual(str(teacher), "John Doe - ABC High School")  # Checking __str__ method

    def test_create_student_profile(self):
        """Test if a StudentProfile is created successfully"""
        student = StudentProfile.objects.create(
            user=self.user2,
            full_name="Jane Doe",
            email="student1@example.com",
            school="XYZ Academy"
        )
        self.assertEqual(str(student), "Jane Doe - XYZ Academy")

class PredictionModelTest(TestCase):
    def setUp(self):
        # Create a test student profile
        self.user = User.objects.create_user(username="student2", email="student2@example.com", password="testpass")
        self.student = StudentProfile.objects.create(user=self.user, full_name="Alex Smith", email="student2@example.com", school="XYZ Academy")

    def test_create_prediction(self):
        """Test if a prediction is created successfully"""
        prediction = Prediction.objects.create(
            student=self.student,
            predicted_subject=4,  # STEM
            recommended_subjects="Math, Physics, Computer Science"
        )
        self.assertEqual(str(prediction), "Prediction for Alex Smith - STEM")  # Checking __str__
        self.assertEqual(prediction.get_recommended_subjects_list(), ["Math", "Physics", "Computer Science"])

class StudentAuthTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_student_signup(self):
        """Test if a student can register successfully"""
        response = self.client.post(reverse("student_signup"), {
            "full_name": "Test Student",
            "email": "student@example.com",
            "school": "Test School",
            "password": "password123",
            "confirm_password": "password123",
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect on success
        self.assertTrue(User.objects.filter(email="student@example.com").exists())  # User should be created
        self.assertTrue(StudentProfile.objects.filter(email="student@example.com").exists())  # Profile should exist

    def test_student_signup_email_exists(self):
        """Test if registration fails when email already exists"""
        User.objects.create_user(username="student@example.com", email="student@example.com", password="password123")

        response = self.client.post(reverse("student_signup"), {
            "full_name": "Test Student",
            "email": "student@example.com",
            "school": "Test School",
            "password": "password123",
            "confirm_password": "password123",
        })
        self.assertEqual(response.status_code, 200)  # Page should reload with an error
        self.assertContains(response, "Email already exists")  # Error message should be shown

    def test_student_login(self):
        """Test if a student can log in successfully"""
        user = User.objects.create_user(username="student@example.com", email="student@example.com", password="password123")
        StudentProfile.objects.create(user=user, full_name="Test Student", email="student@example.com", school="Test School")

        response = self.client.post(reverse("student_login"), {
            "email": "student@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect on success
        self.assertEqual(int(self.client.session["student_id"]), StudentProfile.objects.get(email="student@example.com").id)  # Check if session is set

    def test_student_login_wrong_password(self):
        """Test if login fails with incorrect password"""
        user = User.objects.create_user(username="student@example.com", email="student@example.com", password="password123")
        StudentProfile.objects.create(user=user, full_name="Test Student", email="student@example.com", school="Test School")

        response = self.client.post(reverse("student_login"), {
            "email": "student@example.com",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)  # Page should reload
        self.assertContains(response, "Invalid email or password")  # Error message should be displayed


class TeacherAuthTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_teacher_signup(self):
        """Test if a teacher can register successfully"""
        response = self.client.post(reverse("teacher_signup"), {
            "full_name": "Test Teacher",
            "email": "teacher@example.com",
            "school": "Test School",
            "subject_specialization": "Mathematics",
            "password": "password123",
            "confirm_password": "password123",
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(User.objects.filter(email="teacher@example.com").exists())  # User should be created
        self.assertTrue(TeacherProfile.objects.filter(email="teacher@example.com").exists())  # Profile should exist

    def test_teacher_login(self):
        """Test if a teacher can log in successfully"""
        user = User.objects.create_user(username="teacher@example.com", email="teacher@example.com", password="password123")
        TeacherProfile.objects.create(user=user, full_name="Test Teacher", email="teacher@example.com", school_name="Test School", subject_specialization="Math")

        response = self.client.post(reverse("teacher_login"), {
            "email": "teacher@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(self.client.session["teacher_email"], "teacher@example.com")  # Check if session is set


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="student3", email="student3@example.com", password="password123")
        self.student = StudentProfile.objects.create(user=self.user, full_name="Student Three", email="student3@example.com", school="XYZ Academy")

    def test_homepage_requires_login(self):
        """Test if homepage redirects to login if user is not authenticated"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect to login

    def test_homepage_loads_for_logged_in_user(self):
        """Test if homepage loads successfully for authenticated users"""
        self.client.login(username="student3", password="password123")  # Log in
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)  # Page should load
        self.assertContains(response, "Welcome, Student Three")  # Check if student name is displayed
