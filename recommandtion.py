import os
# from flask import Flask, render_template, request,jsonify
import json
from typing import Collection

import pyttsx3
import speech_recognition as sr
import time
import datetime



model = 1

def assistant(text): 
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate') # getting details of current speaking rate
    engine.setProperty('rate', 150) # setting up new voice rate

    #"""VOLUME"""
    volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0) # setting up volume level between 0 and 1

    #"""VOICE"""
    voices = engine.getProperty('voices') #getting details of current voice
    engine.setProperty('voice', voices[26].id) #changing index, changes voices. o for male
    #engine.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()



def userRec():
    
    r = sr.Recognizer()
    
    
    with sr.Microphone() as source:
        print("PARLER")
        r.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        audio = r.listen(source)

    try: # reconnaissance de la voix
        print("Reconnaissance du texte...")
        text = r.recognize_google(audio, language="fr-FR")
        print(text)


        print("--------------Traduction----------------")
        vocal = r.recognize_google(audio,language = 'fr-FR') 
        print(vocal) 
        if "non" in vocal :
            return "non"
        elif "oui" in vocal:
            return "oui" 
        elif vocal=="None": 
            assistant('Répondez par OUI ou NON') 
            time.sleep(1)
            userRec()
            reponse=userRec()
            return reponse
        else:
            assistant('Répondez par OUI ou NON') 
            time.sleep(1)
            userRec()
            reponse=userRec()
            return reponse

    except Exception as ex:
        print(ex)
    



def wishme():
    # Salutations
    
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        assistant("Bonjour Monsieur et Bienvenue")
    elif hour>=12 and hour<18:
        assistant("Bon après-midi Monsieur et Bienvenue ")
    else:
        assistant("Bonsoir Monsieur,Bienvenue")

    assistant(" Docteur paludisme à votre service")

#les questions et recommandations 
q0="Avez vous déja eu plusieurs fois le paludisme ? ( plus de 5 fois)"
q1=["Est-ce que votre corps chauffe ?","Depuis quand votre corps chauffe ainsi ? ", "Aujourd’hui? ","Souffrez vous de maux de tête?", "A quelle moment de la journée commence t-il à chauffer?","Le matin?","Le soir?","L'après-midi?","Vous sentez vous faible?","Avez vous des courbatures?","Souffrez vous de troubles digestifs(nausées,vomissements ou diarrhées)?","Avez vous du mal à manger?"]
q2=["A quel moment de la journée votre vous commencez a chauffer ? ","Le matin"]
q3=["Depuis hier ?","A quel moment moment de la journée commence t-il à chauffer?","Le matin?","L'après-midi?","Le soir?","Avez vous du mal à manger?","Souffrez vous de troubles digestifs(nausées,vomissements ou diarrhées)?"]
q4=["Vous êtes vous vacciné contre la fièvre typhoide au cours des 3 dernières années?","Consommez vous de l'eau potable(robinet,minérale,filtrée ou chauffée avant consommation)?"]
q5=["Vous sentez vous faible?","Souffrez vous de troubles digestifs(nausées,vomissements ou diarrhées)?","Avez vous du mal à manger(perte d'appétit)?"]
q6=["Vous êtes vous vacciné contre la fièvre typhoide au cours des 3 dernières années?","Consommez vous de l'eau potable(robinet,minérale,filtrée ou chauffée avant consommation)?"]

Recommandation=["Nous relevons certains symptômes au niveau de vos yeux. Veuillez consulter un médécin au plus vite.",
                "Vos données ne nous permettent pas d'établir des analyses pertinentes sur votre état. Veuillez consulter un médécin.",
                "Vous semblez avoir certains symptômes du paludisme. Veuillez consulter un médécin pour vérification.",
                "Vous présentez les symptômes du paludisme. Veuillez consulter un médécin au plus vite.",
                "Vous semblez avoir les symtômes du paludisme, cependant vos vaccin n'étant à jour veuillez consulter un médecin",
                "Nous relevons certains symptômes du paludisme. Veuillez consulter un médécin au plus vite.",
                "Nous relevons certains symptômes du paludisme.Cependant vos vaccins n'étant pas à jour, Veuillez consulter un médécin au plus vite pour vérification.",
                "Vous semblez avoir certains symptômes du paludisme.Cependant vos vaccins n'étant pas à jour, Veuillez consulter un médécin au plus vite pour vérification.",
                "Vos données ne nous permettent pas de nous prononcer sur votre état. Veuillez refaire le test à l'apparition de nouveaux symptômes ou consulter directement un médécin.",
                "Nous relevons des symptômes de fatigue avec fièvre. Veuillez consulter un médécin.",
                "Vous semblez avoir de la fièvre. Veuillez consulter un médécin.",
                "Vous présentez les symptômes d'une maladie. Veuillez consulter un médécin pour vérification.",
                "Vous semblez avoir certains symptômes du paludisme. Veuillez consulter un médécin au plus vite.",
                "L'analyse faciale nous a revelé certains symptômes de maladie. Veuillez consulter un médécin au plus vite.",
                "Vous ne présentez aucun symptôme. Continuez à entretenir votre hygiène de vie et essayer de dormir au moins 8 heures par jour.",
                "Vous présentez les symptômes d'une anémie ou de l'ictère. Veuillez consulter un médécin pour vérification.",
                "Vous semblez être fatigué. Reposez vous! Cependant à l'apparition de nouveaux symptômes ou si vôtre état ne s'arrange pas, veuillez consulter un médécin.",
                "Vous semblez être fatigué. Veuillez consulter un medecin pour une prise charge",
                "vous présentez certains symptômes du paludisme. Veuillez consulter un médécin au plus vite"
                "Vous semblez avoir entrer des résultats érronés. Merci de recommencer l'analyse."]

# predictionRecommandation=["Vous semblez ne présenter aucun symptôme. Toute fois, veuillez consulter un médecin.",
#                 "Vous semblez être fatigué. Cependant, l'analyse faciale a révélée des symptômes de maladie. Veuillez consulter un médecin",
#                 "Vous semblez être fatigué. Reposez vous cependant à l'apparition de nouveaux symptômes ou si votre état ne s'arrange pas veuillez consulter un médecin.",
#                 "Vous semblez avoir les symtômes du paludisme, veuillez consulter un médecin",
#                 "Vous semblez avoir les symtômes du paludlsme, cependant vos vaccin n'étant pas à jour veuillez consulter un médecin"]

def maux_tete():

        assistant(q1[3])
        reponse=input(q1[3])

        if reponse=="oui": #courbature 
            assistant(q1[9])
            reponse=input(q1[9])
            
            if reponse=="oui": 
                assistant(q1[11]) #du mal a manger à mettre dans une fonction
                reponse=input(q1[11])

                if reponse=="oui":
                    if model==2:

                        rec=Recommandation[3]
                        assistant(Recommandation[3])
                        print(Recommandation[3])

                    else:
                        rec=Recommandation[2]
                        assistant(Recommandation[2])
                        print(Recommandation[2])
                elif reponse =="non":
                    if model==1:

                        rec=Recommandation[3]
                        assistant(Recommandation[3])
                        print(Recommandation[3])

                    else:
                        rec=Recommandation[2]
                        assistant(Recommandation[2])
                        print(Recommandation[2])

            elif reponse=="non":
                assistant(q1[10]) # trouble 
                reponse=input(q1[10])

                if reponse=="oui":
                    assistant(q1[11]) #du mal a manger 
                    reponse=input(q1[11])

                    if reponse=="oui":
                        if model==0:

                            rec=Recommandation[3]
                            assistant(Recommandation[3])
                            print(Recommandation[3])

                        else:
                            rec=Recommandation[2]
                            assistant(Recommandation[2])
                            print(Recommandation[2])
                    elif reponse =="non":
                        if model==1:

                            rec=Recommandation[3]
                            assistant(Recommandation[3])
                            print(Recommandation[3])

                        else:
                            rec=Recommandation[2]
                            assistant(Recommandation[2])
                            print(Recommandation[2])

        elif reponse =="non":# pas de maux de tetes
            assistant(q1[11]) #du mal a manger 
            reponse=input(q1[11])

            if reponse=="oui":
                assistant(q1[10]) # trouble 
                reponse=input(q1[10])

                if reponse=="oui":
                    if model==2:
                        
                        rec=Recommandation[3]
                        assistant(Recommandation[3])
                        print(Recommandation[3])

                    else:

                        rec=Recommandation[2]
                        assistant(Recommandation[2])
                        print(Recommandation[2])
                
                else:
                    if model==0:

                        rec=Recommandation[5]
                        assistant(Recommandation[5])
                        print(Recommandation[5])

                    else:
                        rec=Recommandation[2]
                        assistant(Recommandation[2])
                        print(Recommandation[2])

def couplage1():
    assistant(q1[10]) # trouble 
    reponse = input(q1[10] )
    
    if reponse=="oui":
        couplage2()

    elif reponse=="non":
        assistant(q1[9]) # courbature
        reponse = input(q1[9] )
        if reponse=="oui":
            couplage2()
        elif reponse=="non":
            assistant(q1[11]) # du mal a manger
            reponse = input(q1[11] )
            if reponse=="oui":
                couplage2()
            else:
                if model==1:

                    rec=Recommandation[5]
                    assistant(Recommandation[5])
                    print(Recommandation[5])

                else:
                    rec=Recommandation[8]
                    assistant(Recommandation[8])
                    print(Recommandation[8])


def couplage2():
    assistant(q4[0]) # vaccin
    reponse = input(q4[0] )
    if reponse=="oui":
        if model==1:

            rec=Recommandation[18]
            assistant(Recommandation[18])
            print(Recommandation[18])

        else:
            rec=Recommandation[2]
            assistant(Recommandation[2])
            print(Recommandation[2])

    elif reponse=="non":
        assistant(q1[10]) # trouble 
        reponse = input(q1[10] )
        if reponse=="oui":
            if model==1:

                rec=Recommandation[18]
                assistant(Recommandation[18])
                print(Recommandation[18])

            else:
                rec=Recommandation[2]
                assistant(Recommandation[2])
                print(Recommandation[2])

        else:
            if model==1:

                rec=Recommandation[6]
                assistant(Recommandation[6])
                print(Recommandation[6])

            else:
                rec=Recommandation[7]
                assistant(Recommandation[7])
                print(Recommandation[7])

def couplageRith1():
    assistant(q1[9]) # coubatures 
    reponse = input(q1[9] )
    
    if reponse=="oui":
        couplageRith2()
    elif reponse=="non":
        assistant(q1[10])
        reponse=input(q1[10]) # trouble 
        if reponse=="oui":
            couplageRith2()
        elif reponse=="non":
            assistant(q1[11]) #du mal a manger 
            reponse=input(q1[11])

            if reponse=="oui":
                if model==1:

                    rec=Recommandation[5]
                    assistant(Recommandation[5])
                    print(Recommandation[5])

                else:
                    rec=Recommandation[2]
                    assistant(Recommandation[2])
                    print(Recommandation[2])
            
            else:

                if model==1:

                    rec=Recommandation[15]
                    assistant(Recommandation[15])
                    print(Recommandation[15])

                else:
                    rec=Recommandation[16]
                    assistant(Recommandation[16])
                    print(Recommandation[16])


def couplageRith2():

    assistant(q1[11]) #du mal a manger 
    reponse=input(q1[11])

    if reponse=="oui":
        assistant(q6[0]) #vacciné? 
        reponse=input(q6[0])
        if reponse=="oui":

            if model==1:
                rec=Recommandation[18]
                assistant(Recommandation[18])
                print(Recommandation[18])

            else:
                rec=Recommandation[2]
                assistant(Recommandation[2])
                print(Recommandation[2])

        elif reponse=="non":
            assistant(q6[1]) #eaux potable?
            reponse=input(q6[1])

            if reponse=="oui":
                
                if model==1:
                    rec=Recommandation[18]
                    assistant(Recommandation[18])
                    print(Recommandation[18])

                else:
                    rec=Recommandation[2]
                    assistant(Recommandation[2])
                    print(Recommandation[2])
            
            else:

                if model==1:

                    rec=Recommandation[11]
                    assistant(Recommandation[11])
                    print(Recommandation[11])

                else:
                    rec=Recommandation[7]
                    assistant(Recommandation[7])
                    print(Recommandation[7])
    else:
        if model==1:

            rec=Recommandation[12]
            assistant(Recommandation[12])
            print(Recommandation[12])

        else:
            rec=Recommandation[8]
            assistant(Recommandation[8])
            print(Recommandation[8])

        



        




wishme()
time.sleep(2) # une pose de 3 seconde avant de poursuivre 
# print(q1[0])
assistant("OUI ou NON a toutes les questions")
# print("Répondez par OUI ou NON a toute les questions")
question=q1[0]
# return render_template("index.html", question=question)
assistant(q0)
#reponsev = userRec()
#if reponsev =="":
reponse = input(q0)

# reponsev = userRec()
if reponse=="non":
    assistant(q1[0])
    #reponsev = userRec()
    #if reponsev =="":
    reponse = input(q1[0])
        
    if reponse=="oui": # depuis quand vous chauffez ainsi 
        print(q1[1])
        question=q1[1]
        assistant(q1[1])
        assistant(q1[2])
        #reponsev = userRec()
        #if reponsev =="":
        reponse = input(q1[2])
        
        #reponsev = userRec() 

        if reponse =="oui": # aujourd'hui
            question=q2[0]
            assistant(q2[0])
            # print(q2[0])
            
            question=q2[1]
            assistant(q2[1]) # le matin
            #reponsev = userRec()
            #if reponsev =="":
            reponse = input(q2[1])# le moment de la journée # matin 
            if reponse=="oui":
                question=q1[8] # sentir faible
                assistant(q1[8])
                reponse=input(question)
                if reponse== "oui":

                    maux_tete()


                elif reponse=="non":
                    if model==0:

                        rec=Recommandation[5]
                        assistant(Recommandation[5])
                        print(Recommandation[5])

                    else:
                        rec=Recommandation[2]
                        assistant(Recommandation[2])
                        print(Recommandation[2])


            elif reponse=="non": 

                assistant(q3[4])# le soir
                reponse=input(q3[4])

                        
                if reponse=="oui": 
                    maux_tete()
                        
                elif reponse=="non":# Après midi
                    assistant(q3[3])
                    reponse=input(q3[3])  
                
                    if reponse=="oui": 
                        maux_tete()

                    else:
                        rec=Recommandation[len(Recommandation)-1]
                        assistant(Recommandation[len(Recommandation)-1])
                        print(Recommandation[len(Recommandation)-1])


        elif reponse=="non":
            assistant(q3[0])
            reponse = input(q3[0]) # depuis hier?

            if reponse=="oui":
                question=q2[0]
                assistant(q2[0])
                # print(q2[0])
                
                question=q2[1]
                assistant(q2[1]) # le matin
                #reponsev = userRec()
                #if reponsev =="":
                reponse = input(q2[1])# le moment de la journée # matin 
                if reponse=="oui":
                    question=q1[8] # sentir faible
                    assistant(q1[8])
                    reponse=input(question)
                    if reponse== "oui":

                        maux_tete()


                    elif reponse=="non":
                        if model==2:

                            rec=Recommandation[5]
                            assistant(Recommandation[5])
                            print(Recommandation[5])

                        else:
                            rec=Recommandation[2]
                            assistant(Recommandation[2])
                            print(Recommandation[2])


                elif reponse=="non": 

                    assistant(q3[4])# le soir
                    reponse=input(q3[4])

                                
                    if reponse=="oui": 
                        maux_tete()
                            
                    elif reponse=="non":# Après midi
                        assistant(q3[3])
                        reponse=input(q3[3])  
                    
                        if reponse=="oui": 
                            maux_tete()

                        else:
                            rec=Recommandation[len(Recommandation)-1]
                            assistant(Recommandation[len(Recommandation)-1])
                            print(Recommandation[len(Recommandation)-1])

    elif reponse=="non":
        question=q1[8] # sentir faible
        assistant(q1[8])
        reponse=input(question)
        if reponse=="oui":
            if model==2:

                rec=Recommandation[1]
                assistant(Recommandation[1])
                print(Recommandation[5])

            else:
                rec=Recommandation[2]
                assistant(Recommandation[2])
                print(Recommandation[2])

        elif reponse =="non":
            assistant(q1[3])
            reponse=input(q1[3])

            if reponse=="oui":
                if model==2:

                    rec=Recommandation[5]
                    assistant(Recommandation[5])
                    print(Recommandation[5])

                else:
                    rec=Recommandation[len(Recommandation)-2]
                    assistant(Recommandation[len(Recommandation)-2])
                    print(Recommandation[len(Recommandation)-2])
        
            else:
                if model==2:

                    rec=Recommandation[13]
                    assistant(Recommandation[13])
                    print(Recommandation[13])

                else:
                    rec=Recommandation[14]
                    assistant(Recommandation[14])
                    print(Recommandation[14])

else: 
    assistant(q1[0])
    reponse = input(q1[0] )
    if reponse=="oui":
        assistant(q1[3])
        reponse = input(q1[3] )# maux de tete
        if reponse=="oui":
            couplage1()
        elif reponse=="non":
            assistant(q1[8])
            reponse = input(q1[8])# sentir faible 

            if reponse=="oui":
                couplage1()

            else:
                if model==1:

                    rec=Recommandation[9]
                    assistant(Recommandation[9])
                    print(Recommandation[9])

                else:
                    rec=Recommandation[10]
                    assistant(Recommandation[10])
                    print(Recommandation[10])

    else:
        assistant(q1[8])
        reponse = input(q1[8])# sentir faible 

        if reponse=="oui":
             couplageRith1()
            
        elif reponse=="non":
            assistant(q1[3])
            reponse = input(q1[3] )# maux de tete
            if reponse=="oui":
                couplageRith1()
            else:
                if model==1:

                    rec=Recommandation[13]
                    assistant(Recommandation[13])
                    print(Recommandation[13])

                else:
                    rec=Recommandation[14]
                    assistant(Recommandation[14])
                    print(Recommandation[14])

               
        




        ###################### FIN ####################
            


            

        




        





