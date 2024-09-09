from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306221056',
        'name': 'Aliefa Alsyafiandra Setiawati Mahdi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)