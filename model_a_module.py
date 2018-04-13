from controller_module import controller_obj


class Model_A:
    """Uruchamia wprowadzanie danych przez użytkownika: eksport pliku tekstowego z danymi (wybór "A"). Analizuje spójność wprowadzonych danych."""
    """start data entry by user: upload of a text file with data (user's choice "A"). Data cleaning."""
    
    def __init__(self, boxes):
        self.boxes = boxes

    
    def form_pattern_display(self):
        # pobiera plik tekstowy wskazany przez użytkownika
        # get a text file from user as input   
    
        dataFile = input("""Podaj nazwę pliku tekstowego z danymi do eksportu. Pamiętaj, aby wymiary paczek w pliku podane były według następującego wzoru:
        Paczka nr 1; długość: ... cm; szerokość: ... cm; wysokość: ... cm; waga ... kg 
        Paczka nr 2; długość: ... cm; szerokość: ... cm; wysokość: ... cm; waga ... kg
        Paczka nr 3; długość: ... cm; szerokość: ... cm; wysokość: ... cm; waga ... kg
        itd...\n""")
    
        return self.count_lines_in_file(dataFile)
   
    
    def count_lines_in_file(self, dataFile):
        # liczy ilość wierszy w pliku tekstowym i na tej podstawie podaje ilość paczek do dalszego sortowania (1 wiersz = 1 paczka)
        # count a number of lines in the text file, then get the number of boxes (1 line = 1 box)
        
        numLines = 0
        try:
            data = open(dataFile, 'r')
        except OSError:  # FileNotFoundError is a subclass of OSError
            dataFile = input('\nPlik, o podanej nazwie, nie został odnaleziony. Wprowadź prawidłową nazwę: "data.txt"\n')
            self.count_lines_in_file(dataFile)

        try:      
            for line in data:
                numLines += 1
        except UnboundLocalError:
            pass

        else: self.create_dicts_for_boxes_from_file(dataFile, numLines)


    def create_dicts_for_boxes_from_file(self, dataFile, numLines):
        # dla każdej z paczek tworzy słownik zawierający klucze dla: nr paczki, jej wymiarów i wagi
        # create an empty dic for each box, containing keys for: the box number, its dimensions and weight
        
        allBoxesFromFile = []
        for line in range(0, numLines):
            box = {'boxNumber': '', 'length': '', 'width': '', 'height': '', 'weight': ''}
            allBoxesFromFile.append(box)
                    
        return self.put_boxes_from_file_into_list_of_dicts(allBoxesFromFile, dataFile)
      

    def put_boxes_from_file_into_list_of_dicts(self, allBoxesFromFile, dataFile):
        # odczytuje dane paczek (nr paczki, wymiary, wagę) i kopiuje je do utworzonych, pustych słowników
        # read boxes data (nr of box, dimensions, weight) from the file and put it into the created empty dics
        
        file = open(dataFile, 'r')
        lineCounter = 0
            
        for eachLine in file:
            try:
                (boxNumber, length, width, height, weight) = eachLine.split(';')
            except ValueError:
                input("\nUps...coś poszło nie tak z odczytywaniem danych. Upewnij się, że dane każdej z paczek zaczynają się od nowego akapitu, a ich poszczególne wymiary oddzielone są od siebie średnikami \";\".\nNastępnie ponownie podaj nazwę pliku. \n")
                return self.count_lines_in_file(dataFile)

            eachLineList = []
            eachLineList.append(boxNumber)
            eachLineList.append(length)
            eachLineList.append(width)
            eachLineList.append(height)
            eachLineList.append(weight)

            for eachString in eachLineList:

                eachStringList = []
                            
                for letter in str(eachString):

                    if letter.isdigit():
                        eachStringList.append(letter)

                cleanStringDimension = int((''.join(eachStringList)))

                try:                
                    if eachLineList.index(eachString) == 0:         
                        allBoxesFromFile[lineCounter]['boxNumber']=cleanStringDimension

                    elif eachLineList.index(eachString) == 1:         
                        allBoxesFromFile[lineCounter]['length']=cleanStringDimension

                    elif eachLineList.index(eachString) == 2:
                        allBoxesFromFile[lineCounter]['width']=cleanStringDimension
                                                        
                    elif eachLineList.index(eachString) == 3:         
                        allBoxesFromFile[lineCounter]['height']=cleanStringDimension

                    elif eachLineList.index(eachString) == 4:         
                        allBoxesFromFile[lineCounter]['weight']=cleanStringDimension

                except IndexError:
                    pass

                del eachStringList, cleanStringDimension
                            
            lineCounter += 1

        return self.check_total_weight_limit_from_exported_file(allBoxesFromFile)


    def check_total_weight_limit_from_exported_file(self, allBoxesFromFile):
        # sprawdza dopuszczalny limit wagowy na naczepie (max 24000kg); sumuje wagi wszystkich paczek
        # check the weight limit (24000kg max allowed on a trailer) by adding weights of all boxes

        totalWeight = sum([box['weight'] for box in allBoxesFromFile])

        if totalWeight > 24000:
            weightSurplus = totalWeight - 24000
            input("\nŁączna waga twoich paczek przekracza dopuszczalną ładowność ciężarówki, która wynosi max. 24 tony. Naczepa przeładowana jest o {} kg. Usuń część paczek i spróbuj jeszcze raz.\n".format(weightSurplus))
            return view.user_input_choice()
            
        else: self.boxes = allBoxesFromFile

        return self.request_for_sorting_nr_a(allBoxesFromFile)


    def request_for_sorting_nr_a(self, allBoxesFromFile):
        # informuje użytownika, że plik został prawidłowo zapisany i jest gotowy do rozpoczęcia sortowania
        # inform user that the file has been succefully uploaded and is ready to start sorting
            
        input("\nTwój plik został prawidłowo wyeksportowany. Kliknij ENTER, aby uruchomić sortowanie paczek.")  

        return controller_obj.put_data_into_objcts(allBoxesFromFile)




model_a_obj = Model_A("undefined")

