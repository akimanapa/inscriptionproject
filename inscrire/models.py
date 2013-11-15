from django.db import models

# Create your models here.

class Faculte(models.Model):
    faculte= models.CharField(max_length=100)
    def __unicode__(self):
        return self.faculte
        

class Departement(models.Model):
    name=models.CharField(max_length=100)
    faculte=models.ForeignKey(Faculte)
    
    def __unicode__(self):
        return self.name      

class Niveau(models.Model):
    PREMIERE_ANNEE = '1ERE'
    DEUXIEME_ANNEE = '2eme'
    TROISIEME_ANNEE = '3eme'
    QUATRIEME_ANNEE = '4eme'
    choix_annee_etude=(
	     (PREMIERE_ANNEE,'1ere candidature'),
	     (DEUXIEME_ANNEE , '2eme candidature'),
	     (TROISIEME_ANNEE, '1ere licence'),
	     (QUATRIEME_ANNEE, '2eme licence'),
	
	 )
    designation=models.CharField(max_length=4,
                                 choices=choix_annee_etude,)
                        
    departement= models.ManyToManyField(Departement)
    def __unicode__(self):
        return self.designation
       
class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    date_naissance=models.DateTimeField('date naissance')
    designation=models.ManyToManyField( Niveau)
    def __unicode__(self):
        return self.nom
        return self.prenom
        return self.date_naissance
        
class Avancement(models.Model):
    etudiant= models.ForeignKey(Etudiant)
    niveau = models.ForeignKey(Niveau) 
    annee_academique= models.DateTimeField('Annee academique' )
       
