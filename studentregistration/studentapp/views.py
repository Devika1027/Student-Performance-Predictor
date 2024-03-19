from django.shortcuts import render,redirect
from studentapp.models import Student

# Create your views here.
def homePageView(request):
    return render(request=request, template_name = 'home.html',context={})
def aboutPageView(request):
    return render(request=request, template_name = 'about.html',context={})
def loginPageView(request):
    return render(request=request, template_name = 'login.html',context={})
def stloginPageView(request):
    return render(request=request, template_name = 'getsinglestudent.html',context={})
def adduserStudentView(request):
    return render(request=request, template_name = 'adduser.html',context={})
def saveStudentView(request):
    name=request.POST["name"]
    print("Name:",name)
    address=request.POST["address"]
    print("Address:",address)
    course=request.POST["course"]
    print("Course:",course)
    email=request.POST["email"]
    print("Email:",email)
    password=request.POST["password"]
    print("Password:",password)
    attendance=request.POST["attendance"]
    print("Attendance:", attendance)
    marks=request.POST["marks"]
    print("Serial Marks:",marks)
    student= Student(name=name,address=address,course=course,email=email,password=password,attendance=attendance,marks=marks)
    student.save()
    return redirect('adduser')
def getALLStudents(request):
    students=Student.objects.all()
    context={'allstudents':students}
    return render(request=request, template_name = 'allstudents.html',context=context)
def singleStudentView(request,student_id):
    student=Student.objects.get(pk=student_id)
    context={'singlestudent':student}
    return render(request=request, template_name = 'getsinglestudent.html',context=context)
def deleteStudentView(request,student_id):
    student=Student.objects.filter(pk=student_id)
    student.delete()
    return redirect('all')
def updateStudentView(request,student_id):
    student=Student.objects.filter(pk=student_id)
    student.update()
    return redirect('all')
def stlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Student.objects.get(email=email)
            if user.check_password(password):
                # Authentication successful, redirect to some page
                students = Student.objects.all()
                for student in students:
                    if student.email == email:
                        # Assuming you have a separate URL for individual student pages,
                        # and you're passing the student_id as a parameter in the URL
                        return redirect('getsinglestudent.html', student_id=student.id)
                else:
                    # Authentication failed, handle appropriately
                    return render(request, 'stlogin.html', {'error_message': 'Invalid credentials'})
            else:
                # Authentication failed, handle appropriately
                return render(request, 'stlogin.html', {'error_message': 'Invalid credentials'})
        except Student.DoesNotExist:
            # User with given email does not exist, handle appropriately
            return render(request, 'stlogin.html', {'error_message': 'User does not exist'})
    else:
        return render(request, 'stlogin.html')
