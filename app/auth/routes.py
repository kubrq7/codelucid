import random # Bunu eklemeyi unutma
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_login import UserMixin, login_user, logout_user, login_required
from flask_mail import Message
from app.extensions import mail, login_manager

# Blueprint tanımlaması
auth_bp = Blueprint("auth", __name__)

# Learner Modeli (Bunu ayrı bir models.py dosyasına alman daha iyi ama şimdilik burada kalabilir)
class Learner(UserMixin):
    def __init__(self, email):
        self.email = email
    def get_id(self):
        return self.email

@login_manager.user_loader
def load_user(user_id):
    return Learner(user_id)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        if "@" not in email:
            flash("Please enter a valid email address.", "error")
            return render_template("auth/login.html")

        otp = str(random.randint(100000, 999999))
        session["otp"] = otp
        session["pending_email"] = email

        msg = Message("Your CodeLucid Access Key", recipients=[email])
        msg.body = f"CodeLucid Secure Access.\n\nYour one-time verification code is: {otp}"
        mail.send(msg)

        return redirect(url_for("auth.verify"))
    return render_template("auth/login.html")

@auth_bp.route("/verify", methods=["GET", "POST"])
def verify():
    email = session.get("pending_email")
    if not email:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        code = "".join(request.form.getlist("digit")).strip()
        if code == session.get("otp"):
            user = Learner(email) 
            login_user(user, remember=True)
            session.pop("otp", None)
            session.pop("pending_email", None)
           # Hata: return redirect(url_for("main.dashboard"))
            return redirect(url_for("main.dashboard"))
        
        flash("Geçersiz doğrulama kodu.", "error")
    
    return render_template("auth/verify.html", email=email)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("auth.login"))