from rest_framework import serializers
from .models import *

class InsdustrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name','icon']

class ProjectListSerializers(serializers.ModelSerializer):
    industry_name = serializers.SerializerMethodField()
    
    class Meta:

        model = Projects
        fields = ['id','title','short_description','banner_image','industry_name']

        def get_image_url(self,obj):
            request = self.context.get('request')
            image_url = obj.fingerprint.url
            return request.build_absolute_uri(image_url)
        
    def get_industry_name(self, obj:Projects):
        return obj.industry_id.name
        