import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Las píldoras sólo de progestina (PSP) son anticonceptivos que se toman una vez al día para prevenir el embarazo. Las PSP no contienen estrógeno.', [
                 'pildoras', 'Anticonceptivos', 'Altrnativas', ], single_response=True)
        response('Hacen que el moco cervical se espese  Dificultan la penetración de los espermatozoides.  Hacen cambiar el endometrio (Hacen que la implantacComo funciona la pspión sea menos probable.  Inhiben parcialmente la ovulación  en el 60% de los ciclos .', [
            'funcion la psp', 'Que ase la psp', 'Efectos de la psp', ], single_response=True)
        response('Estoy bien y tu?', [
                 'como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('El condón femenino es una funda delgada, suave y holgada de plástico de poliuretano que se usa para cubrir la vagina. Tiene dos anillos flexibles: un anillo interior en el extremo cerrado, que se usa para insertar y colocar el dispositivo dentro de la vagina, y un anillo exterior, que queda fuera de la vagina y cubre los genitales externos. Dado que el dispositivo está hecho de poliuretano, puede usarse con cualquier tipo de lubricante sin dañar su integridad.', [
                 'condon', 'anticonceptivos', 'prinsipal', ], single_response=True)
        response('Los condones constituyen una barrera física e impiden que los espermatozoides entren en el aparato reproductor femenino. También constituyen una barrera contra los microorganismos infecciosos y previenen la transmisión de ETS/VIH de un compañero sexual a otro.', [
            'condones', 'usocondon', 'Accion.codon', ], single_response=True)
        response('Toda mujer de cualquier edad de procrear o que haya tenido cualquier número de partos que: 1. Desee usar este método anticonceptivo 2. No pueda o no deba tomar píldoras que contienen estrógeno 3. Esté amamantando (Las PSP no afectan a la cantidad ni la calid pero Las mujeres que tienen las siguientes condiciones :  Embarazo, Cáncer mamario actual', [
             'criteriopsp', ], single_response=True)
        
        response('1.Los hombres y las mujeres que corren el riesgo de contraer ETS/VIH, 2.Los hombres y las mujeres de cualquier edad de procrear y que hayan tenido cualquier número de partos, que deseen usar condones como método regular de anticoncepción 3.Los hombres y las mujeres que practican el sexo con frecuencia', [
            'criteriocondon', ], single_response=True)
        response('El DIU es un dispositivo pequeño de plástico que se inserta en la cavidad uterina de la mujer para prevenir el embarazo. El DIU que contiene cobre (CuT 380A) es el que más se usa y su eficacia dura hasta 10 años.', [
            'diu' ,'alternativa2', ], single_response=True)
        response('Interfiere con el proceso reproductor antes de que el óvulo llegue a la cavidad uterina. (Afecta a la viabilidad y la motilidad de los espermatozoides, con lo cual impide la fecundación.) Se desconoce el mecanismo de acción exacto.', [
            'usodiu', 'usoAlternativa2', ], single_response=True)
        response('Las mujeres de cualquier edad de procrear o que hayan tenido cualquier número de partos, incluidas las jóvenes y las nulíparas Las mujeres que no tienen contraindicaciones para el uso del DIU pero Las mujeres que tienen las siguientes condiciones: 1.Embarazo 2.Infección después de un parto o de un aborto 3.Sangrado vaginal inexplicado (necesita una evaluación)4.Cáncer del cuello uterino, del endometrio o del ovario 5.EPI, actual o en los últimos tres meses 6.ETS (cervicitis purulenta), actual o en los últimos tres meses 7.Enfermedad trofoblástica gestacional maligna 8.Cavidad uterina malformada (incompatible con la inserción del DIU) 9.Tuberculosis pélvica diagnosticada.', [
            'criteriodiu', 'riesgodiu', ], single_response=True)
        response('Es un procedimiento quirúrgico en el que las trompas de Falopio, que transportan el óvulo desde el ovario hasta el útero, se bloquean (se atan y se cortan, se cauterizan, se cierran con un anillo o grapa). La esterilización pone fin a la fertilidad permanentemente (sólo 2% de fracaso después de 10 años).', [
            'esteril', 'bloqueo', ], single_response=True)
        response('El bloqueo de las trompas de Falopio impide que los espermatozoides se unan con el óvulo, y por consiguiente se previene la fertilización.', [
            'usoesteril', 'trompas', ], single_response=True)
       
             
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))
