from django.db import models


"""
"""
SUBJECT_ =  [("English", "English"),("Mathematics", "Mathematics"),("Science", "Science"),
("Social Science", "Social Science"),("Arts", "Arts"),("Making A Living", "Making A Living"),
("Health & Physical Education", "Health & Physical Education")]


GRADE_LEVEL = [
(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)
]


class AssessmentPeriod(models.Model):
	year = models.CharField(max_length=4)
	order = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return f'{self.order}, {self.year}'


class GradeLevel(models.Model):
	year = models.CharField(max_length=4)
	level = models.PositiveSmallIntegerField(choices=GRADE_LEVEL)

	def __str__(self):
		return f'Grade {self.level}'


class Student(models.Model):
	studentid = models.CharField(max_length=10, primary_key=True, verbose_name="StudentID")
	givenname = models.CharField(max_length=50, verbose_name="Given Name")
	middlename = models.CharField(max_length=20, verbose_name="Middle Name", blank=True)
	surname = models.CharField(max_length=20, verbose_name="Surname")
	dateofbirth = models.DateField()
	gender = models.CharField(
		max_length=6, choices=[
		("Female", "Female"), ("Male", "Male")]
	)


class Subject(models.Model):
	subjectid = models.CharField(max_length=20, primary_key=True)
	subject_name = models.CharField(max_length=50, choices=SUBJECT_)
	assessmentperiod = models.ForeignKey(to=AssessmentPeriod, on_delete=models.CASCADE)
	gradelevel = models.ForeignKey(to=GradeLevel, on_delete=models.CASCADE)
	periodscore = models.IntegerField()

	def __str__(self):
		return f'{self.gradelevel} {self.subject_name} - Assessment Period:{self.assessmentperiod} - Overal Score:{self.periodscore}'