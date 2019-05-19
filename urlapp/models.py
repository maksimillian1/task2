from django.db import models

class ShorterUrl(models.Model):

    request_id = models.AutoField(primary_key=True, unique=True)
    base_url = models.URLField(max_length=100)
    short_url = models.URLField(max_length=50, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "id:{}, url:{}".format(self.request_id, self.base_url)
