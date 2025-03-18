from django.contrib import admin
from .models import *

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {"slug":("name",)}
    ordering = ["name"]

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug']
    prepopulated_fields = {"slug":("title",)}
    ordering = ["title"]

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display=["id","project_id"]
    ordering = ["project_id"]

@admin.register(ProjectProblem)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display=["id","project_id"]
    ordering = ["project_id"]

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['name']


@admin.register(ServiceProject)
class ServiceProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_id', 'service_id']
    ordering = ['project_id', 'service_id']

@admin.register(ServicePoint)
class ServicePointAdmin(admin.ModelAdmin):
    list_display = ["id", "service_id", "title"]
    ordering = ["service_id"]

@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    ordering = ["name"]

@admin.register(Technologies)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["id","name","slug"]
    ordering = ["name"]
    prepopulated_fields = {"slug":("name",)}

@admin.register(TechServicePoint)
class ServicePointAdmin(admin.ModelAdmin):
    list_display = ["id", "tech_id", "title"]
    ordering = ["tech_id"]

admin.site.register(TechSolutionPoint)
admin.site.register(TechExperties)

@admin.register(TechnologiesProject)
class ServiceProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_id', 'tech_id']
    ordering = ['project_id', 'tech_id']

@admin.register(ClientStatement)
class ClientStatment(admin.ModelAdmin):
    list_display= ['name','designation','company_name']
    ordering = ['name','company_name']
    