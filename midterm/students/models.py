from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=True)
    years_of_study = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)



