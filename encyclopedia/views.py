from re import A
from django.http import request,HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
#from markdown2 import Markdown
import markdown2
from pkg_resources import EntryPoint
from .forms import PostForm
from django import forms
from django.urls import reverse
from . import util
import random
from . import search
import random as rdm
from scipy import *
a = markdown2.markdown_path("encyclopedia/CSS.md")
rs = []

def index(request):
    search_post = request.GET.get('q')
    if search_post:
        rs = search.search(search_post)
        return render(request, 'encyclopedia/index.html',{
        'entries':rs
        })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        })


 # def test(request):
    return render(request, "encyclopedia/entry_view.html",{
        "a": a
    }) 
    


def entryview(request,TITLE):
    return render(request, "encyclopedia/entry_view.html",{
        
        #"b": util.get_entry(TITLE),
        #"a": markdown2.markdown_path(f"entries/{TITLE}.md")
        "a": markdown2.markdown(util.get_entry(TITLE)),
        "b": TITLE


    }) 


def searchform(request):
    key = request.GET.get('q')
    rs = search.search(key)
    if rs[0] == "test_ok":
        return render(request, "encyclopedia/entry_view.html",{
        
        "a": markdown2.markdown(util.get_entry(rs[1])),

    }) 

    return render(request, 'encyclopedia/index.html',{
        'entries':rs
    })

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label='Content', widget=forms.Textarea)
    
def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            a=form['title'].value()
            b=form['content'].value()
            util.save_entry(a,b)
            return HttpResponseRedirect(reverse('encyclopedia:index'))
        else:
            return render(request, 'encyclopedia/add1.html',{
                'form':form
            })
    else:
        return render(request, "encyclopedia/add1.html",{
            'form':NewTaskForm()
        })
            


def edit(request,abs):
    a = util.get_entry(abs)
    c = {
        'title':abs,
        'content': a,
    }
    b = NewTaskForm(c)
    return render (request, 'encyclopedia/edit.html', {
        'form':b
    })
    add()



def random(request):
    mylist = util.list_entries()
    print(mylist)
    rdentry = rdm.choice(mylist)
    print(f"THE RANDOM TITLE IS:{rdentry}")
    return entryview(request,rdentry)
    


            
