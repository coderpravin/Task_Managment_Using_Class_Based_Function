from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.
'''
def TaskList(request):
    tasks = Task.objects.all()
    return render(request, 'task/taskList.html', {'tasks':tasks})
'''

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task/taskList.html'
    context_object_name = 'tasks'

    # Redirect to login page if not logged in
    login_url = 'userLogin'  # Set this to the name of your login URL

'''
@login_required
def TaskCreate(request):
    print("User Logged in ", request.user)
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        duedate = request.POST.get('duedate')
        status = request.POST.get('status')
        

        task = Task(title =title, desc=desc, duedate=duedate, status=status, user = request.user)

        task.save()

        return HttpResponse("Task save sucess")

    return render(request, 'task/taskCreate.html')
'''

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'desc', 'duedate', 'status']
    template_name = 'task/taskCreate.html'
    success_url = reverse_lazy("TaskList")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
'''    
@login_required    
def TaskUpdate(request, id):
    print(f"The login user is ", request.user)
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        duedate = request.POST.get('duedate')
        status = request.POST.get('status')

        #update
        task.title = title
        task.desc = desc 
        task.duedate = duedate
        task.status = status

        task.save()
        return redirect('TaskList')
        
    return render(request,'task/taskUpdate.html', {'task':task})
'''

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'desc', 'duedate', 'status']
    template_name = 'task/taskUpdate.html'
    success_url = reverse_lazy('TaskList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

'''    
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('TaskList')
'''
    
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('TaskList')

def homeLogin(request):
    return render(request, 'task/LoginPage.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)

            return redirect('TaskList')

    return render(request, 'task/LoginUser.html')