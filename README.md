...
# Job Application Tracker 
A Personal web app to track job and internship applications. It can update application status by scanning your email inbox. 

...
## Features

- Add and track an application with company name, role, recuiter email, and optional notes.
- Update status by scanning emails.
- Edit notes for each application. 
- Secure setup with .env for storing email credentials.
- One-command local launch using a custom script. 

...
## Setup

1. Clone the repository
`git clone https://github.com/YOUR_USERNAME/job-tracker.git
cd job-tracker`

2. Create virtual env
```bash
python3 -m venv env
source env/bin/activate
```

3. Install the dependencies
`pip install -r requirements.txt`

4. Create a `.env` file with your email credentials
```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=app_password
```
note: Use a generated app password (not your main password).

5. Initialize the database 
`python3 app.py`

6. Run the app using the shell script
`./run_app.sh`
This will launch the web app in your browser.

...
## Screenshots

### Homepage (Empty)
![Homepage_Empty](assets/homepage_empty.png)

### Homepage
![Homepage](assets/homepage.png)

### Edit Page
![Edit Page](assets/edit_page.png)

...
## Upcoming Features

- Filtering and search for applications
- Automatic status updates 
- Authentication 


