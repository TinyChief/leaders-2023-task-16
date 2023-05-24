from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from staff.models import Organization


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        surname: str,
        **extra_fields
    ) -> "User":
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        surname: str,
        **extra_fields
    ):
        user = self.create_user(
            email, password, first_name, last_name, surname, **extra_fields
        )
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CANDIDATE = "CANDIDATE", "Кандидат"
        INTERN = "INTERN", "Стажер"
        CURATOR = "CURATOR", "Куратор"
        STAFF = "STAFF", "Кадровый специалист"
        MENTOR = "MENTOR", "Наставник"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "surname"]

    objects = UserManager()

    email = models.EmailField("E-Mail", unique=True)
    role = models.CharField(
        verbose_name="Роль",
        max_length=16,
        choices=Role.choices,
        default=Role.CANDIDATE,
        db_index=True,
    )
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    surname = models.CharField(verbose_name="Отчество", max_length=50)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True)

    organization = models.ForeignKey(
        Organization, on_delete=models.RESTRICT, verbose_name="Организация", null=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_active(self):
        return True


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="info"
    )
    birthdate = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    university_name = models.CharField(
        verbose_name="Учебное заведение", max_length=50, blank=True
    )
    university_year = models.PositiveSmallIntegerField(
        verbose_name="Курс", blank=True, null=True
    )
    job_experience = models.TextField(verbose_name="Опыт работы", blank=True)
    skills = models.TextField(verbose_name="Навыки", blank=True)
    departments = models.TextField(
        verbose_name="Предпочитаемые направления стажировки", blank=True
    )
    citizenship = models.CharField(
        verbose_name="Гражданство", blank=True, max_length=50
    )

    class Meta:
        verbose_name = "Информация о пользователе"
