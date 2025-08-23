from django.shortcuts import render

def index1(request):
    return render(request, 'tweet/index1.html')  # ✅ no "templates/"
