from django.contrib import admin
from inscrire.models import Faculte,Etudiant,Departement,Niveau,Avancement



class FaculteAdmin(admin.ModelAdmin):
	fields=['faculte']
admin.site.register(Faculte, FaculteAdmin)	

admin.site.register(Departement)

admin.site.register(Niveau)

	
class EtudiantAdmin(admin.ModelAdmin):
	fieldsets=[
             (None,               {'fields':['nom']}),
	     (None,               {'fields':['prenom']}),
             ('Date de Naissance',{'fields':['date_naissance'],'classes':['collapse']}),]
        list_filter = ['date_naissance']

admin.site.register(Etudiant,EtudiantAdmin)
admin.site.register(Avancement)

