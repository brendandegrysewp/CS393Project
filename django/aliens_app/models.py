# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Alien(models.Model):
    alienid = models.AutoField(db_column='alienId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'alien'


class Alientoexpedition(models.Model):
    alienid = models.OneToOneField(Alien, models.DO_NOTHING, db_column='alienId', primary_key=True)  # Field name made lowercase. The composite primary key (alienId, expeditionId) found, that is not supported. The first column is selected.
    expeditionid = models.ForeignKey('Expedition', models.DO_NOTHING, db_column='expeditionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alientoexpedition'
        unique_together = (('alienid', 'expeditionid'),)


class Comment(models.Model):
    commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    # userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    # ubody = models.ForeignKey(User, models.DO_NOTHING, null=True)
    sightingid = models.ForeignKey('Sighting', models.DO_NOTHING, db_column='sightingId')  # Field name made lowercase.
    text = models.CharField(max_length=1500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    believability = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Expedition(models.Model):
    expeditionid = models.AutoField(db_column='expeditionId', primary_key=True)  # Field name made lowercase.
    sightingid = models.ForeignKey('Sighting', models.DO_NOTHING, db_column='sightingId')  # Field name made lowercase.
    craftmodel = models.CharField(db_column='craftModel', max_length=35, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedition'


class Governmentemployee(models.Model):
    employeeid = models.AutoField(db_column='employeeId', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=35, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    position = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'governmentemployee'


class Governmentnote(models.Model):
    noteid = models.AutoField(db_column='noteId', primary_key=True)  # Field name made lowercase.
    sightingid = models.ForeignKey('Sighting', models.DO_NOTHING, db_column='sightingId')  # Field name made lowercase.
    employeeid = models.ForeignKey(Governmentemployee, models.DO_NOTHING, db_column='employeeId')  # Field name made lowercase.
    text = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'governmentnote'


class Sighting(models.Model):
    sightingid = models.AutoField(db_column='sightingId', primary_key=True)  # Field name made lowercase.  
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=1500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    shape = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    dateposted = models.DateTimeField(db_column='datePosted', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sighting'


# class User(models.Model):
    # userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    # name = models.CharField(max_length=35, blank=True, null=True)
    # email = models.CharField(max_length=35, blank=True, null=True)
    # datejoined = models.DateTimeField(db_column='dateJoined', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'user'
