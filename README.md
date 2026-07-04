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

Test Case ID: TC-01

Feature: Sign Up

Just open the Sign Up page, fill in a valid Employee ID, Email, Password, pick a Role, then hit Sign Up.

You get a message that your account’s been created.

Actual Result: Account created successfully.

Status: Pass

---

Test Case ID: TC-02

Feature: Login

Type in a valid Email and Password, then click Login.

You land right on the dashboard.

Actual Result: Dashboard opened successfully.

Status: Pass

---

Test Case ID: TC-03

Feature: Invalid Login

Enter the wrong Email or Password, then click Login.

You’ll see an error message pop up.

Actual Result: Error message showed up as expected.

Status: Pass

---

Test Case ID: TC-04

Feature: Employee Dashboard

Sign in as an Employee.

The dashboard gives you options for Profile, Attendance, Leave, and Logout.

Actual Result: All those options showed up.

Status: Pass

---

Test Case ID: TC-05

Feature: Admin Dashboard

Sign in as an Admin.

You’ll see Employee List, Attendance Records, Leave Approvals, and Payroll on your dashboard.

Actual Result: Dashboard displayed everything needed.

Status: Pass

---

Test Case ID: TC-06

Feature: View Profile

Go to the Profile page.

Employee details show up correctly.

Actual Result: Details all there.

Status: Pass

---

Test Case ID: TC-07

Feature: Edit Profile

Change something like your address or phone and save.

Your updates stick.

Actual Result: Profile updated.

Status: Pass

---

Test Case ID: TC-08

Feature: Attendance

Head over to the Attendance page.

You can see daily and weekly attendance.

Actual Result: Attendance info matched.

Status: Pass

---

Test Case ID: TC-09

Feature: Apply Leave

Pick a leave type, set the dates, write any remarks, and submit.

Your leave request shows up as Pending.

Actual Result: Request submitted.

Status: Pass

---

Test Case ID: TC-10

Feature: Leave Approval

Login as Admin and either approve or reject a leave request.

The leave status updates to Approved or Rejected.

Actual Result: Status reflected the change.

Status: Pass

---

Test Case ID: TC-11

Feature: Payroll

Open the Payroll page.

Salary details are easy to see.

Actual Result: Payroll info displayed.

Status: Pass

---

Test Case ID: TC-12

Feature: Logout

Click on Logout.

You’re sent back to the Login page.

Actual Result: Logout worked.

Status: Pass