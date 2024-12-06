from django import forms

class SightingForm(forms.Form):
    date = forms.DateTimeField(required=False)
    comments = forms.CharField(max_length=1500, required=True)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=25, required=False)
    shape = forms.CharField(max_length=25, required=False)
    country = forms.CharField(max_length=255, required=False)
    duration = forms.IntegerField(required=False)
    dateposted = forms.DateTimeField(required=False)
    longitude = forms.FloatField(required=False)
    latitude = forms.FloatField(required=False)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, required=True)

class CommentForm(forms.Form):
    # commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    # sightingid = models.ForeignKey('Sighting', models.DO_NOTHING, db_column='sightingId')  # Field name made lowercase.
    text = forms.CharField(max_length=1500, required=True)
    believability = forms.IntegerField(min_value=0, max_value=10)