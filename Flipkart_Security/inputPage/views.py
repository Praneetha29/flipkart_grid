from django.shortcuts import render

# Create your views here.


def input_view(request):
    return render(request, 'inputPage/input.html')
