from django.shortcuts import render, redirect
from .forms import CreateQuoteForm
# Create your views here.


# home view
def home(request):
    return render(request, "index.html")



def create_quote(request):
    if request.method == 'POST':
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace with your desired redirect view
    else:
        form = CreateQuoteForm()

    return render(request, 'create_quote.html', {'form': form})
