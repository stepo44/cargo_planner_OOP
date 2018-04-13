import model_a_module
import model_b_module

class View:

    object = None
    
    """Interfejs użytkownika.
       1. Pobiera preferencje użytkownika odnośnie sposobu wprowadzania danych o ładunku.
       2. Podaje wzór według, którego użytkownik powinnien wprowadzać dane.
       3. Wyświela wynik sortowania paczek (ułożenie w parach na naczepie) i końcowe komunikaty do użytkownika."""

    """User interface.
       1. Get the user's preference on the boxes data entry.
       2. Follow the user while typing data.
       3. Output: sorted data (boxes put in pairs on trailer) and final comments to user."""
    
    def __init__(self, userChoice): 
        self.userChoice = userChoice
    
    def user_input_choice(self):
        # pobiera preferencje użytkownika odnośnie sposobu wprowadzenia danych o paczkach. Dwie opcje do wyboru: plik tekstowy lub ręczne wpisywanie
        # get the user's preference on the data entry of boxes. Two options possible: text file upload or manual entry
    
        userChoice = input("Wybierz opcję, w jaki sposób chcesz wprowadzić dane o wymiarach twoich paczek: \n \
        1. Export pliku tekstowego z gotowymi danymi - kliknij 'A'.\n \
        2. Manualne wprowadzenie wymiarów i wagi każdej z paczkek - kliknij 'B'\n")

        return self.user_input_choice_check(userChoice)


    def user_input_choice_check(self, userChoice):
        # zapisuje preferencje użytkownika w atrybucie obiektu "view" klasy View
        # put the user'preference into an attribute of the object "view" of class View
    
        if userChoice == "A" or userChoice == "a":
            self.userChoice = "a"
            
        elif userChoice == "B" or userChoice == "b":
            self.userChoice = "b"
        
        else:
            userChoice = input("Wybierz prawidłowo jedną z dwóch opcji, wpisując 'A' lub 'B'...")
            return self.user_input_choice_check(userChoice) 

        return self.input_choice_action()
    

    def input_choice_action(self):
        # uruchamia wprowadzanie danych przez użytkownika oraz analizę ich spójności
        # start data entry by user and data cleaning

        if self.userChoice == "a":
            model_a_module.model_a_obj.form_pattern_display()

        elif self.userChoice == "b":
            model_b_module.model_b_obj.number_of_boxes_input()

        else:
            userChoice = input("Wybierz prawidłowo jedną z dwóch opcji, wpisując 'A' lub 'B'...")
            return self.user_input_choice()        


    def create_output(self, allBoxes, allSortedBoxes, garbageBoxes):
        # tworzy output string dla każdej z paczek i umieszcza je w liście: allSortedBoxesString
        # create output strings for each of boxes and put them into a list: allSortedBoxesString

        allSortedBoxesString = []
        
        for sortedBox in allSortedBoxes:
            for box in allBoxes:
                if sortedBox == box:
                    boxNumber = str(allBoxes.index(box)+1)
                    sortedBoxString = "paczka nr {} o wymiarach: {}(szer) x {}(dł) x {}(wys)".format(boxNumber, str(sortedBox.length), str(sortedBox.width), str(sortedBox.height))
                    allSortedBoxesString.append(sortedBoxString)
                                    
        return self.print_output(allBoxes, allSortedBoxesString, garbageBoxes)
        

    def garbage_output(self, allBoxes, garbageBoxes):
        # tworzy output string dla każdej z paczek i umieszcza je w liście: allSortedBoxesString
        # create output strings for each of boxes in the garbageBoxes and put them into a list: garbageBoxesString
        
        garbageBoxesString = []
        for garbageBox in garbageBoxes:
            for box in allBoxes:
                if garbageBox == box:
                    boxNumber = str(allBoxes.index(box)+1)
                    garbageBoxeString = "paczka nr {} o wymiarach: {}(dł) x {}(szer) x {}(wys)".format(boxNumber, str(garbageBox.length), str(garbageBox.width), str(garbageBox.height)) 
                    garbageBoxesString.append(garbageBoxeString)

        for garbageString in garbageBoxesString:
            print(garbageString)

        print("\nPamiętaj!. Wymiary naczepy w ciężarówce typu 'plandeka standard', zwanej potocznie 'TIR-em', to: 13,4(dł), 2,45(szer) i 2,8(wys) metra.\
                  \nTwoje paczki muszą mieścić się w następujących limitach:\nDŁUGOŚĆ: nie mniejsza niż 50 i nie większa niż 400 cm,\
                  \nSZEROKOŚĆ: nie mniejsza niż 50 i nie większa niż 240 cm,\nWYSOKOŚĆ: nie większa niż 260 cm,\noraz ŁĄCZNA WAGA PACZEK: nie większa niż 24 tony.\n")

        
    def print_output(self, allBoxes, allSortedBoxesString, garbageBoxes):
        # tworzy końcowy output do użytkownika: print dane z allSortedBoxesString i garbageBoxesString
        # create the final output to user: print data from the allSortedBoxesString and the garbageBoxesString

        for boxString in allSortedBoxesString:
            boxIndex = allSortedBoxesString.index(boxString)
            if boxIndex < len(allSortedBoxesString) - 1:
                if boxIndex == 0:
                    print("\n\n      SORTOWANIE ZAKOŃCZONE \n\nUłóż paczki względem ich szerokości w następujących parach:","\n\n", boxString, " i ", allSortedBoxesString[allSortedBoxesString.index(boxString)+1])
                elif boxIndex % 2 == 0:
                    print(boxString, " i ", allSortedBoxesString[allSortedBoxesString.index(boxString)+1])

        if len(garbageBoxes) == 0:
            try:
                print("Bez pary, luzem, pozostała {} \n".format(allSortedBoxesString[len(allSortedBoxesString)-1]))
            except IndexError:
                pass
        else:
            try:
                print("Bez pary, luzem, została {}.\n\nNiezaplanowane zostały również paczki z wymiarami, które były zbyt małe lub zbyt duże, aby móc załadować je na ciężarówkę:".format(allSortedBoxesString[len(allSortedBoxesString)-1]))
                self.garbage_output(allBoxes, garbageBoxes)
            except IndexError:
                pass
                
        reload = input("\nKliknij ENTER, jeśli chcesz wprowadzić nowy zestaw paczek \n")
        print("\n\n\n\n      <<< ROZPOCZYNAMY NOWE SORTOWANIE >>>\n")

        return self.user_input_choice() 


def start():
    view_obj = View("undefined")
    View.object = view_obj
    return view_obj.user_input_choice()



def catch_controller_obj(allBoxes, allSortedBoxes, garbageBoxes):
    View.object.create_output(allBoxes, allSortedBoxes, garbageBoxes)
