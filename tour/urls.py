from django.urls import path
from .views import *

urlpatterns = [
    ## Титульные страницы
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    
    path('', index, name='home'),
    path('administrator', administrator, name='administrator'),
    path('all_reviews', all_reviews, name='all_reviews'),
    path('galery', galery, name='galery'),
    path('documents', documents, name='documents'),
    path('how_to_apply', how_to_apply, name='how_to_apply'),
    
    ## Страницы с турами
    path('tour/<int:tour_id>/', tour, name='tour'),
    path('tour_galery/<int:tour_id>/', tour_galery, name='tour_galery'),
    path('thank_you/<int:tour_id>/', thank_you, name='thank_you'),
    path('edit_tour/<int:tour_id>/', edit_tour, name='edit_tour'),
    
    ## Создаем новые объекты автоматически
    path('create_tour', create_tour, name='create_tour'),
    path('create_holiday', create_holiday, name='create_holiday'),
    
    ## Создаем новые объекты вручную
    path('new_tour', new_tour, name='new_tour'),
    path('new_day/<int:tour_id>/', new_day, name='new_day'),
    path('new_image_forday/<int:day_id>/', new_image_forday, name='new_image_forday'),
    path('new_icon/<int:tour_id>/', new_icon, name='new_icon'),
    path('new_inclusive/<int:tour_id>/', new_inclusive, name='new_inclusive'),
    path('new_not_inclusive/<int:tour_id>/', new_not_inclusive, name='new_not_inclusive'),
    path('new_why_we', new_why_we, name='new_why_we'),
    path('new_review_title', new_review_title, name='new_review_title'),
    path('new_review/<int:tour_id>/', new_review, name='new_review'),
    path('upload_galery_images/<int:tour_id>/', upload_galery_images, name='upload_galery_images'),
    
    ## Редактируем объекты комплексно
    path('change_tour/<int:tour_id>/', change_tour, name='change_tour'),
    path('change_day/<int:day_id>/', change_day, name='change_day'),
    path('change_inclusive/<int:card_id>/', change_inclusive, name='change_inclusive'),
    path('change_not_inclusive/<int:card_id>/', change_not_inclusive, name='change_not_inclusive'),
    path('change_why_we/<int:card_id>/', change_why_we, name='change_why_we'),
    path('change_image_forday/<int:image_id>/', change_image_forday, name='change_image_forday'),
    
    ## Редактируем отдельные элементы тура
    path('change_first_title/<int:tour_id>/', change_first_title, name='change_first_title'),
    path('change_second_title/<int:tour_id>/', change_second_title, name='change_second_title'),
    path('change_date_start/<int:tour_id>/', change_date_start, name='change_date_start'),
    path('change_date_end/<int:tour_id>/', change_date_end, name='change_date_end'),
    path('change_tagline/<int:tour_id>/', change_tagline, name='change_tagline'),
    path('change_description/<int:tour_id>/', change_description, name='change_description'),
    path('change_price_adult/<int:tour_id>/', change_price_adult, name='change_price_adult'),
    path('change_price_child/<int:tour_id>/', change_price_child, name='change_price_child'),
    path('change_background1/<int:tour_id>/', change_background1, name='change_background1'),
    path('change_background2/<int:tour_id>/', change_background2, name='change_background2'),
    path('change_background3/<int:tour_id>/', change_background3, name='change_background3'),
    path('change_image1/<int:tour_id>/', change_image1, name='change_image1'),
    path('change_image2/<int:tour_id>/', change_image2, name='change_image2'),
    path('change_image3/<int:tour_id>/', change_image3, name='change_image3'),
    
    ## Манипулируем объектами
    path('activate_tour/<int:tour_id>/', activate_tour, name='activate_tour'),
    path('relocate_tour/<int:tour_id>/', relocate_tour, name='relocate_tour'),
    path('short_long_tour/<int:tour_id>/', short_long_tour, name='short_long_tour'),
    
    ## Удаляем объекты
    path('delete_tour/<int:tour_id>/', delete_tour, name='delete_tour'),
    path('delete_day/<int:day_id>/', delete_day, name='delete_day'),
    path('delete_inclusive/<int:card_id>/', delete_inclusive, name='delete_inclusive'),
    path('delete_not_inclusive/<int:card_id>/', delete_not_inclusive, name='delete_not_inclusive'),
    path('delete_why_we/<int:card_id>/', delete_why_we, name='delete_why_we'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('delete_tour_galery/<int:tour_id>/', delete_tour_galery, name='delete_tour_galery'),
]