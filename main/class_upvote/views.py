from django.shortcuts import render, redirect
from .forms import ClassForm
from django.urls import reverse
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def form_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            # Get the selected weapon and attachments from the form
            post_name = form.cleaned_data['post_name']
            main_weapon = form.cleaned_data['weapon_name']
            attachment1 = form.cleaned_data['attachment1']
            attachment2 = form.cleaned_data['attachment2']
            attachment3 = form.cleaned_data['attachment3']
            attachment4 = form.cleaned_data['attachment4']
            attachment5 = form.cleaned_data['attachment5']

            # Create a new Post object
            new_post = Post.objects.create(
                post_name=post_name,
                main_weapon=main_weapon,
                attachment1=attachment1,
                attachment2=attachment2,
                attachment3=attachment3,
                attachment4=attachment4,
                attachment5=attachment5
            )

            # Redirect to the post details page after creation
            return redirect(reverse('postdetails'))
    else:
        form = ClassForm()

    context = {'form': form}
    return render(request, 'create_a_class.html', context)

def post_details(request):
    post_data = Post.objects.all()
    context = {
        'post_data': post_data
    }
    print(post_data.query)
    return render(request, 'index.html', context)