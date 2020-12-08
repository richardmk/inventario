from django.db import models



#clase general inicial
class Base(models.Model):
    created = models.DateTimeField('Created', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True, auto_now_add=False)
    deleted = models.DateTimeField('Deleted', auto_now=True, auto_now_add=False)
    state = models.BooleanField('State', default=True)

    class Meta:
        abstract = True




class Site(Base):
    description = models.CharField('Description', max_length=50)

    def __str__(self):
        return self.description





class Zone(Base):
    description = models.CharField('Description', max_length=50)

    def __str__(self):
        return self.description





class Area(Base):
    description = models.CharField('Description', max_length=50)

    def __str__(self):
        return self.description
    



#clase para los usuarios
class Staff(Base):
    first_name = models.CharField('First name', max_length=20)
    last_name = models.CharField('Last name', max_length=20)
    user_ad = models.CharField('User AD', max_length=20)
    pass_ad = models.CharField('Pass AD', max_length=20)
    user_admin = models.CharField('User admin', max_length=20)
    pass_admin = models.CharField('Pass admin', max_length=20)
    user_nisira = models.CharField('Pass admin', max_length=20)
    pass_nisira = models.CharField('Pass admin', max_length=20)
    email = models.EmailField('Email', max_length=120)
    anydesk = models.CharField('Anydesk', max_length=10)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name




class CPU(Base):
    operative = models.BooleanField(default=True)
    code = models.CharField('Code', max_length=20)
    pc_name = models.CharField('PC Name', max_length=20)
    ip = models.GenericIPAddressField(protocol='IPv4')
    mac = models.CharField('Mac', max_length=20)
    brand = models.CharField('Brand', max_length=20)
    model = models.CharField('Model', max_length=20)
    serial = models.CharField('Serial', max_length=50)  
    microprocessor = models.CharField('Microprocessor', max_length=50)
    ram = models.CharField('Ram', max_length=50)
    storage = models.CharField('Storage', max_length=50)
    cd_reader = models.BooleanField(default=True)
    so = models.CharField('SO', max_length=50)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff
    