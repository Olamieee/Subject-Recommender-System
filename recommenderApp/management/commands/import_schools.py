from django.core.management.base import BaseCommand
from recommenderApp.models import School

class Command(BaseCommand):
    help = "Import school names from a list"

    def handle(self, *args, **kwargs):
        school_names = [
        "GSNDG JANJA Secondary School",
        "Glory Secondary School",
        "World Mission Secondary School",
        "Kagarama Secondary School",
        "GS Rubona Secondary School",
        "GS NYAKAYAGA Secondary School",
        "APEM NGARAMA Secondary School",
        "Hamdan Bun Rashid Girls Scientific Secondary School",
        "Coko Secondary School",
        "MONTFORT SECONDARY SCHOOL",
        "Cog St Patrick Secondary School",
        "GS Muhura Taba Secondary School",
        "G.S Gakoni Catholic Secondary School",
        "Kiyanza Secondary School",
        "CMUR Secondary School",
        "APAPEDUC BUNGWE Secondary School",
        "Gitisi Secondary School",
        "Bisika Secondary School",
        "Dihiro Primary and Secondary School",
        "COBANGA Secondary School",
        "NYAMYUMBA SECONDARY SCHOOL",
        "Nemba Secondary School",
        "Karama Secondary School",
        "ESIR Secondary School",
        "Juru Secondary School",
        "Nyagasozi Primary And Secondary School",
        "GS ST TITE BUTERERI Secondary School",
        "Authentic International Academy",
        "Ecole Technique SOS Hermann Gmeiner",
        "Ecole Notre Dame dela Providence de Karubanda",
        "Ecole lumiere de kibuye",
        "Gs.Gitarama",
        "GS Tero",
        "G.S de Byimana",
        "Kigali International Community School (KICS)",
        "The International School of Kigali (ISK)",
        "Riviera High School",
        "King David Academy",
        "Green Hills Academy",
        "Ecole Belge de Kigali",
        "Nu-Vision High School",
        "Lycee Notre-Dame de Ciseaux",
        "Ecole des Sciences de Musanze",
        "FAWE Girls School",
        "Groupe Scolaire Marie Reine Rwaza",
        "Samuduha Integrated College (SICO)",
        "Groupe Scolaire APAPEB",
        "Groupe Scolaire St. Andre",
        "Lycee de Kigali"
        ]

        School.objects.bulk_create([School(name=name) for name in school_names])

        self.stdout.write(self.style.SUCCESS("Schools added successfully!"))