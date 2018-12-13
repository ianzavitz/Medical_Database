import os
import secrets
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, PatientUpdateForm, PatientForm, CaseUpdateForm, CaseForm
from flaskDemo.models import User, Post, Hospital, Physician, Patient, Medical_Procedure, Medical_Case, Works_On
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

@app.route("/")
@app.route("/home")
def home():
    #posts =db.engine.execute('select cou * from Medical_Case where outcome=="REFERED";')
    posts = Post.query.all()
    cnx = mysql.connector.connect(user="student", password="student",database="ProjectDatabase")
    cursor=cnx.cursor()
    query = "SELECT COUNT(*) AS count FROM medical_case"

    
    cursor.execute(query)
    out = str(int(cursor.fetchall()[0][0]))
	
    return render_template('home.html', out = out)
@app.route("/cases")
def cases():
    results2 = Physician.query.join(Works_On,Physician.physician_id == Works_On.physician_id) \
               .add_columns(Works_On.case_id,Physician.hospital_id_FK,Physician.physician_id, Physician.physician_last_name) \
               .join(Hospital, Hospital.hospital_id == Physician.hospital_id_FK).add_columns(Hospital.hospital_name)
    results =  Physician.query.join(Works_On,Physician.physician_id == Works_On.physician_id) \
               .add_columns(Physician.hospital_id_FK,Works_On.case_id, Physician.physician_id, Physician.physician_last_name) 
			   
    return render_template('join.html', title='Join',joined_1_n=results, joined_m_n=results2)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/referal")
def referal():
	results = Medical_Case.query.filter(Medical_Case.outcome=='REFERED')
	return render_template('referal.html',outString = results)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/patient/new", methods=['GET', 'POST'])
@login_required
def new_patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(patient_id=form.patient_id.data, age=form.age.data,diagnosis=form.diagnosis.data)
        #patient = Patient(age=form.age.data,diagnosis=form.diagnosis.data)
        #db.session.add(patient_id)
        db.session.add(patient)
        db.session.commit()
        flash('You have added a new Patient!', 'success')
        return redirect(url_for('home'))
    return render_template('create_patient.html', title='New Patient',
                           form=form, legend='New Patient')


@app.route("/patient/<patient_id>")
@login_required
def patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return render_template('patient.html', title=patient.patient_id, patient=patient, now=datetime.utcnow())


@app.route("/patient/<patient_id>/update", methods=['GET', 'POST'])
@login_required
def update_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    currentPatient = patient.patient_id

    form = PatientUpdateForm()
    if form.validate_on_submit():          # notice we are are not passing the dnumber from the form
        if currentPatient !=form.patient_id.data:
            patient.patient_id=form.patient_id.data
        patient.age=form.age.data
        patient.diagnosis=form.diagnosis.data
        db.session.commit()
        flash('Patient has been updated!', 'success')
        return redirect(url_for('patient', patient_id=patient_id))
    elif request.method == 'GET':             
        form.patient_id.data = patient.patient_id   # notice that we ARE passing the dnumber to the form
        form.age.data = patient.age
        form.diagnosis.data = patient.diagnosis
    return render_template('update_patient.html', title='Update Patient',
                           form=form, legend='Update Patient')          # note the update template!




@app.route("/patient/<patient_id>/delete", methods=['POST'])
@login_required
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    flash('The Patient has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/case/new", methods=['GET', 'POST'])
@login_required
def new_case():
    form = CaseForm()
    if form.validate_on_submit():
        medical_case = Medical_Case(case_id=form.case_id.data, outcome=form.outcome.data,stay_duration=form.stay_duration.data,patient_id_FK=form.patient_id_FK.data,procedure_id_FK=form.procedure_id_FK.data)
        works_on = Works_On(case_id=form.case_id.data, physician_id = form.physician_id.data, hours = form.hours.data)
        #db.session.add(case_id)
        db.session.add(medical_case)
        db.session.add(works_on)
        db.session.commit()
        flash('You have added a new Case!', 'success')
        return redirect(url_for('home'))
    return render_template('create_case.html', title='New Case',
                           form=form, legend='New Case')


@app.route("/case/<case_id>")
@login_required
def medical_case(case_id):
    medical_case = Medical_Case.query.get_or_404(case_id)
    return render_template('case.html', title=medical_case.case_id, medical_case=medical_case, now=datetime.utcnow())


@app.route("/case/<case_id>/update", methods=['GET', 'POST'])
@login_required
def update_case(case_id):
    medical_case = Medical_Case.query.get_or_404(case_id)
    case_id_FK = case_id
    works_on=Works_On.query.get_or_404(case_id_FK)
    currentCase = medical_case.case_id
    currentW_O = works_on.case_id_FK

    form = CaseUpdateForm()
    if form.validate_on_submit():          # notice we are are not passing the dnumber from the form
        if currentCase !=form.case_id.data:
            medical_case.case_id=form.case_id.data
        if currentW_O !=form.case_id.data:
            works_on.case_id_FK=form.case_id.data
        medical_case.outcome=form.outcome.data
        medical_case.stay_duration=form.stay_duration.data
        medical_case.procedure_id_FK=form.procedure_id_FK.data
        medical_case.patient_id_FK=form.patient_id_FK.data
        works_on.physician_id=form.physician_id.data
        works_on.hours=form.hours.data
        db.session.commit()
        flash('Case has been updated!', 'success')
        return redirect(url_for('case', case_id=case_id))
    elif request.method == 'GET':             
        form.case_id.data = medical_case.case_id   # notice that we ARE passing the dnumber to the form
        form.outcome.data = medical_case.outcome
        form.stay_duration.data = medical_case.stay_duration
        form.procedure_id_FK.data = medical_case.procedure_id_FK
        form.patient_id_FK.data = medical_case.patient_id_FK
        form.physician_id.data = works_on.physician_id
        form.hour.data = works_on.hours
    return render_template('update_case.html', title='Update Case',
                           form=form, legend='Update Case')          # note the update template!




@app.route("/case/<case_id>/delete", methods=['POST'])
@login_required
def delete_case(case_id):
    medical_case = Medical_Case.query.get_or_404(case_id)
    db.session.delete(medical_case)
    db.session.commit()
    flash('The Case has been deleted!', 'success')
    return redirect(url_for('home'))




















