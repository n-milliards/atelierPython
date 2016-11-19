#Installation des logiciels pour l’atelier Python
</br>

###Explications sur comment installer Atom, GIMP et Pygame  
**Atom** : éditeur de texte pour coder notre jeu  
**GIMP** : logiciel de dessin pour modifier les graphisme si on le souhaite entre les ateliers  
**Pygame** : librairie Python qui nous aidera à coder notre jeu

Suivant votre système d’exploitation il faudra installer plus ou moins de bricoles mais tout y est décris !
</br></br>

* [Installer sur linux](#toc_2)
* [Installer sur mac](#toc_6)
* [Installer sur windows](#toc_10)

</br>

##Sur linux

####Installer Atom

Téléchargez le fichier `.deb` sur [https://atom.io/](https://atom.io/

Ouvrez un **terminal** et déplacer-vous dans votre dossier téléchargement (remplacez `download` par le nom du dossier si nécessaire) :

    cd download/
    
Tapez :

    sudo dpkg -i atom-amd64.deb
    
remplacer `atom-amd64.deb` par le nom du fichier téléchargé si différent.
    
Puis : 

    sudo apt-get -f install
    
Une fois Atom installé, allez dans les préférences (`Edition` => `Preferences`)  
Dans l’onglet `install` recherchez le package `terminal-plus` et installez-le.
</br></br>

####Installer GIMP [OPTIONNEL]

Dans le **terminal** tapez :

    sudo apt-get install gimp
</br>

####Installer Pygame  (pour les séances 2, 3 et 4)

Installez les dépendances :

    sudo apt-get install mercurial python3-dev python3-numpy ffmpeg \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
    
Déplacer vous dans votre dossier téléchargement (suivant comment il s’appelle) :

    cd download/
    
Téléchargez les sources en tapant :

    hg clone https://bitbucket.org/pygame/pygame
    
Compilez le programme en exécutant les commandes suivante :

    cd pygame

Puis :

    python3 setup.py build
    
Et enfin :

    sudo python3 setup.py install
    
</br></br></br></br></br>
  
##Sur mac

####Installer Atom

Téléchargez-le sur [https://atom.io/](https://atom.io/) et installez-le normalement.

Une fois atom installé, allez dans les préférences (`cmd` + `,`)  
Dans l’onglet `install` recherchez le package `terminal-plus` et installez-le.
</br></br>

####Installer GIMP [OPTIONNEL]

Téléchargez-le sur [https://www.gimp.org/](https://www.gimp.org/) et installez-le normalement.
</br></br>

####Installer Pygame (pour les séances 2, 3 et 4)

Creez un nouveau fichier texte avec **Atom**   
Copier-coller cela dedans :

    # Homebrew binaries now take precedence over Apple defaults
    export PATH=/usr/local/bin:$PATH

enregistrez le fichier sous ce nom : `.bash_profile` dans le dossier général utilisateur `/Users/lenomdevotreutilisateur` - c’est le dossier avec l’icone de maison.

 
Ouvrez un **terminal** (avec spotlight par exemple en tapant `Terminal`)

Les lignes de commande suivante vous demanderont probablement votre mot de passe, entrez-le.

Tapez ou copiez-collez dans le **terminal** :

    xcode-select --install

  
Téléchargez et installez Xquartz [https://www.xquartz.org/](https://www.xquartz.org/)


Tapez dans le **terminal** :

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

 
Puis :

    brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi


Et enfin :

    pip3 install hg+http://bitbucket.org/pygame/pygame

Si vous n’avez pas de message d’erreur pygame est maintenant installé ainsi que tout ce dont il a besoin pour fonctionner. Vous pouvez redémarrer votre ordi pour que Xquartz opère les changements nécessaires.

Voilà pour la partie pygame.

</br></br></br></br></br>

##Sur windows

####Installer Git et Git Bash

Téléchargez et installez [Git](https://github.com/git-for-windows/git/releases/download/v2.9.2.windows.1/Git-2.9.2-64-bit.exe)

Pendant l’installation n’oubliez pas de cocher **`Git bash`** pour l’installer.
</br></br>

####Installer Atom

Téléchargez-le sur [https://atom.io/](https://atom.io/) et installez-le normalement.
</br></br>

####Installer GIMP [OPTIONNEL]
Téléchargez-le sur [https://www.gimp.org/downloads/](https://www.gimp.org/downloads/) et installez-le normalement.
</br></br></br></br>

###Installer Python et Pygame :

####Pour la séance 1 :
Téléchargez et installez [Python 3.5](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe), pas la peine de faire la suite.

####Pour les séances 2, 3 et 4 :

Téléchargez et installez [Python 3.5](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe).

Puis :

- Retenez où vous avez installer Python 
- Rendez-vous sur cette [page](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) et téléchargez `pygame‑1.9.2b1‑cp35‑cp35m‑win32.whl`
- Déplacez ce fichier `.whl` dans le dossier `python35/Scripts` de votre installation de Python
- Ouvrez une console dans le dossier `Script` (`Shift`+`Clic Droit` dans ce dossier puis `Open a command window here`)
- Écrivez cette commande :
`pip3 install pygame‑1.9.2b1‑cp35‑cp35m‑win32.whl`
- Si vous avez une erreur à la suite de cette commande, tentez :
`python -m pip install pygame‑1.9.2b1‑cp35‑cp35m‑win32.whl`

Si ça ne marche pas vous pouvez tenter cette solution mais la 1ère est préférable :

####Technique alternative mais pas glop :

Téléchargez et installez [Python 3.1 x86](https://www.python.org/ftp/python/3.1.1/python-3.1.1.msi) ou [Python 3.1 x86-64 (AMD)](https://www.python.org/ftp/python/3.1.1/python-3.1.1.amd64.msi)

Téléchargez et installez [Pygame](http://pygame.org/ftp/pygame-1.9.1.win32-py3.1.msi).
</br></br></br></br>

Si rien ne marche, on essaira de trouver la solution ensemble !