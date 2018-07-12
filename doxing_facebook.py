#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import signal
import webbrowser
import platform
import subprocess
cyan = "\033[1;36m"
green = "\033[1;32m"
reset = "\033[00m"

print 'Stalker pro/\n'
user_id = raw_input('Ingresa el perfil id: \n')
#user_id = "100000982635005"
def menu_general():
    time.sleep(1)
    print """
		1.\033[1;m Perfil, fotos, etc
	   	2.\033[1;m Etiquetados
	 	3.\033[1;m Comentarios
	 	4.\033[1;m Likes
		5.\033[1;m Lugares
		6.\033[1;m Gente
		7.\033[1;m Intereses
	"""
    OPTION = raw_input('Selecciona una opcion \n')
    if OPTION == '1':
        menu_profile()
    elif OPTION == '2':
        menu_etiquetados()
    elif OPTION == '3':
        menu_comentarios()
    elif OPTION == '4':
        menu_likes()
    elif OPTION == '5':
        menu_lugares()
    elif OPTION == '6':
        menu_gente()
    elif OPTION == '7':
        menu_intereses()
    else:
        print 'opcion invalida'
        menu_general()


def menu_etiquetados():
    time.sleep(1)
    print 'Etiquetados.............'
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/photos-of/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/videos-of/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/stories-tagged/intersect')
    menu_general()


def menu_comentarios():
    time.sleep(1)
    print 'Comentarios.............'
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/photos-commented/intersect')
    menu_general()


def menu_likes():
    time.sleep(1)
    print 'Likes.............'
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/photos-liked/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/videos-liked/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/stories-liked/intersect')
    menu_general()


def menu_lugares():
    time.sleep(1)
    print 'Lugares....'
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/')

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/110290705711626/places/intersect/'
                    )

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/273819889375819/places/intersect/'
                    )

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/200600219953504/places/intersect/'
                    )

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/935165616516865/places/intersect/'
                    )

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/164243073639257/places/intersect/'
                    )

    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-visited/192511100766680/places/intersect/'
                    )
    menu_general()


def menu_gente():
    time.sleep(1)
    print 'Gente.......'
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/relatives/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/friends/intersect')
    webbrowser.open('Friends of friends:', reset
                    + 'https://www.facebook.com/search/' + user_id
                    + '/friends/friends/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/employees/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/schools-attended/ever-past/intersect/students/intersect/'
                    )
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/current-cities/residents-near/present/intersect'
                    )
    menu_general()


def menu_intereses():
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/intersect')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/161431733929266/pages/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/religion/pages/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/musician/pages/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/movie/pages/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/pages-liked/book/pages/intersect/')
    webbrowser.open('https://www.facebook.com/search/' + user_id
                    + '/places-liked/\n')
    menu_general()


def menu_profile():
    time.sleep(1)
    print """
		1.\033[1;m Fotos
	   	2.\033[1;m Videos
	 	3.\033[1;m Posts
	 	4.\033[1;m Grupos
		5.\033[1;m Eventos futuros
		6.\033[1;m Eventos pasados
		7.\033[1;m Juegos
		8.\033[1;m Aplicaciones
	"""

    OPT = raw_input('Selecciona una opcion \n')
    if OPT == '1':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/photos-by/')
        menu_profile()
    elif OPT == '2':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/videos-by/')
        menu_profile()
    elif OPT == '3':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/stories-by/')
        menu_profile()
    elif OPT == '4':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/groups')
        menu_profile()
    elif OPT == '5':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/events-joined/')
        menu_profile()
    elif OPT == '6':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/events-joined/in-past/date/events/intersect/'
                        )
        menu_profile()
    elif OPT == '7':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/apps-used/game/apps/intersect')
        menu_profile()
    elif OPT == '8':
        webbrowser.open('https://www.facebook.com/search/' + user_id
                        + '/apps-used/')
        menu_profile()
    else:
        print 'opcion invalida \n'
        menu_profile()

menu_general()