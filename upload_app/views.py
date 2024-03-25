from django.shortcuts import render, redirect
from .models import *
import pandas as pd
from .form import UserForm
from django.http import JsonResponse
from django.http import HttpResponse
global email

def homepage(request):
    return render(request=request, template_name= 'home.html',)
def menupage(request):
    return render(request=request, template_name='index.html')

def create_db(file_path,email):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        Company.objects.create(
            company_name=l[1],
            year_founded=l[3],
            industry=l[4],
            city=l[6].split(',')[0],
            state=l[6].split(',')[1],
            country=l[7],
            current_emp=l[9],
            total_emp=l[10],
            email=email
        )
def uploadpage(request):
    email = request.user.email
    if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file=file,email=email)
        create_db(obj.file,email)
        # return JsonResponse({'message': 'File uploaded successfully'})
    return render(request=request, template_name='upload.html')
def userpage(request):
    users = User.objects.all()
    # msg = None
    if(request.GET.get('source') == 'add_user'):
        msg = 'New user added'
        request.session['message'] = msg
    return render(request=request, template_name='user.html', context={'users':users})
def add_user(request):
    if request.method == "GET":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_user/')
        return render(request, 'add_user.html', {'form': form})
    else:
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email']
        )
        return redirect('/user/?source=add_user')
    # return render(request, 'add_user.html', {'form':form})
def delete_user(request,id):
    try:
        obj = User.objects.get(id=id)
        obj.delete()
        return redirect('/user/')
    except Exception as ex:
        print(ex)
def builderpage(request):
    company = Company.objects.filter(email=request.user.email)
    return render(request=request, template_name='builder.html', context={'company':company})
def add_query(request):
    company = Company.objects.all()
    if request.method=='POST':
        Query.objects.create(
            keyword=request.POST['keyword'],
            industry = request.POST['industry'],
            year_founded = request.POST['year_founded'],
            state = request.POST['state'],
            country = request.POST['country'],
            total_emp = request.POST['total_emp'],
            current_emp = request.POST['current_emp']
        )
        filtered_data = Query.objects.filter(keyword=request.POST['keyword'],
                                             industry=request.POST['industry'],
                                             year_founded=request.POST['year_founded'],
                                             state=request.POST['state'],
                                             country=request.POST['country'],
                                             total_emp = request.POST['total_emp'],
                                            current_emp = request.POST['current_emp'])
        count= filtered_data.count()
        return render(request=request, template_name='builder.html', context={'count': count})
    return render(request, 'builder.html', context={'company': company})