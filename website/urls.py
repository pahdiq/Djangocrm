
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('viewer/', views.viewer, name='viewer'),
    path('aboutUs/' , views.aboutUs, name='aboutUs'),
    path('contactUs/' , views.contactUs, name='contactUs'),
    path('adder/', views.addProduct, name='adder'),
    path('pages/rugs', views.rugs_view, name='rugs.html'),
    path('pages/misc', views.misc_view, name='misc.html'),
    path('pages/wallcoverings', views.wall_covering_view, name='wallcoverings.html'),
    path('pages/mirror', views.mirror_view, name='mirror.html'),
    path('pages/fireplace', views.fireplace_view, name='fireplace.html'),
    path('pages/paint/', views.paint_view, name='paint.html'),
    path('pages/moulding/', views.moulding_view, name='moulding.html'),
    path('pages/doors', views.doors_view, name='doors.html'),
    path('pages/plumbing', views.plumbing_view, name='plumbing.html'),
    path('pages/floral', views.floral_view, name='floral.html'),
    path('pages/seasonal', views.seasonal_view, name='seasonal.html'),
    path('pages/decor', views.decor_view, name='decor.html'),
    path('pages/textiles', views.textiles_view, name='textiles.html'),
    path('pages/fine-art', views.fine_art_view, name='fine-art.html'),
    path('pages/flooring', views.flooring_view, name='flooring.html'),
    path('pages/tile', views.tile_view, name='tile.html'),
    path('pages/hardware', views.hardware_view, name='hardware.html'),
    path('pages/lighting', views.lighting_view, name='lighting.html'),
    path('pages/sofa', views.sofa_view, name='sofa.html'),
    path('pages/bed', views.bed_view, name='bed.html'),
    path('pages/table', views.table_view, name='table.html'),
    path('pages/painting', views.painting_view, name='painting.html'),
    path('pages/bench', views.bench_view, name='bench.html'),
    path('pages/chair', views.chair_view, name='chair.html'),

    path('category/<str:category_name>/', views.category_products_view, name='category_products'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 