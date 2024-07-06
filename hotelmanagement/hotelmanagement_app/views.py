from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.views import View
from hotelmanagement_app.form import RegisterForm,LoginForm,HotelForm,EditForm
from django.contrib.auth.models import User
from hotelmanagement_app.models import HotelModel
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.
class Home(TemplateView):
    template_name='home.html'
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        data=RegisterForm(request.POST)
        if data.is_valid():
            dataform=data.cleaned_data
            User.objects.create_user(**dataform)
            return HttpResponse('data saved')
        else:
            return HttpResponse('invalid credential')
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(request,'login successful')
            return redirect('userprofile_view')
        else:
            messages.ERROR(request,'invalidcredential')
            return redirect('home_view')
class UserHome(TemplateView):
    template_name='user_home.html' 

class LogoutView(View):
    def get (self,request):
        logout(request)
        return redirect('home_view')


class HotelCreateView(CreateView):
    form_class=HotelForm
    template_name='create.html'
    model=HotelModel
    success_url=reverse_lazy('home1_view')

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Task Created Successfully")
        return super().form_valid(form)
    
class ListView(ListView):
    model=HotelModel
    template_name='list.html'
    context_object_name="data"

    def get_queryset(self):
        return HotelModel.objects.filter(user=self.request.user) 

class EditView(UpdateView):
    model=HotelModel
    form_class=EditForm
    template_name='edit.html'
    success_url=reverse_lazy('list_view')
    pk_url_kwarg='id'     

class DeleteView(DeleteView):
    model=HotelModel
    pk_url_kwarg='id'  
    success_url=reverse_lazy('list_view') 
    template_name='delete.html'