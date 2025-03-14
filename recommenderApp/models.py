from django.db import models
from django.utils import timezone


class TeacherProfile(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    school_name = models.CharField(max_length=255)
    subject_specialization = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.school_name}"
    

class StudentProfile(models.Model):
    #basic registration info
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #optional fields that can be filled during prediction
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