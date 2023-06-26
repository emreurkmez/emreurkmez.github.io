from django.shortcuts import render
from .models import *

def indexPage(request):
    content2 = Card.objects.get(id=2)
    news = Card.objects.filter(new=True)
    cards=Card.objects.all()
    context ={
        "content2":content2,
        "news4":news[:4],
        "news2":news[:2],
        "cards":cards,

    }
    return render(request,"index.html",context)
def detailPage(request,idcard):
    card = Card.objects.get(id=idcard)
    context ={
        "card":card,
        
    }
    return render(request,"detail.html",context)
def categoryPage(request):
    context ={}
    return render(request,"category.html",context)