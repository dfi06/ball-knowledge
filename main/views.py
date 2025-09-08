from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Daffa Ismail',
        'kelas': 'A'
    }

    return render(request, "main.html", context)