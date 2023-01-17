from django.contrib import admin
from .models import Student, Subject, AssessmentPeriod, GradeLevel


admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(AssessmentPeriod)
admin.site.register(GradeLevel)
