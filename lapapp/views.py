from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout
from lapapp.models import Contact,addUser




# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,"base.html")

def contact(request):
    return render(request,"contact.html")

#1 Hp 

url1="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&p%5B%5D=facets.brand%255B%255D%3DHP&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105"
response=requests.get(url1)
#print(response1)
names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])

list1=zip(names,prices,ratings,discounts,o_prices,images,links)
@login_required(login_url='login')
def hp(request):
    return render(request,"hp.html",{'list1':list1})

   
 
#2 lenovo

url2="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3DLenovo"
response=requests.get(url2)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])

list2=zip(names,prices,ratings,discounts,o_prices,images,links)  

def lenovo(request):
    return render(request,"lenovo.html",{'list2':list2}) 

#3 Asus

url3="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3DASUS"
response=requests.get(url3)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])

list3=zip(names,prices,ratings,discounts,o_prices,images,links)  

def asus(request):
    return render(request,"asus.html",{'list3':list3}) 

#4 acer
url4="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3Dacer"

response=requests.get(url4)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])

list4=zip(names,prices,ratings,discounts,o_prices,images,links)  


def acer(request):
    return render(request,"acer.html",{'list4':list4}) 

#5 realme
url5="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3Drealme"
response=requests.get(url5)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])

list5=zip(names,prices,ratings,discounts,o_prices,images,links)  

def realme(request):
    return render(request,"realme.html",{'list5':list5})

#6 MSI
url6="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3DMSI"
response=requests.get(url6)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])




list6=zip(names,prices,ratings,discounts,o_prices,images,links)  

def msi(request):
    return render(request,"msi.html",{'list6':list6})

#7 smarton
url7="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhQIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_41.metroExpandable.METRO_EXPANDABLE_HP_laptops-store_DUA3GDGO4GNV_wp10&fm=neo%2Fmerchandising&iid=M_28975a62-5533-4b31-8090-598d855eaa44_41.DUA3GDGO4GNV&ppt=clp&ppn=laptops-store&ssid=n6chxiw8ps0000001686157425105&p%5B%5D=facets.brand%255B%255D%3DSmartron"

response=requests.get(url7)

names=[]
prices=[]
ratings=[]
discounts=[]
o_prices=[]
images=[]
links=[]
soup=BeautifulSoup(response.content,"html.parser")
name=soup.find_all("div",class_="_4rR01T")
for i in name[1:len(name)+1]:
    names.append(i.get_text())  
price=soup.find_all('div',class_="_30jeq3 _1_WHN1")  
for i in price[1:len(names)+1]:
    prices.append(i.get_text())
    
rate=soup.find_all('div',class_="_3LWZlK")    
for i in rate[1:len(name)+1]:
    ratings.append(i.get_text())
discount=soup.find_all('div',class_="_3Ay6Sb")    
for i in discount[1:len(names)+1]:
    discounts.append(i.get_text())
original=soup.find_all('div',class_="_3I9_wc _27UcVY")    
for i in original[1:len(names)+1]:
    o_prices.append(i.get_text())
image=soup.find_all('div',class_="CXW8mj")    
for i in image[1:len(names)+1]:
    d=i.img['src']
    images.append(d) 
link=soup.find_all("a",class_="_1fQZEK")       
for i in link[1:len(names)+1]:
    links.append("https://www.flipkart.com"+i["href"])


list7=zip(names,prices,ratings,discounts,o_prices,images,links)  

def smarton(request):
    return render(request,"smarton.html",{'list7':list7})



def login_user(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get("Password")
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
        return redirect("home")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("user name")
        email=request.POST.get("email address")
        password=request.POST.get("user password")
        c=User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    return render(request,"register.html")    

def logout_user(request):
    logout(request)
    return redirect("login")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect('home')
    return render(request,"contact.html")