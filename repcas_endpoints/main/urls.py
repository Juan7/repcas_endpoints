from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api, views

app_name = 'main'

router = DefaultRouter()
router.register('salesman', api.SalesmanViewSet, base_name='api_salesman')
router.register('clients', api.ClientViewSet, base_name='api_client')
router.register('distribution-channel', api.DistributionChannelViewSet, base_name='api_distribution_channel')
router.register('billing-document', api.BillingDocumentViewSet, base_name='api_billing_document')
router.register('laboratories', api.LaboratoryViewSet, base_name='api_laboratory')
router.register('articles', api.ArticleViewSet, base_name='api_article')
router.register('distribution-channel-price', api.DistributionChannelPriceViewSet, base_name='api_distribution_channel_price')
router.register('promotions', api.PromotionViewSet, base_name='api_promotion')
router.register('scales-price', api.ScalePriceViewSet, base_name='api_scales_price')
router.register('special-price', api.SpecialPriceViewSet, base_name='api_special_price')
router.register('special-finantial-discount', api.SpecialFinantialDiscountViewSet, base_name='api_special_finantial_discount')

apipatterns = router.urls + [

]

urlpatterns = [
    path('api/', include(apipatterns)),
]