from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm

def index(request):
    return render(request, 'appTwo/index.html')

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users': user_list}
    # return render(request, 'appTwo/users.html', context=user_dict)
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
            
    return render(request, 'appTwo/users.html', {'form': form})
