from django import forms

from studentssms.models import Student, Course, Teacher


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    role = forms.CharField(max_length=100)  # 确保在表单中定义了role字段
    # Add any additional validation or custom methods as needed

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # 可以添加更多的字段验证规则，例如：
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'teacher', 'start_date', 'end_date', 'classroom']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }
class ExamForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    classroom = forms.CharField(max_length=50)


# class StudentForm(forms.ModelForm):
#     courses = forms.CharField(required=False)
#     # email = forms.EmailField(required=False)
#
#     class Meta:
#         model = Student
#         fields = ['name', 'age', 'gender', 'email', 'courses', 'address']
#         # fields = '__all__'
#         # exclude = ['courses']
#         # widgets = {
#         #     'name': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'age': forms.TextInput(attrs={'class': 'form-control'}),