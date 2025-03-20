from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
import string
import uuid
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    
    def is_valid(self):
        """Check if token is still valid (not expired and not used)"""
        return not self.is_used and timezone.now() <= self.expires_at
    
    @classmethod
    def generate_token(cls, user, expiry_hours=24):
        """Generate a new password reset token for the user"""
        # Mark any existing tokens as used
        cls.objects.filter(user=user, is_used=False).update(is_used=True)
        
        # Calculate expiry time
        expires_at = timezone.now() + timezone.timedelta(hours=expiry_hours)
        
        # Create and return the token object
        return cls.objects.create(user=user, expires_at=expires_at)

class OTPVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def is_valid(self):
        """Check if OTP is still valid (not expired)"""
        return timezone.now() <= self.expires_at

    @classmethod
    def generate_otp(cls, user, expiry_minutes=10):
        """Generate a new OTP for the user"""
        # Delete any existing OTPs for this user
        cls.objects.filter(user=user).delete()
        
        # Generate a random 6-digit OTP
        otp = ''.join(random.choices(string.digits, k=6))
        
        # Calculate expiry time
        expires_at = timezone.now() + timezone.timedelta(minutes=expiry_minutes)
        
        # Create and return the OTP object
        return cls.objects.create(user=user, otp=otp, expires_at=expires_at)


class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    subject_specialization = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)  # Add verification field

    def __str__(self):
        return f"{self.full_name} - {self.school}"
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False) 
    age = models.IntegerField(null=True, blank=True)
    math_score = models.FloatField(null=True, blank=True)
    english_score = models.FloatField(null=True, blank=True)
    science_score = models.FloatField(null=True, blank=True)
    history_score = models.FloatField(null=True, blank=True)
    attendance_rate = models.FloatField(null=True, blank=True)
    study_hours_per_week = models.FloatField(null=True, blank=True)
    household_income = models.FloatField(null=True, blank=True)
    gender = models.IntegerField(
        choices=[(0, "Female"), (1, "Male")],
        null=True, blank=True
    )
    school_type = models.IntegerField(
        choices=[(0, "Private"), (1, "Public")],
        null=True, blank=True
    )
    location = models.IntegerField(
        choices=[(0, "Rural"), (1, "Urban")],
        null=True, blank=True
    )
    parental_education_level = models.IntegerField(
        choices=[(0, "Primary"), (1, "Secondary"), (2, "Tertiary")],
        null=True, blank=True
    )
    internet_access = models.IntegerField(
        choices=[(0, "No"), (1, "Yes")],
        null=True, blank=True
    )
    parental_career = models.IntegerField(
        choices=[(0, "Arts"), (1, "Business"), (2, "Education"), 
                 (3, "Healthcare"), (4, "Technology")],
        null=True, blank=True
    )
    extracurricular_activity = models.IntegerField(
        choices=[(0, "Entrepreneurship Club"), (1, "Music"), (2, "None"), 
                 (3, "Science Club"), (4, "Sports")],
        null=True, blank=True
    )
    interest = models.IntegerField(
        choices=[(0, "Arts"), (1, "Business"), (2, "Healthcare"), 
                 (3, "Humanities"), (4, "STEM")],
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.school}"


class Prediction(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="predictions")
    created_at = models.DateTimeField(auto_now_add=True)
    
    predicted_subject = models.IntegerField(
        choices=[(0, "Arts"), (1, "Business"), (2, "Healthcare"), 
                 (3, "Humanities"), (4, "STEM")]
    )
    recommended_subjects = models.CharField(max_length=255, help_text="Comma-separated recommended subjects")
    
    
    def __str__(self):
        return f"Prediction for {self.student.full_name} - {self.get_predicted_subject_display()}"

    def get_recommended_subjects_list(self):
        """Returns the recommended subjects as a list."""
        return self.recommended_subjects.split(",") if self.recommended_subjects else []

class Testimonial(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"

class RecommendationOverride(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    old_recommendation = models.IntegerField(
        choices=[(0, "Arts"), (1, "Business"), (2, "Healthcare"), (3, "Humanities"), (4, "STEM")]
    )
    new_recommendation = models.IntegerField(
        choices=[(0, "Arts"), (1, "Business"), (2, "Healthcare"), (3, "Humanities"), (4, "STEM")]
    )
    reason = models.TextField(help_text="Reason for override", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.full_name} changed {self.student.full_name}'s recommendation"

class Feedback(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    feedback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback for {self.student.full_name} by {self.teacher.full_name}"

class ContactMessageLanding(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Message from {self.user} ({self.email})"
    
    class Meta:
        ordering = ['-timestamp']

# First, let's uncomment and enhance the IQ Question model

class IQQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    question_type = models.CharField(max_length=50, choices=[
        ('logical', 'Logical Reasoning'),
        ('verbal', 'Verbal Reasoning'),
        ('numerical', 'Numerical Reasoning'),
        ('spatial', 'Spatial Reasoning'),
    ])
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    
    def __str__(self):
        return f"{self.get_question_type_display()} Question ({self.get_difficulty_display()})"

class IQTestResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="iq_results")
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE, related_name="iq_results", null=True, blank=True)
    logical_score = models.IntegerField(default=0)
    verbal_score = models.IntegerField(default=0)
    numerical_score = models.IntegerField(default=0)
    spatial_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
    
    def calculate_normalized_score(self):
        """Convert raw scores to a normalized IQ-like score (mean 100, std 15)"""
        # Get the maximum possible score for each category
        max_per_category = 5  # Based on your test structure (5 questions per category)
        max_total = max_per_category * 4  # 4 categories
        
        # Calculate total raw score
        total_raw = self.logical_score + self.verbal_score + self.numerical_score + self.spatial_score
        
        # Calculate percentage of correct answers
        percentage_correct = (total_raw / max_total) * 100
        
        # Map percentage to IQ-like scale (70-130)
        # This creates a more balanced distribution
        if percentage_correct <= 25:
            normalized = 70 + (percentage_correct * 0.4)
        elif percentage_correct <= 50:
            normalized = 80 + ((percentage_correct - 25) * 0.6)
        elif percentage_correct <= 75:
            normalized = 95 + ((percentage_correct - 50) * 0.8)
        else:
            normalized = 115 + ((percentage_correct - 75) * 0.6)
            
        self.total_score = round(normalized)
        return self.total_score
    
    def get_suitable_areas(self):
        """Map cognitive strengths to academic areas"""
        max_score = 5  # Maximum score per category
        threshold_high = 0.8  # 80% correct (4 out of 5)
        threshold_medium = 0.6  # 60% correct (3 out of 5)
        
        # Calculate relative strengths
        scores = {
            "logical": self.logical_score / max_score,
            "verbal": self.verbal_score / max_score,
            "numerical": self.numerical_score / max_score,
            "spatial": self.spatial_score / max_score
        }
        
        # Find the highest score(s)
        max_score_value = max(scores.values())
        primary_strengths = [k for k, v in scores.items() if v == max_score_value]
        
        # Map cognitive abilities to academic areas
        strengths = []
        
        # Add areas based on absolute performance
        if scores["logical"] >= threshold_high:
            strengths.append("STEM")
        if scores["verbal"] >= threshold_high:
            strengths.append("Humanities")
        if scores["numerical"] >= threshold_high:
            strengths.append("Business")
        if scores["spatial"] >= threshold_high:
            strengths.append("Arts")
            
        # If no clear strength based on absolute performance, use relative strengths
        if not strengths:
            if "logical" in primary_strengths and scores["logical"] >= threshold_medium:
                strengths.append("STEM")
            if "verbal" in primary_strengths and scores["verbal"] >= threshold_medium:
                strengths.append("Humanities")
            if "numerical" in primary_strengths and scores["numerical"] >= threshold_medium:
                strengths.append("Business")
            if "spatial" in primary_strengths and scores["spatial"] >= threshold_medium:
                strengths.append("Arts")
                
        # If still no clear strength, suggest based on combinations
        if not strengths:
            # Logical + Numerical -> STEM
            if scores["logical"] + scores["numerical"] >= 1.0:
                strengths.append("STEM")
            # Verbal + Logical -> Humanities
            elif scores["verbal"] + scores["logical"] >= 1.0:
                strengths.append("Humanities")
            # Numerical + Verbal -> Business
            elif scores["numerical"] + scores["verbal"] >= 1.0:
                strengths.append("Business")
            # Spatial + any -> Arts
            elif scores["spatial"] + max(scores["logical"], scores["verbal"], scores["numerical"]) >= 1.0:
                strengths.append("Arts")
            else:
                # Fallback to highest absolute score
                if max_score_value == scores["logical"]:
                    strengths.append("STEM")
                elif max_score_value == scores["verbal"]:
                    strengths.append("Humanities")
                elif max_score_value == scores["numerical"]:
                    strengths.append("Business")
                else:  # spatial
                    strengths.append("Arts")
                
        # Add Healthcare as a secondary recommendation for combinations
        if "STEM" in strengths and scores["verbal"] >= threshold_medium:
            strengths.append("Healthcare")
        
        return list(set(strengths))  # Remove duplicates
    
    def __str__(self):
        return f"IQ Test Result for {self.student.full_name} - Score: {self.total_score}"