# 🏥 Hospital Information System Web Application - Ophthalmology Department

## 📌 Project Overview

This project is a **Hospital Information System (HIS)** developed as a web application using **Django**. The focus of the system is on the **Ophthalmology Department**, aiming to manage interactions between patients, doctors, and administrative users. It facilitates secure access, patient-doctor interactions, report generation, appointment scheduling, and more.

The application is responsive, dynamic, and user-role-based, supporting multiple user types such as **Doctors**, **Patients**, and **Admins**.

---

## 🧩 Key Features

- 🌐 **Home Page** for general visitors
- 🔐 **User Registration and Login** with role-based access
- 👤 **Profile Management** for Patients and Doctors
- 📁 **File Uploads** including images and medical scans
- 🩺 **Appointment Scheduling** between patients and doctors
- 📊 **Admin Dashboard** for statistical analysis and system management
- ✉️ **Contact Form** for user inquiries
- ☁️ **Cloud-hosted Assets**: All images and media are uploaded to a cloud server to ensure global accessibility across all website pages

---

## 🏗️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL hosted on [**Neon**](https://neon.tech)
- **Cloud Storage**: Cloud-based image hosting for website presentation

---

## 🗃️ Database Design

We carefully designed the database schema tailored to the needs of the **Ophthalmology Department**. Our schema follows best practices in relational modeling and includes normalization for performance and consistency.

### ✅ ER Diagram

![ER Diagram](/mnt/data/WhatsApp%20Image%202025-05-01%20at%2011.14.52%20PM.jpeg)

The schema includes the following core entities:

- `USER`: Abstract model for all user types (Patient, Doctor, Admin)
- `PATIENT`: Stores patient-specific data including medical history
- `DOCTOR`: Stores doctor credentials, specialties, and experience
- `ADMIN`: Handles administrative roles like system supervision and staff management
- `APPOINTMENT`: Connects patients and doctors with scheduling and status tracking
- `REPORT`: Summarizes appointment outcomes with diagnosis and follow-up recommendations
- `BILLING`: Links to reports and handles payment and insurance information
- `PRESCRIPTION_GLASSES`: Records ophthalmic prescriptions issued by doctors

This model ensures seamless interaction between users while maintaining data integrity.

---

## 🚀 Phase 1: Implementation Highlights

In **Phase 1**, we successfully completed:

- 🎯 Full database design (see ER diagram above)
- 🔐 Secure login/register functionality for Doctors and Patients
- 👥 Profile pages for both Doctors and Patients
- 🧠 Initial data models and relationships with Django ORM
- 🌐 Deployed frontend components with responsive design and cloud image support

---

## 💡 Future Work

- Implement full appointment booking and tracking logic
- Expand admin dashboard with real-time statistics
- Integrate communication between doctors and patients via chat or notifications
- Enable file-based scan uploads and secure media storage

