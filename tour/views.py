import os
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TourForm, DayForm, InclusiveForm, NotInclusiveForm, Titlte1Form, Titlte2Form,\
    DateStartForm, DateEndForm, TaglineForm, DescriptionForm, PriceAdultForm, PriceChildForm,\
    Background1Form, Background2Form, Background3Form,\
    Image1Form, Image2Form, Image3Form, ImageForDayForm, IconForm, \
    ReviewTitleForm, ReviewForm, WhyWeForm, ClientForm, UserLoginForm, \
    ImageForGaleryForm, MultiImageForm
from .models import Tour, Day, Inclusive, NotInclusive, ImageForDay, Icon, Review, WhyWe, Client, ImageForGalery
from django.contrib.auth import login, logout
from datetime import date
from django.core.mail import send_mail

today = date.today()

## Форма входа

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('administrator')
    else:
        form = UserLoginForm()
    return render(request, 'tour/user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('administrator')

## Титульные страницы
        
def index(request):
    tours = Tour.objects.filter(isActive=True, isOneDay=False)
    holidays = Tour.objects.filter(isActive=True, isOneDay=True)
    why_we = WhyWe.objects.all()
    reviews = Review.objects.all()[0:6]
    return render(request, 'tour/index.html', 
                  {'tours': tours, 'holidays': holidays, 'reviews': reviews, 'why_we': why_we})
    
def documents(request):
    return render(request, 'tour/documents.html', {})

def how_to_apply(request):
    return render(request, 'tour/how_to_apply.html', {})

def contacts(request):
    return render(request, 'tour/contacts.html', {})

def administrator(request):
    tours = Tour.objects.filter(isOneDay=False)
    holidays = Tour.objects.filter(isOneDay=True)
    why_we = WhyWe.objects.all()
    reviews = Review.objects.all()[0:6]
    return render(request, 'tour/administrator.html', 
                  {'tours': tours, 'holidays': holidays, 'reviews': reviews, 'why_we': why_we})

def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'tour/all_reviews.html', {'reviews': reviews})

def galery(request):
    tours = Tour.objects.filter(isActive=True, isOneDay=False)
    view_tours = [i for i in tours if (len(i.images.all()) > 0)]
    holidays = Tour.objects.filter(isActive=True, isOneDay=True)
    view_holidays = [i for i in holidays if (len(i.images.all()) > 0)]
    return render(request, 'tour/galery.html', 
                  {'tours': tours, 'view_tours': view_tours, 'holidays': holidays, 'view_holidays': view_holidays})

## Страницы с турами

def tour(request, tour_id):
    clients = Client.objects.all()
    emails = [i.email for i in clients]
    tour = get_object_or_404(Tour, id=tour_id)
    days = Day.objects.filter(tour=tour)
    cards = Inclusive.objects.filter(tour=tour)
    reviews = Review.objects.filter(tour=tour)[0:4]
    not_cards = NotInclusive.objects.filter(tour=tour)
    upcoming_tours = [i for i in Tour.objects.all() if (i.isActive == True and i.pk != tour.pk and i.dateStart != None and i.dateStart > today)][0:3]
    if request.method == 'POST':
        form1 = ReviewForm(request.POST)
        form2 = ClientForm(request.POST)
        if form1.is_valid():
            review = Review.objects.create(**form1.cleaned_data)
            review.tour = tour
            review.save()
            return redirect('tour', tour.pk)
        if form2.is_valid():
            if form2.cleaned_data['email'] not in emails:
                client = Client.objects.create(**form2.cleaned_data)
            content = f"Клієнт: {form2.cleaned_data['name']} \n \
                        Телефон: {form2.cleaned_data['phone']} \n \
                        email: {form2.cleaned_data['email']} \n \
                        Забронював тур: {tour.title1}"
            send_mail('Новий клієнт', content, 'odesatours@ukr.net', ['ch.chaplynska@gmail.com'], fail_silently=False)
            return redirect('thank_you', tour.pk)
    else:
        form1 = ReviewForm()
        form2 = ClientForm()
    return render(request, 'tour/tour.html', 
                  {'tour': tour,'days': days, 'cards': cards, 'not_cards': not_cards, 
                   'upcoming_tours': upcoming_tours, 'reviews': reviews, 'form1': form1, 'form2': form2})

def tour_galery(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour/tour_galery.html', {'tour': tour})


def thank_you(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour/thank_you.html', {'tour': tour,})

def edit_tour(request, tour_id):
    clients = Client.objects.all()
    emails = [i.email for i in clients]
    tour = get_object_or_404(Tour, id=tour_id)
    days = Day.objects.filter(tour=tour)
    cards = Inclusive.objects.filter(tour=tour)
    reviews = Review.objects.filter(tour=tour)[0:4]
    not_cards = NotInclusive.objects.filter(tour=tour)
    upcoming_tours = [i for i in Tour.objects.all() if (i.isActive == True and i.pk != tour.pk and i.dateStart != None and i.dateStart > today)][0:3]
    if request.method == 'POST':
        form1 = ReviewForm(request.POST)
        form2 = ClientForm(request.POST)
        if form1.is_valid():
            review = Review.objects.create(**form1.cleaned_data)
            review.tour = tour
            review.save()
            return redirect('tour', tour.pk)
        if form2.is_valid():
            if form2.cleaned_data['email'] not in emails:
                client = Client.objects.create(**form2.cleaned_data)
            content = f"Клієнт: {form2.cleaned_data['name']} \n \
                        Телефон: {form2.cleaned_data['phone']} \n \
                        email: {form2.cleaned_data['email']} \n \
                        Забронював тур: {tour.title1}"
            send_mail('Новий клієнт', content, 'odesatours@ukr.net', ['ch.chaplynska@gmail.com'], fail_silently=False)
            return redirect('thank_you', tour.pk)
    else:
        form1 = ReviewForm()
        form2 = ClientForm()
    return render(request, 'tour/edit_tour.html', 
                  {'tour': tour,'days': days, 'cards': cards, 'not_cards': not_cards, 
                   'upcoming_tours': upcoming_tours, 'reviews': reviews, 'form1': form1, 'form2': form2})

## Создаем новые объекты автоматически

def create_tour(request):
    tour = Tour.objects.create(
        title = 'new_tour',
        title1 = 'Название тура',
        title2 = 'Вторая строка названия тура',
        dateStart = None,
        dateEnd = None,
        
        priceAdult = '1000 грн',
        priceChild = '1000 грн',
        
        tagline = 'Слоган для второй секции',
        description = 'Полное описание тура',
        image1Section2 = 'photos/default_image.jpg',
        image2Section2 = 'photos/default_image.jpg',
        image3Section2 = 'photos/default_image.jpg',
        
        isActive = True,
        isOutside = True,
        isOneDay = False,
        
        backgroundSection1 = 'photos/default_image.jpg',
        backgroundAdditionalServices = 'photos/default_image.jpg',
        backgroundSectionBooking = 'photos/default_image.jpg'
    )
    return redirect('edit_tour', tour.pk)

def create_holiday(request):
    tour = Tour.objects.create(
        title = 'new_tour',
        title1 = 'Название тура',
        title2 = 'Вторая строка названия тура',
        dateStart = None,
        dateEnd = None,
        
        priceAdult = '1000 грн',
        priceChild = '1000 грн',
        
        tagline = 'Слоган для второй секции',
        description = 'Полное описание тура',
        image1Section2 = 'photos/default_image.jpg',
        image2Section2 = 'photos/default_image.jpg',
        image3Section2 = 'photos/default_image.jpg',
        
        isActive = True,
        isOutside = True,
        isOneDay = True,
        
        backgroundSection1 = 'photos/default_image.jpg',
        backgroundAdditionalServices = 'photos/default_image.jpg',
        backgroundSectionBooking = 'photos/default_image.jpg'
    )
    return redirect('edit_tour', tour.pk)


## Создаем новые объекты вручную

def new_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = TourForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_day(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            day = Day.objects.create(**form.cleaned_data)
            day.tour = tour
            day.save()
            return redirect('change_day', day.pk)
    else:
        form = DayForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_image_forday(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    if request.method == 'POST':
        form = ImageForDayForm(request.POST, request.FILES)
        if form.is_valid():
            image = ImageForDay.objects.create(**form.cleaned_data)
            image.day = day
            image.save()
            return redirect('change_day', day.pk)
    else:
        form = ImageForDayForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_icon(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = IconForm(request.POST, request.FILES)
        if form.is_valid():
            icon = Icon.objects.create(**form.cleaned_data)
            return redirect('edit_tour', tour.pk)
    else:
        form = IconForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_inclusive(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = InclusiveForm(request.POST)
        if form.is_valid():
            card = Inclusive.objects.create(**form.cleaned_data)
            card.tour = tour
            card.save()
            return redirect('edit_tour', tour.pk)
    else:
        form = InclusiveForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_not_inclusive(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = NotInclusiveForm(request.POST)
        if form.is_valid():
            card = NotInclusive.objects.create(**form.cleaned_data)
            card.tour = tour
            card.save()
            return redirect('edit_tour', tour.pk)
    else:
        form = NotInclusiveForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_why_we(request):
    if request.method == 'POST':
        form = WhyWeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('administrator')
    else:
        form = WhyWeForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_review_title(request):
    if request.method == 'POST':
        form = ReviewTitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewTitleForm()
    return render(request, 'tour/change_obj.html', {'form': form})

def new_review(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(**form.cleaned_data)
            review.tour = tour
            review.save()
            return redirect('tour', tour.pk)
    else:
        form = ReviewForm()
    return render(request, 'tour/change_obj.html', {"form" : form})

def upload_galery_images(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    if request.method == 'POST':
        form = MultiImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in form.cleaned_data['images']:
                ImageForGalery.objects.create(tour=tour, image=image)
            return redirect('tour_galery', tour.pk)
    else:
        form = MultiImageForm()
    return render(request, 'tour/upload_galery_images.html', {'tour': tour, 'form': form,})


## Редактируем объекты комплексно

def change_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = TourForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_day(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    tour = day.tour
    images = ImageForDay.objects.filter(day=day)
    if request.method == 'POST':
        form = DayForm(request.POST, request.FILES, instance=day)
        if form.is_valid():
            form.save()            
            return redirect('change_day', day.pk)
    else:
        form = DayForm(instance=day)
    return render(request, 'tour/change_day.html', {'form': form, 'day': day, 'images': images, 'tour': tour})

def change_inclusive(request, card_id):
    card = get_object_or_404(Inclusive, id=card_id)
    tour = card.tour
    if request.method == 'POST':
        form = InclusiveForm(request.POST, instance=card)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = InclusiveForm(instance=card)
    return render(request, 'tour/change_obj.html', {'form': form, 'card': card})

def change_not_inclusive(request, card_id):
    card = get_object_or_404(NotInclusive, id=card_id)
    tour = card.tour
    if request.method == 'POST':
        form = NotInclusiveForm(request.POST, instance=card)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = NotInclusiveForm(instance=card)
    return render(request, 'tour/change_obj.html', {'form': form, 'card': card})

def change_why_we(request, card_id):
    card = get_object_or_404(WhyWe, id=card_id)
    if request.method == 'POST':
        form = WhyWeForm(request.POST, instance=card)
        if form.is_valid():
            form.save()            
            return redirect('administrator')
    else:
        form = WhyWeForm(instance=card)
    return render(request, 'tour/change_obj.html', {'form': form, 'card': card})

# def change_image_forday(request, image_id):
#     image = get_object_or_404(ImageForDay, id=image_id)
#     day = image.day
#     tour = day.tour
#     if request.method == 'POST':
#         form = ImageForDayForm(request.POST, request.FILES, instance=image)
#         if form.is_valid():
#             form.save()            
#             return redirect('change_day', day.pk)
#     else:
#         form = ImageForDayForm(instance=image)
#     return render(request, 'tour/change_img_for_day.html', {'form': form, 'tour': tour, 'day': day})

def change_image_forday(request, image_id):
    image = get_object_or_404(ImageForDay, id=image_id)
    day = image.day
    tour = day.tour
    old_image_path = image.image.path
    if request.method == 'POST':
        form = ImageForDayForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            new_image = form.cleaned_data['image']  # Получаем новое изображение из формы
            form.save()
            if image.image and image.image != new_image:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                os.remove(old_image_path)  # Удаляем старое изображение из файловой системы
            return redirect('change_day', day.pk)
    else:
        form = ImageForDayForm(instance=image)

    return render(request, 'tour/change_img_for_day.html', {'form': form, 'tour': tour, 'day': day})



## Редактируем отдельные элементы тура

def change_background1(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.backgroundSection1.path
    if request.method == 'POST':
        form = Background1Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_background = form.cleaned_data['backgroundSection1']
            form.save()    
            if tour.backgroundSection1 and tour.backgroundSection1 != new_background:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы        
            return redirect('edit_tour', tour.pk)
    else:
        form = Background1Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_background2(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.backgroundAdditionalServices.path
    if request.method == 'POST':
        form = Background2Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_background = form.cleaned_data['backgroundAdditionalServices']
            form.save()
            if tour.backgroundAdditionalServices and tour.backgroundAdditionalServices != new_background:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы
            return redirect('edit_tour', tour.pk)
    else:
        form = Background2Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_background3(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.backgroundSectionBooking.path
    if request.method == 'POST':
        form = Background3Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_background = form.cleaned_data['backgroundSectionBooking']
            form.save() 
            if tour.backgroundSectionBooking and tour.backgroundSectionBooking != new_background:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы
            return redirect('edit_tour', tour.pk)
    else:
        form = Background3Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_image1(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.image1Section2.path
    if request.method == 'POST':
        form = Image1Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_img = form.cleaned_data['image1Section2']
            form.save()       
            if tour.image1Section2 and tour.image1Section2 != new_img:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы
            return redirect('edit_tour', tour.pk)
    else:
        form = Image1Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_image2(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.image2Section2.path
    if request.method == 'POST':
        form = Image2Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_img = form.cleaned_data['image2Section2']
            form.save()       
            if tour.image2Section2 and tour.image2Section2 != new_img:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы
            return redirect('edit_tour', tour.pk)
    else:
        form = Image2Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_image3(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    old_image_path = tour.image3Section2.path
    if request.method == 'POST':
        form = Image3Form(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            new_img = form.cleaned_data['image3Section2']
            form.save()       
            if tour.image3Section2 and tour.image3Section2 != new_img:  # Проверяем, есть ли старое изображение и оно не совпадает с новым
                if os.path.basename(old_image_path) != 'default_image.jpg':
                    os.remove(old_image_path)  # Удаляем старое изображение из файловой системы    
            return redirect('edit_tour', tour.pk)
    else:
        form = Image3Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_first_title(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = Titlte1Form(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = Titlte1Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_second_title(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = Titlte2Form(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = Titlte2Form(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_date_start(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = DateStartForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = DateStartForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_date_end(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = DateEndForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = DateEndForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_tagline(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = TaglineForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = TaglineForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_description(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = DescriptionForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = DescriptionForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_price_adult(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = PriceAdultForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = PriceAdultForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})

def change_price_child(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = PriceChildForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()            
            return redirect('edit_tour', tour.pk)
    else:
        form = PriceChildForm(instance=tour)
    return render(request, 'tour/change_obj.html', {'form': form, 'tour': tour})


## Манипулируем объектами

def activate_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if tour.isActive:
        tour.isActive = False
    else:
        tour.isActive = True
    tour.save()
    return redirect('administrator')

def relocate_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if tour.isOutside:
        tour.isOutside = False
    else:
        tour.isOutside = True
    tour.save()
    return redirect('edit_tour', tour.pk)

def short_long_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if tour.isOneDay:
        tour.isOneDay = False
    else:
        tour.isOneDay = True
    tour.save()
    return redirect('edit_tour', tour.pk)
    

## Удаляем объекты

def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    for i in tour.days.all():
        delete_day(request, i.pk)
    delete_tour_galery(request, tour_id)
    backgroundSection1_path = tour.backgroundSection1.path
    backgroundAdditionalServices_path = tour.backgroundAdditionalServices.path
    backgroundSectionBooking_path = tour.backgroundSectionBooking.path
    image1Section2_path = tour.image1Section2.path
    image2Section2_path = tour.image2Section2.path
    image3Section2_path = tour.image3Section2.path
    tour.delete()
    if os.path.basename(backgroundSection1_path) != 'default_image.jpg':
        os.remove(backgroundSection1_path)
    if os.path.basename(backgroundAdditionalServices_path) != 'default_image.jpg':
        os.remove(backgroundAdditionalServices_path)
    if os.path.basename(backgroundSectionBooking_path) != 'default_image.jpg':
        os.remove(backgroundSectionBooking_path)
    if os.path.basename(image1Section2_path) != 'default_image.jpg':
        os.remove(image1Section2_path)
    if os.path.basename(image2Section2_path) != 'default_image.jpg':
        os.remove(image2Section2_path)
    if os.path.basename(image3Section2_path) != 'default_image.jpg':
        os.remove(image3Section2_path)
    return redirect('administrator')

def delete_day(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    tour = day.tour
    for i in day.images.all():
        old_image_path = i.image.path
        i.delete()
        os.remove(old_image_path)
    day.delete()
    return redirect('edit_tour', tour.pk)

def delete_inclusive(request, card_id):
    card = get_object_or_404(Inclusive, id=card_id)
    tour = card.tour
    card.delete()
    return redirect('edit_tour', tour.pk)

def delete_not_inclusive(request, card_id):
    card = get_object_or_404(NotInclusive, id=card_id)
    tour = card.tour
    card.delete()
    return redirect('edit_tour', tour.pk)

def delete_why_we(request, card_id):
    card = get_object_or_404(WhyWe, id=card_id)
    card.delete()
    return redirect('administrator')

def delete_image(request, image_id):
    image = get_object_or_404(ImageForDay, id=image_id)
    old_image_path = image.image.path
    day = image.day
    image.delete()
    os.remove(old_image_path)
    return redirect('change_day', day.pk)

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()           
    return redirect('all_reviews')

def delete_tour_galery(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    for i in tour.images.all():
        old_image_path = i.image.path
        i.delete()
        os.remove(old_image_path)
    return redirect('galery')