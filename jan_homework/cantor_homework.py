from IPython.display import display
import requests
import json
import ipywidgets as widgets

def utworzTabliceDostepnychWalut():
    
    listaWalut = []
    
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/?format=json')
    
    json_var = r.content
    json_obj = json.loads(json_var)
    
    for i in range(33):
        listaWalut.append ( json_obj[0]["rates"][i]['code'])
        
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/b/?format=json')
    
    json_var = r.content
    json_obj = json.loads(json_var)
    
    for i in range(116):
        listaWalut.append(json_obj[0]["rates"][i]['code'])
    
    
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/c/?format=json')
    
    json_var = r.content
    json_obj = json.loads(json_var)
    
    for i in range(13):
        powtorzenie = False
        kod1 = json_obj[0]["rates"][i]["code"]
        for j in range(149):
            kod2 = listaWalut[j]
            if(kod1 == kod2):
                powtorzenie = True
        if(powtorzenie == False):
            listaWalut.append(json_obj[0]["rates"][i]['code'])
    
    listaWalut.sort()
    
    return listaWalut

def sprzedajWalute(waluta, kwota):
    r = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/?format=json")
    
    json_var = r.content
    json_obj = json.loads(json_var)
    
    znalezionoWalute = 0;
    
    for i in range(33):
        if(waluta == json_obj[0]["rates"][i]["code"]):
            znalezionoWalute = 1
            tabela = "a"
            break
        
        
    if(znalezionoWalute == 0):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/b/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(116):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                znalezionoWalute = 1
                tabela = "b"
                break
                
    if(znalezionoWalute == 0):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(13):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                znalezionoWalute = 1
                tabela = "c"
                break
                
                
                
    if(znalezionoWalute == 1):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(13):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                kurs = json_obj[0]["rates"][i]["bid"]
                cena = kwota * kurs
                return (  round(cena, 2)  )
        
        r = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/{tabela}/{waluta}/")
        json_var = r.content
        json_obj = json.loads(json_var)
        kurs = json_obj["rates"][0]["mid"]
        cena = kwota * kurs
        return (  round(cena, 2)  )
    
    else:
        return ("Brak podanej waluty")
    

def kupWalute(waluta, kwota):
    
    r = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/?format=json")
    
    json_var = r.content
    json_obj = json.loads(json_var)
    
    znalezionoWalute = 0;
    
    for i in range(33):
        if(waluta == json_obj[0]["rates"][i]["code"]):
            znalezionoWalute = 1
            tabela = "a"
            break
        
        
    if(znalezionoWalute == 0):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/b/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(116):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                znalezionoWalute = 1
                tabela = "b"
                break
                
    if(znalezionoWalute == 0):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(13):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                znalezionoWalute = 1
                tabela = "c"
                break
                
    if(znalezionoWalute == 1):
        r = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/?format=json")
        json_var = r.content
        json_obj = json.loads(json_var)
        
        for i in range(13):
            if(waluta == json_obj[0]["rates"][i]["code"]):
                kurs = json_obj[0]["rates"][i]["ask"]
                cena = kwota * kurs
                return (  round(cena, 2)  )
        
        r = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/{tabela}/{waluta}/")
        json_var = r.content
        json_obj = json.loads(json_var)
        kurs = json_obj["rates"][0]["mid"]
        cena = kwota * kurs
        return (  round(cena, 2)  )
    
    else:
        return ("Brak podanej waluty")
    
        
output = widgets.Output()
       
zakupy = widgets.RadioButtons(
    options=['Zakup waluty', 'Sprzedaż waluty'],
#    value='pineapple', # Defaults to 'pineapple'
#    layout={'width': 'max-content'}, # If the items' names are long
    description='Zakup czy sprzedaż:',
    disabled=False
)

waluty = widgets.Dropdown(
    options= utworzTabliceDostepnychWalut(),
    description= "Wybierz",
    disabled=False,
)

kwota = widgets.FloatText(
    value=7.5,
    description='Kwota:',
    disabled=False
)


oblicz = widgets.Button(
    description='Oblicz',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)


def wykonaj_na_klik(b):
    waluta = waluty.value
    cena = kwota.value
    wybranie = zakupy.value
    
    cena = round(cena, 2)
    
    if(wybranie == 'Zakup waluty'):
        with output:
            print (kupWalute(waluta, cena))
    else:
        with output:
            print (sprzedajWalute(waluta, cena))
            

def wyczysc(b):
    output.clear_output()


display(zakupy, waluty, kwota, oblicz, output)

oblicz.on_click(wyczysc)

oblicz.on_click(wykonaj_na_klik)


    
    
