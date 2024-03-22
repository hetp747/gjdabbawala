from django.shortcuts import redirect, render
from myadmin.models import *
from django.contrib import auth
from customer.forms import *
# Create your views here.


def agency_dashboard(request):
  context = {}
  return render(request, 'agency/agency_dashboard.html', context)

# ------ Food Category ------------
def add_foodcategory(request):
  if request.method == 'POST':
    name = request.POST['name']
    FoodCategory.objects.create(agency= Profile.objects.filter(user=request.user).first(),name=name)
    return redirect('view_foodcategory')
  context = {}
  return render(request, 'agency/add_foodcategory.html', context)

def edit_foodcategory(request, id):
  food_cat = FoodCategory.objects.get(pk=id)
  context = {'food_cat':food_cat}
  return render(request, 'agency/edit_foodcategory.html', context)

def update_foodcategory(request, id):
  name = request.POST['name']
  FoodCategory.objects.update_or_create(pk=id, defaults={'name':name})
  return redirect('view_foodcategory')

def delete_foodcategory(request, id):
  FoodCategory.objects.get(pk=id).delete()
  return redirect('view_foodcategory')

def view_foodcategory(request):
  agency = Profile.objects.filter(user=request.user).first()
  food_cat = FoodCategory.objects.filter(agency=agency)
  context = {'food_cat':food_cat}
  return render(request, 'agency/view_foodcategory.html', context)


# ---------- Food ------------
def add_food(request):
  agency = Profile.objects.filter(user=request.user).first()
  food_cat = FoodCategory.objects.filter(agency=agency)
  if request.method == 'POST':
    ftime = request.POST['ftime']
    fname = request.POST['fname']
    fprice = request.POST['fprice']
    description = request.POST['description']
    fimage = request.FILES['fimage']
    ftype = FoodCategory.objects.get(pk=int(request.POST['ftype']))
    roti = request.POST['roti']
    rise = request.POST['rise']
    veg = request.POST['veg']
    butter_milk = request.POST['butter_milk']
    papad = request.POST['papad']
    agency = Profile.objects.filter(user=request.user).first()

    Food.objects.create(agency=agency, ftime=ftime, fname=fname, fprice=fprice, description=description, fimage=fimage, ftype=ftype, roti=roti, veg=veg, rise=rise, butter_milk=butter_milk, papad=papad)

    return redirect('view_food')
  context = {'food_cat':food_cat}
  return render(request, 'agency/add_food.html', context)

def edit_food(request, id):
  food = Food.objects.get(pk=id)
  food_cat = FoodCategory.objects.all()  
  context = {'food':food, 'food_cat':food_cat}
  return render(request, 'agency/edit_food.html', context)

def update_food(request, id):
  food = Food.objects.get(pk=id)
  ftime = request.POST['ftime']
  fname = request.POST['fname']
  fprice = request.POST['fprice']
  description = request.POST['description']
  if request.FILES.get('fimage', False):
    fimage = request.FILES['fimage']
  else:
    fimage = food.fimage
  ftype = FoodCategory.objects.get(pk=int(request.POST['ftype']))
  roti = request.POST['roti']
  rise = request.POST['rise']
  veg = request.POST['veg']
  butter_milk = request.POST['butter_milk']
  papad = request.POST['papad']

  Food.objects.update_or_create(pk=id,  defaults={ 'ftime':ftime, 'fname':fname, 'fprice':fprice, 'description':description, 'fimage':fimage, 'ftype':ftype, 'roti':roti, 'veg':veg, 'rise':rise, 'butter_milk':butter_milk, 'papad':papad})

  return redirect('view_food')


def view_food(request):
  agency = Profile.objects.filter(user=request.user).first()
  food = Food.objects.filter(agency=agency)
  context = {'food':food}
  return render(request, 'agency/view_food.html', context)

def delete_food(request, id):
  Food.objects.get(pk=id).delete()
  return redirect('view_food')


def agency_order_details(request, id):
  ords= OrderItems.objects.filter(order_id=id)
  context = {'ords':ords}
  return render(request, 'agency/agency_order_details.html', context)

def agency_orders(request):
  usr = Profile.objects.filter(user=request.user).first()
  ords = Orders.objects.filter(agency=usr)
  context = {'ords':ords}
  return render(request, 'agency/agency_orders.html', context)


def agency_profile(request):
  agency = Profile.objects.filter(user=request.user).first() 
  state = State.objects.all()
  city = City.objects.all()
  area = Area.objects.all()
  if request.method == 'POST':
    name = request.POST['name']
    description = request.POST['description']
    email = request.POST['email']
    contact = request.POST['contact']
    owner_name = request.POST['owner_name']
    owner_number = request.POST['owner_number']
    address = request.POST['address']
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area']
    certified = request.POST['certified']
    gst_no = request.POST['gst_no']
    if request.FILES.get('image', False):
      image = request.FILES['image']
    else:
      image = agency.image

    User.objects.update_or_create(pk=request.user.id, defaults={'username':name, 'email':email})

    Profile.objects.update_or_create(pk=agency.id, defaults={'description':description, 'contact':contact, 'owner_name':owner_name, 'owner_number':owner_number, 'address':address, 'state_id':int(state), 'city_id':int(city), 'area_id':int(area), 'certified':certified, 'gst_no':gst_no, 'image':image})

    return redirect('agency_profile')
  context = {'state':state, 'city':city, 'area':area, 'agency':agency}
  return render(request, 'agency/agency_profile.html', context)

def agency_change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_login')
  
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'agency/agency_change_password.html', {'form':form})

