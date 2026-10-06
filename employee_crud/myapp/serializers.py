from rest_framework import serializers
from myapp.models import Employee


class EmployeeSerializer(serializers.Serializer):

    empid = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    place = serializers.CharField(max_length=30)

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    gender = serializers.ChoiceField(choices=gender_choices)
    joining_date = serializers.DateField()
    salary = serializers.IntegerField()
    designation = serializers.CharField(max_length=30)
    image=serializers.ImageField()

    # after validation and before saving
    def create(self, validated_data):
        e = Employee.objects.create(**validated_data)
        return e


    def update(self, instance, validated_data):

        instance.empid = validated_data.get('empid', instance.empid)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.place = validated_data.get('place', instance.place)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.joining_date = validated_data.get(
            'joining_date', instance.joining_date
        )
        instance.salary = validated_data.get('salary', instance.salary)
        instance.designation = validated_data.get(
            'designation', instance.designation
        )

        instance.save()

        return instance


##  used for extra validation
    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError("Age must be positive")
        return data
    