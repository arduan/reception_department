from django.db import models

class Patient(models.Model):
    """Модель пациента"""

    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    diagnosis = models.TextField(verbose_name='Диагноз')
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, verbose_name='Лечащий врач')
    date_of_admission = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    date_of_discharge = models.DateTimeField(null=True, blank=True, verbose_name='Дата выписки')

    def __str__(self):
        return f'{self.surname} {self.name} ({self.diagnosis})'

class Doctor(models.Model):
    """Модель врача"""

    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    speciality = models.CharField(max_length=100, verbose_name='Специальность')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f'{self.surname} {self.name} ({self.speciality})'
