from django.shortcuts import redirect, render
from accounts.models import Account
from employee.models import Employee
from contract.models import Contract
from payment_history.models import Payment_history
from recent_trades.models import Recent_Trades
from avg_trade_quantity.models import Avg_trade_quantity
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout as django_logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from accounts.tokens import account_activation_token
from django.utils.translation import gettext_lazy as _
def index(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,    
    } 
    
    return render(request,'pages/index.html',context)


def about(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    } 
    return render(request,'pages/about.html',context)


def contract(request):
    contract = Contract.objects.all()
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
        'contract': contract
        
    } 
    
    return render(request,'pages/contract.html',context)



    


def investment(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    } 
    return render(request,'pages/investment.html',context)


def news(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    } 
    return render(request,'pages/news.html',context)

def setting(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    } 
    return render(request,'pages/setting.html',context)


def bank(request):
    accounts = Account.objects.all()
    payment_history = Payment_history.objects.all()

    context = {
        'payment_history': payment_history,
        'accounts': accounts
    }


    return render(request,'pages/bank.html',context)

def dashboard(request):
    accounts= Account.objects.all()
    employee = Employee.objects.all()
    avgtrade = Avg_trade_quantity.objects.all()
    recenttrade = Recent_Trades.objects.all()
    
    context = {
        'accounts': accounts,
        'employee': employee,
        'avgtrade': avgtrade,
        'recenttrade': recenttrade 
    }
    return render(request,'pages/dashboard.html',context)

    
def contractprofit(request):
    contract = Contract.objects.all()
    accounts = Account.objects.all()
    context = {
        'contract': contract,
        'accounts': accounts
        
    } 

    return render(request,'pages/contractprofit.html',context)





def profile(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    }


    return render(request,'pages/profile.html',context)    


def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('index')
    else:
        return render(request,'pages/index.html')    


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('index')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('index')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your Account"
    message = render_to_string("accounts/template_activate_account.html",{
        'user':user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol":'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():  
        messages.success(request,f'Dear user please go to your email and confirm your account.',)
    else:
        message.error(request,f'Problem sending email to {to_email}')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname_signup']
        last_name = request.POST['lastname_signup']
        email = request.POST['email_signup']
        username = request.POST['username_signup']
        password = request.POST['password_signup']
        password2 = request.POST['password2_signup']
        title = request.POST['title_signup']
        country = request.POST['country_signup']
        language = request.POST['language_signup']
        phone = request.POST['phone_signup']
    
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username has been taken')
                return redirect('index')
            # else:
            #     if User.objects.filter(email=email).exists():
            #         messages.error(request, 'email has been taken')
            #         return redirect('index')
            else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name) 
                    user.is_active=False
                    user.save()
                    account = Account.objects.create(accountname = username,title=title, country=country,language=language,phone=phone)
                    account.save()
                    activateEmail(request, user, email)
                    return redirect('index')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('index')

    else:
        return render(request,'pages/index.html') 
def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or password is not correct')
            return redirect('index')
    else:
            return render(request,'pages/index.html')
    