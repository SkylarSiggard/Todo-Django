from django.shortcuts import render


def base(request):
    return render(request, 'list.html')
