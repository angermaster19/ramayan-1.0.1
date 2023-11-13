from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import requests,html5lib
from bs4 import BeautifulSoup
from django.utils.safestring import mark_safe


# Create your views here.
def index(request):
    name = request.POST.get('name','default')
    password = request.POST.get('password')
    check = request.POST.get('check','off')

    
    if password!="JAISHRIRAM" and check=="on":
        messages.success(request,(f"Please Enter a valid password!!!!"))
            
    elif password=="JAISHRIRAM" and check!="on":
        messages.success(request,(f"Make sure your are cuirous!!!!"))
            
    elif password!="JAISHRIRAM" and check!="on":
        messages.success(request,(f"Please Enter a valid password and Check Button !!!!"))
        



    return render(request,'index.html',{})

def main(request):
    name = request.POST.get('name','default')
    password = request.POST.get('password')
    check = request.POST.get('check','off')



    

    if password=="JAISHRIRAM" and check=="on":
        params = {"uu": "/main"}
        print(name," ",password)
        messages.success(request,(f"Welcome {name}, {password}!!!!"))
        return render(request,'main.html',params)
    
    else:
        params = {"uu": "/home"}
        return render(request,'index.html',params)
    

def page(request):
    name = request.POST.get("Kaand")
    name = str(name)
    chapter = request.POST.get("chapter")
    chapter = str(chapter)

    print(name, chapter)
    name = int(name)
    chapter = int(chapter)
    kand = ["Select","BalKand","AyodyaKand","AranyaKand","KishkindhaKand","SunderKand","LankaKand","UttarKand"]
    kaand = kand[name]

    url = f"https://hindi.webdunia.com/religion/religion/hindu/ramcharitmanas/{kaand}/{chapter}.htm"
    data1 = scrape(url,link="slok")
    data2 = scrape(url,link="bhawarth")
    data3 = scrape(url,link="orangeFont headingSub")

    print(len(data1))
    print(len(data2))
    print(len(data3))

    context_data = html_content(url,"slok_wrapper")
    html_content1 = "<p> Hello </p>"
    safe = mark_safe(html_content1)

    print(request.POST)
    


    

    params = {"name":name,"chapter":chapter,"data":zip(data1,data2),"html_cont":safe,"context_data":context_data}
    return render(request,'page.html',params)

def scrape(url,link):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = []
    for div in soup.find_all('div',attrs={"class" : link}):
        text.append(div.text)
    return text  

def html_content(url,link):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = ""
    for div in soup.find_all('div',attrs={"class" : link}):
        tag+=str(div)
    
    html_4 = tag
    safe_html = mark_safe(html_4)
    # context_data = {'html_content':safe_html}

    return safe_html
    
