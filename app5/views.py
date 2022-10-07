from django.shortcuts import render


# Create your views here.
def function1(request):
    d={'name':'srikanth','age':21}
    return render(request,'forloop.html',d)

