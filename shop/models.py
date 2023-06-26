from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoris'

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse("Category_detail", kwargs={"pk": self.pk})


class Organization(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/')
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=100, default='Marrakech')
    zip_code = models.CharField(max_length=5, default='40160')
    created_by = models.ForeignKey(User, 
                                    on_delete=models.CASCADE, 
                                    related_name='Organisation_creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse("Organisation_detail", kwargs={"pk": self.pk})

class Event(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    subttitle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, 
                                        on_delete=models.CASCADE,
                                        related_name='event_category')
    main_image = models.ImageField(upload_to='eventImages/')
    thumbnail = models.ImageField(upload_to='eventThumbnails/')
    licence = models.FileField(upload_to='licences/')
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=100, default='Marrakech')
    created_by = models.ForeignKey(User, 
                                    on_delete=models.CASCADE, 
                                    related_name='Event_creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
#        return reverse("Event_detail", kwargs={"pk": self.pk})

class Pricing_plan(models.Model):
    plan_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tickets_available = models.IntegerField(default=1000, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    event = models.ForeignKey(Event, 
                                on_delete=models.CASCADE,
                                related_name='corresponding_event')
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Pricing_plan'
        verbose_name_plural = 'Pricing_plans'

    def __str__(self):
        return self.plan_type

#    def get_absolute_url(self):
#        return reverse("Pricing_plan_detail", kwargs={"pk": self.pk})
