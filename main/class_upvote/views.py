from django.shortcuts import render, redirect
from .forms import ClassForm

# Create your views here.
def form_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success_url')  # Redirect to a success page or another view
    else:
        form = ClassForm()

    context = {'form': form}
    return render(request, 'index.html', context)  # Render the template with the form in context