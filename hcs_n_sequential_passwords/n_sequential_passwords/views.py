from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PinForm, PasswordForm, PinForm1, PasswordForm1

combos = {"pin": ["604287"],
          "password": ["&BDY4s$v!v4s"],
          "pin + pin": ["479367", "710441"],
          "pin + pin + pin": ["123456", "869632", "918423"],
          "pin + pin + pin + pin": ["351984", "812595", "918423", "869632"],
          "password + password": ["^pP3@BeHSoP4", "aVE&!ATu4emz"],
          "password + password + password": ["&Ew3Rjtjkqn$", "5##kxTtuL&jD", "9d^zKtHPh%5z"],
          "password + password + password + password": ["XkX67as#HgVP", "s@8@ptuQ!2@f", "9d^zKtHPh%5z", "5##kxTtuL&jD"],
          "password +pin": ["&BDY4s$v!v4s", "604287"],
          "password +pin + password + pin": ["^pP3@BeHSoP4", "479367", "aVE&!ATu4emz", "710441"],
          "password +pin + password": ["^pP3@BeHSoP4", "604287", "aVE&!ATu4emz"],}

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
            if str(pin) == combos["pin"][0]:
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
            if password == combos["password"][0]:
                request.session["password"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
        
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password.html', {'form': form})

def pin_2pin_view_1(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin"][0]:
                request.session["pin_2pin"] = pin
                return redirect("/n_sequential_passwords/pin_2pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin_2pin_1.html', {'form': form})

def pin_2pin_view_2(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin"][1]:
                request.session["pin_2pin_2"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin_2pin_2.html', {'form': form})

def pin_3pin_view_1(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin"][0]:
                request.session["pin_3pin_1"] = pin
                return redirect("/n_sequential_passwords/pin_3pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()

    return render(request, 'n_sequential_passwords/pin_3pin_1.html', {'form': form})

def pin_3pin_view_2(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin"][1]:
                request.session["pin_3pin_2"] = pin
                return redirect("/n_sequential_passwords/pin_3pin_3")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_3pin_2.html', {'form': form})

def pin_3pin_view_3(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin"][2]:
                request.session["pin_3pin_3"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_3pin_3.html', {'form': form})

def pin_4pin_view_1(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin + pin"][0]:
                request.session["pin_4pin_1"] = pin
                return redirect("/n_sequential_passwords/pin_4pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_4pin_1.html', {'form': form})

def pin_4pin_view_2(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin + pin"][1]:
                request.session["pin_4pin_2"] = pin
                return redirect("/n_sequential_passwords/pin_4pin_3")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_4pin_2.html', {'form': form})

def pin_4pin_view_3(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin + pin"][2]:
                request.session["pin_4pin_3"] = pin
                return redirect("/n_sequential_passwords/pin_4pin_4")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_4pin_3.html', {'form': form})

def pin_4pin_view_4(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["pin + pin + pin + pin"][3]:
                request.session["pin_4pin_4"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_4pin_4.html', {'form': form})

def password_2password_view_1(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password"][0]:
                request.session["password_2password_1"] = password
                return redirect("/n_sequential_passwords/password_2password_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_2password_1.html', {'form': form})

def password_2password_view_2(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password"][1]:
                request.session["password_2password_2"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_2password_2.html', {'form': form})

def password_3password_view_1(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password"][0]:
                request.session["password_3password_1"] = password
                return redirect("/n_sequential_passwords/password_3password_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_3password_1.html', {'form': form})

def password_3password_view_2(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password"][1]:
                request.session["password_3password_2"] = password
                return redirect("/n_sequential_passwords/password_3password_3")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_3password_2.html', {'form': form})

def password_3password_view_3(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password"][2]:
                request.session["password_3password_3"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_3password_3.html', {'form': form})

def password_4password_view_1(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password + password"][0]:
                request.session["password_4password_1"] = password
                return redirect("/n_sequential_passwords/password_4password_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()

    return render(request, 'n_sequential_passwords/password_4password_1.html', {'form': form})

def password_4password_view_2(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password + password"][1]:
                request.session["password_4password_2"] = password
                return redirect("/n_sequential_passwords/password_4password_3")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_4password_2.html', {'form': form})

def password_4password_view_3(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password + password"][2]:
                request.session["password_4password_3"] = password
                return redirect("/n_sequential_passwords/password_4password_4")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_4password_3.html', {'form': form})

def password_4password_view_4(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password + password + password + password"][3]:
                request.session["password_4password_4"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write(password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_4password_4.html', {'form': form})


def password_1_view(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password +pin"][0]:
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
            if str(pin) == combos["password +pin"][1]:
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
            if password == combos["password +pin + password"][0]:
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
            if str(pin) == combos["password +pin + password"][1]:
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
            if password == combos["password +pin + password"][2]:
                request.session["password_2_2"] = password
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Password 2 (3 step) " + password + "\n")

    else:
        form = PasswordForm1()
    
    return render(request, 'n_sequential_passwords/password_2_2.html', {'form': form})

def password_2password2pin_view_1(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password +pin + password + pin"][0]:
                request.session["password_2password2pin_1"] = password
                return redirect("/n_sequential_passwords/pin_2password2pin_1")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Password 1 (4 step) " + password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_2password2pin_1.html', {'form': form})

def pin_2password2pin_view_1(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["password +pin + password + pin"][1]:
                request.session["pin_2password2pin_1"] = pin
                return redirect("/n_sequential_passwords/password_2password2pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Pin (4 step) " + str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_2password2pin_1.html', {'form': form})

def password_2password2pin_view_2(request):
    if request.method == "POST":
        form = PasswordForm1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == combos["password +pin + password + pin"][2]:
                request.session["password_2password2pin_2"] = password
                return redirect("/n_sequential_passwords/pin_2password2pin_2")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Password 2 (4 step) " + password + "\n")
    else:
        form = PasswordForm1()
    return render(request, 'n_sequential_passwords/password_2password2pin_2.html', {'form': form})

def pin_2password2pin_view_2(request):
    if request.method == "POST":
        form = PinForm1(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            if str(pin) == combos["password +pin + password + pin"][3]:
                request.session["pin_2password2pin_2"] = pin
                return redirect("/n_sequential_passwords/success")
            else:
                with open("passwords.txt", "a") as f:
                    f.write("Pin 2 (4 step) " + str(pin) + "\n")
    else:
        form = PinForm1()
    return render(request, 'n_sequential_passwords/pin_2password2pin_2.html', {'form': form})
    
            

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


        
