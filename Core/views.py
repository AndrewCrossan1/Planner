from django.shortcuts import render

# View creation starts here


def index(request):
    page_name = 'home'  # Used for setting active link in navigation
    return render(request, 'Core/home/index.html', context={'page_name': page_name})


def contact(request):
    page_name = 'contact'  # Used for setting active link in navigation
    # TODO: Implement contact form
    return render(request, 'Core/contact/contact.html', context={'page_name': page_name})


def about(request):
    page_name = 'about'  # Used for setting active link in navigation
    return render(request, 'Core/about/about.html', context={'page_name': page_name})
