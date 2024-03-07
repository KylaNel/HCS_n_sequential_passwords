from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PinForm, PasswordForm, PinForm1, PasswordForm1

combos = {"Trickily2500": {"password": "&BDY4s$v!v4s", "pin": "604287", "pattern": None},
          "Cyclic5576": {"password": "^pP3@BeHSoP4", "pin": "479367", "pattern": None},
          "Paying0620": {"password": "aVE&!ATu4emz", "pin": "710441", "pattern": None},
          "Feminism0341": {"password": "&Ew3Rjtjkqn$", "pin": "012483", "pattern": None},
          "Fretted9336": {"password": "5##kxTtuL&jD", "pin": "869632", "pattern": None},
          "Sweep1878": {"password": "9d^zKtHPh%5z", "pin": "918423", "pattern": None},
          "Sinuous6928": {"password": "XkX67as#HgVP", "pin": "351984", "pattern": None},
          "Vantage1216": {"password": "s@8@ptuQ!2@f", "pin": "812595", "pattern": None},}

def index(request):
    return render(request, 'n_sequential_passwords/index.html')

def pattern_lock(request):
    return render(request, 'n_sequential_passwords/pattern_lock.html')

def start(request):
    return render(request, 'n_sequential_passwords/start.html')

def success(request):
    return render(request, 'n_sequential_passwords/success.html')

def pin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pin = request.POST.get('pin')

        # check if the pin is correct
        if combos.get(username, None) == pin:
            return render(request, 'n_sequential_passwords/index.html')
        


def password_1_view(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == "&BDY4s$v!v4s":
                request.session["password_1"] = password
                return redirect("/n_sequential_passwords/pin_1")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
        
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_1.html', {'form': form})

def pin_1_view(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == "604287":
                request.session["pin_1"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin_1.html', {'form': form})
            
        
