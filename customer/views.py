from django.http import HttpResponse
from django.shortcuts import redirect, render
from razorpay import Order
from myadmin.models import *
from django.contrib import auth
import razorpay
from django.views.decorators.csrf import csrf_exempt
from customer.forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

# ------------ Agency ----------
def tiffin_register(request):
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
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    address = request.POST['address']
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area']
    certified = request.POST['certified']
    gst_no = request.POST['gst_no']
    image = request.FILES['image']

    if password == cpassword:
      user = User.objects.create_user(username=name, email=email, password=password)

      Profile.objects.create(user=user, role_id=2, description=description, contact=contact, owner_name=owner_name, owner_number=owner_number, address=address, state_id=int(state), city_id=int(city), area_id=int(area), certified=certified, gst_no=gst_no, image=image)

      
      #End By me
      return redirect('user_login')
    else:
      print('error')

  context = {'state':state, 'city':city, 'area':area}
  return render(request, 'customer/tiffin_register.html', context)



# ------------ Customer ----------
def register(request):
  state = State.objects.all()
  city = City.objects.all()
  if request.method == 'POST':
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    address = request.POST['address']
    state = request.POST['state']
    city = request.POST['city']
    image = request.FILES['image']

    if password == cpassword:
      user = User.objects.create_user(username=name, email=email, password=password)

      Profile.objects.create(user=user, role_id=3, gender=gender, dob=dob, contact=contact, address=address, state_id=int(state), city_id=int(city), image=image)
      #addedd by me
      subject = 'Welcome to GJ Dabbawala'
      body = f"Dear {name},\n\nWelcome to GJ Dabbawala! We are excited to have you as a member.\n\nThank you for joining us!\n\nBest regards,\nGJ Dabbawala Team"

            # Set up SMTP connection
      smtp_server = 'smtp.gmail.com'
      smtp_port = 587  # Update with your SMTP server port
      sender_email = 'henil2705@gmail.com'  # Update with your email
      sender_password = 'rrpojgqhbcheoxih'  # Update with your email password
      receiver_email = email

      msg = MIMEMultipart()
      msg['From'] = sender_email
      msg['To'] = receiver_email
      msg['Subject'] = subject

      msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server
      with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
        #end by me
      return redirect('user_login')
    else:
      print('error')

  context = {'state':state, 'city':city}
  return render(request, 'customer/register.html', context)

def edit_profile(request):
  state = State.objects.all()
  city = City.objects.all()
  profile = Profile.objects.filter(user=request.user).first() 
  context = {'state':state, 'city':city, 'profile':profile}
  return render(request, 'customer/edit_profile.html', context)


def update_profile(request, id):
  profile = Profile.objects.get(pk=id)
  name = request.POST.get('name')
  gender = request.POST.get('gender')
  if request.POST.get('dob'):
    dob = request.POST['dob']
  else:
    dob = profile.dob
  email = request.POST.get('email')
  contact = request.POST.get('contact')
  address = request.POST.get('address')
  state = request.POST.get('state')
  print(state)
  city = request.POST.get('city')
  if request.POST.get('image'):
    image = request.POST['image']
  else:
    image = profile.image

  User.objects.update_or_create(pk=request.user.id, defaults={'username':name, 'email':email})
  Profile.objects.update_or_create(pk=id, defaults={'gender':gender, 'dob':dob, 'contact':contact, 'address':address, 'state_id':int(state), 'city_id':int(city), 'image':image})
  return redirect('edit_profile')

def user_login(request):
  if request.method == 'POST':
    username = request.POST['name']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      if user.profile.role_id == 3:
        return redirect('customer_home')
      elif user.profile.role_id == 2:
        return redirect('agency_dashboard')
      elif user.profile.role_id == 1:
        return redirect('dashboard')
        
    else:
      print('Invalid username and password')
  
  context = {}
  return render(request, 'customer/user_login.html', context)


def user_logout(request):
  auth.logout(request)
  return redirect('user_login')



def customer_home(request):
  agency = Profile.objects.filter(role=2)
  state = State.objects.all()
  city = City.objects.all()
  area = Area.objects.all()
  st, ct, ar = 0, 0, 0

  if request.method == 'POST':
    st = int(request.POST['state'])
    ct = int(request.POST['city'])
    ar = int(request.POST['area'])
    agency = Profile.objects.filter(state_id=st, city_id=ct,area_id=ar)
  context = {'state':state, 'city':city, 'area':area, 'agency':agency, 'st':st, 'ct':ct, 'ar':ar}
  return render(request, 'customer/index.html', context)

def change_pass(request):
  context = {}
  return render(request, 'customer/change_pass.html')

def gallery(request):
  context = {}
  return render(request, 'customer/gallery.html')

def shopping_cart(request):
  customer = Profile.objects.filter(user=request.user).first()
  cart_foods = Cart.objects.filter(user=request.user)
  
  tot_ord_price = 0
  for i in cart_foods:
    tot_ord_price += i.price * i.quantity
  
  if request.method == 'POST':
    tot_price = request.POST['tot_price']
    sname = request.POST['sname']
    semail = request.POST['semail']
    scontact = request.POST['scontact']
    saddress = request.POST['saddress']

    agency = Profile.objects.filter(user=cart_foods[0].food.agency.user).first()
    ord = Orders.objects.create(user=request.user, agency=agency, total_price=tot_price)
    
    TiffinDeliveryAddress.objects.create(user=customer, order=ord, username=sname, email=semail, contact=scontact, address=saddress)

    method = request.POST['method']
    if method == 'Card':
      key_id = 'rzp_test_Q13PoItwfR4lPG'
      key_secret = 'TbWbzaVxyCnR8aeA8d3iaz0I'


      client = razorpay.Client(auth=(key_id, key_secret))

      data = {
          'amount': float(tot_price)*100,
          'currency': 'INR',
          "receipt":"GJ Dabbawala",
          "notes":{
              'name' : request.user.username,
              'payment_for':'GJ Dabbawala'
          }
      }
      payment = client.order.create(data=data)
      context = {'payment' : payment, 'customer':customer}
      return render(request, 'customer/order.html',context)
    elif method == 'COD':
      return redirect('success')

  context = {'cart_foods':cart_foods, 'tot_ord_price':tot_ord_price, 'customer':customer}
  return render(request, 'customer/shopping_cart.html', context)


def update_quantity(request):
    cart_id = request.POST['food_id']
    cart = Cart.objects.get(pk=cart_id)
    quantity = request.POST['quantity']
    Cart.objects.update_or_create(pk=cart_id,defaults={'quantity':quantity, 'total_price':cart.total_price*int(quantity)})
    return HttpResponse(1)

@login_required(login_url='success')
@csrf_exempt
def success(request):
  cart_foods = Cart.objects.filter(user=request.user)
  ord = Orders.objects.filter(user=request.user).last()

  for cf in cart_foods:
    OrderItems.objects.create(order=ord, food=cf.food, fname=cf.fname, ftime=cf.ftime,price=cf.total_price, quantity=cf.quantity)
    Cart.objects.filter(pk=cf.id).first().delete()
  order = Orders.objects.filter(id=ord.id).last()
  order.status = 'Delivered'
  order.save()
  
  return render(request, 'customer/success.html')

def add_to_cart(request, id):
  food = Food.objects.get(pk=id)
  fname = food.fname
  ftime = food.ftime
  price = food.fprice
  quantity = 1
  total_price = quantity * price
  if not Cart.objects.filter(food_id=id, user=request.user).exists():
    Cart.objects.create(user=request.user, food=food, fname=fname, ftime=ftime, price=price, quantity=quantity, total_price=total_price)
    
  return redirect('shopping_cart')



def remove_from_cart(request, id):
  Cart.objects.get(pk=id).delete()
  return redirect('shopping_cart')



def services_search(request):
  context = {}
  return render(request, 'customer/services_search.html')

def services(request):
  context = {}
  return render(request, 'customer/services.html')


def single(request):
  context = {}
  return render(request, 'customer/single.html')





def view_more_details(request, id):
  lunch_foods = Food.objects.filter(agency_id=id, ftime='Lunch')
  dinner_foods = Food.objects.filter(agency_id=id, ftime='Dinner')
  context = {'lunch_foods':lunch_foods, 'dinner_foods':dinner_foods}
  return render(request, 'customer/view_more_details.html', context)

def order(request):
  context = {}
  return render(request, 'customer/order.html')


def profile(request):
  context = {}
  return render(request, 'customer/profile.html')

def blog(request):
  context = {}
  return render(request, 'customer/blog.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    subject = request.POST['subject']
    message = request.POST['message']

    Inquiry.objects.create(name=name, email=email, contact=contact, subject=subject, message=message)
  context = {}
  return render(request, 'customer/contact.html', context)

def feedback(request):
  if request.method == 'POST':
    review = int(request.POST['review'])
    feedback = request.POST['feedback']
    user = Profile.objects.filter(user=request.user).first()
    Feedback.objects.create(user=user, review=review, feedback=feedback)
  context = {}
  return render(request, 'customer/feedback.html', context)

def about(request):
  context = {}
  return render(request, 'customer/about.html', context)

def customer_orders(request):
  ords = Orders.objects.filter(user=request.user)
  context = {'ords':ords}
  return render(request, 'customer/customer_orders.html', context)

def customer_order_details(request, id):
  ords= OrderItems.objects.filter(order_id=id)
  context = {'ords':ords}
  return render(request, 'customer/customer_order_details.html', context)




def customer_change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
  
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'customer/customer_change_password.html', {'form':form})