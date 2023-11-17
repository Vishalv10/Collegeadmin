from django.shortcuts import render,redirect
from app1.models import Course,Student,Teacher
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404




def login(request):
    return render(request,'login.html')


def addcourse(request):
    return render(request,'addcourse.html')


def addcourse1(request):
    if request.method == "POST":
        course_name=request.POST['course_name']
        fee=request.POST['fee']
        course=Course(course_name=course_name,fee=fee)
        course.save()
        return redirect('admin1')
    

def addstudent(request):
    courses=Course.objects.all()
    return render(request,'addstudent.html',{"course":courses})

def addstudent1(request):
    if request.method == "POST":
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        joining_date=request.POST['date']
        print(joining_date)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(student_name=student_name,address=student_address,age=age,joining_date=joining_date,course=course1)
        student.save()
        return redirect('admin1')


def studentdetails(request):
    student = Student.objects.all()
    print(student)
    return render(request, "studentdetails.html", {"students": student})


def editpage(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses = Course.objects.all()
    return render(request, 'editstudent.html', {'student': student, 'courses': courses})

def updatestudent(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(pk=student_id)
        student.student_name = request.POST['name']
        student.address = request.POST['address']
        student.age = request.POST['age']
        student.joining_date = request.POST['date']
        student.course_id = request.POST['sel']
        student.save()
        return redirect('/studentdetails')


    student = Student.objects.get(pk=student_id)
    courses = Course.objects.all()
    return render(request, 'editstudent.html', {'student': student, 'courses': courses})


def deletepage(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/studentdetails')



def admin1(request):
    return render(request,'admin.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth_login(request,user)
                return redirect('admin1')
            else:
            # request.session['uid']=user.id
                auth.login(request,user)
                # messages.info(request, f'Welcome {username}')
                return redirect('teacheradmin')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    # request.session['uid']=''
    # if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')


def showteacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'showteacherdetails.html', {'teachers': teachers})


def teacher(request):
    courses = Course.objects.all()
    return render(request, 'teacher.html', {"course": courses})

def addteacher(request):
    if request.method == "POST":
        # Get data from the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        address = request.POST.get('address')
        age = request.POST.get('age')
        email = request.POST.get('email')
        course_id = request.POST.get('sel')  # Fix here
        photo = request.FILES.get('photo')  # Use FILES to get uploaded files

        # Check if the password and confirm password match
        if password == cpassword:
            # Create a User object for authentication
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email
            )
            user.save()

            # Create a Teacher object to store additional information
            course = Course.objects.get(id=course_id)
            teacher = Teacher(
                user=user,  # Assign the user as a foreign key
                address=address,
                age=age,
                contact_number=request.POST.get('contact_number'),  # adjust this as per your form
                course=course,
                photo=photo
            )
            teacher.save()

            messages.success(request, "Teacher registered successfully.")
            return redirect('login')

        else:
            messages.error(request, "Password and Confirm Password do not match.")
            return redirect('teacher')

    courses = Course.objects.all()
    return render(request, 'teacher.html', {"course": courses})



@login_required
def showteacherdetails(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'showteacherdetails.html', {'teacher': teacher})
    
    
@login_required(login_url='login') 
def editteacher(request, teacher_id):
    teacher, created = Teacher.objects.get_or_create(user=request.user, defaults={})
    courses = Course.objects.all()
    # teacher = Teacher.objects.get(user=request.user, pk=teacher_id)
    # courses = Course.objects.all()
    return render(request, 'editteacher.html', {'teacher': teacher, 'courses': courses})

def update_teacher(request, teacher_id):
    if request.method == "POST":
        teacher = Teacher.objects.get(pk=teacher_id)
        teacher.user.first_name = request.POST['first_name']
        teacher.user.last_name = request.POST['last_name']
        teacher.user.username = request.POST['username']
        teacher.age = request.POST['age']
        teacher.address = request.POST['address']
        teacher.contact_number = request.POST['contact_number']
        teacher.course_id = request.POST['sel']

        # Check if a new photo is uploaded
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']

        teacher.user.save()
        teacher.save()

        messages.success(request, "Teacher information updated successfully.")
        return redirect('show_teacher_details')

    teacher = Teacher.objects.get(pk=teacher_id)
    courses = Course.objects.all()
    return render(request, 'editteacher.html', {'teacher': teacher, 'courses': courses})

def deleteteacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    user = teacher.user
    user.delete()
    teacher.delete()
    messages.success(request, "Teacher deleted successfully.")
    return redirect('teacherdetails')

def teacherdetails(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacherdetails.html', {'teachers': teachers})

def teacheradmin(request):
    teacher = Teacher.objects.first()
    return render(request, 'teacheradmin.html', {'teacher': teacher})
