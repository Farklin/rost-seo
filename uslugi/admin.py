from django.contrib import admin
from .models import Category, Region
from .models import Uslusgi, Meta, Article, ApplicationForm

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources 
from import_export import fields 
from import_export.widgets import ForeignKeyWidget

class GenerateUrlChPU(resources.ModelResource):
    prepopulated_fields = {'slug': ('title',)}
    parent = fields.Field(column_name='parent', attribute='parent', widget=ForeignKeyWidget(Category, 'title'))
    
    class Meta: 
        model = Category 
 

class UslusgiResource(resources.ModelResource): 
    prepopulated_fields = {'slug': ('title',)}
    parent_category = fields.Field(column_name='parent_category', attribute='parent_category', widget=ForeignKeyWidget(Category, 'title'))
    
    class Meta: 
        model = Uslusgi 

class CategoryAdmin(ImportExportActionModelAdmin): 
    resource_class = GenerateUrlChPU 
    list_display = [field.name for field in Category._meta.fields if field.name != "id" and field.name != "content"]
    list_display.append('image_img')
    list_display.remove('image')
    list_filter = ['published', 'basic']
    search_fields = ['title']
    readonly_fields = ['image_img',]
    
        
class UslugiAdmin(ImportExportActionModelAdmin): 
    resource_class = UslusgiResource 
    list_display = [field.name for field in Uslusgi._meta.fields if field.name != "id"]


        
class MetaAdmin(ImportExportActionModelAdmin): 
    list_display = [field.name for field in Meta._meta.fields if field.name != "id"]


#Заявка 
class ApplicationFormAdmin(ImportExportActionModelAdmin): 
    resource_class = GenerateUrlChPU 
    list_display = [field.name for field in ApplicationForm._meta.fields if field.name != "id"]
    search_fields = ['phone']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Uslusgi, UslugiAdmin ) 
admin.site.register(Meta, MetaAdmin)
admin.site.register(Article)
admin.site.register(ApplicationForm, ApplicationFormAdmin)
admin.site.register(Region)