from django.db import models

# Create your models here.
class Categories(models.Model):
	catagory_name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.catagory_name
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class Persons(models.Model):
	person_name = models.CharField(max_length=2000, unique=True)
	person_whatsapp_no = models.IntegerField()
	catagory = models.ForeignKey(Categories, on_delete=models.CASCADE)

	def __str__(self):
		return self.person_name

	class Meta:
		verbose_name = "Person"
		verbose_name_plural = "Persons"