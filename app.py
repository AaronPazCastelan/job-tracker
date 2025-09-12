from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from email_util import fetch_app_status, determine_status

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class JobApps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="pending")
    notes = db.Column(db.Text)
    applied_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    last_updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"<JobApp {self.id} {self.company} - {self.role}>"


# Routes to Webpage
# Home page
@app.route("/",methods=["POST","GET"])
def index():
    # Add a Task
    if request.method == "POST":
        company = request.form['company']
        email = request.form['email']
        role = request.form['role']
        notes = request.form.get('notes')  # optional

        new_app = JobApps(
            company=company,
            email=email,
            role=role,
            notes=notes
        )
        try:
            db.session.add(new_app)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    # See all current tasks
    else:
        apps = JobApps.query.order_by(JobApps.applied_at).all()
        return render_template('index.html', apps=apps)

# Delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_app = JobApps.query.get_or_404(id)
    try:
        db.session.delete(delete_app)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"

# Edit an item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    appl = JobApps.query.get_or_404(id)
    if request.method == "POST":
        appl.notes = request.form['notes']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template('edit.html', app=appl)

# Refresh status of item 
@app.route("/refresh/<int:id>")
def refresh(id:int):
    appl = JobApps.query.get_or_404(id)
    body = fetch_app_status(appl.email)
    appl.status = determine_status(body)
    try:
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"


# Runner and Debugger
if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)