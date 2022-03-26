import random
import csv
import os
import time

#FUNKCIJAS*********************************************************************************************

def noteikumi():
  print('Spēles noteikumi:\n\t* Spēlē norisinās ceļojums ar elektroauto no Valmieras Valsts ģimnāzijas līdz Liepājas karostai.\n\t* Brauciena laikā tev ir obligāti jāapmeklē 10 kontrolpunkti ieskaitot sākumpunktu un galapunktu.\n\t* Attālumus starp punktiem varēsi trast tabulā, kuru redzēsi katru reizi, kad vajadzēs izvēlēties nākamo galapunktu. \n\t* Elektroauto labos apstākļos var nobraukt 140 km, bet sliktos - 80km.\n\t* Ievēro to, ka laikapstākļi var mainīties pēc katra brauciena, ko spēle tev paziņos.\n\t* Lai varētu veiksmīgi pabeigt ceļojumu, tu vari apmeklēt kādu no uzlādes stacijām, un uzlādēt savu auto par 5 punktiem.\n\t* Spēles laikā tev arī būs jākrāj punkti. Sākot braucienu, tev būs 100 punkti.\n\t* Kad būsi sasniedzis kontrolpunktu vai pirmo reizi apmeklējis kādu uzlādes staciju, tevi sagaidīs jautājums ar 3 atbildes iespējām. Lai varētu braukt tālāk, tev būs pareizi jāatbild uz šo jautājumu. Ja atbildēsi uz jautājumu ar 1. mēģinājumu, iegūsi 20 punktus, bet par katru nepareizu atbildi iespējamais punktu skaits samazināsies par 10 punktiem.\n\t* Ja nebūsi pareizi aprēķinājis brauciena attālumu, un tavs auto izlādēsies, tad tev par 20 punktiem būs jāizsauc evakuātors, kurš tevi aizvedīs uz jebkuru uzlādes staciju, kuru vēlēsies.\n\t* Par 5 punktiem vari mazliet pagaidīt, lai redzētu vai varbūt mainīsies laikapstākļi.\n\t* Spēli uzvarēsi, kad būsi veiksmīgi izpildījis Liepājas karostas uzdevumu. Ievēro, ka karostas kontrolpunktu var apmeklēt tikai kā pēdējo.\n\t* Spēli zaudēsi, ja tavs punktu skaits sasniegs 0.\n\t* Ja aizmirsti spēles noteikumus, ieraksti jebkurā spēles ievades lodziņā precīzi "/h".')
  

def saraksts_uz_str(l):
  str1 = ''
  for i in l:
    str1 = str1 + i+ ' '
  return str1
  


def clearConsole():
  # notīra konsoli
  
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def next_p(apmekletie_kontrolpunkti,punkts,pasr):
  # prasa nakamo galapunktu
  
  while True:
    
    print(f'Izvēlies nākamo {punkts} vai, ja vēlies, tad ievadi "p", lai pagaidītu kad būs labs laiks, bet tādējādi zaudējot 5 punktus: ')
    kontp = input()
    if kontp == '':
      print('Lūdzu aizpildi šo laukumu')

    elif kontp in ['P', 'p']:
      return kontp

    elif kontp == '/h':
      noteikumi()
      
    elif len(list(kontp)) == 2:
      
      if not kontp[0].isalpha() or not kontp[1].isdigit():
        print('Piedod, es nesaprotu.')
      else:
        if kontp[0] not in ['U','u','K','k']:
          print('Piedod es nesaprotu.')
        else:
          
          if kontp[0] in ['U','u']:
            if int(kontp[1]) not in range(1,10):
              print('Piedod, es nesaprotu.')
            else:
              if kontp[0].upper() + kontp[1::] == pasr: 
                print('Tu jau atrodies šajā punktā.')
              else:
                return kontp[0].upper() + kontp[1::]
              
          if kontp[0] in ['K','k']:
            if int(kontp[1]) not in range(1,10):
              print('Piedod, es nesaprotu.')
            else:
              if kontp[0].upper() + kontp[1::] in apmekletie_kontrolpunkti:
                print('Tu jau apmeklējis šo kontrolpunktu')
              else:
                if len(apmekletie_kontrolpunkti) < 9 and kontp in ['K7','k7']:
                  print('Liepājas karosta ir obligāti pēdējais galapunkts.')
                else:
                  apmekletie_kontrolpunkti.append(kontp[0].upper() + kontp[1::])
                  return kontp[0].upper() + kontp[1::]

    elif len(list(kontp)) == 3:
      if not kontp[0].isalpha() or not kontp[1].isdigit() or not kontp[2].isdigit():
        print('Piedod, es nesaprotu.')
      else:
        if kontp[0] not in ['U','u','K','k']:
          print('Piedod es nesaprotu.')
        else:
          
          if kontp[0] in ['U','u']:
            if int(kontp[1::]) not in range(1,12):
              print('Piedod, es nesaprotu.')
            else:
              if kontp[0].upper() + kontp[1::] == pasr:
                print('Tu jau atrodies šajā punktā.')
              else:
                return kontp[0].upper() + kontp[1::]
              
          if kontp[0] in ['K','k']:
            if int(kontp[1::]) not in range(1,11):
              print('Piedod, es nesaprotu.')
            else:
              if kontp[0].upper() + kontp[1::] in apmekletie_kontrolpunkti:
                print('Tu jau esi apmeklējis šo kontrolpunktu')
              else:
                if kontp[0].upper() + kontp[1::] == pasr:
                  print('Tu jau atrodies šajā punktā')
                else:
                  apmekletie_kontrolpunkti.append(kontp[0].upper() + kontp[1::])
                  return kontp[0].upper() + kontp[1::]

    else:
      print('Piedod, es nesaprotu.')
              
def labs_laiks():
  # izlemj vai būs labs laiks nākamā brauciena laikā
  i = random.randint(1,2)
  if i == 1:
    return False
  elif i == 2:
    return True

def tabula(lasitajs):
  fails_a.seek(0)
  print('{0:^4} | {1:^4} | {2:^4} | {3:^4} | {4:^4} | {5:^4} | {6:^4} | {7:^4} | {8:^4} | {9:^4} | {10:^4} | {11:^4} | {12:^4} | {13:^4} | {14:^4} | {15:^4} | {16:^4} | {17:^4} | {18:^4} | {19:^4} | {20:^4}'.format('','U1','U2','U3','U4','U5','U6','U7','U8','U9','U10','K1','K2','K3','K4','K5','K6','K7','K8','K9','K10'))
  for i in lasitajs:
    if i['punkts'] == 'punkts':
      continue
    print('{0:^4} | {1:^4} | {2:^4} | {3:^4} | {4:^4} | {5:^4} | {6:^4} | {7:^4} | {8:^4} | {9:^4} | {10:^4} | {11:^4} | {12:^4} | {13:^4} | {14:^4} | {15:^4} | {16:^4} | {17:^4} | {18:^4} | {19:^4} | {20:^4}'.format(i['punkts'],i['U1'],i['U2'],i['U3'],i['U4'],i['U5'],i['U6'],i['U7'],i['U8'],i['U9'],i['U10'],i['K1'],i['K2'],i['K3'],i['K4'],i['K5'],i['K6'],i['K7'],i['K8'],i['K9'],i['K10']))

def izvelas_jautajumu(pasr,j_lasitajs,jaunie,fails_j):
  
  global jautajums,pa,na1,na2
  
  fails_j.seek(0)
  if pasr[0] == 'K':
    jaut = random.randint(1,jaunie)
  else:
    jaut = 1
    
  for line in j_lasitajs:
    if line['punkts'] == pasr:
      jautajums = line['jautājums'+str(jaut)]
      pa = line['P'+str(jaut)+'A']
      na1 = line[str(jaut)+'B']
      na2 = line[str(jaut)+'C']

  return jautajums,pa,na1,na2

def atbildes(pa,na1,na2):
  
  seciba = random.randint(1,6)
  
  if seciba == 1:
    pa = 'A:'+pa
    na1 = 'B:'+na1
    na2 = 'C:'+na2
    print(pa)
    print(na1)
    print(na2)
  elif seciba == 2:
    pa = 'A:'+pa
    na2 = 'B:'+na2
    na1 = 'C:'+na1
    print(pa)
    print(na2)
    print(na1)
  elif seciba == 3:
    na1 = 'A:'+na1
    pa = 'B:'+pa
    na2 = 'C:'+na2
    print(na1)
    print(pa)
    print(na2)
  elif seciba == 4:
    na1 = 'A:'+na1
    na2 = 'B:'+na2
    pa = 'C:'+pa
    print(na1)
    print(na2)
    print(pa)
  elif seciba == 5:
    na2 = 'A:'+na2
    na1 = 'B:'+na1
    pa = 'C:'+pa
    print(na2)
    print(na1)
    print(pa)
  elif seciba == 6:
    na2 = 'A:'+na2
    pa = 'B:'+pa
    na1 = 'C:'+na1
    print(na2)
    print(pa)
    print(na1)

  return pa,na1,na2

def parbauda_zaudejumu(punkti,zaudetie_punkti):
  if punkti - zaudetie_punkti > 0:
    return True
  else:
    print('############################\nTavs punktu skaits ir sasniedzis 0. Tu zaudēji.\n############################\n')
    return False

def spele(j_lasitajs,jaunie,vardu_saraksts,fails_j):

  apmekletie_kontrolpunkti = ['K3']
  pasr = 'K3'
  attalums = 0
  pasreizeja_vieta = 'Valmieras Valsts ģimnāzija'
  nakama_vieta = ''
  uzl_lim = 100
  iesp_att = 0
  ieprieks_uzl_lim = 0
  punkti = 100
  labs_laiksa = True
  jautajums = ''
  pa = ''
  na1 = ''
  na2 = ''
  iesp_punkti = 20
  sakt_laiku = time.time()
  kopejais_cels = 0
  uzlades_stacijas = 0
  uzlades_stacijas_l = []
  turpinat = True
  mainit_laiku = True
  
  print(f'Tu sāksi savu ceļojumu punktā K3, jeb Valmieras Valsts Ģimnāzijā')
      
  print('Lai brauktu tālāk, tev pareizi jāatbild uz jautājumu. Maksimālais iegūstamo punktu skaits ir 20, bet par katru nepareizu atbildi tas samazinās par 10 punktiem.')
  
  jautajums,pa,na1,na2 = izvelas_jautajumu(pasr,j_lasitajs,jaunie,fails_j)
      
  print(jautajums)
  pa,na1,na2 = atbildes(pa,na1,na2)
  
  while True:
    iesp_punkti = 20
    atbilde = input('Ievadi atbildes burtu: ')
    if atbilde not in ['A','B','C','c','b','a','/h']:
      print('Tādas atbildes nav')
    else:
      if atbilde.upper() == pa[0]:
        print(f'Pareizā atbilde, tu ieguvi {iesp_punkti} punktus')
        punkti += iesp_punkti
        break
      elif atbilde == '/h':
        noteikumi()
      else:
        print('Nepareizā atbilde!')
        if iesp_punkti >= 10:
          iesp_punkti -= 10

  while True:
    talak = input('Esi gatavs braukt tālāk? (j vai n): ')
    if talak not in ['j','n','J','N','/h']:
      print('Piedod, es nesaprotu.')
    else:
      if talak in ['J','j']:
        pasreizeja_vieta = nakama_vieta
        clearConsole() 
        break
      elif talak == '/h':
        noteikumi()
  
  while True:
    clearConsole()
    print('Šeit tabula ar attālumiem starp kontrolpunktiem un uzlādes stacijām')
    fails_a.seek(0)
    tabula(a_lasitajs)
    print(f'Tu pašlaik atrodies punktā {pasreizeja_vieta}, jeb {pasr}, tavs punktu skaits ir {punkti}')
    print(f'Mašīnas uzlādes līmenis ir {round(uzl_lim)}% un labā laikā tā var nobraukt {round(uzl_lim/100*140,3)} km, bet sliktā - {round(uzl_lim/100*80,3)} km.')
    print(f'Tu jau esi apmeklējis kontrolpunktus: {saraksts_uz_str(apmekletie_kontrolpunkti)}')

    if mainit_laiku:
      labs_laiksa = labs_laiks()
    
    if labs_laiksa:
      print('Nākamā brauciena laikā sola labu laiku.')
    else:
      print('Nākamā brauciena laikā sola sliktu laiku.')
      
    next = next_p(apmekletie_kontrolpunkti,'kontrolpunktu vai uzlādes stacju',pasr)
    
    if next in ['P','p']:

      turpinat = parbauda_zaudejumu(punkti,5)
      
      punkti -= 5

      if not turpinat:
        break
        
      clearConsole()
      continue
      
    fails_v.seek(0)
    for i in v_lasitajs:
      if i['Sifrejumi'] == next:
        nakama_vieta = i['Vieta']
        
    fails_v.seek(0)
    for i in v_lasitajs:
      if i['Sifrejumi'] == pasr:
        pasreizeja_vieta = i['Vieta']
  
    fails_a.seek(0)
    for i in a_lasitajs:
      if i['punkts'] == pasr:
        attalums = float(i[next])
    
    while True:
      print(f'Vai vēlies sākt braucienu no punkta {pasreizeja_vieta} uz punktu {nakama_vieta}, starp kuriem attālums ir {attalums} kilometri, vai arī vēlies izvēlēties citu punktu?')
      sakt_braucienu = input('(j vai n, vai c): ')
      if sakt_braucienu not in ['J','j','N','n','C','c','/h']:
        print('Piedod es nesaprotu')
      else:
        if sakt_braucienu in ['J','j']:
          mainit_laiku = True
          clearConsole()
          break
        elif sakt_braucienu in ['C','c']:
          clearConsole()
          break
        elif sakt_braucienu in ['N','n']:
          clearConsole()
          continue
        elif sakt_braucienu == '/h':
          noteikumi()
  
    if sakt_braucienu in ['C','c']:
      mainit_laiku = False
      if next[0] == 'K':
        apmekletie_kontrolpunkti.pop(-1)
      continue
  
    if labs_laiksa:
      iesp_att = 140 * (uzl_lim / 100)
    else:
      iesp_att = 80 * (uzl_lim / 100)
  
  # nepietiek enerģijas
    
    if iesp_att < attalums:
      if next[0] == 'K':
        apmekletie_kontrolpunkti.pop(-1)
      print('Ak nē, tava mašīna apstājās. Tu zaudēji 10 punktus. Izvēlies uz kuru uzlādes staciju tevi aizvest.')
      
      kopejais_cels += iesp_att  

      turpinat = parbauda_zaudejumu(punkti,10)
      if not turpinat:
        break
      
      punkti -= 10
      tabula(a_lasitajs)
      while True:
        a = next_p(apmekletie_kontrolpunkti,'uzlādes staciju','')
        if a[0] in ['K','k']:
          print('Tev obligāti jāizvēlas uzlādes stacija!')
        elif a[0] in ['p','P']:

          turpinat = parbauda_zaudejumu(punkti,5)
          
          if not turpinat:
            break
          
          punkti -= 5

        else:
          break
      clearConsole()
          
      fails_v.seek(0)
      for i in v_lasitajs:
        if i['Sifrejumi'] == a:
          nakama_vieta = i['Vieta']
      pasr = a
      
  # vaiksmīgi sasniedz galapunktu
      
    else:
      print(f'Tu esi veiksmīgi sasniedzis savu galapunktu {nakama_vieta}.')
      kopejais_cels += attalums
      if labs_laiks:
        ieprieks_uzl_lim = uzl_lim
        uzl_lim = ieprieks_uzl_lim - (attalums / 140) * 100
      else:
        ieprieks_uzl_lim = uzl_lim
        uzl_lim = ieprieks_uzl_lim - (attalums / 80) * 100
      pasr = next
  
  # ja galapunkts ir uzlādes stacija

    if pasr[0] in ['U','u']:
      uzlades_stacijas += 1

      if pasr not in uzlades_stacijas_l:

        print('Lai sāktu uzpildi, tev pareizi jāatbild uz jautājumu. Maksimālais iegūstamo punktu skaits ir 20, bet par katru nepareizu atbildi tas samazinās par 10 punktiem.')
      
        jautajums,pa,na1,na2 = izvelas_jautajumu(pasr,j_lasitajs,jaunie,fails_j)
        
        print(jautajums)
        pa,na1,na2 = atbildes(pa,na1,na2)

        iesp_punkti = 20
        
        while True:
          
          atbilde = input('Ievadi atbildes burtu: ')
          if atbilde not in ['A','B','C','c','b','a','/h']:
            print('Tādas atbildes nav')
          else:
            if atbilde.upper() == pa[0]:
              print(f'Pareizā atbilde, tu ieguvi {iesp_punkti} punktus')
              punkti += iesp_punkti
              break
            elif atbilde == '/h':
              noteikumi()
            else:
              print('Nepareizā atbilde!')
              if iesp_punkti >= 10:
                iesp_punkti -= 10

        uzlades_stacijas_l.append(pasr)
      
      while True:
        uzpilde = input('Vai vēlies uzsākt uzpildi par 5 punktiem? (j vai n)')
        if uzpilde not in ['J','j','N','n','/h']:
          print('Piedod, es nesaprotu.')
        else:
          if uzpilde in ['J','j']:
            break
          elif uzpilde in ['N','n']:
            continue
          elif uzpilde == '/h':
            noteikumi()

      if uzpilde in ['J','j']:
        turpinat = parbauda_zaudejumu(punkti,5)
        
        if not turpinat:
          break
            
        punkti -= 5
            
      clearConsole()
      
      print('Esi veiksmīgi uzpildījis auto')
      uzl_lim = 100
     
  # ja galapunkts ir kontrolpunkts
    
    if pasr[0] in ['K','k']:
      
      iesp_punkti = 20
      
      print('Lai brauktu tālāk, tev pareizi jāatbild uz jautājumu. Maksimālais iegūstamo punktu skaits ir 20, bet par katru nepareizu atbildi tas samazinās par 10 punktiem.')
      
      jautajums,pa,na1,na2 = izvelas_jautajumu(pasr,j_lasitajs,jaunie,fails_j)
      
      print(jautajums)
      pa,na1,na2 = atbildes(pa,na1,na2)
  
      while True:
        atbilde = input('Ievadi atbildes burtu: ')
        if atbilde not in ['A','B','C','c','b','a','/h']:
          print('Tādas atbildes nav')
        else:
          if atbilde.upper() == pa[0]:
            print(f'Pareizā atbilde, tu ieguvi {iesp_punkti} punktus')
            punkti += iesp_punkti
            break
          elif atbilde == '/h':
            noteikumi()
          else:
            print('Nepareizā atbilde!')
            if iesp_punkti >= 10:
              iesp_punkti -= 10

# spēlē uzvarēja
    
    if len(apmekletie_kontrolpunkti) == 10:
      laiks = (round(time.time()-sakt_laiku))
      minutes = laiks//60
      sekundes = laiks%60
      
      
      print(f'############################\nApsveicam tu pabeidzi spēli ar {punkti} punktiem.\n############################')
      print(f'Tu spēlē pavadīji {minutes} minūtes un {sekundes} sekundes.')
      print(f'Kopumā tu nobrauci {kopejais_cels} km un apmeklēji {uzlades_stacijas} uzlādes stacijas. ')
      
      fails_r_l = open('rezultati.csv','r')
      r_lasitajs = csv.DictReader(fails_r_l,delimiter = '/')
      for i in r_lasitajs:
        vardu_saraksts.append(i['vards'])
      fails_r_l.close()
        
      while True:
        vards = input('Ievadi savu vārdu: ')
        if vards == '':
          print('Lūdzu aizpildi šo lauciņu')
        else:
          if len(vards) > 10 :
            print('Vārdā var tikt izmantoti tikai 10 burti.')
          else:
            if not vards.isalpha():
              print('Vārdā var izmantot tikai lielos vai mazos burtus, bez īpašām rakstzīmēm.')
            else:
              if vards in vardu_saraksts:
                print('Šis vārds jau ir aizņemts')
              else:
                break
            
      fails_r_r = open('rezultati.csv','a')
      r_rakstitajs = csv.DictWriter(fails_r_r,delimiter = '/',fieldnames = ['vards','laiks','punkti','cels','stacijas'])
      r_rakstitajs.writerow({'vards':vards,'laiks':laiks,'punkti':punkti,'cels':kopejais_cels,'stacijas':uzlades_stacijas})
      fails_r_r.close()

      clearConsole()

      while True:
        leaderboard = input('Vai vēlies apskatīties 10 labākos spēles rezultātus? (j vai n): ')
        
        clearConsole()
        
        vards_laiks = {}      
        
        if leaderboard in ['J','j']:
          
          fails_r_l = open('rezultati.csv','r')
          r_lasitajs = csv.DictReader(fails_r_l,delimiter = '/')
          
          for i in r_lasitajs:
            vards_laiks[i['vards']] = int(i['laiks'])


          vards_laiks = sorted(vards_laiks.items(), key=lambda x: x[1])

          print('{0:^11}|{1:^8}|{2:^8}'.format('Vārds','Laiks','Punkti'))
          skaits = 0
          
          l_punkti = 0
          
          for k in vards_laiks:
            skaits += 1
            if skaits > 10:
              break

            
            for i in r_lasitajs:
              if i['vards'] == k[0]:
                l_punkti = i['punkti']

            print('{0:^11}|{1:^8}|{2:^8}'.format(k[0],f'{k[1]//60}:{k[1]%60}',l_punkti))
          

          fails_r_l.close()
          break

        elif leaderboard in ['N','n']:
          break

        else:
          print('Piedod, es nesaprotu.')
          
      break
      
# Brauc tālāk
      
    else:
      while True:
        talak = input('Esi gatavs braukt tālāk? (j vai n): ')
        if talak not in ['j','n','J','N','/h']:
          print('Piedod, es nesaprotu.')
        else:
          if talak in ['J','j']:
            pasreizeja_vieta = nakama_vieta
            clearConsole() 
            break
          elif talak == '/h':
            noteikumi()
  
#SPĒLE*********************************************************************

k = 1
u = 1
vardu_saraksts = []
game_on = False

clearConsole()

print('Sveicināti spēlē "Tūrisma rallijs Liepāja 2022"')
print('Spēles autori: Liepājas atklātās programmēšanas olimpiādes 2022 komandas "Chipots Dizelis" biedri - Kaspars Jānis Plūme, Ralfs Imants Unāms, Rainers Zviedris')
noteikumi()
while not game_on:
  sakt = input('Nospied enter, lai sāktu spēli: ')
  game_on = True

while game_on:

  #FAILU ATVĒRŠANA *******************************************************************************************

  fails_a = open('TABULA-Lapa1.csv','r')
  a_lasitajs = csv.DictReader(fails_a)
  fails_v = open('kontrolpunktu_vietas-Lapa1.csv','r')
  v_lasitajs = csv.DictReader(fails_v)
  fails_j = open('jautajumi-Lapa1.csv','r')
  j_lasitajs = csv.DictReader(fails_j)
  fails_jaunie_j_r = open('jaunie_jaut.csv','w')
  jaunie_j_rakstitajs = csv.DictWriter(fails_jaunie_j_r, delimiter = '/', fieldnames = ['punkts','jautājums1','P1A','1B','1C'])
  jaunie_j_rakstitajs.writeheader()
  fails_jaunie_j_l = open('jaunie_jaut.csv','r')
  jaunie_j_lasitajs = csv.DictReader(fails_jaunie_j_l,delimiter='/')
  
  while True:
    print('Ja vēlies, vari aizvietot spēles oriģinālos jautājumus?')
    a = input('(j vai n): ')
    if a not in ['j','n','J','N']:
      print('Piedod, es nesaprotu.')
    else:
      if a in ['J','j']:
        
        while k <= 10:
          print(f'Ievadi jautājumu punktam K{k}: ')
          jaun_jautajums = input()
          print('Ievadi pareizo atbildi: ')
          paj = input()
          print('Ievadi nākamo, nepareizo atbildi: ')
          naj1 = input()
          print('Ievadi nākamo, nepareizo atbildi: ')
          naj2 = input()

          while True:
            apstiprina = input('Vai esi apmierināts ar ievadītajiem jautājumiem? Ja nospiedīsi "n", tev būs iespēja nomainīt jautāumu.')
          jaunie_j_rakstitajs.writerow({'punkts':'K'+str(k),'jautājums1':jaun_jautajums,'P1A':paj,'1B':naj1,'1C':naj2})
          k += 1

        while u <= 10:
          print(f'Ievadi jautājumu punktam U{u}: ')
          jaun_jautajums_u = input()
          print('Ievadi pareizo atbildi: ')
          paj_u = input()
          print('Ievadi nākamo, nepareizo atbildi: ')
          naj1_u = input()
          print('Ievadi nākamo, nepareizo atbildi: ')
          naj2_u = input()
          jaunie_j_rakstitajs.writerow({'punkts':'U'+str(u),'jautājums1':jaun_jautajums_u,'P1A':paj_u,'1B':naj1_u,'1C':naj2_u})

          u += 1
          
        fails_jaunie_j_r.close()
        break
  
      else:
        fails_jaunie_j_r.close()
        break
        
  clearConsole()
  
  if a in ['n','N']:   
    spele(j_lasitajs,3,vardu_saraksts,fails_j)
    
  else:
    spele(jaunie_j_lasitajs,1,vardu_saraksts,fails_jaunie_j_l)
  
  fails_a.close()
  fails_v.close()
  fails_j.close()
  fails_jaunie_j_l.close()

  while True:
    atkal = input('Vai vēlies spēlēt atkal? (j vai n): ')
    if atkal in ['N','n']:
      print('Paldies par spēlēšanu! Atā!')
      game_on = False
      break
    elif atkal in ['J','j']:
      break
    else:
      print('Piedod, es nesaprotu.')