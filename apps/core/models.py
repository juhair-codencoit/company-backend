from django.db import models

#### Project Related Tables ####

class Industry(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="industry_icon/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    banner_image = models.ImageField(upload_to="banner_pic/",blank=True)
    industry_id = models.ForeignKey(Industry,on_delete=models.CASCADE)
    timeline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_pic/")  

    def __str__(self):
        return self.project_id.title
    
class ProjectProblem(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    statement = models.TextField()

class Services(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_icon = models.ImageField(upload_to="service_short_icon/")
    long_icon = models.ImageField(upload_to="service_long_icon/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ServiceProject(models.Model):
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('service_id','project_id')

class ServicePoint(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class TechCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="tech_category_icon/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Technologies(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="technology_icon/")
    tech_category_id = models.ForeignKey(TechCategory, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TechServicePoint(models.Model):
    tech_id = models.ForeignKey(Technologies, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class TechSolutionPoint(models.Model):
    tech_id = models.ForeignKey(Technologies, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class TechnologiesProject(models.Model):
    tech_id = models.ForeignKey(Technologies,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tech_id','project_id')

class TechExperties(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="tech_expert_pic/")

    def __str__(self):
        return self.name
    
class ClientStatement(models.Model): 
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    client_statement = models.TextField()
    client_picture = models.ImageField(upload_to='client_pic/')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
