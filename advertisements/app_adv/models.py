from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.html import format_html

User=get_user_model() #получаем модель Userа

class Advertisements(models.Model):
    title=models.CharField("Заголовок", max_length=128)
    description=models.TextField("Описание")
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction=models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image=models.ImageField("Изображение", upload_to="advertisements/")

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_time.date()== timezone.now().date():
            creat_time=self.created_time.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; '
                               'font-weight: bold">Сегодня в '
                               '{}</span>', creat_time)
        return self.created_time.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_time.date() == timezone.now().date():
            upd_time = self.updated_time.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; '
                               'font-weight: bold">Сегодня в '
                               '{}</span>', upd_time)
        return self.updated_time.strftime("%d.%m.%Y в %H:%M:%S")

    # def __str__(self):
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"