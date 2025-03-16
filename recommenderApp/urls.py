from . import views
from django.urls import path

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),
    path("student_signin/", views.student_signin, name="student_signin"),
    path('teacher_signin/', views.teacher_signin, name='teacher_signin'),
    path("predict/", views.predict_student, name="predict"),
    path("result/<int:prediction_id>/", views.result_view, name="result"),
    path("result/", views.result_view, name="result_no_id"),
    path("add-testimonial/", views.add_testimonial_view, name="add_testimonial"),
    path("logout/", views.logout_view, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("guide/", views.student_guide_view, name="guide"),
    path("visuals/", views.visuals, name='visuals'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('override_recommendation/<int:prediction_id>/', views.override_recommendation, name='override_recommendation'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('student/feedback/', views.student_feedback, name='student_feedback'),
    path('submit_contact_landing/', views.submit_contact_landing, name='submit_contact_landing'),
]