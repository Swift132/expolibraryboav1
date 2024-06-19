from flask import render_template, request, current_app as app

# Static list of items with extended information
items = [
    {
        "Titulo": "Revista de La Academia Canaria de Ciencias - Volumen XXIV",
        "Autor": "Folia Canariensis Academiae Scientiarum",
        "Ano": 2012,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RevistaDeLaAcademiaCanariaDeCienciasVolumenXXIV.jpg"
    },
    {
        "Titulo": "Revista de La Academia Canaria de Ciencias - Volumen XXIX",
        "Autor": "Folia Canariensis Academiae Scientiarum",
        "Ano": 2017,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RevistaDeLaAcademiaCanariaDeCienciasVolumenXIX.jpg"
    },
    {
        "Titulo": "Revista de La Academia Canaria de Ciencias - Volumen XXX",
        "Autor": "Folia Canariensis Academiae Scientiarum",
        "Ano": 2018,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RevistaDeLaAcademiaCanariaDeCienciasVolumenXX.jpg"
    },
    {
        "Titulo": "Revista de La Academia Canaria de Ciencias - Volumen XXXIII",
        "Autor": "Folia Canariensis Academiae Scientiarum",
        "Ano": 2021,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RevistaDeLaAcademiaCanariaDeCienciasVolumenXXIII.jpg"
    },
    {
        "Titulo": "Revista de La Academia Canaria de Ciencias - Volumen XXXIV",
        "Autor": "Folia Canariensis Academiae Scientiarum",
        "Ano": 2022,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RevistaDeLaAcademiaCanariaDeCienciasVolumenXXIV.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LI - 2ª série, 51",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1977,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLI.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LII - 2ª série, 52",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1978,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LIII - 2ª série, 53 - 1º Parte",
        "Autor": "Prof. Dr. J. Barros Neves, Prof. Dr. J. Firmino Mesquita, Prof. Dr. J. Montezuma De Carvalho, Lic.do Jorge Paiva",
        "Ano": "1979-1980",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLIII1.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LIII - 2ª série, 53 - 2º Parte",
        "Autor": "Prof. Dr. J. Barros Neves, Prof. Dr. J. Firmino Mesquita, Prof. Dr. J. Montezuma De Carvalho, Lic.do Jorge Paiva",
        "Ano": 1981,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLIII2.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LIV - 2ª série, 54",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": "1980-1981",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLIV.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LV - 2ª série, 55",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": "1981-1982",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLV.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LVI- 2ª série, 56",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLVI.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LVII - 2ª série, 57",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1984,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLVII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LVIII - 2ª série, 58",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1985,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLVIII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LIX - 2ª série, 59",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1986,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLIX.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LX - 2ª série, 60",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1987,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLX.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXI - 2ª série, 61",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1988,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXI.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXII - 2ª série, 62",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1989,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXV - 2ª série, 65",
        "Autor": "Prof. Dr. A. Fernandes e Prof. Dr. J. Firmino Mesquita",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXV.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXVI - 2ª série, 66",
        "Autor": "Prof. Dr. J. Firmino Mesquita e Dr.ª Maria Teresa Leitão",
        "Ano": "1993-1994",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXVI.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXVII - 2ª série, 67",
        "Autor": "Prof. Dr. J. Firmino Mesquita e Dr.ª Maria Teresa Leitão",
        "Ano": "1995-1996",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXVII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXVIII - 2ª série, 68",
        "Autor": "Prof. Dr. J. Firmino Mesquita e Dr.ª Maria Teresa Leitão",
        "Ano": 1997,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BoletimDaSociedadeBroterianaVolumeLXVIII.jpg"
    },
    {
        "Titulo": "Boletim Da Sociedade Broteriana - Volume LXVIX, 69",
        "Autor": "Prof. Dr. J. Firmino Mesquita e Dr.ª Maria Teresa Leitão",
        "Ano": "1998-1999",
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Multi idiomas",
        "Material": "Não Plastificado",
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 91",
        "Autor": "Hugo Genser",
        "Ano": 2001,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand91.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 92 - Heft 1",
        "Autor": "Hugo Genser",
        "Ano": 2002,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand92Heft1.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 92 - Heft 2",
        "Autor": "Hugo Genser",
        "Ano": 2002,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand92Heft2.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 93",
        "Autor": "Hugo Genser",
        "Ano": 2003,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand93.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 95/1",
        "Autor": "Hugo Genser",
        "Ano": 2005,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand951.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 95/2",
        "Autor": "Hugo Genser",
        "Ano": 2005,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand952.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 96",
        "Autor": "Hugo Genser",
        "Ano": 2006,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand96.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 97/1",
        "Autor": "Hugo Genser",
        "Ano": 2007,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand971.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 98",
        "Autor": "Hugo Genser",
        "Ano": 2008,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand98.jpg"
    },
    {
        "Titulo": "Berichte der Naturforschenden Gesellschaft - Band 99",
        "Autor": "Hugo Genser",
        "Ano": 2009,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geociência",
        "Linguagem": "Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaturforschendenGesellschaftBand99.jpg"
        
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 53(1)",
        "Autor": "Manuel Laínz e William Sanders",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen531.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 53(2)",
        "Autor": "Manuel Laínz e William Sanders",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen532.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 54(1)",
        "Autor": "Manuel Laínz e William Sanders",
        "Ano": 1996,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen541.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 54(2)",
        "Autor": "Manuel Laínz e William Sanders",
        "Ano": 1996,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen542.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 55(1)",
        "Autor": "Manuel Laínz e William Sanders",
        "Ano": 1997,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen551.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 55(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 1997,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen552.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 56(1)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 1998,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen561.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 56(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 1998,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen562.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 57(1)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 1999,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen571.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 57(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 1999,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen572.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 58(1)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen581.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 58(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen582.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 59(1)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen591.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 59(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen592.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 60(1)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen601.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Volumen 60(2)",
        "Autor": "Manuel Laínz e Diana Wrigley De Basanta",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadridVolumen601.jpg"
    },
    {
        "Titulo": "Catálogo de CD ROM'S",
        "Autor": "Escola Secundária Antero de Quental",
        "Ano": 2008,
        "Categoria": "Escolar",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CatalogodeCDROMS.jpg"
    },
    {
        "Titulo": "Catálogo de Videogramas",
        "Autor": "Escola Secundária Antero de Quental",
        "Ano": 2008,
        "Categoria": "Escolar",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CatalogodeVideogramas.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 106",
        "Autor": "Ake Niemi",
        "Ano": 1978,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo106.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 107",
        "Autor": "Terttu Lempiainen",
        "Ano": 1978,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo107.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 108",
        "Autor": "Pertti Uotila",
        "Ano": 1978,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo108.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 109",
        "Autor": "Viljo Kujala, Lars Fagerstrom & Arvi Ulvinen",
        "Ano": 1979,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo109.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 120",
        "Autor": "Carl-Adam Haeggstrom",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica120.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 121",
        "Autor": "Riclef Grolle",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica121.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 122",
        "Autor": "Niilo Soyrinki",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica122.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 123",
        "Autor": "Hans Luther",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica123.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 124",
        "Autor": "Britt Snogerup",
        "Ano": 1983,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica124.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 125",
        "Autor": "Riclef Grolle e Sinikka Piippo",
        "Ano": 1984,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica125.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 126",
        "Autor": "Guy Hallfors",
        "Ano": 1984,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica126.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 127",
        "Autor": "Sakari Tuhkanen",
        "Ano": 1984,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica127.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 128",
        "Autor": "Lars Edler, Guy Hallfors e Ake Niemi",
        "Ano": 1984,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Finlandês e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica128.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 129",
        "Autor": "Zhi-hua Li",
        "Ano": 1985,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica129.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 130",
        "Autor": "Pertti Uotila e Kerttu Pellinen",
        "Ano": 1985,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica130.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 131",
        "Autor": "Timo Koponen (ed.)",
        "Ano": 1985,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica131.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - No. 133",
        "Autor": "Timo Koponen (ed.)",
        "Ano": 1986,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica133.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 142",
        "Autor": "Sheng Hua Wu",
        "Ano": 1990,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica142.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 145",
        "Autor": "Sakari Tuhkanen",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica145.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 146",
        "Autor": "Kaarina Sarmaja - Korjonen",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica146.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 147",
        "Autor": "Trevor Goward e Teuvo Ahti",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica147.jpg"
    },
    {
        "Titulo": "Annales Botanici Fennici - Vol. 29 no. 2",
        "Autor": "Desconhecido",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnnalesBotaniciFenniciVol29No2.jpg"
    },
    {
        "Titulo": "Annales Botanici Fennici - Vol. 29 no. 3",
        "Autor": "Desconhecido",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnnalesBotaniciFenniciVol29No3.jpg"
    },
    {
        "Titulo": "Annales Botanici Fennici - Vol. 29 no. 4",
        "Autor": "Desconhecido",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnnalesBotaniciFenniciVol29No4.jpg"
    },
    {
        "Titulo": "Annales Botanici Fennici - Vol. 30 no. 1",
        "Autor": "Desconhecido",
        "Ano": 1993,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnnalesBotaniciFenniciVol30No1.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 148",
        "Autor": "Timo Koponen (ed.)",
        "Ano": 1993,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica148.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 150",
        "Autor": "Soili Stenroos (ed.)",
        "Ano": 1994,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica150.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica - 153",
        "Autor": "Lauri Oksanen e Risto Virtanen (eds.)",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennica153.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica No. 169",
        "Autor": "Dariusz L. Szlachetko e Piotr Rutkowski",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo169.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica  No. 174",
        "Autor": "S. Rob Gradstein, Xiao-Lan He, Sinikka Piippo e Masami Mizutani",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo174.jpg"
    },
    {
        "Titulo": "Acta Botanica Fennica  No. 177",
        "Autor": "TImo Koponen, Tong Cao, Sanna Huttunen, Aino Juslén, Chenliang Peng, Sinikka Piippo, Pengcheng Rao, Jirí Vána e Viivi Virtanen",
        "Ano": 2004,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActaBotanicaFennicaNo177.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 35 No. 5 & 6",
        "Autor": "G.A. Mengden, D.F. Hoese, W.F.Ponder",
        "Ano": 1983,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume35N5E6.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 50 No. 2",
        "Autor": "Sandra K. Claxton, Geoffrey K. Prestedge, D.L. Strusz, I.G. Percival, A.J. Wright, J.W. Pickett, A. Byrnes, A.A. Myers, Thomas Heep, Jan Rohozinski, Alastair Simpson, David J. Patterson, Shane T. Anyong",
        "Ano": 1998,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia e Arqueologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume50N2.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 50 No. 3",
        "Autor": "M.D Jones, P.J Sheppard, D.G Sutton, F.L Sutherland, B.J Barron, William R. Dickinson, R. Bonetti, P. Di Cesare, A. Guglielmetti, F. Malerba, E. Migliorini, M. Oddone, J.R Bird, R. Torrence, R.J Bultitude, B.David, M. Hyman, M.W. Rowe, C. Tuniz, E. Lawson, G. Jacobsen, Q. Hua, Gregory D. Edgecombe, Zerina Johanson",
        "Ano": 1998,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia e Arqueologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume50N3.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 51 No. 1",
        "Autor": "Michael Ayress, Timothy Barrows, Vicki Passlow, Robin Whatley, Amélie H. Scheltema, Brenton Knott, Stuart A. Halse, Glenn M. Shea, Ross A. Sadlier, Aaron M. Bauer",
        "Ano": 1999,
        "Categoria": "Biologia",
        "Sub_Categoria": "Malacologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume51N1.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 51 No. 2 & 3",
        "Autor": "Kim Larsen, P.H.J. Castles, John E. McCosker, K.S.W. Campbell, R.E. Barwick, Anthony C. Gill, Alasdair J. Edwards, C.J. Muller, W.J. Tennent, Gleen A Brock, R.B. Rickards, A.J. Wright",
        "Ano": 1999,
        "Categoria": "Biologia",
        "Sub_Categoria": "Taxonomia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume51N2E3.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 52 No. 1",
        "Autor": "R.J. Blakemore, Alexei V. Korniushin, K.S.W. Campbell e R.E. Barwick",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Taxonomia, Anatomia e Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume52N1.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 52 No. 3",
        "Autor": "Desmond L. Strusz, Carl J. Ferraris Jr., Mark A. McGrouther, Kerryn L. Parkinson, W.F Ponder, G.J Avern",
        "Ano": 2000,
        "Categoria": "Geologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume52N3.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Vol. 53 No. 2",
        "Autor": "David K. McAlpine, Gregory D. Edgecombe, Michelle L. Horne, Brian V. Timms, Shane F. McEvey, J.S.F Barker",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Entomologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumVolume53N2.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Supplement 5",
        "Autor": "A.A. Myers",
        "Ano": 1985,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumSupplement5.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Supplement 6",
        "Autor": "Niel L. Bruce",
        "Ano": 1986,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumSupplement6.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Supplement 9",
        "Autor": "Barry C. Russell",
        "Ano": 1988,
        "Categoria": "Geologia",
        "Sub_Categoria": "Antropologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumSupplement9.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Supplement 25",
        "Autor": "Christopher J. Glasby",
        "Ano": 1999,
        "Categoria": "Geologia",
        "Sub_Categoria": "Taxonomia, Filogenia e Biogeografia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumSupplement25.jpg"
    },
    {
        "Titulo": "Records Of The Australian Museum Supplement 26",
        "Autor": "Shane T. Anyong",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Entomologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/RecordsOfTheAustralianMuseumSupplement26.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 61 (1)",
        "Autor": "P.S Wharton, J. Diéguez-Uríbeondo, G. López González, R. Morales, M. Sanz-Elorza, E.D Dana Sánchez, E. Sobrino Vesperinas, B. Gutiérrez Larena, J. Fuertes Aguilar, G. Nieto Feliner, F. Munoz Garmendia, M.D Ribeiro Orge, M. Álvarez Cobelas, P. Riolobos, S. Cirujano, Á. Beyra Matos, G. Reyes artiles, L. Hernández Valdés, H. Pascual, J.B Gallego Fernández e L. Sáez. ",
        "Ano": 2004,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid611.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 61 (2)",
        "Autor": "I. Bárbara, J. Cremades, R. Morales, J. Castillo, A.J Pujadas Salvá, L. Plaza Arregui, Á. Beyra, G. Reyes Artilles, J.M Gorostiaga, A. Santolaria, A. Secilla, C. Cesares, I. Díez, M.C León, E. Inglesas, D. Ferrándiz, R. Herra, G. Volpato, D. Godínez, M. Guimarais, R. Álvarez, F.  Gómiz Garcia, R. García-Camacho, C. Santamaría, C.J Martín-Blanco, M.A Carrasco.",
        "Ano": 2004,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid612.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 62 (1)",
        "Autor": "M. Erben, V.J Arán, A. Guillén, E. Rico, S. Carranza, A. Sosnovsky, S. Cirujano, M. Álvarez Cobelas, M. Moreno Pérez, E. Pina, B. Senterre, J.F Morales, I. Bárbara, J. Cremades, S. Calvo, M.C López-Rodríguez, J. Dosil, J. Diéguez-Uribeondo, J.C Hernández-Crespo, R. Cortés, F. López, J.L Pech.",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid621.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 62 (2)",
        "Autor": "J.L Garrido, P.J Rey, C.M Herrera, E. Torres, S. Botti, J. Rahola, M.P Martín, A. Bertaccini, G. Bacchetta, S. Brullo, L.S Burry, H.L D'Antoni, J.L Frangi, M. Vázquez-Sánchez, T. Terrazas, S. Arias, V. Conforti, M. Lionard, M. Segura, C. Rojo, Á. Beyra Matos, G. Reyes Artiles, L. Palacios-Duque.",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid622.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 63 (1)",
        "Autor": "M. Sanz-Elorza, E.D Dana Sánchez, E. Sobrino Vesperinas, V. Pena, I. Bárbara, M.L Rico Arce, E. Bueno, A. Juan, M.B Crespo, J.F Morales, E. Alfaro, G. Degtjareva, C. Valiejo-Roman, T. Samigullin, D. Sokoloff, L. Chamorro, B. Caballero, J.M Blanco-Moreno, L. Cano, H. Garcia-Serrano, R.M Masalles, F.X Sans, Y.L Dupont, J.M Olesen, C.H Rolleri, C. Prada, P. Van Rijckevorsel.",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid631.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 63 (2)",
        "Autor": "C. Aedo, C. Venhuis, P. Venhuis,, A.C. Ellis-Adam, J.L. Fernández Alonso, G.J. Anderson, G. Bernardello, L. Bohs, T. Weese, A. Santo-Guerra, J. Cremades Ugarte, Ó. Freire Gago, C. Peteiro Gárcia, M.L. Rico Arce, S. Bachman, S. Flores-Maya, I. Flores-Moreno, S. Romero-Rangel, C. Rojas-Zenteno, L.E. Rubio-Licona, X. Cornejo, F. Diego Calonge.",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid632.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 64 (1)",
        "Autor": "M. Martínez-Azorín, M.B. Crespo, A. Juan, A. Gómez Garreta, J. Rull Lluch, M.C. Barceló Martí, M.A. Ribera Siguan, J. Cremades Ugarte, I. Bárbara Criado, E. No Couto, P. Ribeiro, J. Paiva, H. Freitas, S. Brullo, G.P. Giusso del Galdo, S. Sciandrello, J. Guerra, X. Cornejo, C. Ulloa Ulloa, A. Manghisi, M.A. Ribera, M.C. Lavalle, A. Mengascini, S. Cirujano, P. García Murillo, A. Meco, R. Fernández Zamudio, R.H. Zander, J. Vallès Xirau.",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid641.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 64 (2)",
        "Autor": "V.W. Steinmann, B. Van Ee, P.E. Berry, J. Gutiérrez, M. Menezes de Sequeira, R. Jardim, M. Silva, L. Carvalho, J.F. Morales, J. González, F. Chiarini, G. Barboza, J.A. Pérez-Zabala, J. Muller, S. Knapp, C. Romero Zarco, J.A. Camargo, A. Jiménez, I. Olariaga, I. Salcedo, S. Romero, E.C. Rojas, O.H. Garay-Velázquez, J.B. Blanco-Dios, Q.D. Wheeler, A.G. Valdecasas, J. Vigo i Bonada.",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid642.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 65 (1)",
        "Autor": "S. Knapp, J.A. Reyes-Betancort, A. Santos Guerra, I.R. Guma, C.J. Humphries, M.A. Carine, Á. Marrero, J.A. Rojas-Fernández, A. Balza-Quintero, V. Marcano, P.A. Rojas, D. Dávila-Vera, Z. Peña-Contreras, R.V. Mendoza-Briceño, Palacios-Pru, W. Nauray Huari, A. Galán de Mera, Sh. Lewis, P. Gacesa, M.C. Gil-Rodríguez, F. Valdés, I. Frías, E.A. Cantoral-Uriza, M. Aboal, E.V. Zarembo, E.V. Boyko, M.B. Aulicino, M.J. Arturi, E. Mattana, O. Grillo, G. Venora, G. Bacchetta.",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid651.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 65 (2)",
        "Autor": "A. Costa, C.H. Rolleri, C. Prada, L. Passarelli, A. Askgaard, F.W. Stauffer, D.R. Hodel, A.S. Barfod, C. Lado, D. Wrigley de Basanta, L.M. Rico, S.L. Gale, N. Maxted, S. Knapp, E. López, J.A. Devesa, J.L. Fernández-Alonso, M.V. Arbeláez, P. Vargas, B. García, L. Katinas, M.C. Tellería, A. Susanna, S. Ortiz, C. Ulloa Ulloa, J. Homeier, J. Menjívar C., G. Cerén, G. Kadereit, A.E. Yaprak, W. Nauray Huari, A. Galán de Mera.",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid652.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 66 S1",
        "Autor": "M.T. Telleria, R.A. Healy, G. Bonito, J.M. Trappe, C. Silvera-Simón, J. Mena-Portales, J. Gené, J. Cano, J. Guarro, M. Dueñas, M.T. Telleria, I. Melo, M.P. Martín, Á. Bañares, E. Beltrán, C. Lado, D. Wrigley de Basanta, A. Estrada-Torres, E. García Carvajal, M. Aguilar, J.C. Hernández-Crespo, A. Crespo, S. Pérez-Ortega, S. Pérez-Ortega, C. Phosri, M.P. Martín, R. Watling, M. Jeppson, P. Sihanonth.",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid66S1.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 66 (1)",
        "Autor": "A.Ó. Prina, R. Oviedo, A. Traveset, A. Valido, G. Brull, P.M. Jorgensen, R. Vásquez, M. Menezes de Sequeira, A. Díaz-Pérez, A. Santos-Guerra, J. Viruel, P. Catalán, S. Knapp, C. Brullo, S. Brullo, G.P. Giusso del Galdo, L. Scuderi, P. Ubiergo, M. Lapp, P. Torrecilla, J.Baonza Díaz.",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid661.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 66 (2)",
        "Autor": "M. Peinado Lorca, M.A. Macíaz Rodríguez, J.L. Aguirre Martínez, J. Delgadillo Rodríguez, M.A. Rodrigo, J.L. Alonso-Guillén, S. Cirujano, I. Soulié-Marsche, A. Fleischmann, G. Heubl, J.F. Morales, R.H. Zander, S.G. Rabasa, D. Gutiérrez, A. Escudero, S. Wicke, D. Quandt.",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid662.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 67 (1)",
        "Autor": "Livro plastificado ou Autor Desconhecido",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid671.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 67 (2)",
        "Autor": "P. Escobar García, F. Mascia, G. Bacchetta, J.A. Carvalho, T. Pontes, M.I. Batista-Marques, R. Jardim, K. Sutorý, A.M. González, J.L. Vesprini, E. López, J.A. Devesa, J.L. Fernández-Alonso, L. Podda, P. Fraga i Arguimbau, O. Mayoral García-Berlanga, N.L. Cuello, A.M. Cleef, G. Aymard, S. Nozawa, J.R. Grande, O. Huber.",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid672.jpg"
    },
    {
        "Titulo": "Anales Del Jardín Botánico De Madrid - Vol. 68 (1)",
        "Autor": "Livro plastificado ou Autor Desconhecido",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Inglês e Espanhol",
        "Material": "Plastificado",
        "Imagem": "/livros/AnalesDelJardinBotanicoDeMadrid681.jpg"
    },
    {
        "Titulo": "Actas Del V. Simposio Iberico Del Bentos Marino - Tomo I",
        "Autor": "J.J Bacallado e J. Barquín",
        "Ano": 1991,
        "Categoria": "Fisica/Química",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActasDelVSimposioIbericoDelBentosMarinoTomoI.jpg"
    },
    {
        "Titulo": "Actas Del V. Simposio Iberico Del Bentos Marino - Tomo II",
        "Autor": "J.J Bacallado e J. Barquín",
        "Ano": 1992,
        "Categoria": "Fisica/Química",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ActasDelVSimposioIbericoDelBentosMarinoTomoII.jpg"
    },
    {
        "Titulo": "Matemática Cálculo Diferencial em IR - 2ª edição",
        "Autor": "M. Olga Baptista",
        "Ano": 2000,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaCalculoDiferencialemIR.jpg"
    },
    {
        "Titulo": "Bioquímica",
        "Autor": "Manuel Júdice Halpern ",
        "Ano": 1997,
        "Categoria": "Química",
        "Sub_Categoria": "Bioquímica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BioquimicaEdicaoRevista.jpg"
    },
    {
        "Titulo": "Química - 5ª edição",
        "Autor": "Raymond Chang",
        "Ano": 1994,
        "Categoria": "Química",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Quimica5Edição.jpg"
    },
    {
        "Titulo": "Microbiologia - volume 1",
        "Autor": "Wanda F. Canas Ferreira e João Carlos F. de Sousa",
        "Ano": 1998,
        "Categoria": "Biologia",
        "Sub_Categoria": "Microbiologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MicrobiologiaVolume1.jpg"
    },
    {
        "Titulo": "Biologia Celular e Molecular - 3ª edição",
        "Autor": "Carlos Azevedo",
        "Ano": 1999,
        "Categoria": "Biologia",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BiologiaCelularEMolecular.jpg"
    },
    {
        "Titulo": "Análise Matemática Primitivas Integrais Aplicações Exercícios resolvidos e propostos - 3º Volume",
        "Autor": "Fernanda Sequeira",
        "Ano": 1982,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AnaliseMatematica.jpg"
    },
    {
        "Titulo": "Cálculo Matricial Volume II - Exemplos e Aplicações",
        "Autor": "Adelaide Carreira",
        "Ano": 1999,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CalculoMatricialVolumeIIExemploseAplicações.jpg"
    },
    {
        "Titulo": "Matemática Exercícios Primitivas Integrais",
        "Autor": "Manuel Alberto M. Ferreira, Isabel Amaral",
        "Ano": 2001,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaExerciciosPrimitivasIntegrais.jpg"
    },
    {
        "Titulo": "Cálculo Diferencial e Integral - Volume II",
        "Autor": "N. Piskounov",
        "Ano": 2002,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CalculoDiferencialeIntegralVolumeII.jpg"
    },
    {
        "Titulo": "Cálculo Diferencial e Integral - Volume I",
        "Autor": "N. Piskounov",
        "Ano": 2000,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CalculoDiferencialeIntegralVolumeI.jpg"
    },
    {
        "Titulo": "Matemática Formulário",
        "Autor": "Manuel Alberto M. Ferreira, Isabel Amaral",
        "Ano": 2002,
        "Categoria": "Matemática",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaFormulario.jpg"
    },
    {
        "Titulo": "Nova Fisica Divertida",
        "Autor": "Carlos Fiolhais",
        "Ano": 2017,
        "Categoria": "Fisica",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NovaFisicaDivertida.jpg"
    },
    {
        "Titulo": "A Ciencia e os Seus Inimigos",
        "Autor": "Carlos Fiolhais e David Marçal",
        "Ano": 2017,
        "Categoria": "Ciência",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ACienciaEOsSeusInimigos.jpg"
    },
    {
        "Titulo": "Os Ursinhos Folgazões Festa de Anos Surpresa",
        "Autor": "Tormont Publications Inc.",
        "Ano": 1992,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OsUrsinhosFolgazoesFestaDeAnosSurpresa.jpg"
    },
    {
        "Titulo": "Os Ursinhos Folgazões Uma Boa Ação",
        "Autor": "Tormont Publications Inc.",
        "Ano": 1992,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OsUrsinhosFolgazoesUmaBoaAccao.jpg"
    },
    {
        "Titulo": "Ali Babá e Os Quarenta Ladrões",
        "Autor": "F. Domingues e F. Silva",
        "Ano": 1989,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Francês e Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AliBabaEOsQuarentaLadroes.jpg"
    },
    {
        "Titulo": "Ciclo do Azeite",
        "Autor": "Cristina Quental e Mariana Magalhães",
        "Ano": 2009,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CicloDoAzeite.jpg"
    },
    {
        "Titulo": "Albert I do Mónaco, Afonso Chaves e a Meteorologia Nos Açores",
        "Autor": "Conceição Tavares",
        "Ano": 2009,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Francês e Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Ten Years Ten Portraits",
        "Autor": "European Research Council",
        "Ano": 2017,
        "Categoria": "Fotografia",
        "Sub_Categoria": "NaN",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Ten Years - Ten Protraits.jpg"
    },
    {
        "Titulo": "Um Mar Cheio de Vida - A Sea Full of Life",
        "Autor": "Alison Laurie Neilson",
        "Ano": 2021,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UmMarCheiodeVidaVisoesdosAcores.jpg"
    },
    {
        "Titulo": "Guia de História Natural da Ilha do Pico - Pico Island Natural History Hanbook",
        "Autor": "Zilda Melo França, Victor-Hugo Forjaz, Carlos Alberto Ribeiro, Amélia Matias Vaz, Elvira Ribeiro, Eduardo Brito de Azevedo, Jorge Miguel Tavares e Luís Miguel Almeida",
        "Ano": 2014,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GuiadeHistoriaNaturaldaIlhadoPico.jpg"
    },
    {
        "Titulo": "Um bosque perto de si - Conhecer ecossistemas florestais",
        "Autor": "César Garcia",
        "Ano": 2012,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UmBosquePertoDeSi.jpg"
    },
    {
        "Titulo": "O mundo de Gaspar Frutuoso",
        "Autor": "Gaspar Frutuoso Fundação",
        "Ano": 2023,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OMundoDeGasparFrutuoso.jpg"
    },
    {
        "Titulo": "Biologia Um ano de Ciência",
        "Autor": "Universidade dos Açores: Manuela Lima, Armindo Rodrigues e Patrícia Garcia",
        "Ano": 2014,
        "Categoria": "Biologia",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BiologiaUmAnoDeCiencia.jpg"
    },
    {
        "Titulo": "Relação da Primeira Viagem Em Torno do Mundo",
        "Autor": "Antonio Pigafetta",
        "Ano": "NaN",
        "Categoria": "NaN",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Plastificado",
        "Imagem": "/livros/AntonioPigafettaRelacaoDaPrimeiraViagemEmTornoDoMundo.jpg"
    },
    {
        "Titulo": "Atlantida",
        "Autor": "Carlos Bessa",
        "Ano": 2020,
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Atlantida.jpg"
    },
    {
        "Titulo": "Plantas dos Açores",
        "Autor": "Gilda Pontes e Teófilo Braga",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Cultura dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/PlantasdosAçores.jpg"
    },
    {
        "Titulo": "Plantas Ornamentais dos Açores",
        "Autor": "Gilda Pontes e Teófilo Braga",
        "Ano": 2004,
        "Categoria": "Biologia",
        "Sub_Categoria": "Cultura dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/PlantasOrnamentaisdosAçores.jpg"
    },
    {
        "Titulo": "Guia de interpretação da Flora da Reserva Natural da Lagoa do Fogo",
        "Autor": "Gilda Pontes e Teófilo Braga",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Cultura dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GuiaDeInterpretaçãoDaFloraDaReservaNaturalDaLagoaDoFogo.jpg"
    },
    {
        "Titulo": "Insvlana - Órgão do Instituto Cultural de Ponta Delgada - LXVI",
        "Autor": "Humberto Bettencourt, Rodrigo Rodrigues, Armando Côrtes-Rodrigues, José Bruno Carreiro e Francisco Carreiro da Costa",
        "Ano": 2010,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Insvlana2010.jpg"
    },
    {
        "Titulo": "Insvlana - Órgão do Instituto Cultural de Ponta Delgada - LXVIII",
        "Autor": "Humberto Bettencourt, Rodrigo Rodrigues, Armando Côrtes-Rodrigues, José Bruno Carreiro e Francisco Carreiro da Costa",
        "Ano": 2012,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Insvlana2012.jpg"
    },
    {
        "Titulo": "Flora da Madeira - Plantas Vasculares Naturalizadas no Arquipélago da Madeira",
        "Autor": "Rui Manuel da Silva Vieira",
        "Ano": 2002,
        "Categoria": "História",
        "Sub_Categoria": "Botânica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/FloraDaMadeiraPlantasVascularesNaturalizadasNoArquipelagoDaMadeira.jpg"
    },
    {
        "Titulo": "As atitudes face ao ambiente em Regiões Periféricas",
        "Autor": "Emiliana Leonilde Diniz Gil Soares da Silva e Rosalina Maria de Almeida Gabriel ",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AsAtitudesFaceAoAmbienteEmRegioesPerifericas.jpg"
    },
    {
        "Titulo": "Towards planning of seafloor observatory programs for the MAR region - Proceedings of the II MoMAR Workshop - Arquipélago - Life and Marine Sciences Supplement 3",
        "Autor": "Ricardo Serrão Santos, Javier Escartín, Ana Colaço e Agnieszka Adamczewska ",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TowardsPlanningOfSeafloorObservatoryProgramsForTheMarRegion.jpg"
    },
    {
        "Titulo": "Fauna and Flora of the Atlantic Islands - Proceedings of the 3rd symposium - Part A - Arquipélago - Life and Marine Sciences Supplement 2 ",
        "Autor": "Universidade dos Açores",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/FaunaAndFloraOfTheAtlanticIslands.jpg"
    },
    {
        "Titulo": "O Barco e O Sonho",
        "Autor": "Manuel Ferreira",
        "Ano": 2019,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Barco e o Sonho.jpg"
    },
    {
        "Titulo": "Notas de Campo na Beira Baixa",
        "Autor": "Luísa Ferreira Nunes",
        "Ano": 2019,
        "Categoria": "Biologia",
        "Sub_Categoria": "Zoologia e Botânica",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NotasDeCampoNaBeiraBaixa.jpg"
    },
    {
        "Titulo": "História Natural dos Açores",
        "Autor": "António Neves Trota e Maria João Pereira",
        "Ano": 2013,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/HistoriaNaturalDosAcores.jpg"
    },
    {
        "Titulo": "Açores Magiae Naturalis",
        "Autor": "Humberto De Sousa",
        "Ano": 2006,
        "Categoria": "Fotografia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AcoresMagiaeNaturalis.jpg"
    },
    {
        "Titulo": "Boletim",
        "Autor": "Núcleo Cultural da Horta",
        "Ano": 2004,
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Boletim.jpg"
    },
    {
        "Titulo": "A Cultura Sefardita no Nordeste Transmontano",
        "Autor": "A.A.Marques de Almeida",
        "Ano": 2016,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ACulturaSefarditaNoNordesteTransmontano.jpg"
    },
    {
        "Titulo": "The Volcanoes of Azores Islands: a world-class heritage -  example from Terceira, Pico, and Faial Islands",
        "Autor": "José Madeira",
        "Ano": 2005,
        "Categoria": "Geologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TheVolcanoesOfAzoresIslandsAWorldClassHeritage.jpg"
    },
    {
        "Titulo": "Os Últimos Priolos - The Last Azores Bullfinches",
        "Autor": "Desconhecido",
        "Ano": 2009,
        "Categoria": "DVD",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OsUltimosPriolos.jpg"

    },
    {
        "Titulo": "O Sapo ajuda... - Testes de Avaliação",
        "Autor": "Desconhecido",
        "Ano": 2005,
        "Categoria": "DVD",
        "Sub_Categoria": "Ciências da Natureza",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OSapoAjudaTestesDeAvaliação.jpg"
    },
    {
        "Titulo": "Roteiro dos Museos",
        "Autor": "Brangança Municipio",
        "Ano": "NaN",
        "Categoria": "Panfleto",
        "Sub_Categoria": "Roteiro",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BragancaMunicipio.jpg"
    },
    {
        "Titulo": "Blue Azores",
        "Autor": "Governo dos Açores, Oceano Azul Foundation e Waitt Institute",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Blue Azores.jpg"
    },
    {
        "Titulo": "Grande Enciclopédia das Ciências, Tecnologia e Natureza - A evolução da vida",
        "Autor": "Mark Galan",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GrandeEnciclopediaAEvolucaoDaVida.jpg"
    },
    {
        "Titulo": "Grande Enciclopédia das Ciências, Tecnologia e Natureza - Ecologia",
        "Autor": "Mark Galan",
        "Ano": 2001,
        "Categoria": "Ecologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GrandeEnciclopediaEcologia.jpg"
    },
    {
        "Titulo": "Grande Enciclopédia das Ciências, Tecnologia e Natureza - Geografia",
        "Autor": "Mark Galan",
        "Ano": 2001,
        "Categoria": "Geologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GrandeEnciclopediaGeografia.jpg"
    },
    {
        "Titulo": "Grande Enciclopédia das Ciências, Tecnologia e Natureza - Máquinas e Inventos",
        "Autor": "Patricia Daniels",
        "Ano": 2001,
        "Categoria": "Tecnologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GrandeEnciclopediaMaquinaSeInventos.jpg"
    },
    {
        "Titulo": "Grande Enciclopédia das Ciências, Tecnologia e Natureza - O Comportamento dos Animais",
        "Autor": "Mark Galan",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GrandeEnciclopediaOComportamentoDosAnimais.jpg"
    },
    {
        "Titulo": "Lagos, Guia de Geologia e Paleontologia Urbana - Urban Geology and Paleontology Guide",
        "Autor": "Luis Azevedo Rodrigues e Margarida Agostinho",
        "Ano": 2016,
        "Categoria": "Geologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/LagosGuiaDeGeologiaEPaleontologiaUrbana.jpg"
    },
    {
        "Titulo": "Faro, Guia de Geologia e Paleontologia Urbana - Urban Geology and Paleontology Guide",
        "Autor": "Luis Azevedo Rodrigues e Margarida Agostinho",
        "Ano": 2016,
        "Categoria": "Geologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/FaroGuiaDeGeologiaEPaleontologiaUrbana.jpg"
    },
    {
        "Titulo": "Tavira, Guia de Geologia e Paleontologia Urbana - Urban Geology and Paleontology Guide",
        "Autor": "Luis Azevedo Rodrigues e Margarida Agostinho",
        "Ano": 2016,
        "Categoria": "Geologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TaviraGuiaDeGeologiaePaleontologiaUrbana.jpg"
    },
    {
        "Titulo": "Aves Peixes Mamíferos",
        "Autor": "Camera Municipal de Gaia",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AvesPeixesMamiferos.jpg"
    },
    {
        "Titulo": "Manual Para Segurança na Pesca",
        "Autor": "Direção Regional das Pescas",
        "Ano": 2020,
        "Categoria": "Segurança",
        "Sub_Categoria": "Pesca",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ManualParaSegurancaNaPesca.jpg"
    },
    {
        "Titulo": "A Caravela",
        "Autor": "Eduardo Frutuoso, Paulo Guinote e António Lopes",
        "Ano": 2011,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ACaravela.jpg"
    },
    {
        "Titulo": "Guia Prático da Biologia da Abelha",
        "Autor": "Luís Moreira e Nuno Farinha",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Apicultura",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BiologiaDaAbelha.jpg"
    },
    {
        "Titulo": "Charcos Temporários Do Sul de Portugal",
        "Autor": "Carla Pinto Cruz",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Zoologia e Botânica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CharcosTemporariosDoSulDePortugal.jpg"
    },
    {
        "Titulo": "Circuitos Ciência Viva - 3ª edição",
        "Autor": "Filipa Dias, Francisco Motta Veiga e Cláudia Montenegro ",
        "Ano": 2020,
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CircuitosCienciaViva3.jpg"
    },
    {
        "Titulo": "Circuitos Ciência Viva - 2ª edição",
        "Autor": "Filipa Dias, Francisco Motta Veiga e Cláudia Montenegro ",
        "Ano": 2018,
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CircuitosCienciaViva2.jpg"
    },
    {
        "Titulo": "Panorama Spokes",
        "Autor": "Maarten Okkersen, Julie Becker, Andrea Bandelli, Raphael Chanay, Marie Couedic, Raquel da Cunha, Wiktor Gajewski, Aliki Giannakopoulou, Antonio Gomes da Costa, Lucie Steigleder e Maria Xanthoudaki",
        "Ano": 2018,
        "Categoria": "Ciências",
        "Sub_Categoria": "Revista",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Panorama Spokes 2018.jpg"
    },
    {
        "Titulo": "Panorama Spokes",
        "Autor": "Maarten Okkersen, Julie Becker, Andrea Bandelli, Raphael Chanay, Marie Couedic, Raquel da Cunha, Wiktor Gajewski, Aliki Giannakopoulou, Antonio Gomes da Costa, Lucie Steigleder e Maria Xanthoudaki",
        "Ano": 2017,
        "Categoria": "Ciências",
        "Sub_Categoria": "Revista",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Panorama Spokes 2017.jpg"
    },
    {
        "Titulo": "Together",
        "Autor": "Ecsite",
        "Ano": 2018,
        "Categoria": "Entrevista",
        "Sub_Categoria": "NaN",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Together 2018.jpg"
    },
    {
        "Titulo": "Rising Tide",
        "Autor": "Ecsite",
        "Ano": 2017,
        "Categoria": "Entrevista",
        "Sub_Categoria": "NaN",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Rising Tide 2017.jpg"
    },
    {
        "Titulo": "Geodiversidade, Valores e Usos",
        "Autor": "Diamantino Pereira, José Brilha e Paulo Pereira",
        "Ano": 2008,
        "Categoria": "Geodiversidade",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Geodiversidade Valores e Usos.jpg"
    },
    {
        "Titulo": "Energia e Alterações Climáticas",
        "Autor": "Ana Filipa Silva, Hélder Careto e Manuel Ferreira dos Santos",
        "Ano": 2008,
        "Categoria": "Ciências",
        "Sub_Categoria": "Energia e Meteorologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Energia e Alterações Climáticas.jpg"
    },
    {
        "Titulo": "OGM - Organismos Geneticamente Modificados",
        "Autor": "Lurder Soares, Teresa Venceslau e José Carlos Boto",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OGM - Organissmos Geneticamente Modificados.jpg"
    },
    {
        "Titulo": "O Milhafre uma história natural",
        "Autor": "Gilda Pontes e Judite Cardoso",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Milhafre uma História Natural.jpg"
    },
    {
        "Titulo": "A Terra Aquece, Arrefeça-a",
        "Autor": "National Geographic Society",
        "Ano": 2015,
        "Categoria": "Geografia",
        "Sub_Categoria": "Meteorologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Terra Aquece - Arrefeça-a.jpg"
    },
    {
        "Titulo": "O Novo Mundo De Magalhães",
        "Autor": "Jornal de Noticias",
        "Ano": 2021,
        "Categoria": "História",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/História Jornal de Noticias.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 12",
        "Autor": "José António Matos, Sara Duarte e Sofia Brogueira",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade 12.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 11",
        "Autor": "José António Matos, Sara Duarte e Sofia Brogueira",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade 11.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 10",
        "Autor": "José António Matos, Sara Duarte e Sofia Brogueira",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade 10.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 9",
        "Autor": "José António Matos, Sara Duarte e Sofia Brogueira",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade 09.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 8",
        "Autor": "José António Matos, Sara Duarte e Sofia Brogueira",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade 08.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 5",
        "Autor": "Desconhecido",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade Numero 5.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 3",
        "Autor": "Desconhecido",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade Número 3.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade número 2",
        "Autor": "Desconhecido",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade Numero 2.jpg"
    },
    {
        "Titulo": "Biologia e Sociedade Edição Especial",
        "Autor": "Alvin Toffler",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Biologia & Sociedade Edição Especial.jpg"
    },
    {
        "Titulo": "Showbiz culture No. 6",
        "Autor": "Backstage",
        "Ano": "2019-2020",
        "Categoria": "Revista",
        "Sub_Categoria": "NaN",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Showbiz Culture Backstage.jpg"
    },
    {
        "Titulo": "A evolução de Darwin",
        "Autor": "Daniel Loxton",
        "Ano": 2009,
        "Categoria": "Ciências",
        "Sub_Categoria": "Natureza",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Evolução de Darwin.jpg"
        
    },
    {
        "Titulo": "Ciência Viva - because science is for everyone",
        "Autor": "Catarina Figueira e José Vitor Malheiros",
        "Ano": 2019,
        "Categoria": "Ciências",
        "Sub_Categoria": "Revista",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Ciência Viva.jpg"
    },
    {
        "Titulo": "Esponjas ",
        "Autor": "Pedro Teixeira Gomes, Flávia Alves Coelho e Bruno Panta Ferreira",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia marinha",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Esponjas.jpg"
    },
    {
        "Titulo": "As espécies mais populares do mar de Portugal num restaurante perto de si",
        "Autor": "Marianne Correia, Ana Martins",
        "Ano": 2015,
        "Categoria": "Enciclopédia",
        "Sub_Categoria": "Biologia marinha",
        "Linguagem": "Português, Inglês e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AsEspeciesMaisPopularesDoMarDePortugal.jpg"
    },
    {
        "Titulo": "Descobrir a Ciência Bricando: Porque é escura a noite? ",
        "Autor": "Sophy Tahta",
        "Ano": 1989,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/PorqueEEscuraANoite.jpg"
    },
    {
        "Titulo": "Eu sei ler: O Capuchinho Vermelho ",
        "Autor": "Desconhecido",
        "Ano": 2001,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OCapuchinhoVermelho.jpg"
    },
    {
        "Titulo": "A chuva e o bom tempo",
        "Autor": "Adré Pozner",
        "Ano": 1992,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AChuvaEOBomTempo.jpg"
    },
    {
        "Titulo": "Sabes porque é que o fogo é vida",
        "Autor": "Emanuela Bussolati",
        "Ano": 2009,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OFogoEVida.jpg"
    },
    {
        "Titulo": "Sabes porque é que a terra é vida",
        "Autor": "Emanuela Bussolati",
        "Ano": 2009,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ATerraEVida.jpg"
    },
    {
        "Titulo": "Sabes porque é que o ar é vida",
        "Autor": "Emanuela Bussolati",
        "Ano": 2009,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OArEVida.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Robots",
        "Autor": "Clive Gifford",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Robots.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Mapas e Cartas",
        "Autor": "Deborah Chancellor",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MapasECartas.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Materiais Líquidos, sólidos e gasosos - as suas propriedades e usos",
        "Autor": "Clive Gifford",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Materiais.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Clima",
        "Autor": "Caroline Harris",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Clima.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Desertos",
        "Autor": "Nicola Davies",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Desertos.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Terras Polares",
        "Autor": "Margaret Hynes",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TerrasPolares.jpg"
    },
    {
        "Titulo": "Enciclopédia Temática Educativa: Disfarce dos Animais",
        "Autor": "Belinda Weber",
        "Ano": 2005,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DisfarceDosAnimais.jpg"
    },
    {
        "Titulo": "Grandes Clássicos de Aventuras: A Ilha Misteriosa",
        "Autor": "Rita da Costa",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AIlhaMisteriosa.jpg"
    },
    {
        "Titulo": "Grandes Clássicos de Aventuras: A Ilha do Tesouro",
        "Autor": "R.L. Stevenson",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AIlhaDoTesouro.jpg"
    },
    {
        "Titulo": "O Mistério da Lagarta",
        "Autor": "José Francisco Rica",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OMisterioDaLagarta.jpg"
    },
    {
        "Titulo": "Branca de Neve e Outras Histórias",
        "Autor": "Maria Adelaine Vaz",
        "Ano": 1993,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BrancaDeNeveEOutrasHistórias.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Explorar os números",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaExplorarOsNumeros.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Medir o Tamanho",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaMedirOTamanho.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Fazer Fracções",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaFazerFraccoes.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Identificar pontos e posições",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaIdentificarPontosEPosicoes.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Explorar as Formas",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaExplorarAsFormas.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Medir o Peso e o Tempo",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaMedirOPesoEOTempo.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Tratar Dados",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaTratarDados.jpg"
    },
    {
        "Titulo": "Matemática Divertida: Descobrir Padrões",
        "Autor": "Sally Hewitt",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MatematicaDivertidaDescobrirPadroes.jpg"
    },
    {
        "Titulo": "Miúdos espertos! Experiências com cores",
        "Autor": "Ruth Gellersen e Ulrich Velte",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ExperienciasComCores.jpg"
    },
    {
        "Titulo": "Miúdos espertos! Experiências com a natureza",
        "Autor": "Ruth Gellersen e Ulrich Velte",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ExperienciasComANatureza.jpg"
    },
    {
        "Titulo": "Miúdos espertos! Experiências com tecnologia",
        "Autor": "Ruth Gellersen e Ulrich Velte",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ExperienciasComTecnologia.jpg"
    },
    {
        "Titulo": "Eu e a Química - 8º ano - Caderno de atividades",
        "Autor": "Noémia Maciel e Ana Miranda",
        "Ano": 2002,
        "Categoria": "Físico-Química",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Eu e a Quimica - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Bioterra Parte 1 - 5º ano",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2007,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 5 Parte 1.jpg"
    },
    {
        "Titulo": "Bioterra Parte 2 - 5º ano",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2007,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 5 Parte 2.jpg"
    },
    {
        "Titulo": "Bioterra - 5º ano - Caderno de atividades",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2007,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 5 - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Biovida - 8º ano",
        "Autor": "Lucinda Motta e Maria dos Anjos Viana",
        "Ano": "NaN",
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bio Vida.jpg"
    },
    {
        "Titulo": "Eu e a Química - 8º ano ",
        "Autor": "Noémia Maciel e Ana Miranda",
        "Ano": 2002,
        "Categoria": "Físico-Química",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Eu e a Quimica.jpg"
    },
    {
        "Titulo": "O Mistério da vida - 5º ano",
        "Autor": "Helena Vaz Domingues, José Augusto Batista, Marília Serrano Sobral",
        "Ano": 2004,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Mistério da Vida.jpg"
    },
    {
        "Titulo": "Da célula ao universo - 11º ano",
        "Autor": "Elsa Oliveira, Carmen Pedrosa, Rosa Pires",
        "Ano": 1997,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Da Célula no Universo.jpg"
    },
    {
        "Titulo": "A minha primeira enciclopédia com winnie the pooh e seus amigos",
        "Autor": "A. A. Milne",
        "Ano": 2006,
        "Categoria": "Infantil",
        "Sub_Categoria": "Enciclopédia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Minha Primeira Enciclopédia.jpg"
    },
    {
        "Titulo": "Bioterra > Parte 1 - 6º Ano",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2006,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 6 Parte 1.jpg"
    },
    {
        "Titulo": "Bioterra > Parte 2 - 6º Ano",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2006,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 6 Parte 2.jpg"
    },
    {
        "Titulo": "Bioterra > Caderno de Atividades 6º Ano",
        "Autor": "Lucinda Motta, Maria dos Anjos Viana, Emídio Isaías",
        "Ano": 2005,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bioterra 6 - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Descobrir a Terra: Livro do Aluno",
        "Autor": "Cristina Antunes, Manuela Bispo e Paula Guindeira",
        "Ano": "NaN",
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Descobrir a Terra Livro do Aluno.jpg"
    },
    {
        "Titulo": "Descobrir a Terra: Livro do Professor",
        "Autor": "Cristina Antunes, Manuela Bispo e Paula Guindeira",
        "Ano": "NaN",
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Descobrir a Terra Livro do Professor.jpg"
    },
    {
        "Titulo": "Descobrir a Terra: Caderno de Atividades",
        "Autor": "Cristina Antunes, Manuela Bispo e Paula Guindeira",
        "Ano": "NaN",
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Descobrir a Terra - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Ciências: Manual do Aluno",
        "Autor": "João Azevedo, Paula Santana e Carlos Teixeira",
        "Ano": 2006,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Ciências: Manual do Professor",
        "Autor": "João Azevedo, Paula Santana e Carlos Teixeira",
        "Ano": 2005,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Ciências: Caderno de Atividades",
        "Autor": "João Azevedo, Paula Santana e Carlos Teixeira",
        "Ano": 2005,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Planeta Terra: Viver melhor na Terra",
        "Autor": "Ana Cristina Barros e Fernando Delgado",
        "Ano": 2008,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Planeta Terra 9.jpg"
    },
    {
        "Titulo": "Terra Mãe CFQ: Sustentabilidade na Terra",
        "Autor": "Lucinda Santos Mendonça, Maria da Conceição Dantas, Marta Duarte Ramalho",
        "Ano": 2005,
        "Categoria": "Físico-Química",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Terra Mãe CFQ - Sustentabilidade na Terra.jpg"
    },
    {
        "Titulo": "6º Ano Matemática Convida: Parte 1",
        "Autor": "Ana Ribeiro Rosa, Lourdes Neves e Natália Vaz",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemática ConVida Parte 1.jpg"
    },
    {
        "Titulo": "6º Ano Matemática Convida: Parte 2",
        "Autor": "Ana Ribeiro Rosa, Lourdes Neves e Natália Vaz",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemática ConVida Parte 2.jpg"
    },
    {
        "Titulo": "6º Ano Matemática Convida: Caderno de Atividades",
        "Autor": "Ana Ribeiro Rosa, Lourdes Neves e Natália Vaz",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemática ConVida Caderno de Actividades.jpg"
    },
    {
        "Titulo": "6º Ano Matemática Convida: Caderno de Materiais",
        "Autor": "Ana Ribeiro Rosa, Lourdes Neves e Natália Vaz",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemática ConVida - Caderno de Materiais.jpg"
    },
    {
        "Titulo": "Mat 6 - Volume 1 - 6º ano",
        "Autor": "Elza Gouveia Durão e Maria Margarida Baldaque",
        "Ano": 2006,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mat 6 Volume 1.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 5º ano - Caderno de atividades",
        "Autor": "Maria Alexandra Conceição, Matilde Gonçalves Almeida, Maria Cristina Conceição e Rita Nascimento Costa",
        "Ano": 2006,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matematicamente Falando 5 - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Descobrir a Terra - 7º ano - Caderno de atividades ",
        "Autor": "Cristina Antunes, Manuela Bispo e Paula Guindeira",
        "Ano": 2005,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Descobrir a Terra - Caderno de Actividades 2.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 5º ano - Parte 1",
        "Autor": "Maria Alexandra Conceição, Matilde Gonçalves Almeida, Maria Cristina Conceição e Rita Nascimento Costa",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemáticamente Falando 5 Parte 1.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 5º ano - Parte 2",
        "Autor": "Maria Alexandra Conceição, Matilde Gonçalves Almeida, Maria Cristina Conceição e Rita Nascimento Costa",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemáticamente Falando 5 Parte 2.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 8º ano - Parte 1",
        "Autor": "Maria Alexandra Conceição e Matilde Gonçalves Almeida",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matematicamente Falando 8 Parte 1.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 8º ano - Parte 2",
        "Autor": "Maria Alexandra Conceição e Matilde Gonçalves Almeida",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemáticamente Falando 8 Parte 2.jpg"
    },
    {
        "Titulo": "Matematicamente falando - 8º ano - Caderno de atividades",
        "Autor": "Maria Alexandra Conceição e Matilde Gonçalves Almeida",
        "Ano": 2007,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Matemáticamente Falando 8 - Caderno de Actividades.jpg"
    },
    {
        "Titulo": "Escritas em dia - Fichas de ortografia para diferenciação na sala de aula - 3º ano",
        "Autor": "Manuel Ramalho",
        "Ano": "NaN",
        "Categoria": "Lingua Portuguesa",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Escrita em dia - Fichas de ortografia.jpg"
    },
    {
        "Titulo": "Mat 6  - 6º ano - Caderno de Exercicios",
        "Autor": "Elza Gouveia Durão e Maria Margarida Baldaque",
        "Ano": 2006,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mat 6 Caderno de Exercícios.jpg"
    },
    {
        "Titulo": "Mat 6 - Volume 2 - 6º ano",
        "Autor": "Elza Gouveia Durão e Maria Margarida Baldaque",
        "Ano": 2005,
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mat 6 Volume 2.jpg"
    },
    {
        "Titulo": "À Procura da Solução: Actividades Matemáticas",
        "Autor": "Ana Ribeiro Rosa, Lourdes Neves e Natália Vaz",
        "Ano":"NaN",
        "Categoria": "Matemática",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/À Procura da Solução Actividades Matemáticas.jpg"
    },
    {
        "Titulo": "O Mundo da Carochinha: Livro Geral",
        "Autor": "Carlos Letra",
        "Ano": 2010,
        "Categoria": "Estudo do Meio",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Mundo da Carochinha Livro Aluno.jpg"
    },
    {
        "Titulo": "O Mundo da Carochinha: Fichas de Avaliação Mensal",
        "Autor": "Carlos Letra",
        "Ano": 2010,
        "Categoria": "Estudo do Meio",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Mundo da Carochinha Fichas de Avaliação Mensal.jpg"
    },
    {
        "Titulo": "O Mundo da Carochinha: Expressão Plástica",
        "Autor": "Carlos Letra",
        "Ano": 2010,
        "Categoria": "Estudo do Meio",
        "Sub_Categoria": "Manual Escolar",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Mundo da Carochinha - Expressão Plástica.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 1: O Patinho Feio",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - O Patinho Feio.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 1: A Panela Mágica",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - A Panela Mágica.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 2: Capuchinho Vermelho",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - Capuchinho Vermelho.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 2: Os três porquinhos",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - Os Três Porquinhos.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 3: O gato das botas",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - O Gato das Botas.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 4: Branca de neves e os sete anões",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - Branca de Neve e os Sete Anões.jpg"
    },
    {
        "Titulo": "Ler é crescer: Leio sozinho nível 4: Pedro e o Lobo",
        "Autor": "Álvaro Antunes",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Leio Sozinho - Pedro e o Lobo.jpg"
    },
    {
        "Titulo": "Solar de Santa Catarina",
        "Autor": "Charles Pereira Nogueira",
        "Ano": 2018,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Solar de Santa Catarina.jpg"
    },
    {
        "Titulo": "Histórias, Conversas e Lengalengas",
        "Autor": "Maria da Conceição de Oliveira Caldeira",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/HistoriasConversasELengalengas.jpg"
    },
    {
        "Titulo": "La Casita de Chocolate",
        "Autor": "Grupo Edider",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "Livro para Colorir",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/LaCasitaDeChocolate.jpg"
    },
    {
        "Titulo": "Blanca Nieves",
        "Autor": "Grupo Edider",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "Livro para Colorir",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/BlancaNieves.jpg"
    },
    {
        "Titulo": "El Mundo de Tarzan",
        "Autor": "Grupo Edider",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "Livro para Colorir",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ElMundoTarzan.jpg"
    },
    {
        "Titulo": "Peter Pan e Pinoquio",
        "Autor": "Grupo Edider",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/PeterPanEPinoquio.jpg"
    },
    {
        "Titulo": "Descobrir a Ciência Brincando: De onde vem a Eletricidade?",
        "Autor": "Susan Mayes",
        "Ano": 1989,
        "Categoria": "Infantil",
        "Sub_Categoria": "Ciência Geral",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DeOndeVemAEletricidade.jpg"
    },
    {
        "Titulo": "Já sei Ler: Parabéns, Igor!",
        "Autor": "Isabel Gaines",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ParabensIgor.jpg"
    },
    {
        "Titulo": "As minhas primeiras Leituras: Que dia tão Bonito!",
        "Autor": "Ana Maria Guedes e Rui Guedes",
        "Ano": 1997,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/QueDiaTaoBonito.jpg"
    },
    {
        "Titulo": "Dicionário Infantil do Ambiente",
        "Autor": "Joaquim Palma",
        "Ano": 2006,
        "Categoria": "Infantil",
        "Sub_Categoria": "Dicionário",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DicionarioInfantilDoAmbiente.jpg"
    },
    {
        "Titulo": "A Cabana do Pai Tomás",
        "Autor": "Harriet Beecher Stowe",
        "Ano": 1998,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ACabanaDoPaiTomas.jpg"
    },
    {
        "Titulo": "Os talheres mágicos do Titanic: Los cubiertos mágicas del Titanic",
        "Autor": "Paulo Trincão",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OsTalheresMagicosDoTitanic.jpg"
    },
    {
        "Titulo": "Histórias multieducativas DISNEY com passatempos e jogos a cores: 101 Dálmatas",
        "Autor": "Everest Editora",
        "Ano": 1994,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/101Dalmatas.jpg"
    },
    {
        "Titulo": "Uma Aventura Estaminal",
        "Autor": "João Ramalho-Santos",
        "Ano": 2013,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UmaAventuraEstaminal.jpg"
    },
    {
        "Titulo": "O Corcunda de Notre Dame",
        "Autor": "Roz Phillips",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OCorcundadeNotreDame.jpg"
    },
    {
        "Titulo": "As Aventuras de TinTim: Os Charutos do Faraó",
        "Autor": "Verbo",
        "Ano": 1983,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TinTimOsCharutosDoFarao.jpg"
    },
    {
        "Titulo": "Uma Aventura de Astérix o Gavlês: O Dominio dos Deuses",
        "Autor": "Goscinny",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UmaAventuraDeAsterixOGavlesODominioDosDeuses.jpg"
    },
    {
        "Titulo": "Grandes Ilustradores da Escola Russa: Os mais belos contos de Andersen",
        "Autor": "Michael Fiodorov",
        "Ano": 1992,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OsMaisBelosContosDeAndersen.jpg"
    },
    {
        "Titulo": "Aladino e a Lâmpada maravilhosa",
        "Autor": "Shogo Hirata",
        "Ano": 1991,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Aladino e a Lâmpada maravilhosa.jpg"
    },
    {
        "Titulo": "Peter Pan",
        "Autor": "Shogo Hirata",
        "Ano": 1991,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Peter Pan.jpg"
    },
    {
        "Titulo": "O gigante e os morangos - 3º  edição",
        "Autor": "Anabela Batista ",
        "Ano": 2002,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Gigante e os morangos.jpg"
    },
    {
        "Titulo": "Bichos grandes: A tartaruga azul ",
        "Autor": "Alan Rogers",
        "Ano": 1990,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Tartaruga Azul.jpg"
    },
    {
        "Titulo": "Quero um dinossáurio ",
        "Autor": "Hiawyn Oram e Satoshi Kitamura",
        "Ano": 1990,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Quero um Dinossáurio.jpg"
    },
    {
        "Titulo": "Gente Diferente: Um Livro com janelinhas ",
        "Autor": "Sadie Fields",
        "Ano": 1995,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Gente Diferente Um Livro com Janelinhas.jpg"
    },
    {
        "Titulo": "Os contos do tio patinhas: João e Maria",
        "Autor": "The walt disney company",
        "Ano": 1995,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/João e Maria.jpg"
    },
    {
        "Titulo": "Farol: Um golfinho em apuros",
        "Autor": "Sofia Quaresma",
        "Ano": 2015,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Farol, Um Golfinho em Apuros.jpg"
    },
    {
        "Titulo": "Tudo ao contrário: Diário de uma equipa de um centro ciência",
        "Autor": "Ciência viva: Agência para a cultura científica e tecnológica",
        "Ano": 2010,
        "Categoria": "Ciências e tecnologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Tudo ao Contrário.jpg"
    },
    {
        "Titulo": "Lagoas e lagoeiros da ilha de São Miguel",
        "Autor": "J.P Constância, T.J Braga, J.C Nunes, E. Machado, L. SIlva",
        "Ano": 2008,
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/LagoasELagoeiros.jpg"
    },
    {
        "Titulo": "A História da Senhora Rata Migalha",
        "Autor": "Beatrix Potter",
        "Ano": 1987,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "A Floresta",
        "Autor": "Angela Weinhold",
        "Ano": 2007,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AFloresta.jpg"
    },
    {
        "Titulo": "Dinossauro",
        "Autor": "Dorling Kindersley",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Dinossauro.jpg"
    },
    {
        "Titulo": "É Divertido Conhecer os Paises da Europa com Walt Disney",
        "Autor": "The walt disney company",
        "Ano": 1988,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/EDivertidoConhecerOsPaisesDaEuropa.jpg"
    },
    {
        "Titulo": "É Divertido Conhecer os Países da América com Walt Disney",
        "Autor": "The walt disney company",
        "Ano": 1988,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/EDivertidoConhecerOsPaisesDaAmerica.jpg"
    },
    {
        "Titulo": "Descobre a Floresta Húmida",
        "Autor": "Jen Green",
        "Ano": 2004,
        "Categoria": "Ciências da natureza",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Descobre a Floresta Húmida.jpg"
    },
    {
        "Titulo": "Dokeo, Proteger a Terra: Os grandes desafios do Ambiente",
        "Autor": "Jean-Michel Billioud",
        "Ano": 2008,
        "Categoria": "Ecologia",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DOKEO Proteger a Terra.jpg"
    },
    {
        "Titulo": "O Leão e o rato",
        "Autor": "F.Melro",
        "Ano": 2000,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OLeaoEORato.jpg"
    },
    {
        "Titulo": "Um livro de Olhos Marotos: O Carro Bombeiro Matias",
        "Autor": "Impala",
        "Ano": 1995,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/OCarroBombeiroMatias.jpg"
    },
    {
        "Titulo": "Luta de Galos",
        "Autor": "José Abrantes",
        "Ano": 1991,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Luta de Galos.jpg"
    },
    {
        "Titulo": "O ladrão Insolente",
        "Autor": "José Abrantes",
        "Ano": 1991,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Ladrão Insolente.jpg"
    },
    {
        "Titulo": "O Eclipse",
        "Autor": "José Abrantes",
        "Ano": 1992,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Eclipse.jpg"
    },
    {
        "Titulo": "O meu primeiro livro sobre Tudo o que voa",
        "Autor": "Impala",
        "Ano": 1990,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Meu Primeiro Livro sobre Tudo o que Voa.jpg"
    },
    {
        "Titulo": "Maravilhas da natureza",
        "Autor": "David Burnie",
        "Ano": 2008,
        "Categoria": "Ciências da natureza",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Maravilhas da Natureza.jpg"
    },
    {
        "Titulo": "A Bela e o Monstro",
        "Autor": "Girassol Edições",
        "Ano": 1998,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado", 
        "Imagem": "/livros/A Bela e o Monstro.jpg"
    },
    {
        "Titulo": "Dentro da floresta",
        "Autor": "Giovanna Mantegazza",
        "Ano": 1993,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Dentro da Floresta.jpg"
    },
    {
        "Titulo": "As viagens de Gulliver",
        "Autor": "Impala",
        "Ano": 1997,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/As Viagens de Gulliver.jpg"
    },
    {
        "Titulo": "O lobo e os sete cabritos",
        "Autor": "Girassol Edições",
        "Ano": 1998,
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Lobo e os sete Cabritos.jpg"
    },
    {
        "Titulo": "A Bela adormecida",
        "Autor": "Girassol Edições",
        "Ano": 1995,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Bela Adormecida.jpg"
    },
    {
        "Titulo": "Polegarzinho",
        "Autor": "H. Christian Andersen",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Polegarzinho.jpg"
    },
    {
        "Titulo": "O rei da selva",
        "Autor": "Marina Moreira",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "Livro para colorir",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Rei da Selva.jpg"
    },
    {
        "Titulo": "Contos de encantar: O livro da selva",
        "Autor": "Edibimbi",
        "Ano": 1994,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Livro da Selva.jpg"
    },
    {
        "Titulo": "O passeio do papagaio de papel",
        "Autor": "Jacqueline Loumaye ",
        "Ano": 1988,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Passeio do Papagaio de Papel.jpg"
    },
    {
        "Titulo": "A minha primeira biblioteca: O gato das botas",
        "Autor": "A.M Lefevre, M. Loiscaux, M. Nathan-Deiller e A. Van Gool",
        "Ano": 1998,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Gato das Botas.jpg"
    },
    {
        "Titulo": "As aventuras que eu gosto de ler: Heidi ",
        "Autor": "M. Nathan-Deiller e A. Van Gool",
        "Ano": 1997,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Heidi.jpg"
    },
    {
        "Titulo": "Circuitos ciência viva - 1ª edição",
        "Autor": "Leonel Alegre",
        "Ano": 2016,
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/CircuitosCienciaViva.jpg"
    },
    {
        "Titulo": "Mistérios disney: Os fantasmas Existem? ",
        "Autor": "Disney",
        "Ano": 1999,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mistérios Disney - Os Fantasmas Existem.jpg"
    },
    {
        "Titulo": "Histórias multieducativas DISNEY com passatempos e jogos a cores: Pinóquio",
        "Autor": "The walt disney company",
        "Ano": 1995,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Histórias Multieducativas Disney Pinóquio.jpg"
    },
    {
        "Titulo": "Histórias multieducativas DISNEY com passatempos e jogos a cores: Os aristogatos",
        "Autor": "The walt disney company",
        "Ano": 1994,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Os Aristogatos.jpg"
    },
    {
        "Titulo": "Histórias multieducativas DISNEY com passatempos e jogos a cores: O livro da selva",
        "Autor": "The walt disney company",
        "Ano": 1994,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Disney O Livro da Selva.jpg"
    },
    {
        "Titulo": "Histórias multieducativas DISNEY com passatempos e jogos a cores: Dumbo",
        "Autor": "The walt disney company",
        "Ano": 1994,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Dumbo.jpg"
    },
    {
        "Titulo": "O pato que veio do frio",
        "Autor": "The walt disney company",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Pato que veio do Frio.jpg"
    },
    {
        "Titulo": "Winnie the pooh: Tudo pode ser divertido",
        "Autor": "Ann Braybrooks",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Tudo Pode ser Divertido.jpg"
    },
    {
        "Titulo": "Os contos do tio patinhas: O alfaiate valentão",
        "Autor": "The walt disney company",
        "Ano": 1996,
        "Categoria": "Infantil",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Alfaiate Valentão.jpg"
    },
    {
        "Titulo": "Pinóquio",
        "Autor": "The walt disney company",
        "Ano": "NaN",
        "Categoria": "Infantil",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Disney Pinóquio.jpg"
    },
    {
        "Titulo": "Aladdin",
        "Autor": "The walt disney company",
        "Ano": 1993,
        "Categoria": "Infantil",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Aladdin.jpg"
    },
    {
        "Titulo": "Flora e Fauna Terreste Invasora na Macaronésia: Top 100 nos Açores, Madeira e Canárias, Flora y Fauna Terrestre Invasora en la Macaronesia: Top 100 en Azores, Madeira y Canarias, Invasive Terrestrial Flora & Fauna of Macaronesia: Top 100 in Azores, Madeira and Canaries",
        "Autor": "Luís Silva, Elizabets Ojeda Land, Juan Luis Rodríguez Luengo",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português, Espanhol e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Flora e Fauna Terrestre Invasora na Macaronésia.jpg"
    },
    {
        "Titulo": "Relict Species: Phylogeography and Conservation Biology",
        "Autor": "Jan Christian Habel, Thorsten Assmann",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Relict Species.jpg"
    },
    {
        "Titulo": "Top 100: Las cien especies amenazadas prioritarias de gestión en la región europea biogeográfica de la Macaronesia, As cem espécies ameaçadas prioritárias em terms de gestão na região europeia biogeográfica da Macaronesia",
        "Autor": "José Luis Martín Esquivel, Manuel Arechavaleta Hernández, Paulo A. V. Borges e Bernardo F. Faria",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português e Espanhol",
        "Material": "Não Plastificado",
        "Imagem": "/livros/TOP 100.jpg"
    },
    {
        "Titulo": "Corvo: Biosphere Reserve Proposal",
        "Autor": "Rui Prieto, Rogério Ferraz, Sara Luís, Susana Pereira e João Carlos Nunes",
        "Ano": ">2006",
        "Categoria": "Ecologia",
        "Sub_Categoria": "Biosfera",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Como Implementar uma Recolha Selectiva.jpg"
    },
    {
        "Titulo": "Corvo: Candidatura a Reserva da Biosfera",
        "Autor": "Rui Prieto, Rogério Ferraz, Sara Luís, Susana Pereira e João Carlos Nunes",
        "Ano": ">2006",
        "Categoria": "Ecologia",
        "Sub_Categoria": "Biosfera",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Corvo Candidatura e Reserva da Biosfera.jpg"
    },
    {
        "Titulo": "Graciosa: Biosphere Reserve Proposal",
        "Autor": "Rui Prieto, Rogério Ferraz, Sara Luís, Susana Pereira, João Carlos Nunes e Victor Rui Dores",
        "Ano": ">2006",
        "Categoria": "Ecologia",
        "Sub_Categoria": "Biosfera",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Graciosa Biosphere Reserve Proposal.jpg"
    },
    {
        "Titulo": "Graciosa: Candidatura a Reserva da Biosfera",
        "Autor": "Rui Prieto, Rogério Ferraz, Sara Luís, Susana Pereira, João Carlos Nunes e Victor Rui Dores",
        "Ano": ">2006",
        "Categoria": "Ecologia",
        "Sub_Categoria": "Biosfera",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Graciosa Candidatura a Reserva da Biosfera.jpg"
    },
    {
        "Titulo": "Flora no litoral dos Açores, Avifauna no litoral dos Açores",
        "Autor": "Gilda Pontes e Jorge Cardoso",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Avifauna no Litoral dos Açores.jpg"
    },
    {
        "Titulo": "Plantas Usadas na Medicina Popular",
        "Autor": "Gilda Pontes e Teófilo Braga",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Plantas Usadas na Medicina Popular.jpg"
    },
    {
        "Titulo": "Pensar como uma Montanha de Aldo Leopold: Um caminho de Educação e Ética Ambiental",
        "Autor": "Emanuel Oliveira Medeiros",
        "Ano": 2008,
        "Categoria": "Ecologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Pensar como uma Montanha de Aldo Leopold Um Caminho de Educação e Ética Ambiental.jpg"
    },
    {
        "Titulo": "Associativismo Ambiental: O caso dos amigos dos Açores",
        "Autor": "Teófilo Braga",
        "Ano": "1984-2007",
        "Categoria": "Ecologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Associativismo Ambiental O Caso dos Amigos dos Açores.jpg"
    },
    {
        "Titulo": "Rapinas Belas e Úteis",
        "Autor": "Amigos dos Açores",
        "Ano": "NaN",
        "Categoria": "Caderno Escolar",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Rapinas Belas e Úteis Caderno Escolar.jpg"
    },
    {
        "Titulo": "Mar e Sociedade: Curiosidades para quem gosta do mar",
        "Autor": "Gonçalo Praça, John Joyce, Niamh Dornan, Tanja Calis e Trevor Purtill",
        "Ano": 2015,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Biologia marinha",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mar e Sociedade.jpg"
    },
    {
        "Titulo": "Briófitos raros dos Açores ",
        "Autor": "Nídia Homem e Rosalina Gabriel",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Briófitos Raros dos Açores & Azorean Rare Bryophytes.jpg"
    },
    {
        "Titulo": "O ordenamento do território nos Açores: política e instrumentos",
        "Autor": "Rui Monteiro, Sílvia Furtado, Melânia Rocha, Mário Freitas, Raquel Medeiros e José Virgílio Cruz",
        "Ano": "NaN",
        "Categoria": "Cultura",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Ordenamento do Território nos Açores política e instrumentos.jpg"
    },
    {
        "Titulo": "Vulcão das sete cidades. Volcano - História Natural - Natural History - Um Guia - A Guide - Açores - Azores",
        "Autor": "Victor Hugo Forjaz, Jorge M. Tavares, Eduardo Brito de Azevedo, João Fontiela, Luis Miguel Almeida, João Pedro Barreiros, Rui B. Elias, Nuno Dias Pereira, Vanessa Rocha, João Madruga, Jorge F. Pinheiro, João F. Sampaio e Pedro R. Medeiros. ",
        "Ano": 2008,
        "Categoria": "Vulcanologia",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Vulcão das Sete Cidades, Volcano.jpg"
    },
    {
        "Titulo": "Our Ocean - Marine Legends, Fairy Tales and Folklore in Ireland",
        "Autor": "Cushla Dromgool-Regan, The Camden Education Trust e Dr Nóirín Burke",
        "Ano": 2019,
        "Categoria": "Infantil",
        "Sub_Categoria": "História",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Our Ocean - Marine Legends.jpg"
    },
    {
        "Titulo": "Gunther Maul: Museu, natureza e ciência",
        "Autor": "Manuel Biscoito, Juan Silva e Carolina Ornelas",
        "Ano": 2018,
        "Categoria": "História",
        "Sub_Categoria": "Museu",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Gunther Maul.jpg"
    },
    {
        "Titulo": "Um Toque Decisivo- A Small but Crucial Push: British Council- 70 anos com Portugal",
        "Autor": "Alison Roberts",
        "Ano": "NaN",
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal com a Britânia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UmToqueDecisivo.jpg"
    },
    {
        "Titulo": "Lisboa, O Descobrimento do Mundo e Fernão de Magalhães",
        "Autor": "José Manuel Garcia",
        "Ano": 2021,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/LisboaODescobrimentoDoMundoEFernaoDeMagalhaes.jpg"
    },
    {
        "Titulo": "Desenhando a Porta do Pacífico - Drawing the Gateway to the Pacific",
        "Autor": "Henrique leitão e José María Moreno Madrid",
        "Ano": "2019-2022",
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DesenhandoAPortaDoPacifico.jpg"
    },
    {
        "Titulo": "Listagem da Fauna (Mollusca e Anthropoda) e Flora (Bryophyta, Pteridophyta e Spermatophyta) Terrestres dos Açores - A List of Terrestrial Fauna (Mollusca and Arthropoda) and Flora (Bryophyta, Pteridophyta and Spermatophyta) from the Azores",
        "Autor": "Paulo A. V. Borges, Regina Cunha, Rosalina Gabriel, António Frias Martins, Luís Silva e Virgílio Vieira",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Listagem da Fauna e Flora Terrestres dos Açores.jpg"
    },
    {
        "Titulo": "Azores: Island to Island",
        "Autor": "José Damião Rodrigues e Ricardo Madruga da Costa",
        "Ano": 2011,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AzoresIslandToIsland.jpg"
    },
    {
        "Titulo": "Açores, São Miguel: A ilha Verde - Azores, São Miguel: The Green Island",
        "Autor": "Publiçor",
        "Ano": "NaN",
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/SaoMiguelAIlhaVerde.jpg"
    },
    {
        "Titulo": "Priolo.",
        "Autor": "Madalena Boto",
        "Ano": "NaN",
        "Categoria": "Ecologia",
        "Sub_Categoria": "DVD",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Priolo. Filme.jpg"
    },
    {
        "Titulo": "Lagoas do Congro e dos Nenúfares: Proposta de recuperação e gestão da Cratera",
        "Autor": "Malgorzata Pietrzak",
        "Ano": 2010,
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Ecologia e Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Lagoas do Congro e dos Nenúfares.jpg"
    },
    {
        "Titulo": "Açores, Terras do Priolo: Leste de São Miguel",
        "Autor": "Azucena de la Cruz, Carlos Pereira, Cláudia Furtado, Eva Lima, Gabinete de Apoio ao Turismo de Natureza e em Espaço Rural, Natália Melo, Câmara Municipal de Nordeste e Câmera Municipal da Povoação",
        "Ano": 2013,
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Ecologia e Hist. Cultural dos Açores",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Açores, Terras do Priolo - Azores, Lands of Priolo",
        "Autor": "Azucena de la Cruz, Carlos Pereira, Cláudia Furtado, Eva Lima, Gabinete de Apoio ao Turismo de Natureza e em Espaço Rural, Natália Melo, Câmara Municipal de Nordeste e Câmera Municipal da Povoação",
        "Ano": 2011,
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Ecologia e Hist. Cultural dos Açores",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",

    },
    {
        "Titulo": "Flora Vascular dos Açores, Prioridades em Conservação - Azorean Vascular Flora Priorities in Conservation",
        "Autor": "Luís Silva, Mónica Cristina Martins, Graciete Belo Maciel e Mónica Moura",
        "Ano": ">2007",
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Flora Vascular dos Açores Prioridades em Conservação.jpg"
    },
    {
        "Titulo": "O Priolo e a floresta natural de altitude",
        "Autor": "Jaime Albino Ramos",
        "Ano": ">2003",
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O Priolo e a Floresta Natural de Altitude.jpg"
    },
    {
        "Titulo": "Guia do Consumidor do Pescado dos Açores - Consumer's Guide to Azorean Seafood",
        "Autor": "Les Gallagher, Filipe Porteiro, Carla Dâmaso e Ricardo Serrão Santos",
        "Ano": 2012,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Guia do Consumidor do Pescado dos Açores.jpg"
    },
    {
        "Titulo": "Mistério do Vulcão da Urzelina da Ilha de São Jorge dos Açores",
        "Autor": "Victor Hugo Forjaz, Zilda T. M. França e Luísa Pinto Ribeiro",
        "Ano": 1808,
        "Categoria": "Geologia",
        "Sub_Categoria": "Vulcanologia e Geotérmica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mistério do Vulcão da Urzelina da Ilha de São Jorge dos Açores.jpg"
    },
    {
        "Titulo": "Lagoas e Lagoeiros do Concelho de Ponta Delgada",
        "Autor": "J. P. Constância, T. J. Braga, J. C. Nunes, E. Machado e L. Silva",
        "Ano": 2001,
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Lagoas e Lagoeiros do Concelho de Ponta Delgada.jpg"
    },
    {
        "Titulo": "Etnobotânica: Plantas Bravias, Comestíveis, Condimentares e Medicinais",
        "Autor": "José Alves Ribeiro, António Manuel Monteiro e Maria de Lurdes Fonseca da Silva",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Etnobotânica.jpg"
    },
    {
        "Titulo": "Estudos de Geotermia e Geofísica e outros Escritos",
        "Autor": "Júlio Quintino",
        "Ano": 2001,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geotérmica e Geofísica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Estudos de Geotermia e Geofísica e outros Escritos.jpg"
    },
    {
        "Titulo": "Natal Verde: 30 Anos de Postais de Jorge Paiva 1990-2019",
        "Autor": "Paulo Renato Trincão, Lídia Pereira e Ana Rita Paiva",
        "Ano": 2019,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Natal Verde.jpg"
    },
    {
        "Titulo": "Arquipelago: Life and Marine Sciences Nº 36",
        "Autor": "Helen Rost Martins e Paula C.M. Lourinho",
        "Ano": 2019,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Arquipelago Life and Marine Sciences.jpg"
    },
    {
        "Titulo": "Açores: O império dos Fósseis",
        "Autor": "Sérgio Ávila e Pedro Monteiro",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "AçoresoImpériodosFósseis.jpg"
    },
    {
        "Titulo": "As Luzes do Príncipe",
        "Autor": "João Ramalho-Santos e Rui Tavares",
        "Ano": 2019,
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Banda Desenhada",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/As Luzes do Príncipe.jpg"
    },
    {
        "Titulo": "Migrações de Aves",
        "Autor": "Amigos dos Açores",
        "Ano": 2001,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Migrações de Aves.jpg"
    },
    {
        "Titulo": "As Plantas Invasoras: Uma história contada pela Faia-da-terra",
        "Autor": "Luis Filipe Dias Silva",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/As Plantas Invasoras.jpg"
    },
    {
        "Titulo": "Parque Natural Regional da Plataforma Costeira das Lajes do Pico - Proposta de Implementação",
        "Autor": "Sérgio P. Ávila, Rui Bento Elias e Jorge R. B. Medeiros",
        "Ano": 2000,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Parque Natural Regional da Plataforma Costeira das Lajes do Pico.jpg"
    },
    {
        "Titulo": "O género Puffinus nas ilhas dos Açores: Considerações sobre as espécies atlânticas do género Puffinus",
        "Autor": "António Mello Machado e Padre Ernesto Ferreira",
        "Ano": 1996,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/O género Puffinus nas ilhas dos Açores.jpg"
    },
    {
        "Titulo": "Áreas Protegidas e Turismo-Conflito Intransponível?",
        "Autor": "Fernando Santos Pessoa",
        "Ano": 2005,
        "Categoria": "Turismo",
        "Sub_Categoria": "Turismo Rural",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AreasProtegidaseTurismoConflitoIntransponível.jpg"
    },
    {
        "Titulo": "Proposta de Intervenção Museológica na Gruta do Carvão, Ilha de S. Miguel",
        "Autor": "J. P. Constância, T. Braga, J. C. Nunes",
        "Ano": 1997,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geotérmica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Proposta de Intervenção Museológica na Gruta do Carvão, Ilha de S. Miguel.jpg"
    },
    {
        "Titulo": "Marque encontro com a natureza",
        "Autor": "Eco-Seia",
        "Ano": "NaN",
        "Categoria": "Biologia e História",
        "Sub_Categoria": "Panfleto",
        "Linguagem": "Português",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "A Gestão Ambiental no Sector Hoteleiro",
        "Autor": "Susana Lima",
        "Ano": 2008,
        "Categoria": "Turismo",
        "Sub_Categoria": "Turismo Rural",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Gestão Ambiental no Sector Hoteleiro.jpg"
    },
    {
        "Titulo": "Borboletas dos Açores: Papilionoidea e Sphingoidea",
        "Autor": "Virgílio Vieira",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Borboletas dos Açores.jpg"
    },
    {
        "Titulo": "Térmitas dos Açores",
        "Autor": "Paulo Borges e Timothy Miles",
        "Ano": 2007,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Térmicas dos Açores.jpg"
    },
    {
        "Titulo": "Guia do Munícipe Ambientalista",
        "Autor": "Comissão Permanente do GEOTA",
        "Ano": 1994,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Guia do Municipe Ambientalista.jpg"
    },
    {
        "Titulo": "Como Implementar uma Recolha Selectiva?",
        "Autor": "Ana Ramos, Ana Teresa Calmeiro, Gonçalo Almeida e Susana Serra",
        "Ano": 2004,
        "Categoria": "Reciclagem",
        "Sub_Categoria":"NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Como Implementar uma Recolha Selectiva.jpg"
    },
    {
        "Titulo": "Cise-Seia: Centro de Interpretação da Serra da Estrela",
        "Autor": "Cise-Seia",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Panfleto",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Cise Seia, Centro de Interpretação da Serra da Estrela.jpg"
    },
    {
        "Titulo": "Atuns, Bonitos e Cavalas dos Açores: Nómadas Atlânticos",
        "Autor": "Fernando Correia e Nuno Farinha",
        "Ano": 2006,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Atuns, Bonitos e Cavalas dos Açores.jpg"
    },
    {
        "Titulo": "Turismo e Desenvolvimento Sustentável 1",
        "Autor": "Hélder Careto e Susana Lima",
        "Ano": 2006,
        "Categoria": "Turismo",
        "Sub_Categoria": "Turismo Rural",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Turismo e Desenvolvimento Sustentável 1.jpg"
    },
    {
        "Titulo": "Turismo e Desenvolvimento Sustentável 2",
        "Autor": "Hélder Careto e Susana Lima",
        "Ano": 2007,
        "Categoria": "Turismo",
        "Sub_Categoria": "Turismo Rural",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Turismo e Desenvolvimento Sustentável 2.jpg"
    },
    {
        "Titulo": "Gestão do Litoral e Cidadania Ambiental",
        "Autor": "Lurdes Soares",
        "Ano": 2008,
        "Categoria": "Cidadania",
        "Sub_Categoria": "Metodologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Gestão do Litoral e Cidadania Ambiental.jpg"
    },
    {
        "Titulo": "Mística e Nuvens do Vulcão do Pico",
        "Autor": "Victor Hugo Forjaz, Zilda T. M. França, Lurdes Bettencourt Oliveira, João José Fernandes e Urbano Bettencourt",
        "Ano": 2006,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geotérmica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mística e Nuvens do Vulcão do Pico.jpg"
    },
    {
        "Titulo": "Rondando a Ilha Verde: S. Miguel - Açores",
        "Autor": "Paula Simões e Carlos Garcia",
        "Ano": "NaN",
        "Categoria": "História",
        "Sub_Categoria": "Album de Fotos",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Rondando a Ilha Verde.jpg"
    },
    {
        "Titulo": "Museu Carlos Machado: Memória do Convento",
        "Autor": "Ana Fernandes e Catarina Melo Antunes",
        "Ano": 2016,
        "Categoria": "História",
        "Sub_Categoria": "Museu",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/MemoriaDoConvento.jpg"
    },
    {
        "Titulo": "Evolucionismo nos Açores e Outros Estudos",
        "Autor": "Luís M. Arruda",
        "Ano": 2015,
        "Categoria": "Biologia",
        "Sub_Categoria": "Evolucionismo",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Evolucionismo nos Açores e outros Estudos.jpg"
    },
    {
        "Titulo": "UAciência: Ciencias da Engenharia, Exatas, Saúde e Biotecnologia, e Sociais e Humanas 2012- 2019",
        "Autor": "Armindo Rodrigues e Luís Mendes Gomes",
        "Ano": 2021,
        "Categoria": "Tecnologia",
        "Sub_Categoria": "Biotecnologia e Engenharia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UAciência- Ciências da Engenharia, Exatas, Saúde e Biotécnologia, e Sociais e Humanas.jpg"
    },
    {
        "Titulo": "UAciência: Ciencias Naturais e do Ambiente 2012- 2019",
        "Autor": "Armindo Rodrigues e Luís Mendes Gomes",
        "Ano": 2020,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/UAciência, Ciências Naturais e do Ambiente.jpg"
    },
    {
        "Titulo": "Fogo Frio: O Vulcão dos Capelinhos",
        "Autor": "Duarte Belo",
        "Ano": 2008,
        "Categoria": "Geologia",
        "Sub_Categoria": "Vulcanologia, Sismologia e Geotérmica",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Fogo Frio O vulcão dos Capelinhos.jpg"
    },
    {
        "Titulo": "Arquipelago: Life and Marine Sciences, Supplement 11",
        "Autor": "Helen Rost Martins e Paula C.M. Lourinho",
        "Ano": 2020,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Arquipelago Life and Marine Sciences Supplement 11.jpg"
    },
    {
        "Titulo": "Catálogo das Plantas Vasculares dos Açores",
        "Autor": "Ruy Telles Palhinha",
        "Ano": 1966,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Catálogo das Plantas Vasculares dos Açores.jpg"
    },
    {
        "Titulo": "Briófitos Raros dos Açores & Azorean Rare Bryophytes",
        "Autor": "Nídia Homem & Rosalina Gabriel",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado"
    },
    {
        "Titulo": "Ecologia Costeira dos Açores",
        "Autor": "Brian Morton, Joseph C. Britton, António M. de Frias Martins",
        "Ano": 1998,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Ecologia Costeira dos Açores.jpg"
    },
    {
        "Titulo": "A Casa da Luz: Património Industrial da Senhora do Desterro, Serra da Estrela",
        "Autor": "João Orlindo Marques",
        "Ano": 2011,
        "Categoria": "História",
        "Sub_Categoria": "Hist. Cultural de Portugal",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ACasaDaLuz.jpg"
    },
    {
        "Titulo": "Listagem dos fungos, flora e fauna terrestres dos arquipélagos da Madeira e Selvagens - A list of the terrestrial fungi, flora and fauna of Madeira and Selvagens archipelagos",
        "Autor": "Paulo A. V. Borges, Cristina Abreu, António M. Franquinho Aguiar, Palmira Carvalho, Roberto Jardim, Ireneia Melo, Paulo Oliveira, Cicília Sérgio, Artur R. M. Serrano e Paulo Vieira",
        "Ano": 2008,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Listagem dos fungos, flora e fauna terrestres dos arquipélagos da Madeira e Selvagens.jpg"
    },
    {
        "Titulo": "Albert I do Mónaco, Afonso Chaves e a Meteorologia dos Açores",
        "Autor": "Conceição Tavares",
        "Ano": 2009,
        "Categoria": "História e Geologia",
        "Sub_Categoria": "Meteorologia e Hist. Cultural de Mónaco",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AlbertIDoMonacoAfonsoChavesEAMeterologiaNosAcores.jpg"
    },
    {
        "Titulo": "Os fósseis de Santa Maria (Açores)",
        "Autor": "Sérgio Ávila, Ana Rebelo, André Medeiros, Carlos Melo, Cidalina Gomes, Leila Bagaço, Patrícia Madeira, Paulo Amaral Borges, Pedro Monteiro, Ricardo Cordeiro, Ricardo Meireles e Ricardo Ramalho",
        "Ano": 2010,
        "Categoria": "Geologia",
        "Sub_Categoria": "Paleontologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Os fósseis de Santa Maria (Açores).jpg"
    },
    {
        "Titulo": "Monte Brasil: Percursos de Interpretação Ambiental",
        "Autor": "Lurdes Nunes",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Monte Brasil.jpg"
    },
    {
        "Titulo": "Guerra do Ultramar: Caminhando pela Memória e Pela História",
        "Autor": "Luis M. Arruda",
        "Ano": 2019,
        "Categoria": "História",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GuerraDoUltramar.jpg"
    },
    {
        "Titulo": "Dragoeiros do Museu do Vinho",
        "Autor": "Emanuel Félix Borges da Silva, João Paulo Constância, Manuel Alegre",
        "Ano": 2005,
        "Categoria": "Cultura",
        "Sub_Categoria": "Album de Fotos",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Dragoeiros do Museu do Vinho.jpg"
    },
    {
        "Titulo": "Visões Subterrâneas: Fotografias de Jorge Góis",
        "Autor": "João Paulo Constância, Paulo Barcelos, Paulo Borges, Fernando Pereira, João Carlos Nunes e Paulino Costa",
        "Ano": "2007-2008",
        "Categoria": "Geologia",
        "Sub_Categoria": "Album de Fotos",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Visões Subterrâneas.jpg"
    },
    {
        "Titulo": "Caminhos de Ciência",
        "Autor": "António Piedade",
        "Ano": 2011,
        "Categoria": "Ciências da Natureza",
        "Sub_Categoria": "Microbiologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Caminhos de Ciência.jpg"
    },
    {
        "Titulo": "Mauro e Emília: Os nossos cágados estão em perigo. Vamos ajudá-los! - Mauro y Emília: Nuestras tortugas están en peligro. iVamos a ayudarlas!",
        "Autor": "Ana Mafalda Alves",
        "Ano": 2013,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Mauro e Emília.jpg"
    },
    {
        "Titulo": "Alfonso Olalla and His Family: The ornithological Exploration of Amazonian Peru",
        "Autor": "R, Haven Wiley",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Alfonso Olalla and His Family.jpg"
    },
    {
        "Titulo": "Type Specimens of Birds in the American Museum of Natural History: Part 8. Passeriformes",
        "Autor": "Mary Lecroy",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Type Specimens Of Birds in the American Museum of Natural History.jpg"
    },
    {
        "Titulo": "The Basal Penguin (Aves: Spenisciformes): Perudyptes Devriesi and a Phylogenetic Evaluation of the Penguin Fossil Record",
        "Autor": "Daniel T. Ksepka e Julia A. Clarke",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/The Basal Penguin.jpg"
    },
    {
        "Titulo": "Pseudotoothed Birds (Aves, Odontopterygiformes) from the Early Tertiary of Morocco",
        "Autor": "Estelle Bourdon, Mbarek Amaghzaz e Baadi Bouya",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia e Paleontologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/American Museum Novitates.jpg"
    },
    {
        "Titulo": "As Abelhas dos Açores",
        "Autor": "Casermel",
        "Ano": 2009,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/As Abelhas dos Açores.jpg"
    },
    {
        "Titulo": "Genealogias de S. Miguel e Santa Maria Volume 1º",
        "Autor": "Rodrigo Rodrigues",
        "Ano": 1998,
        "Categoria": "História",
        "Sub_Categoria": "Geneologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/GenealogiasDeSMigueleSantaMariaVolume1.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 75, Number 3",
        "Autor": "A. Serrano, F. Sánchez, A. Punzón, F. Velasco, I. Olaso, D. Jacinto, T. Cruz, T. Silva, J. J. Castro, H. El Habouz, L.Recasens, S. Kifani, A. Moukrin, A. Bouhaimi, S. El Ayoubi, C. San Vicente, J.E. Cartes, A. Punzón, A. Serrano, J. Castro, E. Abad, J. Gil, P. Pereda, M.S. Carvalho, R. Desqueyroux-Faúndez, E. Hajdu, M. Caric, N. Jasprica, M. Calic, M. Batistic, S. Juan, M. Demestre, P. Sánchez A. Asaro,  J.C. del Valle, A.A. López Mañanes, E. Macpherson, A. García-Olivares, J.L. de Pablos e R. Madrigal, R. Rosas-Luis, R. Tafur-Jimenez, A..R. Alegre-Norza, P.R. Castillo-Valderrama, R.M. Cornejo-Urbina, C.A. Salinas-Zavala, VC. Sarmento, A.F.S. Barreto and P.J.P. Santos, J.C.  Báez, J.J. Bellido, F. Ferri-Yáñez, J.J. Castillo, J.J. Martín, J.L. Mons, D. Romero,",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 75 Number 3.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 75, Number 2",
        "Autor": "R. Real, A. Nebra, N. Caiola and C. Ibáñez, F. Uiblein,  P.C. Heemstra, A. Orfila, S. Balle and G. Simarro S.  Somarakis, S. Isari and A. Machias.",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 75 Number 2.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 75, Number 1",
        "Autor": "A. Salman, A. Pisera, J. Vacelet, H. Lundbye, H. Soo Rho and M.V. Sorensen, M. Delgado,  JL. Gairín, R. Carbó, C. Aguilera, J. Terrados, FJ. Medina-Pons, E. Vidal-Vijande, A. Pascual, Bernard Barnier, J.-M. Molines and J. Tintoré, AM. Faria, T. Muha, E. Morote and M.A. Chícharo, J.M. Aguilar-Camacho, S.I. Salazar-Valejo, V. Moschino, L. Chicharo, M.G. Marin, S. Pulina, B.M. Padedda, N. Sechi e A. Lugliè, E. Arce, G. Alcaraz, G. Guerao, K.B. Andree, C. Froglia, C.G. Simeó, G. Rotllant, M.O. Freitas, R.L. de Moura, R.B. Francini-Filho and C.V. Minte-Vera, Jr. J. A. Morris, C.V. Sullivan e  J.J. Govoni, R.P.  Vasconcelos, P. Reis-Santos, A. Maia, M. Ruano, M.J. Costa, H.N. Cabral, A. Bonfitto,  B. Dell' angelo, F. Evangelisti e B. Sabelli.",
        "Ano": 2011,
        "Categoria": "biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 75 Number 1.jpg"

    },
    {
        "Titulo": "Scientia Marina: Volume 74S1, Supplement 1",
        "Autor": "Julián Blasco e Jesús M.Forja",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 74S1 Supplement 1.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 74, Number 4",
        "Autor": "MP. Olivar, MA. Bitner, P. Carpentieri, T. Cantarelli, F. Colloca, A. Criscoli, G. Ardizzone, R. Xavier, FP. Lima, AM. Santos, M. La Mesa, G. Scarcella, F. Grati, G. Fabi, B. Liu, X. Chen, H. Lu, Y. Chen, W. Qian, S. Vila, M. Sabat, M. Muñoz, M. Casadevall, A. Lourido,  J. Moreira, J.S. Troncoso, D. Golani, B. Appelbaum-Golani, J. Fontes, P. Afonso, R.S. Santos, J.E. Caselle, R.M.A. Figueira, R.S. Absalão, JM. Mercado, T. Ramírez, D. Cortés, E. Liger, F.O. Düzbastılar, C. Aydın, G. Metin. A. Lök, A. Ulaş. A. Ozgül, B. Gül, C. Metin, H. Özbilgin, T. Şensurat,  A. Tokaç, E. Morsan, P. Zaidman, M. Ocampo-Reinaldo, N. Ciocco, I. Winfield, M. Ortiz, Y. Zhang, J. Dong, J. Ling, Y. Wang, S. Zhang, A.  Abella, M. Ria, C. Mancusi, V.M. Tuset, S. Piretti, A. Lombarte e J.A. González.",
        "Ano": 2010,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 74 Number 4.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 69, Number 3",
        "Autor": "Pere Abelló",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 69 Number 3.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 69, Supplement 1",
        "Autor": "Pere Abelló e Celia Marrasé",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 69 Supplement 1.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 68, Number 1",
        "Autor": "Pere Abelló",
        "Ano": 2004,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 68 Number 1.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 66, Number 4",
        "Autor": "Pere Abelló",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 66 Number 4.jpg"
    },
    {
        "Titulo": "Scientia Marina: Volume 66, Supplement 2",
        "Autor": "Pere Abelló, Jacques A. Bertrand, Luis Gil de Sola, Costas Papaconstantinou, Giulio Relini e Arnauld Souplet",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Biologia Marinha",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Scientia Marina Volume 66 Supplement 2.jpg"
    },
    {
        "Titulo": "Viagens e diálogos epistolares na construção científica do mundo atlântico: Albert I do Mónaco, Afonso Chaves, Meteorologia nos Açores.",
        "Autor": "Maria da Conceição da Silva Tavares",
        "Ano": 2007,
        "Categoria": "História e Geologia",
        "Sub_Categoria": "Meteorologia e Hist. Cultural de Mónaco",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ViagensEDialogosEpistolaresNaConstrucaoCientificaDoMundoAtlantido.jpg"
    },
    {
        "Titulo": "Bulletin de L'Institut Royal Des Sciences Naturelles De Belgique - Bulletin Van Het Koninklijk, Belgisch Instituut Voor Natuurwetenschappen",
        "Autor": "Leon BAERT",
        "Ano": 2010,
        "Categoria": "Biologia e Entomologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Espanhol e Alemão",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bulletin de L'Institut Royal Des Sciences Naturelles de Belgique.jpg"
    },
    {
        "Titulo": "A Castanha na Mesa de Bragança",
        "Autor": "Presidente da Câmara Municipal de Bragança",
        "Ano": 2015,
        "Categoria": "Receitas",
        "Sub_Categoria": "NaN",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/A Castanha na Mesa de Bragança.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. XI - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2023,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Exploring the marine meiofauna of the Azores - Suplemento 11",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2019,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento11.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. XI - Fasc.III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2021,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: The marine fauna and flora of the Açores",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento10.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Eleventh international symposium of neuropterology",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento9.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Supplemento 8",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2013,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento8.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Supplemento 7",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2011,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento7.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Supplemento 5",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2007,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento5.jpg"
    },
    {
        "Titulo": "Açoreana: The Marine Fauna and Flora of the Azores - Second International Workshop",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSuplemento1995.jpg"
    },
    {
        "Titulo": "Açoreana: Centenaire de la Derniere Campagne Oceanographique du Prince Albert de Monaco aux Açores à bord de L'Hirondelle",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1988,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento1992.jpg"
    },
    {
        "Titulo": "Açoreana: The Marine Fauna and Flora of the Azores - First International Workshop",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1990,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosSupplemento1990.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. XI - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2018,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. XI - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2017,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. X - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2015,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos: Vol. X - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2012,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. X - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2005,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. X - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2003,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolXFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. IX - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2002,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolIXFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. IX - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2001,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolIXFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. IX - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 2000,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolIXFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Revista de Estudos Açoreanos:  Vol. IX - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1999,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaRevistaDeEstudosAcoreanosVolIXFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VIII - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1998,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VIII - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1997,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VIII - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1996,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VIII - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VII - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1993,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VII - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1992,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VII - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1991,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VII - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1989,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vo. VI - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1987,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VI - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VI - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. VI - Fasc.I ",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1987,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. V - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. V - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. V - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1995,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. V - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1981,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolVFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. IV - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1949,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIVFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. IV - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1948,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português, Inglês e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIVFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. IV - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1947,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIVFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. IV - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1946,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Francês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIVFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. III - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1945,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. III - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1944,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. III - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1943,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. III - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1942,
        "Categoria": "Geologia e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. II - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1941,
        "Categoria": "Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. II - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1940,
        "Categoria": "Cultura e Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. II - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1939,
        "Categoria": "Cultura e Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. II - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1938,
        "Categoria": "Cultura e Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIIFascI.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. I - Fasc. IV",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1937,
        "Categoria": "Cultura e Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIFascIV.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. I - Fasc. III",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1936,
        "Categoria": "Cultura e Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIFascIII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. I - Fasc. II",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1935,
        "Categoria": "Cultura e Geologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIFascII.jpg"
    },
    {
        "Titulo": "Açoreana: Vol. I - Fasc. I",
        "Autor": "Sociedade Afonso Chaves e Associação de Estudos Açoreanos",
        "Ano": 1934,
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AçoreanaVolIFascI.jpg"
    },
    {
        "Titulo": "Haja Luz! Uma história da química através de tudo",
        "Autor": "Jorge Calado",
        "Ano": "NaN",
        "Categoria": "Química",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/HajaLuz.jpg"
    },
    {
        "Titulo": "Arquipelago: Life Marine Sciences",
        "Autor": "Helen Rost Martins e José Nuno Gomes-Pereira",
        "Ano": 2017,
        "Categoria": "Biologia",
        "Sub_Categoria": "Revista",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ArquipelagoLifeAndMarineSciences.jpg"
    },
    {
        "Titulo": "Bragança, um território para conquistar",
        "Autor": "NaN",
        "Ano": "NaN",
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Bragança.jpg"
    },
    {
        "Titulo": "Paisagem da cultura da vinha da ilha do Pico ",
        "Autor": "Amanda Matias Tavares, Manuel Paulino Costa, Maria José Bettencourt, Nuno Pacheco, Ângela Garcia, Dália Leal, Ivone Machado, Jorge Honório,  Mónica Silva Goulart, Nuno Ribeiro Lopes, Ruben Menezes",
        "Ano": 2004,
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português e Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Pico.jpg"
    },
    {
        "Titulo": "Azores a natural portrait",
        "Autor": "Clara Gaspar, Paulo A.V Borges, Pedro Cardoso, Rosalina Gabriel, Isabel R. Amorim, António Frias Martins, Francisco Maduro-Dias, João Mora Porteiro, Luís Silva e Fernando Pereira",
        "Ano": 2009,
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/AzoresANaturalPortrait.jpg"
    },
    {
        "Titulo": "Insect: Discover the busy and intriguing world of insects - their structure, life-history, and fascinating variety",
        "Autor": "Laurence Mound",
        "Ano": 1990,
        "Categoria": "Biologia",
        "Sub_Categoria": "Entomologia",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/Insect.jpg"
    },
    {
        "Titulo": "DragonFlies",
        "Autor": "Peter Van Dokkum",
        "Ano": 2015,
        "Categoria": "Biologia",
        "Sub_Categoria": "Album de Fotos",
        "Linguagem": "Inglês",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DragonFlies.jpg"
    },
    {
        "Titulo": "Vulcão dos Capelinhos memórias 1957-2007",
        "Autor": "Victor Hugo Forjaz",
        "Ano": 2007,
        "Categoria": "Cultura",
        "Sub_Categoria": "Revista",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/VulcaoDosCapelinhos.jpg"
    },
    {
        "Titulo": "Na Rota dos Vulcões da Ilha do Faial",
        "Autor": "Victor Hugo Forjaz",
        "Ano": 2008,
        "Categoria": "Geologia",
        "Sub_Categoria": "Geomorfologia, Vulcanologia e Petrologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/NaRotadosVulcoesDaIlhaDoFaial.jpg"
    },
    {
        "Titulo": "A Diversidade na Orla Costeira: Da Caloura a Ponta Garça",
        "Autor": "Ana Neto, António Félix Rodrigues, Luís Silva, Luísa Magalhães, Jorge M. Tavares, Nuno Álvaro, Azucena de la Cruz, Eduardo Furtado e João Maçoroco",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ADiversidadeNaOrlaCosteiraDaCalouraAPontaGarca.jpg"
    },
    {
        "Titulo": "A Diversidade na Orla Costeira: São Roque a Santa Cruz da Lagoa",
        "Autor": "Luísa Magalhães, Ana Neto, José Pedro Medeiros, Marisa Vieira, Hugo Marques, João Manuel Brum, João Alves, Fernando Abreu, João Paim, António Félix Rodrigues, Carlos Guilherme Riley, Roberto Medeiros",
        "Ano": "NaN",
        "Categoria": "Biologia e Geologia",
        "Sub_Categoria": "Geobiológica e Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/DiversidadeNaOrlaCosteiraSaoRoqueASantaCruzDaLagoa.jpg"
    },
    {
        "Titulo": "A Diversidade na Orla Costeira: Da Ribeira Quente ao Faial da Terra",
        "Autor": "Ana Neto, Maria João Pereira, Marlene Assis, Nuno Álvaro, Jorge Tavares, Clube Naval de Vila Franca do Campo",
        "Ano": "NaN",
        "Categoria": "Biologia",
        "Sub_Categoria": "Ecologia",
        "Linguagem": "Português",
        "Material": "Não Plastificado",
        "Imagem": "/livros/ADiversidadeNaOrlaCosteiraDaRibeiraQuenteAoFaialDaTerra.jpg"
    },
]

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_items = items
    if request.method == 'POST':
        Titulo_filter = request.form.get('Titulo')
        Autor_filter = request.form.get('Autor')
        Categoria_filter = request.form.get('Categoria')
        Sub_Categoria_filter = request.form.get('Sub_Categoria')
        Linguagem_filter = request.form.get('Linguagem')
        Ano_filter = request.form.get('Ano')

        if Titulo_filter:
            filtered_items = [item for item in filtered_items if Titulo_filter.lower() in item['Titulo'].lower()]
        if Autor_filter:
            filtered_items = [item for item in filtered_items if Autor_filter.lower() in item['Autor'].lower()]
        if Categoria_filter:
            filtered_items = [item for item in filtered_items if Categoria_filter.lower() in item['Categoria'].lower()]
        if Sub_Categoria_filter:
            filtered_items = [item for item in filtered_items if Sub_Categoria_filter.lower() in item['Sub_Categoria'].lower()]
        if Linguagem_filter:
            filtered_items = [item for item in filtered_items if Linguagem_filter.lower() in item['Linguagem'].lower()]
        if Ano_filter:
            try:
                Ano_filter = int(Ano_filter)
                filtered_items = [item for item in filtered_items if item['Ano'] == Ano_filter]
            except ValueError:
                pass


    return render_template('index.html', items=filtered_items)

@app.route('/livro/<titulo>')
def livro_detalhes(titulo):
    livro = next((item for item in items if item['Titulo'] == titulo), None)
    if livro:
        return render_template('livro_detalhes.html', livro=livro)
    else:
        return "Livro não encontrado", 404