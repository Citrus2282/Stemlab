import random
print("Какой вы хотите язык?")
lang = input()
print("Сколько вы хотите городов и улиц?")

if lang == "русский":
    num = int(input())
    for i in range(num):
        pry = {1: 'при', 2: 'пра', 3: 'по', 4: 'ка', 5: 'без', 6: 'вел', 7: 'до', 8: 'лот', 9: 'зар', 10: 'уп'}
        kor = {1: 'парасон', 2: 'ссср', 3: 'жаб', 4: 'хом', 5: 'карт', 6: 'валий', 7: 'герман', 8: 'пиреней', 9: 'факул',
               10: 'пролет'}
        syf = {1: 'ская', 2: 'ское', 3: 'ная', 4: 'ейская', 5: 'арская', 6: 'ский', 7: 'нея'}
        gor = {1: 'минск', 2: 'гомель', 3: 'гродно', 4: 'могилев', 5: 'брест', 6: 'борисов', 7: 'заславль', 8: 'витебск',
               9: 'орша', 10: 'чернигов'}

        py = random.randint(1, 10)
        ky = random.randint(1, 10)
        sy = random.randint(1, 7)
        gy = random.randint(1, 10)
        pt = pry[py]
        kt = kor[ky]
        st = syf[sy]
        gt = gor[gy]
        print(gt, "улица", pt + kt + st)
if lang == "английский":
    num = int(input())
    for i in range(num):
        pryE = {1:'the first',2:'the twice',3:'De-',4:'Pek-',5:'Solt-',6:'South-',7:'Park-',8:'Bakli-',9:'Osvego-',10:'Yesel-'}
        korE = {1:'Road',2:'Kleq',3:'Street',4:'Avenu',5:'Springs',6:'Drive',7:'Manliys',8:'Utica',9:'Moxok',10:'Igl'}
        gorE = {1:'york',2:'bomba',3:'vegas',4:'jor',5:'darb',6:'fach',7:'lare',8:'dolga',9:'urtu',10:'erty'}

        pyE = random.randint(1, 10)
        kyE = random.randint(1, 10)
        gyE = random.randint(1, 10)

        ptE = pryE[pyE]
        ktE = korE[kyE]
        gtE = gorE[gyE]
        print(gtE, ptE+ktE)
if lang == "белоруский":
    num = int(input())
    for i in range(num):
        pryB = {1:'пра',2:'пад',3:'ад',4:'пры',5:'да',6:'лад',7:'бяс',8:'ка',9:'пере',10:'ва'}
        korB = {1:'бусел',2:'кабан',3:'савецкi',4:'дораг',5:'чалавек',6:'закрэус',7:'',8:'малад',9:'печ',10:'бульб'}
        gorB = {1:'калгас',2:'бабок',3:'арэшэк',4:'карска',5:'дамба',6:'камень',7:'барысау',8:'менск',9:'тур',10:'заслауе'}

        pyB = random.randint(1, 10)
        kyB = random.randint(1, 10)
        gyB = random.randint(1, 10)

        ptB = pryB[pyB]
        ktB = korB[kyB]
        gtB = gorB[gyB]
        print(gtB, ptB+ktB)










