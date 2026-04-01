from setuptools import setup

APP = ['app.py']
DATA_FILES = [
    '.env',
    'email_util.py', 
    'templates', 
    'static', 
    'instance' 
]

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'packages': [
        'flask', 
        'flask_sqlalchemy', 
        'flask_scss', 
        'imap_tools', 
        'sqlalchemy',
        'dotenv',
        'webview', 
        'Foundation' 
    ],
    'plist': {
        'CFBundleName': "Job Tracker",
        'CFBundleDisplayName': "Job Tracker",
        'CFBundleGetInfoString': "Tracking Job Applications",
        'CFBundleIdentifier': "com.yourname.jobtracker",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)