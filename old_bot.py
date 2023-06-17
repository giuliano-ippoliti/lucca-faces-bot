import pyautogui
import time
import os
import argparse

# screen à 67%

GO_X = 955
GO_Y = 564

FACE_X = 950
FACE_Y = 492

NOM_X = FACE_X-100
NOM1_Y = FACE_Y+160
NOM2_Y = FACE_Y+240
NOM3_Y = FACE_Y+320
NOM4_Y = FACE_Y+400

START_SLEEP = 0.3   # ok parfois 0.18
SLEEP_AFTER_OK = 1
SLEEP_AFTER_OK_A = 1.2
SLEEP_AFTER_KO = 0      # 0 est ok
SLEEP_AFTER_KO_A = 0.5
# 0.3, 1, 0 => 1321

# Créer un objet ArgumentParser
parser = argparse.ArgumentParser(description='Lucca Faces bot')

parser.add_argument('-a', '--apprentissage', action='store_true', help='Activer le mode apprentissage')

args = parser.parse_args()

timestamp0 = time.time()
pyautogui.click(GO_X, GO_Y)
time.sleep(START_SLEEP)

tot_ok = 0;
tot_ko = 0;
while tot_ok < 10 and tot_ko < 200:
    # Obtient le timestamp actuel
    timestamp1 = time.time()

    visage = pyautogui.screenshot(region=(FACE_X-50, FACE_Y-50, 100, 100))

    pixels = visage.getpixel((10, 10)) + visage.getpixel((20, 20))
    id_image = '-'.join(str(x) for x in pixels)
    print(id_image)
    
    face_path = 'faces_ok\\' + id_image + '.png'
    name_path = 'faces_ok\\' + id_image + '_nom.png'
    
    # Apprentissage
    if os.path.exists(face_path) and os.path.exists(name_path):
        print('trouvé')
        print(timestamp1 - timestamp0)
        
        name_location = pyautogui.locateOnScreen(name_path, region=(800, 600, 300, 500), confidence=0.9)
        print(name_location)
        
        if name_location is not None:
            click_spot = pyautogui.center(name_location)
            clickx, clicky = click_spot
            pyautogui.click(clickx, clicky)
            tot_ok += 1
            
            #laisser le temps de charger le résulat
            if args.apprentissage:
                time.sleep(SLEEP_AFTER_OK_A)
            else:
                time.sleep(SLEEP_AFTER_OK)
    else:
        print('non trouvé')
        
        # Intégration des éléments à la base d'images

        if args.apprentissage:
            # Apprentissage : on sauvegarde dans la base des visage
            # il restera à sélectionner le bon "nom" et renomment en enlevant le numéro puis copier dans faces_ok
        
            nom1 = pyautogui.screenshot(region=(NOM_X, NOM1_Y, 240, 40))
            nom2 = pyautogui.screenshot(region=(NOM_X, NOM2_Y, 240, 40))
            nom3 = pyautogui.screenshot(region=(NOM_X, NOM3_Y, 240, 40))
            nom4 = pyautogui.screenshot(region=(NOM_X, NOM4_Y, 240, 40))
            
            visage.save('faces\\' + id_image + '.png')
            nom1.save('faces\\' + id_image + '_nom1.png')
            nom2.save('faces\\' + id_image + '_nom2.png')
            nom3.save('faces\\' + id_image + '_nom3.png')
            nom4.save('faces\\' + id_image + '_nom4.png')
        
        # on appuie d'office sur le 1er
        pyautogui.click(NOM_X-60,NOM2_Y)
        tot_ko += 1

    # On déplace la souris pour ne pas gêner la recherche de l'image
    pyautogui.moveTo(NOM_X-80,NOM2_Y)

    # Obtient le timestamp actuel
    timestamp2 = time.time()
    # Affiche le timestamp
    print(timestamp2 - timestamp1)
    if args.apprentissage:
        time.sleep(SLEEP_AFTER_KO_A)
    else:
        time.sleep(SLEEP_AFTER_KO)
    