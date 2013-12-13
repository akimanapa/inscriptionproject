
from django.shortcuts import redirect, get_object_or_404, \
    render_to_response
from inscrire.models import Faculte,Etudiant,Departement,Niveau



def view_faculte(request):
	
	fac_number=Faculte.objects.count()
	fac=Faculte.objects.all()
	template='inscrire/faculte.html'
	
	return render_to_response(template,{
	                          'fac':fac,
	                          'fac_number':fac_number,})
	

#def view_departement(request,fac_name):
	
	#depart-fac=Departement.objects.filter(faculte__faculte= fac_name)
	#template='inscription/faculte.html'
	
	#return render_to_response(template,{
	                          #'depart-fac':depart-fac,})	
