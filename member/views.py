from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from django.db.models import Q

# Add Contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})


# View all Contacts
def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        contacts = Contact.objects.filter(Q(first_name__icontains=search_query) | Q(email__icontains=search_query))
    else:
        contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})


# View Contact Details
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})


# Edit Contact
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})


# Delete Contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete_contact.html', {'contact': contact})
