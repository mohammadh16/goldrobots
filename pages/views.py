from django.shortcuts import redirect, render
from accounts.models import Account
from employee.models import Employee
from contract.models import Contract
from payment_history.models import Payment_history
from recent_trades.models import Recent_Trades
from avg_trade_quantity.models import Avg_trade_quantity
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout as django_logout

def index(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
    else:
            return render(request,'pages/index.html')
    


def about(request):
    return render(request,'pages/about.html')


def contract(request):
    contract = Contract.objects.all()
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
        'contract': contract
        
    } 
    
    return render(request,'pages/contract.html',context)



    


def investment(request):
    return render(request,'pages/investment.html')


def news(request):
    return render(request,'pages/news.html')

def setting(request):
    return render(request,'pages/setting.html')


def bank(request):
    payment_history = Payment_history.objects.all()

    context = {
        'payment_history': payment_history
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