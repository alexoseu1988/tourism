from django import forms
from .models import Tour, Day, Inclusive, NotInclusive, ImageForDay, Icon, Review, WhyWe, Client, ImageForGalery
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm
from multiupload.fields import MultiFileField

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title', 'title1', 'title2', 'dateStart', 'dateEnd', 
                  'tagline', 'description', 'image1Section2', 'image2Section2', 'image3Section2',
                  'priceAdult', 'priceChild',
                  'isActive', 'isOutside', 'isOneDay',
                  'backgroundSection1', 'backgroundAdditionalServices', 'backgroundSectionBooking')
        widgets = {
            'isActive': forms.CheckboxInput(),
            'isOutside': forms.CheckboxInput(),
            'isOneDay': forms.CheckboxInput(),
            'dateStart': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
            'dateEnd': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
            'description': CKEditorWidget(),
        }
        
        
class Background1Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('backgroundSection1',)
        
class Background2Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('backgroundAdditionalServices',)
        
class Background3Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('backgroundSectionBooking',)
        
class Image1Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('image1Section2',)
        
class Image2Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('image2Section2',)
        
class Image3Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('image3Section2',)
        
class Titlte1Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title1',)
        
class Titlte2Form(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title2',)
        
class DateStartForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('dateStart',)
        widgets = {
            'dateStart': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
        }
        
class DateEndForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('dateEnd',)
        widgets = {
            'dateEnd': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
        }
        
class TaglineForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('tagline',)
        
class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('description',)
        widgets = {
            'description': CKEditorWidget(),
        }
        
class PriceAdultForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('priceAdult', 'dateBeforeAdult', 'priceAdultBefore',)
        widgets = {
                'dateBeforeAdult': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
            }
        
class PriceChildForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('priceChild', 'dateBeforeChild', 'priceChildBefore',)
        widgets = {
                'dateBeforeChild': forms.SelectDateWidget(empty_label=("Рік", "Місяць", "День")),
            }
    
class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('number', 'description')
        widgets = {
            'description': CKEditorWidget(),
        }
        
class InclusiveForm(forms.ModelForm):
    class Meta:
        model = Inclusive
        fields = ('title', 'description', 'icon')
        
class NotInclusiveForm(forms.ModelForm):
    class Meta:
        model = NotInclusive
        fields = ('title', 'description', 'price', 'icon')
        
class WhyWeForm(forms.ModelForm):
    class Meta:
        model = WhyWe
        fields = ('title', 'description', 'icon')
        
class ImageForDayForm(forms.ModelForm):
    class Meta:
        model = ImageForDay
        fields = ('title', 'image')
        
class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ('title', 'icon')
        
class ReviewTitleForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'review', 'tour')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'review')
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'phone', 'email')
        
class ImageForGaleryForm(forms.ModelForm):
    class Meta:
        model = ImageForGalery
        fields = ['image']
        
class MultiImageForm(forms.Form):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1920*1080*5)