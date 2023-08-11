from django.shortcuts import render

# Create your views here.
def button(request):
    return render(request,'button.html')
def card(request):
    return render(request,'card.html')
def alert(request):
    return render(request,'alert.html')
def carousel(request):
    return render(request,'carousel.html')
def cdn_bootstrap(request):
    return render(request,'cdn_bootstrap.html')





