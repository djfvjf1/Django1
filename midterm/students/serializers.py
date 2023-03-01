from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=20, allow_null=False)
    surname = serializers.CharField(min_length=5, max_length=20, allow_null=True)
    years_of_study = serializers.IntegerField(allow_null=False)

    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.years_of_study = validated_data.get('years_of_study', instance.years_of_study)
        instance.save()
        return instance

