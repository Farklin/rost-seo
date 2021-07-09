import re
from django.db.models import base
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from .models import Category, Uslusgi, Article, ApplicationForm , Region 
from django.views.decorators.http import require_GET
from django.urls import reverse 


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Disallow: *.js", 
        "User-agent: Yandex",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Disallow: *.js", 
        "User-agent: Googlebot",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Disallow: *.js", 
        "Sitemap: https://aweb1.ru/sitemap.xml"
        
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def view_categoryes(request):
    categoryes = Category.objects.filter(parent = None)
    return render(request, 'uslugi/index.html', {'categoryes': categoryes})

def view_category(request,slug): 
    try: 
        category = Category.objects.get(slug = slug, parent = None)
        uslugies = category.uslusgi_set.all()
        
        try:
            children_category = Category.objects.filter(parent = category, published = True)
            if children_category == None: 
                children_category = ''
        except: 
            children_category = '' 
        
        return render(request, 'uslugi/category.html', {'category':category, 'uslugies':uslugies, 'children_category': children_category})

    except: 
        artitcle = Article.objects.get(slug = slug)
        return render(request, 'uslugi/article.html', {'article': artitcle})


def view_uslugi(request, slug_category, slug_children_category, slug_uslugi): 
    uslugi = Uslusgi.objects.get(slug = slug_uslugi)
    parent_category = uslugi.parent_category
    return render(request, 'uslugi/uslugi.html', {'uslugi':uslugi, 'parent_category': parent_category})

def view_children_category(request, slug_category, slug_uslugi): 
    try:
        category = Category.objects.get(slug = slug_category)
        children_category = category.category_set.get(slug = slug_uslugi)
        uslugies = children_category.uslusgi_set.all()

        return render(request, 'uslugi/category.html', {'category':children_category, 'uslugies':uslugies, 'parent_category': category})
    except:
        raise Http404 


def application(request): 
    try: 
        name = request.POST['name'] 
        comment = request.POST['comment']
        phone = request.POST['phone']
        if name != '' and comment != '' and phone != '': 
            application = ApplicationForm() 
            application.name = name
            application.phone = phone
            application.comment = comment
            application.save() 
            return render(request, 'uslugi/application.html')
        else: 
            return render(request, '404.html')
    except: 
        raise Http404

    




def e_handler404(request, exception): 
    return render(request, '404.html')

def create_regions(request): 
    for reg in Region.objects.all(): 
        if reg.title != 'Россия': 
            level1 = Category.objects.get(title = reg.title)
            for basic in Category.objects.filter(basic = True): 
                if basic.title != 'Создание и продвижение сайтов':
                    basic_save = basic.copy()  
                    basic.id = None 
                    basic.h1 = basic.h1 + ' ' + reg.title
                    basic.parent_category = level1
                    print('---' + basic.h1)
                    for uslugi in Uslusgi.objects.filter(parent_category = basic_save): 
                       
                        uslugi.id = None 
                        uslugi.h1 = uslugi.h1 + ' ' + reg.title
                        uslugi.parent_category = basic
                        print('-------' + uslugi.title)



def create_services_regions(general_cat_reg, general_basic_category, reg): 
    pass
        


def create_uslugi_regions(category_region, category_serveces, reg): 
    basic_uslugi = Uslusgi.objects.filter(basic=True)

    for uslugi in basic_uslugi: 
        print(uslugi.h1)
        uslugi.id = None 
        uslugi.parent_category = category_serveces 
        uslugi.h1 = uslugi.h1 + ' ' + reg.title
        uslugi.slug += '-' + str(reg.id) 
        uslugi.save()
