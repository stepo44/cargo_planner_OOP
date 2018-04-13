from controller_module import controller_obj


class Model_B:
    """Uruchamia wprowadzanie danych przez użytkownika: manualne wprowadzenie danych o każdej z paczek (wybór "B"). Analizuje spójność wprowadzonych danych."""
    """start data entry by user: manual typing of data of each box (user's choice "B"). Data cleaning."""
    
    def __init__(self, userChoice):
        self.userChoice = userChoice

    def number_of_boxes_input(self):
        # prosi użytkownika o wprowadzenie ilości paczek
        # ask user to type a number of boxex

        try:
            numberOfBoxes = int(input("Podaj ilość paczek do załadowania: "))
        except ValueError:
            print("\nPodana wartość jest nieprawidłowa. Używaj tylko pełnych cyfr.")
            return number_of_boxes_input()
        else:    
            if numberOfBoxes <= 0:
                print("\nUps...podałeś {}. To chyba literówka? Popraw się!".format(numberOfBoxes))
                return number_of_boxes_input()
                
            elif 0 < numberOfBoxes < 3:
                print("\nMasz za mało paczek, aby je sortować. To za łatwe dla mnie!:p Wróć jak będziesz miał ich trochę więcej...:)")  
                return number_of_boxes_input()
                
            elif numberOfBoxes > 100:
                print("\nTrochę przesadziłeś...Miej litość i zmniejsz ilość chociaż do 100 sztuk. Merci:)")
                return number_of_boxes_input()
            
            else: return self.input_data_processing(numberOfBoxes)
            

    def input_data_processing(self, numberOfBoxes):
        # definiuje 4 funkcje pobierające dane odnośnie każdej paczki od użytkownika, odpowiednio: dł., szer., wys., waga
        #   iteruje na każdej z paczek:
        #       - iworzy słownik dla każdej paczki
        #       - pobiera dane odnośnie każdej paczki od użytkownika i umieszcza je w utworzonym słowniku
        #   umieszcza wszystkie słowniki w jednej liście

        # define 4 functions that get user input for each box, respectively, about: length, width, height, weight
        #   loop over boxes:
        #       - create a dic for each box
        #       - get the input data for each box and put it into a dic
        #   put all the created dics into one list

        entryBoxes = []
        # length:
        # długość:    
        def entry_length_clear(length):
            
            try:
                length = int(length)
                if length < 0:
                    raise ValueError(print("Długość nie może mieć watości ujemnej."))
            except ValueError:
                length = input("Podaj długość w formie pełnych cyfr bez wartości dziesiętnych...")    
                return entry_length_clear(length)
            else:
                if length > 400:
                    length = input("Długość paczki jest za duża, max. 400 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_length_clear(length)

                elif length < 50:
                    length = input("Długość paczki jest za mała, min. 50 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_length_clear(length)
                 
                lengthClear = length
                return length
        # width:
        # szerokość:
        def entry_width_clear(width):
            
            try:
                width = int(width)
                if width < 0:
                    raise ValueError(print("Szerokość nie może mieć watości ujemnej."))
            except ValueError:
                width = input("Podaj szerokość w formie pełnych cyfr bez wartości dziesiętnych...")    
                return entry_width_clear(width)
            else:   
                if width > 240:
                    width = input("Szerokość paczki jest za duża, max 240 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_width_clear(width)

                elif width < 50:
                    width = input("Szerokość paczki jest za mała, min. 50 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_width_clear(width)

                widthClear = width 
                return widthClear
        # height:
        # wysokość:
        def entry_height_clear(height):
            
            try:
                height = int(height)
                if height < 0:
                    raise ValueError(print("Wysokość nie może mieć wartości ujemnej."))
            except ValueError:
                height = input("Podaj wysokość w formie pełnych cyfr bez wartości dziesiętnych...")    
                return entry_height_clear(height)
            else:    
                if height > 260:
                    height = input("Wysokość paczki jest za duża, max 260 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_height_clear(height)

                height = int(height)
                if height < 50:
                    height = input("Wysokość paczki jest za mała, min. 50 cm. Przepakuj i wprowadź ponownie: ")
                    return entry_height_clear(height)

                heightClear = height
                return heightClear
        # weight:
        # waga:
        def entry_weight_clear(weight):
            
            try:
                weight = int(weight)
                if weight < 0:
                    raise ValueError(print("Waga nie może mieć watości ujemnej."))
            except:
                weight = input("Podaj wagę w formie pełnych cyfr bez wartości dziesiętnych...")
                return entry_weight_clear(weight)
            else:    
                if weight > 24000:
                    weight = input("Waga paczki jest za duża. Przepakuj i wprowadź ponownie: ")
                    return entry_weight_clear(weight)

                weightClear = weight 
                return weightClear

        for box in range(1, int(numberOfBoxes)+1):
            # pobiera dane od użytkownika i umieszcza je w słownikach
            # get input from user and put it into dicts 
            
            length = input("\nPodaj długość {} paczki (cm): ".format(str(box)))
            lengthClear = entry_length_clear(length)
                 
            width = input("Podaj szerokość {} paczki (cm): ".format(str(box)))
            widthClear = entry_width_clear(width)
            
            height = input("Podaj wysokość " + str(box) + " paczki (cm): ")
            heightClear = entry_height_clear(height)
            
            weight = input("Podaj wagę {} paczki (kg): ".format(str(box)))
            weightClear = entry_weight_clear(weight)
            
            dic = {'length': '', 'width': '', 'height': '', 'weight': ''}
            dic['length'] = lengthClear
            dic['width'] = widthClear
            dic['height'] = heightClear
            dic['weight'] = weightClear
            
            entryBoxes.append(dic)

        return self.check_total_weight_limit_from_manual_entry(entryBoxes)
        

    def check_total_weight_limit_from_manual_entry(self, entryBoxes):
        # sprawdza dopuszczalny limit wagowy na naczepie (max 24000kg); sumuje wagi wszystkich paczek
        # check the weight limit (24000kg max allowed on a trailer) by adding weights of all boxes
        
        totalWeight = sum([box['weight'] for box in entryBoxes])

        if totalWeight > 24000:
            weighSurplus = totalWeight - 24000
            input("\nŁączna waga twoich paczek przekracza dopuszczalną ładowność ciężarówki, która wynosi max. 24 tony. Naczepa przeładowana jest o {} kg. Usuń część paczek i spróbuj jeszcze raz.\n".format(weighSurplus))
            return self.user_input_choice()
            
        else: self.request_for_sorting_nr_b(entryBoxes)


    def request_for_sorting_nr_b(self, entryBoxes):
        # informuje użytownika, że plik został prawidłowo zapisany i jest gotowy do rozpoczęcia sortowania
        # inform user that the file has been succefully uploaded and is ready to start sorting
        
        input("\nPaczki zostały wprowadzone. Kliknij ENTER, aby uruchomić sortowanie...\n")
        return controller_obj.put_data_into_objcts(entryBoxes)


model_b_obj = Model_B("undefined")
