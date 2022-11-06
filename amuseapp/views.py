# from .forms import *
from django.shortcuts import render,redirect
from .models import Rides
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Account, Profile
from django.contrib.auth import login
from django.contrib import auth
from .forms import userupdateform,profileUpdateForm

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control 

def index(request):
    obj=Rides.objects.all()
    context={'result':obj}
    return render(request,'index.html',context)


# Create your views here.
# def index(request):
#     if 'search' in request.GET:
#         search = request.GET['search']
#         product = Product.objects.filter(name__icontains=search)
#     else:
#         product = Product.objects.all()
#     categories = Category.objects.all()
#     obj = Deals.objects.all()
#     data = {'product':product, 'categories':categories, 'result':obj}
#     return render(request, 'index.html')


# def showcategory(request, cid):
#     categories = Category.objects.all()
#     cats = Category.objects.get(pk=cid)
#     product = Product.objects.filter(cat=cats)
#     data = {
#         'categories':categories,
#         'product':product
#     }
#     return render(request, 'index.html', data)


    # if request.method == 'GET':
    #     category_id = request.GET.get('category_id')
    #     #print(category_id)
    #     product = Product.objects.filter(Q(cat=category_id)).values()
    #     # for p in product:
    #     #     #product = p.values()
    #     product=json.dumps(list(product.values()))
    #     print(product)
    #         #print(product)
    #     data ={
    #         'product':product,
    #     }
    #     print(data)
    #     return JsonResponse(data)
    #     #print(data)    

    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            # if Account.objects.filter(username=username).exists():
            #     messages.info(request,"Username Already Exists")
            #     return redirect('register.html')
            if Account.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('register.html') 
            else:    
                user = Account.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
                user.save()   
                messages.success(request, 'Thank you for registering with us.Please Activate your Email id.') 
                current_site = get_current_site(request)
                message = render_to_string('Account_verification.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

        send_mail(
                'Please activate your account',
                message,
                'dreamlandpark2705@gmail.com',
                [email],
                fail_silently=False,
            )
        
        return redirect(login)
          
        
    return render(request, 'register.html') 
            
            
            
            
            
            
            
            
            
    #         return redirect('register.html')
    #     else:
    #         messages.info(request,"password not match")
    #         return redirect('register')
    # return render(request, 'register.html')    
        








def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        print(email)
        user = authenticate(email=email ,password=password)
        print(user)
        print(email,password)
        if user :
            print(email,password)
            auth.login(request, user)
            #save email in session
            request.session['email'] = email
            return redirect('index.html')
        else:
            print(3)
            messages.success(request,"Invalid Credentials")
            return redirect('login')     
    return render(request,'login.html')  


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('login')  
# def logout(request):
#     if 'username' in request.session:
#         request.session.flush()
#     return redirect('login')

# def home(request):
#     if 'username' in request.session:
#         username=request.session['username']
#         obj=Rides.objects.all()
#         object={'result':obj,'name':username}
#         return render(request,'index.html',object)
#     return redirect('login')


def Ticket(request):
    
    return render(request,'Ticket')


def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        cpassword = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)

        if success:
            if new_password==cpassword:
                 user.set_password(new_password)
                 user.save()
                 messages.success(request, 'Password updated successfully.')
                 return redirect('login')
            else:
                 messages.error(request, 'Password does not match!')
                 return redirect('change_password')
    return render(request, 'change/change_password.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email


            current_site = get_current_site(request)
            message = render_to_string('ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'dreamlandpark2705@gmail.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'Forgot_Password.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'ResetPassword.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register.html')


def profile(request):
    # if request.method == 'POST':
    if request.user.is_authenticated:
        u_form=userupdateform(request.POST,instance=request.user)
        p_form=profileUpdateForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Congratulations! Your account ha been Updated.')
            return redirect('profile')
    else:
         u_form=userupdateform(instance=Account.objects.get(email=request.session.get('email')))
         p_form= profileUpdateForm(instance= Profile.objects.get(user=Account.objects.get(email=request.session.get('email')).id))
    context = {
            'u_form':u_form,
            'p_form':p_form
        }
    return render(request,'profile.html',context)
    # else:
    #     return render(request,'login.html')


