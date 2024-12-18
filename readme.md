## Overview

This is the back-end for the unofficial Homestuck NLP project. The intention of this is meant to make it possible for the characters to "converse" with each other. Currently an n-gram is available for some characters.

## QuickStart

pip install requiremens.txt

Will install all the requirements

fastapi dev backEnd.py

Will run the api-webservice for development

# Endpoints

/docs

Will return all the potential api endpoints (automatically created by fastapi)

/api/available

Will return all the available homestuck character's available currently. Is written in shortened named of the character, e.g EB for Egbert, VS for Vriska.

/api/fullName/{ac}

Will return the full name of the character using the shortened name

/api/acronym/{fn}

Will return the acronym of the character using the full name

/api/character/{CharacterName}

Will return the data on the character such as the available conversations that the character can have with other characters

fastapi run backEnd.py --port 80

Will run the api-webservice for production

# Special Thanks

Special thanks to u/DrewLinky[https://www.reddit.com/user/DrewLinky/] from who compiled all the dialogue in homestuck and compiled into odt files seen here[https://drive.google.com/drive/folders/17N84XeIqJMFpbEaPR1LMTXth61Wre_1j] and here[https://www.reddit.com/r/homestuck/comments/cv2ezz/comment/ey1fvho/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button]
