from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django import views


# Create your views here.
class Signup_view(views.View):
    form = UserCreationForm
    template_name = 'AUTH_APP/signup.html'

    def get(self,request):
        return render(request, self.template_name, {'form':self.form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        return render(request, self.template_name, {'form': form})


class Login_view(views.View):
    template_name = 'AUTH_APP/login.html'

    def get(self,request):
        return render(request, self.template_name, {})

    def post(self,request):
        u = request.POST.get('un')
        p = request.POST.get('pw')

        user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('show_url')
        return render(request, self.template_name, {})


class Logout_view(views.View):
    def get(self, request):
        logout(request)
        return redirect('login_url')