# I have created this File - SUJEET 

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    paramas = {'name':"sujeet"}
    return render(request,"index.html",paramas)

def about(request):
    return HttpResponse("Bye")

def analyze(request):
    # print(request.GET.get('text','default'))
    text = request.GET.get('text', 'off')
    removepunc = request.GET.get('removepunc', 'default')

    print(removepunc)

    if removepunc == "on":
        process=""
        for i in text:
            if i.isalpha() or i==" ":
                process=process+i
        
        if not text:
            print("default")
        print(text)

        # return render (request,'analyze.html')
        paramas={"process":process,'purpose':"Remove Punchucation"}

        return render (request,'analyze.html',paramas)
    
    else:
        return HttpResponse("Remove Punc <a href = '/'> Back </a>")