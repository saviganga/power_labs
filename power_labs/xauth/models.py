from django.db import models

import uuid


class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)



class AuthToken(models.Model):

    id= models.UUIDField(
        help_text="Unique token identifier",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        serialize=True,
        null=False
    )

    token = models.CharField(max_length=50)
    user = models.ForeignKey("xuser.CustomUser", on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, null=True)
    expiry_date = models.DateTimeField(null=True)