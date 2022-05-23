from django.contrib import admin
from DB.models import Participants, Finalers

admin.site.register(Finalers)


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('teamname', 'collegename', 'starttime1',
                    'level1', 'level2', 'level3', 'totaltime1')


class FinalersAdmin(admin.ModelAdmin):
    list_display = ('teamname', 'collegename', 'starttime2',
                    'level4', 'level5', 'totaltime2')


admin.site.register(Participants, ParticipantsAdmin)
