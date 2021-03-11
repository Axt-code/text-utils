#created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #checkbox Value
    removePunc = request.POST.get('removepunc', 'off')
    captialize = request.POST.get('captialize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')

    if removePunc =="on":
        #function
        puncutation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedText=""
        for char in djtext:
            if char not in puncutation:
                analyzedText +=char
        #params
        params={
            'purpose': 'Remove Punctuations' ,
            'analyzed_text': analyzedText
        }
        djtext=analyzedText

    if newlineremover =="on":
        #function
        analyzedText=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzedText += char
        params={
            'purpose': 'New Line Remover' ,
            'analyzed_text': analyzedText
        }
        djtext=analyzedText
    
    if removeextraspace =='on':
        #function
        analyzedText=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzedText += char
        params={
            'purpose': 'Remove Extra Space' ,
            'analyzed_text': analyzedText
        }
        djtext=analyzedText

    if captialize == "on":
        #function
        analyzedText=""
        for char in djtext:
            analyzedText = analyzedText + char.upper()
        params={
            'purpose': 'Capatialize Text' ,
            'analyzed_text': analyzedText
        }
        djtext=analyzedText

    if(captialize!="on" and removeextraspace!="on" and newlineremover!="on" and removePunc!="on"):
        return HttpResponse('<h1>Please select atleast one option and try again...</h1>')
    
    return render(request, 'analyze.html', params)
