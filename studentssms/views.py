from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, StudentForm, CourseForm, TeacherForm, ExamForm
from .models import Student, Course, Teacher, Exam

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            if User.objects.filter(username=username).exists():
                # 用户已存在，重定向到登录页面
                return redirect('login')
            else:
                # 创建新用户并保存到数据库
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()


            # 根据角色选择跳转到相应页面
            if role == 'student':
                # 跳转到学生页面
                return redirect('students')  # 使用URL名称而不是HTML文件名
            elif role == 'teacher':
                # 跳转到老师页面
                return redirect('teachers')  # 使用URL名称而不是HTML文件名

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    # 处理登录表单提交
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 登录成功后重定向到Home页面
            return redirect('home')

        else:
            # 处理登录失败的情况
            # ...
            return HttpResponse('登录失败，请检查输入的用户名和密码！')


    # 渲染登录页面
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('home')
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Student saved successfully.')  # 添加调试输出
            return redirect('students')
        else:
            print('Form errors:', form.errors)  # 添加调试输出
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('students')

def courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            print('Course saved successfully.')  # 添加调试输出
            return redirect('courses')
        else:
            print('Form errors:', form.errors)  # 添加调试输出
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.delete()
    return redirect('courses')

def teachers_view(request):
    return render(request, 'teachers.html')

def exams_view(request):
    return render(request, 'exams.html')

# Add other view functions for other pages here
def add_teacher(request):
    teacher = Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            print('Teacher saved successfully.')

    return render(request, 'add_teachers.html', {'teachers': teacher})


def delete_teacher(request, teacher_id=None):
    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.delete()
    return redirect('teachers')


def edit_teacher(request, teacher_id=None):
    teacher = Teacher.objects.get(pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form, 'teacher': teacher})


def add_exam(request):
    exam = Exam.objects.all()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            print('Exam saved successfully.')
    return render(request, 'add_exams.html', {'exams': exam})



def edit_exam(request, exam_id=None):
    exam = Exam.objects.get(pk=exam_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exams')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'edit_exam.html', {'form': form, 'exam': exam})


def delete_exam(request, exam_id=None):
    exam = Exam.objects.get(pk=exam_id)
    exam.delete()
    return redirect('exams')
