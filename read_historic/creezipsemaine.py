#!/usr/bin/env python
# -*- coding: utf-8 -*-

# readsemcsv
# utilisatires pour lire une semain dans les csv de mois

# le fichier zip doit s'appeler BIDAAABBBmmyy

# la fonction presentzip(paire,mois,year) dit si le zip est dispo
# la fonction creenomzip(paire mois year) renvoie la liste des zip correspondant a la semaine

#07sep18 : on dedouble le main en mainsimple (celui d'avant) et main2 qui commence a essayer de rassembler les temps en minutes


import zipfile
import datesemaineutils as datesm
import read_selenium
import ReadWebWindows
import datetime
# renvoie la liste des csv a utiliser pour pouvoir charger cette semaine
# accompagnée de la date (jour, mois annee du premier jour alire dans ce fichier
#le nom du csv est yyymmpaire et du nombre de jours a lire dans chaque fichier
def creenomcsv(paire, semaine, annee):
    listemois = datesm.getlistemois(semaine, annee)
    listezips = []
    for mois in listemois:
        zipname = "%04d%02d%s.csv" % (mois[3],mois[2],paire)
        jourdumois = mois[1]
        nbjours = mois[0]
        listezips.append([nbjours,jourdumois,mois[2],mois[3],zipname])
    print(listezips)
    return listezips

# import zipfile

# rep ou sont les donnees
datarep = "c:\\tmp"


################## readlines ####################
# : lecture de qq jous dans un fichier mois
# lit nbjours dans un fichier csv contenant le mois pour une paire
# a partir du jour du mois =  jour
# ligne par ligne
# renvoie le nb de minutes entre la ligne et datedeb
# yield la date et la valeur
# renvoie le nb de jours lus quand le balayage est fini (None, nbjourslus)
# charge dans le tableau le nombre de jourd nbjours a partir du jour jour
def readlinescsv(debsem,nbjours, jour, nomcsv, paire):
    # on lit le zip sur le disque
    nbjourslus = 0
    lstday = -1
    delta = 6-nbjours #delta en jours depuis le debut de la semain, pour calcul de la coordonnee de la valeur en jour par rapport au dimanche
    
    with open("c:\\tmp\\"+nomcsv, mode='r') as read1:
        for laligne in read1:
            numsample, date, begin = datesm.decodelinemois(laligne)  # lecture de la ligne
            if lstday != date.day:  # la date a changé
                if nbjourslus != 0:  # on a commence a lire des jours
                    nbjourslus = nbjourslus + 1  # un nouveau jour
                else:
                    print("\rjour", date.day, )  # on n'a pas commence a lire des jours : on saute

            lstday = date.day
            
            if date.day == jour:  # on a atteint le jour recherche
                nbjourslus = 1  # on commence

            if nbjourslus > nbjours:  # on a lu le bon nombre de jours
                break  # fin du for
            deltatime = date-debsem
            deltaminutes = int(deltatime.total_seconds()/60)
            if nbjourslus != 0:
               # delta = date - datedeb  # delta depuis debut semaine
                #yield nbjourslus, date, int(delta*24*60), begin  # date, valeur debut heure en minutes
               yield nbjourslus, date, deltaminutes, begin  # date, valeur debut heure en minutes


import os.path

#genere un tableau contenant toutes les donnees pour cette paire et cette semaine
def generesemaine(paire,semaine, annee):
    ok=False
    listezip = creenomzip(paire, semaine, annee) #liste jour du mois, mois, annee, nomzip
    #regarde si les zip existent
    for nomfich in listezip:
        nomfich = datarep+"\\"+nomfich[3]
        print(nomfich)
        if os.path.isfile(nomfich):
            ok = True
        else:
            readwebfile(paire,nomfich[1],nomfich[2])






######
#pour test
#on init le webdriver
#on genere la liste des csv a lire pour cette smeaine avec creenomcsv
#pour tous les noms : on va chercher dans le site le fichier en question ou on l'a deja (loadpairemoisan)
#on lit toutes les lignes a lire (a partir du jour qui est necessaire) avec readlinecsv qui contient un iterateur :
# on le cree et ensuite on le lit en loop


#petit main de test
def mainsimple() :   
    driver = ReadWebWindows.initwebwindows()
  
    
    paire = "EURUSD"
    semaine=9
    annee = 2018
    semainestr = "{0:02}".format(semaine)
    anneestr = "{0:04}".format(annee)
    print(semainestr, anneestr)
    toread = creenomcsv(paire, semainestr, anneestr)
    #on calcule l'heure du dimanche soir avant cette semain (t0 des heures)
    debyear,debmonth,debday = datesm.getdimanchefromweek(semaine,annee)
    dimanche17h = datetime.datetime(debyear,debmonth,debday,17,0,0)
    prvmin=-1
    
    for filesourc in toread:
        print(filesourc)
        read_selenium.loadpairemoisan(driver,paire,"{0:02}".format(filesourc[2]),"{0:04}".format(filesourc[3])) #download le fichier dans tmp
        jourdeb = filesourc[1] #j1er jour du mois a lire
        nbjours = filesourc[0]
        #lecture a partir de datedeb nbjours, nom du csv
        laloop = readlinescsv(dimanche17h,nbjours, jourdeb, filesourc[4], paire)
        for i in laloop:
            if prvmin != i[2] :  #on print quand la minute a change
                prvmin = i[2]
                print (i)
            

    #generesemaine("aaabbb",1,2013)
    #laliste = creenomzip("aaabbb",1,2013)
#print (laliste)
            
#idema a mainsimple mais on cree un csv avec toutes les lignes lues
# on ne les affiche que toutes les minutes      
def main2():
    
    tableauout = []
    driver = ReadWebWindows.initwebwindows()
  
    
    paire = "EURUSD"
    semaine=17
    annee = 2018
    semainestr = "{0:02}".format(semaine)
    anneestr = "{0:04}".format(annee)
    print(semainestr, anneestr)
    toread = creenomcsv(paire, semainestr, anneestr)
    
    debyear,debmonth,debday = datesm.getdimanchefromweek(semaine,annee)
    dimanche17h = datetime.datetime(debyear,debmonth,debday,17,0,0)
    prvmin=-1
    bardeb=barmax=barmin=barlst = 0
    deltamin =0
    count=1
    countok =0
    countmiss =0
        
    for filesourc in toread:
        print(filesourc)
        read_selenium.loadpairemoisan(driver,paire,"{0:02}".format(filesourc[2]),"{0:04}".format(filesourc[3])) #download le fichier dans tmp
        jourdeb = filesourc[1] #j1er jour du mois a lire
        nbjours = filesourc[0]
        #lecture a partir de datedeb nbjours, nom du csv
        laloop = readlinescsv(dimanche17h,nbjours, jourdeb, filesourc[4], paire)
        for i in laloop:
            valeur = i[3]
            if prvmin != i[2] :
                deltamin = i[2]-prvmin-1 #detecte les intervalles de plus de 1 minute : nombre de lignes a rajouter
                timestat = i[1]  #non il faut kl'heure de kla fin de la precedente tranche de temps
                mintime = prvmin
                while deltamin !=0 : # on a saute une ou plus de minutes : on les rajoute sans changement de valeur min max in out = valeur precedente
                    timestat = timestat+datetime.timedelta(minutes=1) #une min de plus a la date
                    mintime = mintime+1  #une min de plus a l'index de cette minute
                    resu = [bardeb,bardeb,bardeb,bardeb,timestat,mintime,0] #resultats avec count a 0
                    deltamin = deltamin-1
                    print ('-------------------------------',resu)
                    countmiss = countmiss+1
                
                resu = [bardeb,barmax,barmin,barlst,i[1],i[2],count]
                if (bardeb !=0): # le premier changement de minute ne contient pas de resultat
                    print (resu)
                    countok = countok +1
                
                prvmin = i[2]
                bardeb=barmax=barmin=barlst = valeur
                count = 1
                                
            else:
                barmax = max(barmax,valeur)
                barmin = min(barmin,valeur)
                barlst = valeur
                count = count+1
            #tableauout.append(i)
            
            
    #print (tableauout)
    print("count ok ",countok)
    print("count missed ",countmiss)
    
            
if __name__=="__main__":
    main2()
    #mainsimple()
            