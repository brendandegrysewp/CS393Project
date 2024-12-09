from django import forms

class SightingForm(forms.Form):
    date = forms.DateTimeField(required=False)
    comments = forms.CharField(max_length=1500, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=25, required=False)
    shape = forms.CharField(max_length=25, required=False)
    country = forms.CharField(max_length=255, required=False)
    duration = forms.IntegerField(required=False)
    # dateposted = forms.DateTimeField(required=False)
    longitude = forms.FloatField(required=False)
    latitude = forms.FloatField(required=False)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, required=True)
    isGov = forms.BooleanField(required=False,label="Government Employee")
    isAlien = forms.BooleanField(required=False, label="Alien")
    isAdmin = forms.BooleanField(required=False, label="Admin")

class CommentForm(forms.Form):
    # commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    # sightingid = models.ForeignKey('Sighting', models.DO_NOTHING, db_column='sightingId')  # Field name made lowercase.
    text = forms.CharField(max_length=1500, required=True)
    believability = forms.IntegerField(min_value=0, max_value=10)

class GovernmentnoteForm(forms.Form):
    text = forms.CharField(max_length=500, required=True,label="Government Note")

class SortForm(forms.Form):
    highLat = forms.FloatField(required=False, max_value=90,min_value=-90, label="Upper latitude limit")
    lowLat = forms.FloatField(required=False, max_value=90,min_value=-90, label="Lower latitude limit")
    highLong = forms.FloatField(required=False, max_value=90,min_value=-90, label="Upper longitude limit")
    lowLong = forms.FloatField(required=False, max_value=90,min_value=-90, label="Lower longitude limit")
    sort = forms.MultipleChoiceField(required=True,widget=forms.RadioSelect,choices={"ASC": "Increasing", "DESC": "Decreasing"})
