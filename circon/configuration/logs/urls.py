from django.conf.urls import url
from .views import ListLogs
from .views import LogsProducts
from .views import LogsEntry
from .views import LogsEntryDetail
from .views import LogsExit
from .views import LogsExitDetail
from .views import LogsUnitsMeasures
from .views import LogsRequest
from .views import LogsCategory


urlpatterns = [
               url(r'^ListLogs$', ListLogs.as_view(),
                   name='list_logs'),
               url(r'^LogsProducts$', LogsProducts.as_view(),
                   name='logs_products'),
               url(r'^LogsEntry$', LogsEntry.as_view(),
                   name='logs_entry'),
               url(r'^LogsEntryDetail$', LogsEntryDetail.as_view(),
                   name='logs_entrydetail'),
               url(r'^LogsExit', LogsExit.as_view(),
                   name='logs_exit'),
               url(r'^LogsExitDetail', LogsExitDetail.as_view(),
                   name='logs_exitdetail'),
               url(r'^LogsUnitsMeasures$', LogsUnitsMeasures.as_view(),
                   name='logs_unitsmeasures'),
               url(r'^LogsRequest$', LogsRequest.as_view(),
                   name='logs_request'),
               url(r'^LogsCategory$', LogsCategory.as_view(),
                   name='logs_category'),
               ]
