from django.shortcuts import render, redirect
#create your views here
import requests
import pandas
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def base(request):
    return render(request, "base.html")

#Xiaomi Mobiles 
response=requests.get("https://www.flipkart.com/search?q=xiaomi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=xiaomi+mobiles%7CMobiles&requestId=29808ed5-2a03-434d-a898-7f0a10447266&as-searchtext=xiaomi%20")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image
# df.to_csv('Mobiles.csv')
# print(df)

mylist1=zip(name,
price,
rate,
image,
link,
)

def xiaomi(request):
    return render(request,"xiaomi.html",{ 'mylist1':mylist1})

#Apple Iphone Mobiles
response=requests.get("https://www.flipkart.com/search?q=iphone%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image
# df.to_csv('Mobiles.csv')
# print(df)

mylist2=zip(name,
price,
rate,
image,
link,
)

def apple(request):
    return render(request,"apple.html",{ 'mylist2':mylist2})

#3.Samsung Mobiles
response=requests.get("https://www.flipkart.com/search?q=xiaomi+13+pro+5g&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_13_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_13_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=xiaomi+13+pro+5g&requestId=772920b1-e630-4bca-bff2-e425c856c129&as-searchtext=xiaomi%2013%20pro")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image
# df.to_csv('Mobiles.csv')
# print(df)

mylist3=zip(name,
price,
rate,
image,
link,
)

def samsung(request):
    return render(request,"samsung.html",{ 'mylist3':mylist3})

#4.Oneplus Mobiles
response=requests.get("https://www.flipkart.com/search?q=oneplus+mobile+11r&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=oneplus+mobile+11r%7CMobiles&requestId=ab1421b2-c789-4603-a55c-923ca2e54810&as-searchtext=oneplus%20mobile")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image

# df.to_csv('Mobiles.csv')
# print(df)
mylist4=zip(name,
price,
rate,
image,
link,
)

def oneplus(request):
    return render(request,"oneplus.html",{'mylist4':mylist4})

#4.Poco Mobiles
response=requests.get("https://www.flipkart.com/search?q=poco+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=poco+mobile%7CMobiles&requestId=74473c60-e226-4a22-aaba-b70a109f04ea&as-searchtext=Pocco%20mobiles")
# print(response2)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image
# df.to_csv('Mobiles.csv')
# print(df)
mylist5=zip(name,
price,
rate,
image,
link,
)

def poco(request):
    return render(request,"poco.html",{ 'mylist5':mylist5})


#5.Oppo Mobiles
response=requests.get("https://www.flipkart.com/search?q=Oppo%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image
# df.to_csv('Mobiles.csv')
# print(df)
mylist6=zip(name,
price,
rate,
image,
link,
)

def oppo(request):
    return render(request,"oppo.html",{ 'mylist6':mylist6})

#6.Realme Mobiles
response=requests.get("https://www.flipkart.com/search?q=realme%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image

# df.to_csv('Mobiles.csv')
# print(df)
mylist7=zip(name,
price,
rate,
image,
link,
)

def realme(request):
    return render(request,"realme.html",{'mylist7':mylist7})

#6.IQOO Mobiles
response=requests.get("https://www.flipkart.com/search?q=iqoo&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
# print(name)

prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
# print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
# print(image)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)
# df=pandas.DataFrame()
# df['Names']=name
# df['prices']=price
# df['Ratings']=rate
# df['links']=link
# df['Images']=image

# df.to_csv('Mobiles.csv')
# print(df)
mylist8=zip(name,
price,
rate,
image,
link,
)

def iqoo(request):
    return render(request,"iqoo.html",{'mylist8':mylist8})

#Login
def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user= authenticate(email=email, password=password)
        if user is not None:

            login(request,user)
        return redirect("base")
    
    
    return render(request,"login.html")

#Register-->Signup
def signup(request):
    if request.method=="POST":
        
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
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
        return redirect("home")

    return render(request,"contact.html")
