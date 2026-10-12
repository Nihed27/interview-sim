from pypdf import PdfReader


reader = PdfReader("../data/cv.pdf")


text = ""
for page in reader.pages:
    text += page.extract_text()


# Les titres de sections de mon CV
SECTIONS = [
    "Profil",
    "Formation",
    "Expériences professionnelles",
    "Projets",
    "Compétences techniques",
    "Certifications et activités",
]

lines = text.split("\n")   

sections = {}             
current = None             

for line in lines:
    line = line.strip()

    if line == "":                 
        continue

    if line in SECTIONS:           
        current = line
        sections[current] = []
    elif current is not None:     
        sections[current].append(line)


chunks = []   

for name, content in sections.items():

    if name in ["Expériences professionnelles", "Projets"]:
        item = []                                   
        for line in content:
            if line.startswith("•"):                
                item.append(line)
            else:                                   
                if item:                            
                    chunks.append(name + " : " + " ".join(item))  
                item = [line]                      
        if item:                                    
            chunks.append(name + " : " + " ".join(item))

    else:                                          
        chunks.append(name + " : " + " ".join(content))


print("Nombre de chunks :", len(chunks))
for i, chunk in enumerate(chunks):
    print(i, "→", chunk[:90])