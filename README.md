# Student Subject Recommendation System 

## **📌 Project Description**  
Rwanda’s secondary education sector faces challenges such as high dropout rates and a skills mismatch between students’ academic choices and labor market demands. This project addresses these issues by developing a Machine Learning–Powered Counseling Recommender System for O-Level and A-Level students in Kigali.  

The system integrates:  
1. Student performance data
2. Individual career interests  
2. Real-time labor market trends  

Using this information, it generates personalized subject and subject recommendations based on machine learning models.  

- **Classification Model**: Uses a **Random Forest Classifier** to predict the most suitable academic track for a student.  
- **Hybrid Recommendation Model**: Combines **content-based filtering and collaborative filtering** to suggest the **top three most relevant subjects or career paths**.  

---

## *Key Features*  
1. **Student Subject Prediction** – Uses Random Forest to classify the best-fit subject for students.  
2. **Personalized Recommendations** – Suggests **top three relevant subjects** using a hybrid recommendation approach.  
3. **User-Friendly Interface** – Students can easily input their details and receive personalized feedback.  
4. **Testimonial System** – Allows students to provide feedback on recommendations.  
5. **Secure Authentication** – User login and session-based authentication.  

---

## Technologies Used  
### **Backend & Machine Learning**  
- **Python** – Core programming language  
- **Django** – Backend framework  
- **Scikit-Learn** – Machine learning model implementation  
- **Pandas & NumPy** – Data processing  
- **PostgreSQL** – Database  

### **Frontend**  
- **HTML, CSS & JS** – Responsive and interactive UI  
- **FontAwesome** – Icons for better UI design  

---

## **Installation Guide**  
### Clone the Repository  
```bash
git clone https://github.com/Olamieee/IGA_Capstone.git
```

### Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations  
```bash
python manage.py migrate
```

### Create Admin Details to Access the Admin Dashboard 
```bash
python manage.py createsuperuser
```

### Start the Server 
```bash
python manage.py runserver
```
Now, open **`http://127.0.0.1:8000/`** in your browser to access the system.  

---

## **📌 Usage Guide**  
### **🔹 Student Workflow**  
1️ **Sign Up / Login** – Students create an account.  
2️ **Enter Academic & Interest Data** – Fill out details like scores, interests, parental career, and extracurricular activities.  
3️ **Get Subject Prediction** – The system predicts the best-fit subject using the Random Forest classifier.  
4️ **View Recommendations** – The hybrid recommender model suggests three additional subjects based on interests & demand.  
5️ **Leave Feedback** – Students can share their experience through testimonials. <br>
6 **Teacher's Dashboard** - Teachers can view and monitor each student recommendations, override and leave feedbacks for students.<br>
7 **IQ Test** - This explains the IQ test functionality that's available in the system, which assesses logical, verbal, numerical, and spatial skills to enhance recommendations.<br>
8 **View Enhanced Results** - This details what students will see after completing the IQ test, including their cognitive scores and the compatibility between their cognitive abilities and recommended subjects.<br>
9 **Teacher's Comments** - View feedback from teachers and see recommendation overrides with explanatory comments in the "My Feedback" section.<br>
10 **Personality Test** - Students can  take free personality assesments to  to discover their learning style and strengths.<br>
11 **Learning Resources** - Students can access materials to help you excel in their recommended subjects.<br>



---

## **📂 Project Folder Structure**  
```
/IGA_Capstone
|__ model                   # Machine learning models.
│── /recommender App
        │──management        # Commands files.
        │──saved_models      # Saved ML models for classification and recommendation.
        │──static
                /css         # Stylesheets.
                /img         # Images.
        │── /templates       # HTML Templates.
        /admin.py            # Admin Interface.
        /apps.py             # Apps.
        /models.py           # Database Models.
        /views.py            # Django Views.
        /urls.py             # URL Routing.
│──recommenderSystem         # Main System that handles app configuration and processes.
        /.env
        /asgi.py             # ASGI config for recommenderSystem project.
        /settings.py         # Django settings for recommenderSystem project.
        /urls.py             # URL configuration for recommenderSystem project.
        /wsgi.py             # WSGI config for recommenderSystem project.
│── manage.py                # Django Project Manager.
│── Procifile                # For Deployment.
│── requirements.txt         # Dependencies.
│── README.md                # Project Documentation.
```  
