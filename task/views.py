from django.shortcuts import render

# Create your views here.
def Task(request):
    context ={
        'age' : 5
    }
    return render(request,'index.html',context)