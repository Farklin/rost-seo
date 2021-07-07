from django.db import models, transaction
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Meta(models.Model): 
    slug = models.TextField(max_length=70, unique=True, verbose_name = 'url') 
    title = models.CharField(max_length=150, verbose_name = 'title')
    description = models.CharField(max_length=150, verbose_name = 'description')



class Region(models.Model): 
    title = models.CharField(max_length=150, verbose_name = 'Название региона')
    slug = models.SlugField(max_length=70, verbose_name = 'url')
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Category(models.Model):

    slug = models.SlugField(max_length=70, verbose_name = 'url')
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
    content = RichTextField(null=True, blank=True, verbose_name ='Описание', default=None)
    image = models.ImageField(verbose_name = 'Изображение', null = True, upload_to = 'images/', blank = 'null', default = 'images/no_photo/no_photo.png')
    published = models.BooleanField(verbose_name="Опубликованный") 
    parent = models.ForeignKey('self', verbose_name="Родительская категория", on_delete = models.PROTECT, null = True, blank=True)
    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.PROTECT, null = True, blank=True)
    
    basic = models.BooleanField(verbose_name="Основной", default='0')  
    immutable = models.BooleanField(verbose_name="Неизменяемый", default='0')  

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
        
    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
        image_img.short_description = 'Картинка'
        image_img.allow_tags = True
    
    def get_absolute_url(self): 
        if self.parent == None: 
            return f'/{self.slug}/'
        else: 
            return f'/{self.parent.slug}/{self.slug}/'
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.pk is None:
            try: 
                Meta.objects.create(slug=self.get_absolute_url(), title = self.h1+'- '+self.region+' Рост SEO', description= self.h1 + ' по лучшим ценам ☛ Качественные услуги ◈ гарантия на все работы ★★★ Звони и заказывай работаем по всей России ☎ +7 904 034 3013.')
            except: 
                pass 
        super(Category, self).save(*args, **kwargs)

class Uslusgi(models.Model):
    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url', null=True, blank=True )
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
    content = RichTextField(null=True, blank=True, verbose_name ='Описание', default=None)
    published = models.BooleanField(verbose_name = 'Публикация', default='False') 
    price = models.IntegerField(verbose_name = 'Цена', default='1')
    image = models.ImageField(verbose_name = 'Изображение', null = True, upload_to = 'images/' , blank = 'null', default = 'images/no_photo/no_photo.png') 
    basic = models.BooleanField(verbose_name="Основной", default='0')  
    parent_category = models.ForeignKey(Category, verbose_name='Главная категория', on_delete=models.PROTECT, null = True, blank=True)
    similar_services = models.ManyToManyField('self', verbose_name='Похожие услуги', null = True,  blank=True)
    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self): 
        if self.parent_category.parent == None:
            return f'/{self.parent_category.slug}/{self.slug}/'
        else: 
            return f'/{self.parent_category.parent.slug}/{self.parent_category.slug}/{self.slug}/'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.pk is None:
            try: 
                Meta.objects.create(slug=self.get_absolute_url(), title = self.h1+' во Владимире сервисный центр ComputerMaster', description= self.h1 + ' по лучшей цене ☛ Выезд мастера по всему Владимиру ◈ гарантия на все работы ★★★ Звони ☎ +7 904 034 3013.')
            except: 
                pass 
        super(Uslusgi, self).save(*args, **kwargs)

class Article(models.Model): 
    slug = models.SlugField(max_length=70, unique=True, verbose_name = 'url', null=True, blank=True )
    title = models.CharField(max_length=150, verbose_name = 'Название')
    h1 = models.CharField(max_length=150, verbose_name = 'Заголовок h1', blank=True, null=True)
    content = RichTextField(null=True, blank=True, verbose_name ='Контент страницы', default=None)
    parent = models.ForeignKey('self', verbose_name="Основаная", on_delete = models.PROTECT, null = True, blank=True)
    published = models.BooleanField(verbose_name = 'Публикация', default='True') 
    sorting = models.IntegerField(max_length=1, verbose_name='Сортировка', default='1', null = True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self): 
        if self.parent == None: 
            return f'/{self.slug}/'
        else: 
            return f'/{self.parent.slug}/{self.slug}/'





class ApplicationForm(models.Model): 
    STATUS_APLICATION = (
        ('new', 'Новая заявка'),
        ('performer_lookup', 'Заявка взята в обработку'),
        ('cancelled', 'Заказ отменен'),
        ('delivered_finish', 'Заказ завершен'),
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    comment = models.TextField(max_length=300, verbose_name='Комментарий')
    name =  models.CharField(max_length=30, verbose_name='Имя')
    status = models.CharField(max_length=30, choices=STATUS_APLICATION, default='new')

    def __str__(self):
        return str(self.date)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки' 
