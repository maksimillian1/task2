from django.shortcuts import render

def viewText(request):
    name = "Mx"
    return render(request, 'urlapp/index.html', context={'name': name})
