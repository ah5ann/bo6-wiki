from django.shortcuts import render, redirect
from .forms import ClassForm

def form_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        print(form, "Form")
        if form.is_valid():
            # Process the form data
            return redirect('success_url')  # Redirect to a success page or another view
    else:
        form = ClassForm()  # Properly instantiate the form

    context = {'form': form}
    return render(request, 'create_a_class.html', context)  # Render the template with the form in context

