from django.db import models

# Create your models here.


# class users(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=45)
#     password = models.CharField(max_length=45)
#     firstname = models.CharField(max_length=145)
#     lastname = models.CharField(max_length=145)
#     position = models.CharField(max_length=245)
#     area = models.PositiveSmallIntegerField(
#         default=0, null=False)        # dmo, pas, sas, las
#     is_active = models.PositiveSmallIntegerField(
#         default=0, null=False)        # active, deleted
#     is_superuser = models.PositiveSmallIntegerField(
#         default=0, null=False)
#     is_staff = models.PositiveSmallIntegerField(
#         default=0, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined
#     class Meta:
#         db_table = "users"

