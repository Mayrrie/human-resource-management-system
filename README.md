# human-resource-management-system
Odoo x Adamas University Hackathon 2026
Project Overview

The Human Resource Management System (HRMS) is an Odoo-based web application designed to simplify and automate human resource operations. It helps organizations manage employee information, attendance, leave requests, payroll visibility, and approval workflows through a secure and user-friendly interface.

Objectives

- Digitize HR operations
- Reduce manual paperwork
- Improve employee management
- Simplify attendance and leave tracking
- Provide secure role-based access

Features 

Authentication
- Secure Sign Up
- Secure Login
- Email Verification
- Role-Based Access (Admin / Employee)

Employee Module
- View Profile
- Edit Personal Details
- View Salary Information
- Upload Profile Picture
Attendance Module
- Daily Attendance
- Weekly Attendance
- Check-In
- Check-Out
- Attendance Status

Leave Management
- Apply for Leave
- Paid Leave
- Sick Leave
- Unpaid Leave
- Leave Status Tracking

Admin Module
- Employee Management
- Attendance Management
- Leave Approval
- Payroll Management
- Dashboard Overview

User Roles

Employee
- Login
- View Profile
- Edit Personal Information
- Mark Attendance
- Apply for Leave
- View Salary

Admin / HR
- Manage Employees
- View Attendance
- Approve/Reject Leave
- Manage Payroll
- Monitor Employee Records

Technology Stack

- Odoo
- Python
- PostgreSQL
- XML
- Git
- GitHub
- Visual Studio Code

Project Modules

- Authentication
- Dashboard
- Employee Management
- Attendance Management
- Leave Management
- Payroll Management

Testing

The following modules were tested:

- User Registration
- User Login
- Dashboard Navigation
- Employee Profile
- Attendance
- Leave Request
- Payroll View
- Logout

Future Enhancements

- Mobile Application
- Email Notifications
- Performance Analytics
- AI-based Attendance Insights
- Employee Performance Dashboard

Conclusion

The Human Resource Management System provides a simple, secure, and efficient solution for managing employees, attendance, leave requests, payroll information, and administrative workflows. It reduces manual effort while improving productivity and accuracy.

Team Members

- Sampadha Sharma
- Swati Kumari Mahatao
- Maria Afri
- Sania Tasnim

License

This project was developed for the Odoo Hackathon and is intended for educational purposes.

TESTING

Test Case ID

Feature

Test Steps

Expected Result

Actual Result

Status

TC-01

Sign Up

Test Steps: Go To Sign Up page Enter valid Employee ID, Email, Password,Role Then Click on sign up

User account is created successfully.

Account created successfully.

Pass

TC-02

Login

Type in the valid Email and Passwordand press Login

The user is navigated to the dashboard.

Dashboard opened successfully.

Pass

TC-03

Invalid Login

In the box, Enter a wrong Email or Password and click on Login.

Error message is displayed.

Error message displayed correctly.

Pass

TC-04

Employee Dashboard

Log in as an Employee.

Dashboard Profile Attendance Leave Logout