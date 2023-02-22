from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Reviews, Rides, amount, booking, Adultpackage, Childpackage
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Account
from django.contrib.auth import login
from django.contrib import auth
from django.db.models import Q
from .forms import  BookForm, userupdateform
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control 
from django.contrib.auth.decorators import login_required
def index(request):
    obj=Rides.objects.all()
    review=Reviews.objects.all()
    context={'result':obj,'review':review}
    return render(request,'index.html',context)
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
        return redirect('register')
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
            return redirect('index')
        else:
            print(3)
            messages.success(request,"Invalid Credentials")
            return redirect('login')     
    return render(request,'login.html')  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('login')  
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
    if request.user.is_authenticated:    
        return render(request,'profile.html')
    else:

        return render(request,'login.html')
def profile_update(request):
    if request.method =='POST':
        u_form  = userupdateform(request.POST,instance=request.user)
        # p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() :
            u_form.save()
            # p_form.save()
            return redirect('profile')    
    else:
       u_form  = userupdateform(instance=request.user)    
    context={
        'u_form' : u_form,
         

    }
    return render(request,'profileupdate.html',context)


def booknow(request):
    if request.method == 'POST':
        print('1')
        date=request.POST['date']
        count1=request.POST['count1']
        count2=request.POST['count2']
        form = BookForm(request.POST)
        if form.is_valid():
            print("2")
            p1_id = form.cleaned_data['p1_id']
            p2_id = form.cleaned_data['p2_id']
            print(int(p2_id.price)*int(count2))
            b = booking(
                user=request.user,
                    date=date,
                    p1_id=p1_id,
                    p2_id=p2_id,
                    count_adult=count1,
                    count_child=count2,
                    total_price=(int(p1_id.price)*int(count1))+(int(p2_id.price)*int(count2))
                
                     )
          
            b.save()
          

            obj=booking.objects.filter(user=request.user)
            return render(request,'book.html',{
                'form': BookForm(),
                'success': True,
                'package' : obj,
            })
        print(1)
        
    else:
        form = BookForm()    
        
    return render(request,'book.html', {
        'form': BookForm(),
        
        
        
    })



def bookticket(request):
    # if request.method == 'POST':
    obj=Adultpackage.objects.all()
    child = Childpackage.objects.all()
    context={'result' : obj ,'child':child }
    return render(request,"bookticket.html",context)
    
def review(request):
    if request.method == "POST":
        usr = request.user
        title = request.POST.get('title')
        review = request.POST.get('review')
        user = Reviews(title=title,review=review,user=usr)
        user.save()
        messages.info(request, 'Your review has been successfully send..!!')
        return redirect('review')
    return render(request, 'mailbox-compose.html')


def service(request):
    if request.user.is_authenticated:
        obj=booking.objects.filter(user=request.user)
        context={'result' : obj }
        return render(request,'service.html',context)
    else:
        return render(request,'service.html')


def Delete(request,id):
    booking_info=booking.objects.filter(id=id)
    booking_info.delete()
    messages.info(request,"Deleted")
    return redirect("booknow")
# def success(request):
#         total_price=booking.objects.get(total_price)
#         total_amount = amount.objects.get(id=1)
#         total_amount.amount=total_amount.amount - total_price
#         total_amount.save()
#         messages.success(request,"Payment Sucessfull")
#         return render(request,'success.html')


def Delete(request, id):
    user = request.user
    cart = booking.objects.filter(user=user)
    if cart.exists():
        booking.objects.get(id=id).delete()
        messages.warning(request, "This product is removed ")
        # messages.info(request, "You don't have an active order")
        return render(request,'success.html')
    return redirect('service')