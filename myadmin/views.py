from django.shortcuts import render, redirect
from myadmin.models import *
from customer.forms import *
from django.contrib import auth,messages
# Create your views here.

def dashboard(request):
  context = {}
  return render(request, 'myadmin/dashboard.html', context)


def agencies(request):
  all_agencies = Profile.objects.filter(role=2)
  context = {'all_agencies':all_agencies}
  return render(request, 'myadmin/agencies.html', context)

def customer_profile(request, id):
  user = Profile.objects.get(pk=id)
  context = {'user':user}
  return render(request, 'myadmin/customer_profile.html', context)

def customer(request):
  customers = Profile.objects.filter(role=3)
  context = {'customers':customers}
  return render(request, 'myadmin/customer.html', context)

def myadmin_login(request):
  context = {}
  return render(request, 'myadmin/myadmin_login.html', context)

def logout(request):
  auth.logout(request)
  return redirect('/myadmin/myadmin_login/')

def login_check(request):
  myusername = request.POST['username']
  mypassword = request.POST['password']
  result = auth.authenticate(username=myusername,password=mypassword)
  if result is None:
    messages.success(request,'Invalid Username or Password')
    return redirect('/myadmin/myadmin_login/')
  else:
    auth.login(request,result)
    return redirect('/myadmin/dashboard/')

def order_details(request, id):
  ords= OrderItems.objects.filter(order_id=id)
  context = {'ords':ords}
  return render(request, 'myadmin/order_details.html', context)

def orders(request):
  ords = Orders.objects.all()
  context = {'ords':ords}
  return render(request, 'myadmin/orders.html', context)

def profile(request, id):
  agency = Profile.objects.get(pk=id)
  context = {'agency':agency}
  return render(request, 'myadmin/profile.html', context)

def view_agency(request):
  context = {}
  return render(request, 'myadmin/view_agency.html', context)

def view_feedback(request):
  feedbacks = Feedback.objects.all()
  context = {'feedbacks':feedbacks}
  return render(request, 'myadmin/view_feedback.html', context)



def view_inquiry(request):
  all_inquiry = Inquiry.objects.all()
  context = {'all_inquiry':all_inquiry}
  return render(request, 'myadmin/view_inquiry.html', context)


# ---------- State ------------
def add_state(request):
  if request.method == 'POST':
    state = request.POST['state']
    State.objects.create(state=state)
    return redirect('view_state')
  context = {}
  return render(request, 'myadmin/add_state.html', context)

def edit_state(request, id):
  state = State.objects.get(pk=id)
  context = {'state':state}
  return render(request, 'myadmin/edit_state.html', context)

def update_state(request, id):
  state = request.POST['state']
  State.objects.update_or_create(pk=id, defaults={'state':state})
  return redirect('view_state')

def delete_state(request, id):
  State.objects.get(pk=id).delete()
  return redirect('view_state')

def view_state(request):
  state = State.objects.all()
  context = {'state':state}
  return render(request, 'myadmin/view_state.html', context)


# ---------- City ------------
def add_city(request):
  state = State.objects.all()
  if request.method == 'POST':
    state = request.POST['state']
    city = request.POST['city']
    City.objects.create(state_id=int(state), city=city)
    return redirect('view_city')
  context = {'state':state}
  return render(request, 'myadmin/add_city.html', context)

def edit_city(request, id):
  state = State.objects.all()
  city = City.objects.get(pk=id)
  context = {'city':city, 'state':state}
  return render(request, 'myadmin/edit_city.html', context)

def update_city(request, id):
  state = request.POST['state']
  city = request.POST['city']
  City.objects.update_or_create(pk=id, defaults={'state_id':int(state), 'city':city})
  return redirect('view_city')

def delete_city(request, id):
  City.objects.get(pk=id).delete()
  return redirect('view_city')

def view_city(request):
  city = City.objects.all()
  context = {'city':city}
  return render(request, 'myadmin/view_city.html', context)


# ---------- Area ------------
def add_area(request):
  state = State.objects.all()
  city = City.objects.all()
  if request.method == 'POST':
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area']
    Area.objects.create(state_id=int(state), city_id=int(city), area=area)
    return redirect('view_area')
  context = {'state':state, 'city':city}
  return render(request, 'myadmin/add_area.html', context)

def edit_area(request, id):
  state = State.objects.all()
  city = City.objects.all()
  area = Area.objects.get(pk=id)
  context = {'area':area, 'state':state, 'city':city}
  return render(request, 'myadmin/edit_area.html', context)

def update_area(request, id):
  state = request.POST['state']
  city = request.POST['city']
  area = request.POST['area']
  Area.objects.update_or_create(pk=id, defaults={'state_id':int(state), 'city_id':int(city),'area':area})
  return redirect('view_area')

def delete_area(request, id):
  Area.objects.get(pk=id).delete()
  return redirect('view_area')

def view_area(request):
  area = Area.objects.all()
  context = {'area':area}
  return render(request, 'myadmin/view_area.html', context)

def myadmin_change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_login')
  
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'myadmin/myadmin_change_password.html', {'form':form})