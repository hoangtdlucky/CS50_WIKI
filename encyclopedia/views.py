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

class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label='Content', widget=forms.Textarea)

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
        "entry_content": markdown2.markdown(util.get_entry(TITLE)),
        "entry_title": TITLE


    }) 


def searchform(request):
    print(request.GET)
    key = request.GET.get('q')

    rs = search.search(key)
    if rs[0] == "test_ok":
        return entryview(request,rs[1])

    elif rs == "None":
        return render(request, 'encyclopedia/not_found.html')

    return render(request, 'encyclopedia/index.html',{
        'entries':rs
    })

    
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
    print(request.GET)
    a = util.get_entry(abs)
    c = {
        'title':abs,
        'content': a,
    }
    c = NewTaskForm(c)
    return render (request, 'encyclopedia/edit.html', {
        'form':c
    })
    add()



def random(request):
    mylist = util.list_entries()
    print(mylist)
    rdentry = rdm.choice(mylist)
    print(f"THE RANDOM TITLE IS:{rdentry}")
    return entryview(request,rdentry)
    


            
