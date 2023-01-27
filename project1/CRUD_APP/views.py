from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin


class Add_view(LoginRequiredMixin,views.View):
    template_name = 'CRUD_APP/add.html'
    form = EmployeeForm
    def get(self, request):
        form = self.form()
        return render(request,template_name=self.template_name,context={'form':form})

    def post(self, request):
        form=self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, template_name=self.template_name, context={'form': form})

class Show_view(views.View):
    def get(self, request):
        data= Employee.objects.all()
        return render(request, 'CRUD_APP/show.html', {'data':data})

class Update_view(views.View):
    def get(self, request,pk):
        obj = Employee.objects.get(id=pk)
        form = EmployeeForm(instance=obj)
        return render(request,'CRUD_APP/add.html', {'form':form})

    def post(self, request, pk):
        obj = Employee.objects.get(id=pk)
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, 'CRUD_APP/add.html', {'form': form})


class Delete_view(views.View):
    def get(self, request, pk):
        data = Employee.objects.get(id=pk)
        context = {'data': data}
        return render(request, 'CRUD_APP/delete.html', context)

    def post(self, request, pk):
        obj = Employee.objects.get(id=pk)
        obj.delete()
    

