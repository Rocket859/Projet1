rnc_sal=0
rnc_rf = 0
rnc_rcm = 0
corrections_revenu_global = 0
revenu_global = rnc_sal + rnc_rf + rnc_rcm
revenu_imposable = revenu_global - corrections_revenu_global
majorations_quotient_familial = 0


def ouinon(prompt) : 
    while True : 
            value = input(prompt).lower().strip()
            if value == "oui" : 
                return True
            elif value == "non" :
                return False
            else : 
                print(" Veuillez répondre par oui ou non. ")

def nombre(prompt) :
    while True :
        try : 
            value = float(input(prompt))
            return value
        except ValueError :
            print(" Veuillez-entrer un nombre valide ")


print(" IMPÔT SUR LE REVENU  ")
print("  Identification de la situation du contribuable ")

situation_couple = ouinon("   Êtes-vous marié(s) ou pacsé(s) ")
if situation_couple == False :
    part_couple = 1
else : 
    part_couple = 2

situation_enfants = ouinon("   Avez-vous des enfants ")
if situation_enfants == True :
    nb_enfants = nombre("   Combien-avez vous d'enfants ? ")
else :
    nb_enfants = 0

situation_autre = ouinon("   Avez-vous d'autres personnes à votre charge ? ")
if situation_autre == True :
    nb_autre = nombre("   Combien d'autres personnes avez-vous à votre charge ? ")
else : 
    nb_autre = 0

def calc_quotient_familial(part_couple, nb_enfants, nb_autre) :
    quotient_familial = part_couple + (nb_enfants * 0.5) + (nb_autre * 0.5)
    return quotient_familial
def calc_majorations_quotient_familial(part_couple, nb_enfants, nb_autre) :
    return 0
def calc_quotient_familial_total(part_couple, nb_enfants, nb_autre) :
    return calc_quotient_familial(part_couple, nb_enfants, nb_autre) + calc_majorations_quotient_familial(part_couple, nb_enfants, nb_autre)

quotient_familial = calc_quotient_familial(part_couple,nb_enfants,nb_autre) + calc_majorations_quotient_familial(part_couple, nb_enfants, nb_autre)

if part_couple + nb_enfants + nb_autre == 1 :
    print("   Il y a ", part_couple + nb_autre + nb_enfants, " personne dans votre foyer fiscal. ")
else : 
    print ("   Il y a ", part_couple + nb_enfants + nb_autre, " personnes dans votre foyer fiscal. ")
print("   Il vous est donc attribué ", quotient_familial, " parts")

print(" Identification des revenus du contribuable")

exist_sal = ouinon("   Percevez-vous des revenus issus d'une activité salariée ?")
if exist_sal == True :
    if situation_couple == True :
        print("   DÉCLARANT 1 : ")
        sal_brut_1 = nombre("   Quel est le montant de vos salaires (avant prélèvement à la source) ?")
        print("   DÉCLARANT 2 : ")
        sal_brut_2 = nombre("   Quel est le montant de vos salaires (avant prélèvement à la source) ?")
        sal_brut = sal_brut_1 + sal_brut_2
    else :
        sal_brut = nombre("   Quel est le montant de vos salaires (avant prélèvement à la source) ?")
else : 
    sal_brut = 0

def calc_rnc_sal(sal_brut) :
    if sal_brut > 0 :
        rnc_sal = sal_brut * 0.9
    return rnc_sal
rnc_sal = calc_rnc_sal(sal_brut)
print (rnc_sal)

def calc_impôt(revenu_imposable) : 
    if revenu_imposable < 10777 :
        impôt_barème = 0
    elif 10778 <= revenu_imposable <= 27478 :
        impôt_barème
    return impôt_barème






