# Secure Coding Review - Task 3

This project is part of CodeAlpha Cybersecurity Internship.

## Project Description
Security review and remediation of vulnerable authentication code with SQL injection risks and plaintext password storage.

## Features
- Secure password hashing with bcrypt
- SQL injection prevention
- Input validation
- Database initialization scripts

## Setup
```bash
pip install bcrypt
python init_db.py
python add_user.py
python app.py