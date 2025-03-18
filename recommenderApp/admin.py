from django.contrib import admin
from .models import (StudentProfile, Prediction, Testimonial, ContactMessage, TeacherProfile,
                     RecommendationOverride, ContactMessageLanding, Feedback, IQQuestion, IQTestResult, School)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', "email", "school", "subject_specialization", "created_at"]

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'school', 'created_at', 'age', 
                    'math_score', 'english_score', 'science_score', 'history_score',
                    'attendance_rate', 'study_hours_per_week', 'household_income',
                    'gender', 'school_type', 'location', 'parental_education_level',
                    'internet_access', 'parental_career', 'extracurricular_activity', 'interest']
    search_fields = ['full_name', 'email', 'school']
    list_filter = ['school', 'gender', 'school_type', 'location']

class PredictionAdmin(admin.ModelAdmin):
    list_display = ['student', 'created_at', 'predicted_subject', 'recommended_subjects']
    search_fields = ['student__full_name', 'predicted_subject']
    list_filter = ['predicted_subject', 'created_at']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('student', 'name', 'content', 'rating', 'created_at')  
    search_fields = ('name', 'content')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']

class RecommendationOverrideAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'old_recommendation', 'new_recommendation', 'timestamp')
    list_filter = ('timestamp', 'old_recommendation', 'new_recommendation')
    search_fields = ('teacher__full_name', 'student__full_name')

@admin.register(ContactMessageLanding)
class ContactMessageLandingAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'timestamp')
    search_fields = ('user', 'email', 'message')
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'feedback', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('teacher__full_name', 'student__full_name', 'feedback')

class IQQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_type', 'difficulty', 'question', 'correct_answer')
    list_filter = ('question_type', 'difficulty')
    search_fields = ('question',)

class IQTestResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'logical_score', 'verbal_score', 'numerical_score', 
                    'spatial_score', 'total_score', 'completed_at')
    list_filter = ('completed_at',)
    search_fields = ('student__full_name',)

admin.site.register(School, SchoolAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(RecommendationOverride,RecommendationOverrideAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(IQQuestion, IQQuestionAdmin)
admin.site.register(IQTestResult, IQTestResultAdmin)