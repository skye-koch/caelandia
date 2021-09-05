from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from wiki.models import Entry, Category
from django.forms import modelform_factory
from .forms import EntryForm
# Create your views here

#def catPage(request):
#    return render(request,"wiki/catpage.html")

def wikipage(request, pk):
    entry = get_object_or_404(Entry, id = pk)
    return render(request, "wiki/wikipage.html",{"entry": entry})

def home(request):
    # entry1 = Entry.objects.filter(category = "Locations")
    # entry2 = Entry.objects.filter(category = "People")
    # entry3 = Entry.objects.filter(category = "Things")
    # entry4 = Entry.objects.filter(category = "Divine Beings")
    catlist = Category.objects.all()
    return render(request, "wiki/home.html", {
        # "entry1": entry1,
        # "entry2": entry2,
        # "entry3": entry3,
        # "entry4": entry4,
        "catlist": catlist 
    })

def catpage(request,catName):
    cat = Category.objects.get(catName = catName)
    entries = Entry.objects.filter(category = cat).order_by('title')
    context = {"entries": entries, "category": cat}
    return render(request, "wiki/catpage.html", context)


def createEntry(request):

    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}    

    return render(request, 'wiki/newEntry.html', context)

def updateEntry(request, pk):

    entry = Entry.objects.get(id = pk)
    form = EntryForm(instance= entry)

    if request.method == 'POST':
        
        form = EntryForm(request.POST, instance = entry)
        if form.is_valid():
            form.save()
            return redirect('wikipage', entry.id)
    context = {'form': form}    

    
    context = {'form':form}

    return render(request, 'wiki/newEntry.html', context)

def deleteEntry(request, pk):
    entry = Entry.objects.get(id = pk)

    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    context = {'entry': entry}
    return render(request, 'wiki/delete.html', context)

def search(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        entriesTitle = Entry.objects.filter(title__icontains = searched).order_by('title')
        entriesBody = Entry.objects.filter(body__icontains = searched).order_by('title')
        entriesSource = Entry.objects.filter(source__icontains = searched).order_by('title')
        return render(request, 'wiki/search.html',{'searched': searched, 'entriesTitle':entriesTitle, 'entriesBody':entriesBody,'entriesSource':entriesSource})
    
    else: 
        return render(request, 'wiki/search.html')