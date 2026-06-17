🚀 SocialSphere – Modern Social Media Platform












📖 Project Overview

SocialSphere is a modern social media platform built using Django, HTML, CSS, JavaScript, and SQLite. The application enables users to connect, share content, interact with posts, and build their online presence through customizable profiles.

The platform provides a complete social networking experience including user authentication, profile management, media sharing, likes, comments, follow system, notifications, and an administrative dashboard.

This project was developed as part of CodeAlfa Internship – Task 2 (Mini Social Media Platform) to demonstrate full-stack web development skills and practical implementation of social networking features.

✨ Key Features
👤 User Authentication
Secure User Registration
User Login & Logout
Session Management
Protected Routes
🧑 User Profiles
Custom User Profiles
Profile Picture Upload
Cover Photo Upload
Personal Bio Section
Followers & Following Count
Edit Profile Functionality
📝 Social Posts
Create Text Posts
Upload Images
Upload Videos
Dynamic News Feed
Post Timestamp Tracking
❤️ Social Interactions
Like & Unlike Posts
Comment on Posts
Follow & Unfollow Users
View Followers List
View Following List
🔔 Notification System
Like Notifications
Comment Notifications
Follow Notifications
Notification Center
🛠 Admin Dashboard
User Management
Profile Management
Posts Management
Comments Management
Likes Management
Followers Management
🏗 Technology Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Django
Database
SQLite3
Media Management
Django Media Files
Image Upload Handling
Video Upload Handling
📂 Project Structure
social-media-app/
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── feed.html
│   ├── profile.html
│   ├── profile_edit.html
│   ├── create_post.html
│   ├── notifications.html
│   └── post_detail.html
│
├── media/
│   ├── profiles/
│   ├── covers/
│   └── posts/
│
├── manage.py
├── requirements.txt
└── README.md
🗄 Database Models

The application manages the following entities:

User
Profile
Post
Comment
Like
Follow
Notification

These models work together to provide a complete social networking experience.

🚀 Installation Guide
Clone Repository
git clone https://github.com/your-username/CodeAlfa-Task2-SocialSphere.git
Navigate to Project
cd CodeAlfa-Task2-SocialSphere
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Database Migrations
python manage.py makemigrations
python manage.py migrate
Create Admin User
python manage.py createsuperuser
Start Development Server
python manage.py runserver
Open Browser
http://127.0.0.1:8000/
🎯 Learning Outcomes

This project demonstrates practical experience in:

Django Framework Development
Authentication & Authorization
Database Design & Relationships
CRUD Operations
Media File Handling
User Profile Management
Social Networking Systems
Frontend UI Development
Backend Logic Implementation
Full-Stack Web Development
🌟 Future Enhancements
Real-Time Chat System
Direct Messaging
Stories Feature
Dark Mode
User Search System
Real-Time Notifications
Friend Requests
Post Sharing Analytics
WebSocket Integration
📸 Core Functionalities Demonstrated

✅ User Registration & Login
✅ Profile Management
✅ Profile & Cover Photos
✅ Create Posts
✅ Image Uploads
✅ Video Uploads
✅ Like System
✅ Comment System
✅ Follow/Unfollow System
✅ Notifications
✅ Followers & Following Lists
✅ Django Admin Panel

👨‍💻 Author

Zohaib Wazir
Software Engineering Student
City University Peshawar
Web & App Developer

🏆 Internship Project
CodeAlfa Internship – Task 2

Mini Social Media Platform

A full-stack social networking application developed using Django that allows users to create profiles, share content, interact through likes and comments, follow other users, and receive notifications in a modern social media environment.

⭐ If you found this project interesting, consider giving it a star on GitHub!