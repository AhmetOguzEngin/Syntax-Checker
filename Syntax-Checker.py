import re
import sys

given_file = open('calc.in', 'r')
file_to_check = given_file.read()
given_file.close()

file_to_check = file_to_check.split('\n')
#To split the input
for element in range(len(file_to_check)):
    file_to_check[element] = file_to_check[element].split()
#To delete empty lists
while [] in file_to_check:
    ind=file_to_check.index([])
    file_to_check.pop(ind)
checker = [0, 0, 0]
init_statement = []
mid_statement = []
final_statement = []
checker2=[0,0,0]

#To end the program if something goes wrong
def closer():
    new_file = open('calc.out', 'w')
    new_file.write('Dont Let Me Down')
    new_file.close()
    sys.exit()

#To split the words according to their titles
def splitter(file_to_split):
    if not file_to_split[0][0]=='AnaDegiskenler':
        closer()
        return False
#To find the titles' indexes
    for line_number in range(len(file_to_split)):
        for word in file_to_split[line_number]:
            if word == 'AnaDegiskenler':
                initind = line_number
                checker[0] = 1
            elif word == 'YeniDegiskenler':
                midind = line_number
                checker[1] = 1
            elif word == 'Sonuc':
                finalind = line_number
                checker[2] = 1
#To check whether all titels exist
    if not (checker == [1, 1, 1]):
        closer()
        return False
#To check order of titles
    if not finalind>midind>initind:
        closer()
        return False
#Spliter
    init_statement = file_to_split[0:midind]
    mid_statement = file_to_split[midind:finalind]
    final_statement = file_to_split[finalind:]
#To check if anything is written to the same line with titles
    if len(init_statement[0])>1 or len(mid_statement[0])>1 or len(final_statement[0])>1:
        closer()

#To check if 'Sonuc' statement is including 0 or 1 statement
    if len(final_statement)>2:
        closer()
    splitter_result = [init_statement, mid_statement, final_statement]

    return (splitter_result)
#Banned words
banned=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta','.']

def syntaxchecker(document):
    list_of_statements = splitter(document)
    #To prepare lists
    if type(list_of_statements) == type([]):
        init_statement = list_of_statements[0]
        mid_statement = list_of_statements[1]
        final_statement = list_of_statements[2]
        initdictarit = {}
        initdictbool = {}

        #Initstatement beginning

        #Title check
        if init_statement[0][0] == 'AnaDegiskenler' and len(init_statement[0]) == 1:
            checker2[0]=1
            for line in init_statement[1:]:
                #Length check
                if len(line)>3:
                    #Repeat check
                    if line[0] in initdictarit.keys() or line[0] in initdictbool.keys():
                        closer()
                    #Syntax check
                    pattern_value = re.compile('^[a-zA-Z0-9]{1,10}$')
                    pattern_degeri = re.compile('^degeri$')
                    pattern_sayi1 = re.compile(
                        '^[0-9]$|^dogru$|^yanlis$|^sifir$|^bir$|^iki$|^uc$|^dort$|^bes$|^alti$|^yedi$|^sekiz$|^dokuz$')
                    pattern_sayi2 = re.compile(
                        '(^([0-9](\.)[0-9]$)|((^sifir|^bir|^iki|^uc|^dort|^bes|^alti|^yedi|^sekiz|^dokuz)\s(nokta)\s(sifir$|bir$|iki$|uc$|dort$|bes$|alti$|yedi$|sekiz$|dokuz$)))')
                    pattern_olsun = re.compile('^olsun$')

                    check1 = re.search(pattern_value, line[0])
                    check2 = re.search(pattern_degeri, line[1])
                    #Variable check
                    if line[0] in banned:
                        closer()
                    #To creat value to check
                    new_deger=' '.join(line[2:-1])
                    if ('nokta' in new_deger) or ('.' in new_deger):
                        check3 = re.search(pattern_sayi2, new_deger)
                    else:
                        check3 = re.search(pattern_sayi1, new_deger)

                    check4 = re.search(pattern_olsun, line[-1])
                    #To check variables in midstatement
                    if new_deger == 'dogru' or new_deger == 'yanlis':

                        initdictbool[line[0]] = new_deger
                    else:
                        initdictarit[line[0]] = new_deger
                    #To check if syntax is correct
                    if check1 == None or check2 == None or check3 == None or check4 == None:
                        closer()
                else:
                    closer()
        #To prepare necessary lists for 'midstatement'
        case1 = []
        sayilar1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in sayilar1:
            for k in sayilar1:
                case1.append(i + '.' + k)

        sayilar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi',
                   'sekiz', 'dokuz', 'sifir']
        midcheckarit = []
        midcheckarit.extend(initdictarit.keys())
        midcheckarit.extend(sayilar)
        allowed = ['(', 'ac-parantez', 'arti', 'eksi', 'carpi', 'kapa-parantez', ')', '+', '-', '*',
                   ' ', '.', 'nokta']
        midcheckarit.extend(allowed)
        midcheckarit.extend(case1)
        midcheckbool = []
        bools = ['dogru', 'yanlis']
        midcheckbool.extend(initdictbool.keys())
        midcheckbool.extend(bools)
        allowed2 = ['(', 'ac-parantez', 've', 'veya', 'kapa-parantez', ')', ' ']
        midcheckbool.extend(allowed2)
        #Beginning of midstatement
        if mid_statement[0][0] == 'YeniDegiskenler' and len(mid_statement[0]) == 1:
            checker2[1]=1
            for line in mid_statement[1:]:
                #Length check
                if len(line)>3:
                    if line[0] in banned:
                        closer()
                    # Repeat check
                    if line[0] in midcheckarit or line[0] in midcheckbool:
                        closer()
                    #Syntax check
                    list_of_values = []
                    pattern_value = re.compile('^[a-zA-Z0-9]{1,10}$')
                    pattern_degeri = re.compile('^degeri$')
                    pattern_olsun = re.compile('^olsun$')
                    checkmid1 = re.search(pattern_value, line[0])
                    checkmid2 = re.search(pattern_degeri, line[1])
                    checkmid4 = re.search(pattern_olsun, line[-1])
                    #Value check

                    for k in line[2:-1]:
                        list_of_values.append(k)


                    statement_mid = False
                    #To check if statement is arit or bool
                    for k in list_of_values:
                        if not (k in midcheckarit):
                            statement_mid = True
                            break
                    # To check if statement is arit or bool
                    if statement_mid:
                        for v in list_of_values:
                            if not (v in midcheckbool):
                                closer()

                    parantezindholder = []
                    #To check number of parantesis
                    numofacpar = list_of_values.count('(') + list_of_values.count('ac-parantez')
                    # To check number of parantesis
                    numofkappar = list_of_values.count(')') + list_of_values.count('kapa-parantez')
                    #To check if number of open parantesis and close parantesis match
                    if numofkappar != numofacpar:
                        closer()

                    if numofacpar == numofkappar:
                        for i in range(len(list_of_values)):
                            mission = 'notcompleted'
                            banned2 = ['arti', 'eksi', 'carpi', '+', '-', '*', 'nokta', '.', 've', 'veya']
                            for t in range(len(list_of_values) - 1):
                                #To syntax check. There should be a value between these special chars.
                                if list_of_values[t] in banned2 and list_of_values[t+1] in banned2:
                                    closer()
                            #To start choosing a part of value which starts with '(' or 'ac-parantez'
                            if list_of_values[i] == '(' or list_of_values[i] == 'ac-parantez':
                                parantezindholder.append(i)
                            #To choose the end of this part.
                            elif list_of_values[i] == ')' or list_of_values[i] == 'kapa-parantez':
                                try:
                                    lsttocheck = list_of_values[parantezindholder[-1]:i + 1]
                                except:
                                    closer()
                                #To convert from a list to a str
                                midstringtocheck=' '.join(lsttocheck)
                                #To check if statement is bool or arit
                                if statement_mid == False:
                                    # To prepare a variable list for 'Sonuc'
                                    if not (line[0] in midcheckarit):
                                        midcheckarit.append(line[0])
                                    #Syntax check
                                    lstchecker = re.compile(
                                        '^((\(|ac-parantez)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))\s((\+|-|\*|arti|eksi|carpi)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))\s)*(kapa-parantez|\))$)')
                                    checkmid3 = re.search(lstchecker, midstringtocheck)
                                    #To check if there is a mistake
                                    if not (checkmid3 == None):
                                        list_of_values.pop(parantezindholder[-1])
                                        list_of_values.pop(i - 1)
                                        list_of_values.insert(parantezindholder[-1], '+')
                                        list_of_values.insert(parantezindholder[-1],
                                                              list_of_values[parantezindholder[-1] + 1])
                                        parantezindholder.pop(-1)
                                # To check if statement is bool or arit
                                if statement_mid:
                                    # To prepare a variable list for 'Sonuc'
                                    if not (line[0] in midcheckbool):
                                        midcheckbool.append(line[0])
                                    #Syntax check
                                    boolchecker = re.compile(
                                        '^(\(|ac-parantez)\s([a-zA-Z0-9]{1,10})\s((ve|veya)\s[a-zA-Z0-9]{1,10}\s)*(kapa-parantez|\))$')
                                    checkmid3 = re.search(boolchecker, midstringtocheck)
                                    if not (checkmid3 == None):
                                        list_of_values.pop(parantezindholder[-1])
                                        list_of_values.pop(i - 1)
                                        list_of_values.insert(parantezindholder[-1], 've')
                                        list_of_values.insert(parantezindholder[-1],
                                                              list_of_values[parantezindholder[-1] + 1])
                                        parantezindholder.pop(-1)
                                #To check if there is a mistake
                                if checkmid1 == None or checkmid2 == None or checkmid3 == None or checkmid4 == None:
                                    closer()
                            #If there is no prantesis in the line this code starts to check
                            if not ('(' in list_of_values or 'ac-parantez' in list_of_values):
                                # To check if statement is bool or arit
                                if statement_mid == False:
                                    #To prepare a variable list for 'Sonuc'
                                    if not (line[0] in midcheckarit):
                                        midcheckarit.append(line[0])

                                    laststrtocheck=' '.join(list_of_values)
                                    #Syntax check
                                    lastchecker = re.compile(
                                        '^(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))(\s(\+|-|\*|arti|eksi|carpi)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz))))*$')
                                    checkmid5 = re.search(lastchecker, laststrtocheck)

                                    mission = 'completed'
                                    break
                                # To check if statement is bool or arit
                                elif statement_mid:
                                    # To prepare a variable list for 'Sonuc'
                                    if not (line[0] in midcheckbool):
                                        midcheckbool.append(line[0])
                                    #Syntax check
                                    laststrtocheck=' '.join(list_of_values)
                                    lastchecker = re.compile(
                                        '^([a-zA-Z0-9]{1,10})(\s(ve|veya)\s[a-zA-Z0-9]{1,10})*$')

                                    checkmid5 = re.search(lastchecker, laststrtocheck)
                                    mission = 'completed'

                                    break
                        #To check if there is any syntax errors.

                        if mission == 'completed' and (
                                checkmid1 == None or checkmid2 == None or checkmid5 == None or checkmid4 == None):
                            closer()


                else:
                    closer()
        #Beginning of 'Sonuc' statement
        if final_statement[0][0] == 'Sonuc' and len(final_statement[0]) == 1:
            checker2[2]=1
            for linef in final_statement[1:]:
                lastlist=linef

                banned2 = ['arti', 'eksi', 'carpi', '+', '-', '*', 'nokta', '.', 've', 'veya']
                for t in range(len(lastlist) - 1):
                    if lastlist[t] in banned2 and lastlist[t+1] in banned2:
                        closer()

                #To check whether all the values are suitable
                statement_final = False
                for k in lastlist:
                    if not (k in midcheckarit):
                        statement_final = True
                        break
                #To check whether all the values are suitable
                if statement_final:
                    for v in lastlist:
                        if not (v in midcheckbool):
                            closer()

                parantezindholderf = []

                numofacparf = lastlist.count('(') + lastlist.count('ac-parantez')

                numofkapparf = lastlist.count(')') + lastlist.count('kapa-parantez')
                if numofkapparf != numofacparf:
                    closer()
                if numofacparf == numofkapparf:
                    for i in range(len(lastlist)):
                        mission = 'notcompletedf'

                        if lastlist[i] == '(' or lastlist[i] == 'ac-parantez':
                            parantezindholderf.append(i)

                        elif lastlist[i] == ')' or lastlist[i] == 'kapa-parantez':
                            try:
                                lastlisttocheck = lastlist[parantezindholderf[-1]:i + 1]
                            except:
                                closer()

                            finalstringtocheck=  ' '.join(lastlisttocheck)
                            # To check if statement is bool or arit
                            if statement_final==False:
                                lstcheckerf = re.compile(
                                    '^((\(|ac-parantez)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))\s((\+|-|\*|arti|eksi|carpi)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))\s)*(kapa-parantez|\))$)')
                                checkfinal1 = re.search(lstcheckerf, finalstringtocheck)


                                if not (checkfinal1 == None):
                                    # Syntax check
                                    lastlist.pop(parantezindholderf[-1])
                                    lastlist.pop(i - 1)
                                    lastlist.insert(parantezindholderf[-1], '+')
                                    lastlist.insert(parantezindholderf[-1],lastlist[parantezindholderf[-1] + 1])
                                    parantezindholderf.pop(-1)

                            # To check if statement is bool or arit
                            if statement_final:
                                boolcheckerf = re.compile(
                                    '^(\(|ac-parantez)\s([a-zA-Z0-9]{1,10})\s((ve|veya)\s[a-zA-Z0-9]{1,10}\s)*(kapa-parantez|\))$')
                                checkfinal1 = re.search(boolcheckerf, finalstringtocheck)
                                # Syntax check
                                if not (checkfinal1 == None):

                                    lastlist.pop(parantezindholderf[-1])
                                    lastlist.pop(i - 1)
                                    lastlist.insert(parantezindholderf[-1], 've')
                                    lastlist.insert(parantezindholderf[-1],lastlist[parantezindholderf[-1] + 1])
                                    parantezindholderf.pop(-1)
                            #Syntax check
                            if checkfinal1 == None:
                                closer()

                        # If there is no prantesis in the line this code starts to check
                        if not ('(' in lastlist or 'ac-parantez' in lastlist):
                            # To check if statement is bool or arit
                            if statement_final == False:
                                # Syntax check
                                finalstrtocheck = ' '.join(lastlist)

                                lastchecker = re.compile(
                                    '^(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)))(\s(\+|-|\*|arti|eksi|carpi)\s(([a-zA-Z0-9]{1,10})|(([0-9])(\.)([0-9]))|((sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s(nokta)\s(sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz))))*$')
                                finalcheck2 = re.search(lastchecker, finalstrtocheck)
                                mission = 'completedf'
                                break
                            # To check if statement is bool or arit
                            elif statement_final:
                                #Syntax check
                                finalstrtocheck=' '.join(lastlist)

                                lastchecker = re.compile(
                                    '^([a-zA-Z0-9]{1,10})(\s(ve|veya)\s[a-zA-Z0-9]{1,10})*$')

                                finalcheck2 = re.search(lastchecker, finalstrtocheck)
                                mission = 'completedf'
                                break

                    if mission == 'completedf' and (finalcheck2 == None):
                        closer()
                else:
                    closer()
        #All cases check
        if checker2==[1,1,1]:
            new_file=open('calc.out', 'w')
            new_file.write('Here Comes the Sun')
            new_file.close()
            sys.exit()

        else:
            closer()

syntaxchecker(file_to_check)
