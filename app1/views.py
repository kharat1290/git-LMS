from django.shortcuts import render,redirect
from .models import BookModel
# Create your views here.
def add (request):
    if request.method=='POST':
        if (request.method == 'POST'):
            bookname = request.POST['bookname']
            authorname = request.POST['authorname']
            price_= request.POST['price']
            booktype = request.POST['booktype']
            insert_data=BookModel.objects.create(book_name=bookname, author_name=authorname, price=price_, type_of_book=booktype)
            insert_data.save()
            return redirect('/app1/home/')
    else :
        return render(request,'app1/add.html')

def home(request):
    datas=BookModel.objects.all()
    return render(request,'app1/home2.html',{'datas':datas})

def update(request,tid):
    if (request.method == 'POST'):
        bookname = request.POST['bookname']
        authorname = request.POST['authorname']
        price_= request.POST['price']
        booktype = request.POST['booktype']
        insert_data=BookModel.objects.filter(id=tid)
        insert_data.update(book_name=bookname, author_name=authorname, price=price_, type_of_book=booktype)       
        return redirect('/app1/home/')
    else:
        content={}
        content['data']=BookModel.objects.get(id=tid)
        return render(request,'app1/update.html',content)

def delete(request,tid):
    record_tobe_deleted = BookModel.objects.filter(id=tid)
    record_tobe_deleted.delete()
    return redirect('/app1/home/')

def htol(request): #price
    datas=BookModel.objects.order_by('-price')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def ltoh(request):#price
    datas=BookModel.objects.order_by('price')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def AtoZ(request):#book
    datas=BookModel.objects.order_by('book_name')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def ZtoA(request):#book
    datas=BookModel.objects.order_by('-book_name')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def AatoZz(request):#author
    datas=BookModel.objects.order_by('author_name')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def ZztoAa(request):#author
    datas=BookModel.objects.order_by('-author_name')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def lowtohigh(request):#id
    datas=BookModel.objects.order_by('id')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def hightolow(request):#id
    datas=BookModel.objects.order_by('-id')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def CAtoZ(request):#category
    datas=BookModel.objects.order_by('type_of_book')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def CZtoA(request):#category
    datas=BookModel.objects.order_by('-type_of_book')
    data={"datas":datas}
    return render(request,'app1/home2.html',context=data)

def catfilter(request,cat):#filter category
    content={}
    content['datas']=BookModel.objects.filter(type_of_book=cat)
    return render(request,'app1/home2.html',content)