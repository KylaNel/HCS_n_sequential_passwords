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

def pin_view(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == "604287":
                request.session["pin"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin.html', {'form': form})

def password_view(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == "&BDY4s$v!v4s":
                request.session["password"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
        
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password.html', {'form': form})
        


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

def password_2_view_1(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == "^pP3@BeHSoP4":
                request.session["password_2"] = password
                return redirect("/n_sequential_passwords/pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Password 1 (3 step) " + password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_2_1.html', {'form': form})

def pin_2_view(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == "479367":
                request.session["pin_2"] = pin
                return redirect("/n_sequential_passwords/password_2_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Pin (3 step) " + str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin_2.html', {'form': form})

def password_2_view_2(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == "aVE&!ATu4emz":
                request.session["password_2_2"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Password 2 (3 step) " + password + "\n")

    else:
        form = PasswordForm1()
    
    return render(request, 'n_sequential_passwords/password_2_2.html', {'form': form})
    
            

def timer(request):
    return render(request, 'n_sequential_passwords/timer.html')

def prompt(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        pin = request.POST.get('pin')
        password2 = request.POST.get('password2')

        # Check passwords and pins here
        # If they are correct, calculate the time taken and return the result

        # For simplicity, let's assume the passwords and pins are correct
        time_taken = 10  # Placeholder for the time taken
        return HttpResponse(f'Time taken: {time_taken} seconds')

    return render(request, 'n_sequential_passwords/prompt.html')


        
