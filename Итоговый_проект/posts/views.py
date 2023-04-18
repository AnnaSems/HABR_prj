from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Дизайн
def design_page(request):
    template = 'posts/design.html'
    return render(request, template)


# Веб-разработка
def web_dev_page(request):
    template = 'posts/web_dev.html'
    return render(request, template)


# Мобильная разработка
def mob_dev_page(request):
    template = 'posts/mob_dev.html'
    return render(request, template)


# Маркетинг
def market_page(request):
    template = 'posts/market.html'
    return render(request, template)
