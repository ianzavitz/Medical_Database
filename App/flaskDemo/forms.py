from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskDemo.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class PatientUpdateForm(FlaskForm):

    patient_id=IntegerField('Patient ID', validators=[DataRequired()])
    #dnumber = HiddenField("")

    age=StringField('Patient Age:', validators=[DataRequired(),Length(max=3)])
#  Commented out using a text field, validated with a Regexp.  That also works, but a hassle to enter ssn.
#    mgr_ssn = StringField("Manager's SSN", validators=[DataRequired(),Regexp('^(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4}$', message="Please enter 9 digits for a social security.")])

#  One of many ways to use SelectField or QuerySelectField.  Lots of issues using those fields!!
    #diagnosis = SelectField("Patient Diagnosis", choices=myChoices)  # myChoices defined at top
    diagnosis = StringField("Patient Diagnosis", validators=[DataRequired(),Length(max=50)])  

# the regexp works, and even gives an error message
#    mgr_start=DateField("Manager's Start Date:  yyyy-mm-dd",validators=[Regexp(regex)])
#    mgr_start = DateField("Manager's Start Date")

#    mgr_start=DateField("Manager's Start Date", format='%Y-%m-%d')
    submit = SubmitField('Update this department')


# got rid of def validate_dnumber

    def validate_patient_id(self, patient_id):    # apparently in the company DB, dname is specified as unique
         patient = Patient.query.filter_by(patient_id=patient_id.data).first()
         if patient and (str(patient.patient_id) != str(self.patient_id.data)):
             raise ValidationError('That patient id is already being used. Please choose a different id.')


class PatientForm(PatientUpdateForm):

    patient_id=IntegerField('patient_id', validators=[DataRequired()])
    submit = SubmitField('Add this department')

    def validate_patient_id(self, patient_id):    #because dnumber is primary key and should be unique
        patient = Patient.query.filter_by(patient_id=patient_id.data).first()
        if patient:
            raise ValidationError('That patient id is taken. Please choose a different one.')


class CaseUpdateForm(FlaskForm):

    case_id=IntegerField('Case ID', validators=[DataRequired()])
    #dnumber = HiddenField("")

    outcome=StringField('Case Outcome:', validators=[DataRequired(),Length(max=50)])
#  Commented out using a text field, validated with a Regexp.  That also works, but a hassle to enter ssn.
#    mgr_ssn = StringField("Manager's SSN", validators=[DataRequired(),Regexp('^(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4}$', message="Please enter 9 digits for a social security.")])

#  One of many ways to use SelectField or QuerySelectField.  Lots of issues using those fields!!
    #diagnosis = SelectField("Patient Diagnosis", choices=myChoices)  # myChoices defined at top
    stay_duration = StringField("Patient Stay Duration", validators=[DataRequired(),Length(max=50)])  

    procedure_id_FK = StringField("Procedure ID", validators=[DataRequired(),Length(max=50)])  

# the regexp works, and even gives an error message
#    mgr_start=DateField("Manager's Start Date:  yyyy-mm-dd",validators=[Regexp(regex)])
#    mgr_start = DateField("Manager's Start Date")

#    mgr_start=DateField("Manager's Start Date", format='%Y-%m-%d')
    submit = SubmitField('Update this department')


# got rid of def validate_dnumber

    def validate_case_id(self, case_id):    # apparently in the company DB, dname is specified as unique
         medical_case = Medical_Case.query.filter_by(case_id=case_id.data).first()
         if medical_case and (str(medical_case.case_id) != str(self.case_id.data)):
             raise ValidationError('That case id is already being used. Please choose a different id.')


class CaseForm(CaseUpdateForm):

    case_id=IntegerField('case_id', validators=[DataRequired()])
    submit = SubmitField('Add this department')

    def validate_case_id(self, case_id):    #because dnumber is primary key and should be unique
        medical_case_id = Medical_Case.query.filter_by(case_id=case_id.data).first()
        if medical_case:
            raise ValidationError('That case id is taken. Please choose a different one.')

