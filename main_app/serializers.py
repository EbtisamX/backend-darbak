from rest_framework import serializers
from .models import JobApplication,Note,Skill


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'company_name', 'job_title', 'application_date', 'application_status']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user  
        return JobApplication.objects.create(user=user, **validated_data)

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'