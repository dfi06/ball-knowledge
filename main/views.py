from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Audemar Pidgeot Ronald',
        'price': '$50m'
    }

    return render(request, "main.html", context)