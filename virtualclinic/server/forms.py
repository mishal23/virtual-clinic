from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from server.models import Account, Profile, Hospital, MedicalInfo, MedicalTest, IND_STATES, Appointment

def validate_username_available(username):
    """ validator that throws an error if the given username already exists."""

    if User.objects.filter(username__icontains=username).count():
        raise forms.ValidationError("This email is already registered")

def validate_username_exists(username):
    """ validator that throws an error if the given username doesn't exists."""

    if not User.objects.filter(username__icontains=username).count():
        raise forms.ValidationError("This email does not exist")

def validate_birthday(birthday):
    """ validator to check if date is realistic """
    if birthday.year < (date.today().year -200):
        raise forms.ValidationError("Please choose a later date")
    elif birthday > date.today():
        raise forms.ValidationError("Please choose an earlier date")


def setup_field(field, placeholder=None):
    """
    This configures the given field to play nice with the bootstrap theme. Additionally, you can add
    an additional argument to set a placeholder text on the field.
    """
    field.widget.attrs['class'] = 'form-control'
    if placeholder is not None:
        field.widget.attrs['placeholder'] = placeholder



class BasicForm(forms.Form):
    def disable_field(self,field):
        """
        marks field as disabled
        :param field: name of the field
        """
        self.fields['field'].widget.attrs['disabled'] = ""

    def mark_error(self, field, description):
        """
        Marks the given field as errous. The given description is displayed when the form it generated
        :param field: name of the field
        :param description: The error description
        """
        self._errors[field] = self.error_class([description])
        del self.cleaned_data[field]

    def clear_errors(self):
        self._errors = {}

class LoginForm(BasicForm):
    email = forms.EmailField(max_length=50,validators=[validate_username_exists])
    setup_field(email,'Enter Email here')
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())
    setup_field(password,'Enter password here')

    def clean(self):
        """
        This is to make sure the password is valid for the given email.
        """
        cleaned_data = super(LoginForm,self).clean()
        username = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                self.mark_error('password','Incorrect password')
        return cleaned_data

class AccountRegisterForm(BasicForm):
    firstname = forms.CharField(label='First Name',max_length=50)
    setup_field(firstname,'Enter first name here')
    lastname = forms.CharField(label='Last Name', max_length=50)
    setup_field(lastname, 'Enter last name here')
    email = forms.EmailField(max_length=50, validators=[validate_username_available])
    setup_field(email, 'Enter email here')
    password_first = forms.CharField(label='Password', min_length=1, max_length=50, widget=forms.PasswordInput())
    setup_field(password_first, "Enter password here")
    password_second = forms.CharField(label='', min_length=1, max_length=50, widget=forms.PasswordInput())
    setup_field(password_second, "Enter password again")

    def clean(self):
        """This is to make sure both passwords fields have the same values in them. If they don't mark
        them as erroneous."""
        cleaned_data = super(AccountRegisterForm, self).clean()
        password_first = cleaned_data.get('password_first')
        password_second = cleaned_data.get('password_second')
        if password_first and password_second and password_first!=password_second:
            self.mark_error('password_second','Passwords do not match')
        return cleaned_data

class PasswordForm(BasicForm):
    password_current = forms.CharField(label='Current', max_length=50, widget=forms.PasswordInput())
    setup_field(password_current, 'Enter your current password here')
    password_first = forms.CharField(label='New', max_length=50, widget=forms.PasswordInput())
    setup_field(password_first, "Enter new password here")
    password_second = forms.CharField(label='', max_length=50, widget=forms.PasswordInput())
    setup_field(password_second, "Enter new password again")

    def clean(self):
        """
        This is to make sure both passwords fields have the same values in them. If they don't, mark
        them as erroneous. Also check if the current and new passwords are they same. If they are, then
        mark them as erroneous (we want different passwords).
        """
        cleaned_data = super(PasswordForm, self).clean()
        password_current = cleaned_data.get('password_current')
        password_first = cleaned_data.get('password_first')
        password_second = cleaned_data.get('password_second')
        if password_second and password_first:
            if password_second!=password_first:
                self.mark_error('password_second','Passwords do not match')
            if password_current and password_current == password_first:
                self.mark_error('password_current','Your current and new passwords must be different')
        return cleaned_data

class ProfileForm(BasicForm):
    firstname = forms.CharField(label='First Name', max_length=50)
    setup_field(firstname,'Enter first name here')
    lastname = forms.CharField(label='Last Name', max_length=50)
    setup_field(lastname, 'Enter last name here')
    sex = forms.ChoiceField(required=False, choices=Profile.GENDER)
    setup_field(sex)
    birthday = forms.DateField(required=False, validators=[validate_birthday])
    setup_field(birthday, 'Enter birthday as YYYY-MM-DD')
    phone = forms.CharField(required=False, max_length=10)
    setup_field(phone, 'Enter phone number here')
    allergies = forms.CharField(required=False, max_length=250)
    setup_field(allergies, 'Enter any allergies here')
    prefHospital = forms.ModelChoiceField(label="Preferred Hospital", required=False, queryset=Hospital.objects.all())
    setup_field(prefHospital)
    primaryCareDoctor = forms.ModelChoiceField(label="Primary Care Doctor", required=False,
                                               queryset=Account.objects.filter(role=Account.ACCOUNT_DOCTOR))
    setup_field(primaryCareDoctor)

    def assign(self,profile):
        profile.firstname = self.cleaned_data['firstname']
        profile.lastname = self.cleaned_data['lastname']
        profile.sex = self.cleaned_data['sex']
        if self.cleaned_data['birthday'] is not None:
            profile.birthday = self.cleaned_data['birthday']
        profile.phone = self.cleaned_data['phone']
        profile.allergies = self.cleaned_data['allergies']
        profile.prefHospital = self.cleaned_data['prefHospital']
        profile.primaryCareDoctor = self.cleaned_data['primaryCareDoctor']

class AppointmentForm(BasicForm):
    description = forms.CharField(required=True, max_length=50)
    setup_field(description,'Enter description here')
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
    setup_field(hospital)
    doctor = forms.ModelChoiceField(queryset=Account.objects.filter(role=Account.ACCOUNT_DOCTOR))
    setup_field(doctor)
    patient = forms.ModelChoiceField(queryset=Account.objects.filter(role=Account.ACCOUNT_PATIENT))
    setup_field(patient)
    startTime = forms.DateTimeField(label="Start Time")
    setup_field(startTime, "Enter as YYYY-MM-DD HH:MM")
    endTime = forms.DateTimeField(label="End Time")
    setup_field(endTime, "Enter as YYYY-MM-DD HH:MM")

    def assign(self, appointment):
        appointment.description = self.cleaned_data['description']
        appointment.hospital = self.cleaned_data['hospital']
        appointment.doctor = self.cleaned_data['doctor']
        appointment.patient = self.cleaned_data['patient']
        appointment.startTime = self.cleaned_data['startTime']
        appointment.endTime = self.cleaned_data['endTime']

    def generate(self):
        return Appointment(
            doctor = self.cleaned_data['doctor'],
            patient = self.cleaned_data['patient'],
            description = self.cleaned_data['description'],
            hospital = self.cleaned_data['hospital'],
            startTime = self.cleaned_data['startTime'],
            endTime = self.cleaned_data['endTime']
        )
    """
    This is a validator that checks if the appointment is conflicting with any other already
    made appointments
    """
    def clean(self):
        cleaned_data = super(AppointmentForm, self).clean()
        startTime = cleaned_data.get('startTime')
        endTime = cleaned_data.get('endTime')
        if startTime and endTime:
            if endTime<=startTime
                self.mark_error('endTime','The appointment end time must come after the start time')
        return cleaned_data

class EmployeeRegistrationForm(BasicForm):
    firstname = forms.CharField(label='First Name', max_length=50)
    setup_field(firstname,'Enter first name here')
    lastname = forms.CharField(label='Last Name', max_length=50)
    setup_field(lastname, 'Enter last name here')
    email = forms.EmailField(max_length=50, validators=[validate_username_available])
    setup_field(email, 'Enter email here')
    password_first = forms.CharField(label='Password', min_length=1, max_length=50, widget=forms.PasswordInput())
    setup_field(password_first, "Enter password here")
    password_second = forms.CharField(label='', min_length=1, max_length=50, widget=forms.PasswordInput())
    setup_field(password_second, "Enter password again")
    employee = forms.ChoiceField(required=False, choices=Account.EMPLOYEE_TYPES)
    setup_field(employee)

    def clean(self):
        """
        This is to make sure both passwords fields have the same values in them. If they don't mark
        them as errous.
        """
        cleaned_data = super(EmployeeRegistrationForm,self).clean()
        password_first = cleaned_data.get('password_first')
        password_second = cleaned_data.get('password_second')
        if password_first and password_second and password_first!=password_second
            self.mark_error('password_second','Passwords do not match')
        return cleaned_data