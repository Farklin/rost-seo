from uslugi.models import Category, Meta, Article


def menu(request): 
    menu_list = Category.objects.filter(parent = None).order_by('sorting')
    
    menu = [] 

    for category in menu_list: 
        
        cat = Category.objects.get(title = category.title)
        children = cat.category_set.all().filter(published = True)

        if len(children) > 0:    
            menu.append( dict({ 
                'level1': cat, 
                'level2': children, 
            }))
        else: 
             menu.append( dict({ 
                'level1': cat, 
            }))
    
    menu_list_article = Article.objects.filter(parent = None)
    menu_article = []

    for article in menu_list_article: 
        
        art = Article.objects.get(title = article.title)
        children = art.article_set.all().filter(published = True).order_by('sorting')

        if len(children) > 0:    
            menu_article.append( dict({ 
                'level1': art, 
                'level2': children, 
            }))
        else: 
             menu_article.append( dict({ 
                'level1': art, 
            }))
        
    return{'menu_list': menu_list, 'menu': menu, 'menu_article': menu_article}

def meta(request):
   
    try:
        meta = Meta.objects.get(slug = request.path)
        return {'meta': meta}
    except:  
        return {'meta': ''}



