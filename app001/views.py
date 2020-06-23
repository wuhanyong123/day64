from django.shortcuts import render,redirect,HttpResponse
from app001 import models
# Create your views here.
#展示出版社
def publisher_list(request):
    #去数据库查出出版社
    ret=models.Publisher.objects.all().order_by("id")
    return render(request,"publisher_list.html",{"publisher_list":ret})

#添加出版社
def add_publisher(request):
    if request.method == "POST":
        new_publisher_name=request.POST.get("publisher_name")
        models.Publisher.objects.create(name=new_publisher_name)
        return redirect("/publisher_list/")
    return render(request,"add_publisher.html")


#编辑出版社
def edit_publisher(request):
    if request.method == "POST":
        edit_id=request.POST.get("id")
        new_publisher_name=request.POST.get("publisher_name")
        publisher_obj=models.Publisher.objects.get(id=edit_id)
        publisher_obj.name=new_publisher_name
        publisher_obj.save()
        return redirect("/publisher_list/")
    edit_id = request.GET.get("id")
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
    return render(request,"edit_publisher.html",{"publisher_obj":publisher_obj})

#删除出版社
def delete_publisher(request):
    delete_id=request.GET.get("id")
    if delete_id:
        delete_obj=models.Publisher.objects.get(id=delete_id)
        delete_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("数据不存在")


#展示书籍
def book_list(request):
    #查询数据库
    all_book=models.Book.objects.all()
    #在html页面渲染
    return render(request,"book_list.html",{"all_book":all_book})

#添加书籍
def add_book(request):
    if request.method == "POST":
        new_title=request.POST.get("boot_title")
        new_publisher_id=request.POST.get("publisher")
        print(new_title)
        #创建新书对象
        models.Book.objects.create(title=new_title,publisher_id=new_publisher_id)
        return redirect("/book_list/")
    #从数据库取出所有的出版社
    publisher_list=models.Publisher.objects.all()
    return render(request,"add_book.html",{"publisher_list":publisher_list})


#删除
def delete_book(request):
    #从url里获取要删除的书籍id
    delete_id=request.GET.get("id")
    #删除指定id的数据
    models.Book.objects.get(id=delete_id).delete()
    #返回书籍列表页
    return redirect("/book_list/")


#编辑书籍
def edit_book(request):
    if request.method == "POST":
        #从提交的数据中取出书名和关联的出版社
        edit_id=request.POST.get("id")
        new_title=request.POST.get("book_title")
        new_publisher_id=request.POST.get("publisher")
        #更新
        edit_book_obj=models.Book.objects.get(id=edit_id)
        edit_book_obj.title=new_title
        edit_book_obj.publisher_id=new_publisher_id
        #将修改提交到数据库
        edit_book_obj.save()
        #返回书籍列表
        return redirect("/book_list/")
    #取到编辑的书的id值
    edit_id=request.GET.get("id")
    #根据id去数据库拿到数据对象
    edit_book_obj=models.Book.objects.get(id=edit_id)
    # 从数据库取出所有的出版社
    publisher_list = models.Publisher.objects.all()
    return render(
        request,"edit_book.html",
        {"publisher_list":publisher_list,"book_obj":edit_book_obj})


#展示作者列表
def author_list(request):
    # #查询作者的作品
    # author_obj=models.Author.objects.get(id=1)
    #查询所以作者
    all_author=models.Author.objects.all()
    return render(request,"author_list.html",{"all_author":all_author})

#添加作者
def add_author(request):
    if request.method == "POST":
        #提取数据
        new_author_name=request.POST.get("author_name")
        books=request.POST.getlist("books")
        #创建作者
        author_obj=models.Author.objects.create(name=new_author_name)
        author_obj.book.set(books)
        return redirect("/author_list/")
    ret=models.Book.objects.all()
    return render(request,"add_author.html",{"book_list":ret})
#删除作者
def delete_author(request):
    del_id=request.GET.get("id")
    #根据id取得作者对象
    del_obj=models.Author.objects.get(id=del_id)
    #删除作者与书籍的关联表及作者表
    del_obj.delete()
    return redirect("/author_list/")
def edit_author(request):
    if request.method =="POST":
        #获取新名字和id
        edit_author_id=request.POST.get("id")
        new_author_name=request.POST.get("new_author_name")
        new_book_name=request.POST.getlist("books")
        #根据id获取作者对象
        edit_author_obj=models.Author.objects.get(id=edit_author_id)
        #更新作者名字
        edit_author_obj.name=new_author_name
        #更新作者关联的书对应关系
        edit_author_obj.book.set(new_book_name)
        #保存
        edit_author_obj.save()
        return redirect("/author_list/")
    edit_id=request.GET.get("id")
    edit_obj=models.Author.objects.get(id=edit_id)
    ret = models.Book.objects.all()
    return render(request,"edit_author.html",{"author":edit_obj,"book_list":ret})