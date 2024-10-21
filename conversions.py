def getAbreviation(fullName):
    match fullName.lower().replace(" ", ""):
        case "johnegbert":
            return "JE"
        case "davestrider":
            return "DS"
        case "roselalonde":
            return "RL"
        case "jadeharley":
            return "JH"
        case "nannasprite":
            return "NS"
        case "karkatvantas":
            return "KV"
        case "kanayamaryam":
            return "KM"
        case "tavrosnitram":
            return "TN"
        case "spadesslick":
            return "SS"
        case "terezipyrope":
            return "TP"
        case "jaspersprite":
            return "JS"
        case "davesprite":
            return "DaSp"
        case "andrewhussie":
            return "AH"
        case "solluxcaptor":
            return "SC"
        case "jakeenglish":
            return "JaEn"
        case "gamzeemakara":
            return "GM"
        case "nepetaleijon":
            return "NL"
        case "aradiamegido":
            return "AM"
        case "vriskaserket":
            return "VS"
        case "equiuszahhak":
            return "EZ"
        case "aradiasprite":
            return "AS"
        case "docscratch":
            return "DoSc"
        case "aradiabot":
            return "AB"
        case "feferipeixes":
            return "FP"
        case "eridanampora":
            return "EA"
        case "dragonsprite":
            return "DrSp"
        case "jadesprite":
            return "JadeS"
        case "altvriska":
            return "AV"
        case "fedorafreak":
            return "FF"
        case "janecrocker":
            return "JC"
        case "calliope":
            return "Ce"
        case "roxylalonde":
            return "RxLa"
        case "lilhal":
            return "LH"
        case "dirkstrider":
            return "DiSt"
        case "meenahpeixes":
            return "MP"
        case "caliborn":
            return "Cb"
        case "araneaserket":
            return "ArSe"
        case "brainghostdirk":
            return "BGD"
        case "kankrivantas":
            return "KnVa"
        case "latulapyrope":
            return "LP"
        case "porrimmaryam":
            return "PM"
        case "cronusampora":
            return "CA"
        case "mitunacaptor":
            return "MC"
        case "meulinleijon":
            return "ML"
        case "kurlozmakara":
            return "KuMa"
        case "rufiohnitram":
            return "RN"
        case "horusszahhak":
            return "HZ"
        case "damaramegido":
            return "DM"
        case "erisolsprite":
            return "ES"
        case "fefetasprite":
            return "FS"
        case "herimperiouscondescension":
            return "HIC"
        case "equiusprite":
            return "EqSp"
        case "arquiusprite":
            return "ARSp"
        case "tricksterjane":
            return "TrJn"
        case "tricksterjake":
            return "TrJk"
        case "tricksterroxy":
            return "TrRx"
        case "grimbarkjade":
            return "GB"
        case "crockertierjane":
            return "CJ"
        case "tavrosprite":
            return "TS"
        case "rosesprite":
            return "RS"
        case "jasprosespritesquared":
            return "JR"
        case "altcalliope":
            return "AC"
        case "nepetasprite":
            return "NS"
        case "davepetaspritesquared":
            return "DP"
        case _:
            return "Unknown Full Name"
def getFullName(abv):
    match abv:
        case "JE":
            return "John Egbert"
        case "DS": 
            return "Dave Strider"
        case "RL":
            return "Rose Lalonde"
        case "JH":
            return "Jade Harley"
        case "NS":
            return "Nannasprite"
        case "KV":
            return "Karkat Vantas"
        case "KM":
            return "Kanaya Maryam"
        case "TN":
            return "Tavros Nitram"
        case "SS":
            return "Spades Slick"
        case "TP":
            return "Terezi Pyrope"
        case "JS":
            return "Jaspersprite"
        case "DaSp":
            return "Davesprite"
        case "AH":
            return "Andrew Hussie"
        case "SC":
            return "Sollux Captor"
        case "JaEn":
            return "Jake English"
        case "GM":
            return "Gamzee Makara"
        case "NL":
            return "Nepeta Leijon"
        case "AM":
            return "Aradia Megido"
        case "VS":
            return "Vriska Serket"
        case "EZ":
            return "Equius Zahhak"
        case "AS":
            return "Aradiasprite"
        case "DoSc":
            return "Doc Scratch"
        case "AB":
            return "Aradiabot"
        case "FP":
            return "Feferi Peixes"
        case "EA":
            return "Eridan Ampora"
        case "DrSp":
            return "Dragonsprite"
        case "JadeS":
            return "Jadesprite"
        case "AV":
            return "Alt-Vriska (Vriska)"
        case "FF":
            return "Fedorafreak"
        case "JC":
            return "Jane Crocker"
        case "Ce":
            return "Calliope"
        case "RxLa":
            return "Roxy Lalonde"
        case "LH":
            return "Lil Hal (auto responder)"
        case "DiSt":
            return "Dirk Strider"
        case "MP":
            return "Meenah Peixes"
        case "Cb":
            return "Caliborn"
        case "ArSe":
            return "Aranea Serket"
        case "BGD":
            return "Brain Ghost Dirk"
        case "KnVa":
            return "Kankri Vantas"
        case "LP":
            return "Latula Pyrope"
        case "PM":
            return "Porrim Maryam"
        case "CA":
            return "Cronus Ampora"
        case "MC":
            return "Mituna Captor"
        case "ML":
            return "Meulin Leijon"
        case "KuMa":
            return "Kurloz Makara"
        case "RN":
            return "Rufioh Nitram"
        case "HZ":
            return "Horuss Zahhak"
        case "DM":
            return "Damara Megido"
        case "ES":
            return "Erisolsprite"
        case "FS":
            return "Fefetasprite"
        case "HIC":
            return "Her Imperious Condescension"
        case "EqSp":
            return "Equiusprite"
        case "ARSp":
            return "Arquiusprite"
        case "TrJn":
            return "Trickster Jane"
        case "TrJk":
            return "Trickster Jake"
        case "TrRx":
            return "Trickster Roxy"
        case "GB":
            return "Grimbark Jade"
        case "CJ":
            return "Crocker Tier Jane"
        case "TS":
            return "Tavrosprite"
        case "RS":
            return "Rosesprite"
        case "JR":
            return "Jasprosesprite Squared"
        case "AC":
            return "Alt-Calliope"
        case "NS":
            return "Nepetasprite"
        case "DP":
            return "Davepetasprite Squared"
        case _:
            return "Unknown"

