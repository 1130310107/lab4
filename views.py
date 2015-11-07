from django.shortcuts import render, render_to_response
from django.http import  HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *


def addbook(request):
    if request.POST:
        post = request.POST
        title=post.get('title','')
        isbn=post.get('isbn','')
        authorname=post.get('author','')
        publisher=post.get('publisher','')
        publish_date=post.get('publish_date','')
        price=post.get('price','')
        try:
            author = Author.objects.get(name=authorname)
        except:
            return HttpResponseRedirect('/addauthor/')
        newbook = Book(
            isbn=isbn,\
            title=title,\
            author=author,\
            publisher=publisher,\
            publish_date=publish_date,\
            price=price,\
        )
        newbook.save()
        #content={'title':title,'isbn':isbn,'author':author,'publisher':publisher,'publish_date':publish_date,'price':price}
        return HttpResponseRedirect('/booklist/')
    return render_to_response('addbook.html')

def revise(request,isbn):
    try:
        book = Book.objects.get(isbn=isbn)
    except:
        return HttpResponseRedirect('/booklist/')
    if request.POST:
        book.delete()
        post = request.POST
        title=post.get('title','')
        isbn=post.get('isbn','')
        authorname=post.get('author','')
        publisher=post.get('publisher','')
        publish_date=post.get('publish_date','')
        price=post.get('price','')
        try:
            author = Author.objects.get(name=authorname)
        except:
            return HttpResponseRedirect('/addauthor/')
        newbook = Book(
            isbn=isbn,\
            title=title,\
            author=author,\
            publisher=publisher,\
            publish_date=publish_date,\
            price=price,\
        )
        newbook.save()
        return HttpResponseRedirect('/booklist/')
    return render(request, 'revise.html',{'book':book})

def delete(request,isbn):
    try:
        bookdelist = Book.objects.filter(isbn=isbn)
        for book in bookdelist:
            book.delete()
    except:
        return HttpResponseRedirect('/booklist/')
    return HttpResponseRedirect('/booklist/')


def addauthor(request):
    if request.POST:
        post = request.POST
        name = post.get('name','')
        age = post.get('age','')
        country = post.get('country','')
        newauthor = Author(
            name=name,\
            age=age,\
            country=country,\
        )
        newauthor.save()
        return HttpResponseRedirect('/addbook/')
    return render_to_response('addauthor.html')

def book_list(request):
    if request.POST:
        post = request.POST
        authorname = post.get('author','')
        booklist = Book.objects.filter(author__name=authorname)
        return render(request,'booklist.html',{'booklist':booklist})
    booklist = Book.objects.all()
    return render(request,'booklist.html',{'booklist':booklist})

def bookdetail(request,isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        return render(request,'book.html',{'book':book})
    except:
        return HttpResponseRedirect('/booklist/')

def authordetail(request,isbn):
        book = Book.objects.get(isbn=isbn)
        author = book.author
        booklist = Book.objects.filter(author=author)
        return render(request,'author.html',{'author':author,'booklist':booklist})

def homepage(request):
    return render_to_response('homepage.html')
