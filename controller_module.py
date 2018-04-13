import view_module

class Controller:
    """Sortuje paczki według ich wymiarów i układa w pasujące do siebie pary."""
    """Sort boxes and put them in suitable pairs."""
    
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight


    def put_data_into_objcts(self, data):
        # tworzy obiekty paczek i przenosi do nich dane przechowywane w słownikach
        # create objects for all boxes and put data into them from the dictionaries

        boxObjects = list()
        for i in range(len(data)):
            boxObject = Controller(data[i]["length"], data[i]["width"], data[i]["height"], data[i]["weight"])
            boxObjects.append(boxObject)
            
        return self.separate_garbage(boxObjects)


    def separate_garbage(self, boxObjects):
        # wyklucza paczki z anomaliami wymiarowymi z dalszego sortowania. Przechowuje paczki z anomaliami w 'garbageBoxes'
        # exclude boxes with anomalies in dimensions from the further sorting. Store the anomaly boxes in 'garbageBoxes'
        
        garbageBoxes = [box for box in boxObjects if box.width < 50 or box.width > 240 or box.length < 50 or box.length > 400 or box.height < 50 or box.height > 260]
        toSortBoxes = []

        for box in boxObjects:
            if box not in garbageBoxes:
                toSortBoxes.append(box)

        return self.sort_width(boxObjects, garbageBoxes, toSortBoxes)


    def sort_width(self, allBoxes, garbageBoxes, toSortBoxes):
        # grupuje paczki według ich szerokości i umieszcza w 4 sekcjach wymiarowych. Każda sekcja jest listą składającą się ze słowników. Każdy słownik to paczka
        # group boxes according to their width and put them into 4 dimensional sections. Each section is a list of dics. Each dic is a box
        
        bigsRaw = []
        equalsRaw = []
        middlesRaw = []
        smallsRaw = []
        
        for box in toSortBoxes:
            if 241 > box.width > 125:
                bigsRaw.append(box)
            elif 110 <= box.width <= 125:
                equalsRaw.append(box)
            elif 80 <= box.width < 110:
                middlesRaw.append(box)
            elif 50 <= box.width < 80:
                smallsRaw.append(box)
                        
        return self.sort_to_ascending_order(allBoxes, bigsRaw, equalsRaw, middlesRaw, smallsRaw, garbageBoxes)
        

    def sort_to_ascending_order(self, allBoxes, bigsRaw, equalsRaw, middlesRaw, smallsRaw, garbageBoxes):
        # sortuje wszystkie grupy paczek wg. szer. w porządku rosnącym
        # sort all the width groups in the ascending order
        
        sortWithLength = lambda x: x.length
        
        bigsOrdered = sorted(bigsRaw, key=sortWithLength)
        equalsOrdered = sorted(equalsRaw, key=sortWithLength)
        middlesOrdered = sorted(middlesRaw, key=sortWithLength)
        smallsOrdered = sorted(smallsRaw, key=sortWithLength)
            
        return self.sort_equals_length(allBoxes, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes)
        

    def sort_equals_length(self, allBoxes, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # w liście equalsOrdered układa paczki w pary wg. ich długości z tolerancją do 60 cm, usuwa sparowane paczki z equalsOrdered, następnie zwraca je w nowej liście: equalsSorted
        # put boxes in pairs within the equalsOrdered list by their length with the tolerance of 60 cm, remove the paired boxes from the equalsOrdered, then return them in a new list: equalsSorted
        
        equalsSorted = []

        def pop_and_append_equals():
     
            if len(equalsOrdered) > 2 and equalsOrdered[1].length - equalsOrdered[0].length < 60:

                thisEqual = equalsOrdered[0]
                thisEqual = equalsOrdered.index(thisEqual)

                elem1InPair = equalsOrdered.pop(thisEqual)
                elem2InPair = equalsOrdered.pop(thisEqual)
                equalsSorted.append(elem1InPair)
                equalsSorted.append(elem2InPair)

                return pop_and_append_equals()
                    
            elif len(equalsOrdered) > 2 and equalsOrdered[2].length - equalsOrdered[1].length < 60:                       

                thisEqual = equalsOrdered[1]
                thisEqual = equalsOrdered.index(thisEqual)
                                           
                elem1InPair = equalsOrdered.pop(thisEqual)
                elem2InPair = equalsOrdered.pop(thisEqual)
                equalsSorted.append(elem1InPair)
                equalsSorted.append(elem2InPair)
     
                return pop_and_append_equals()
                    
            elif len(equalsOrdered) == 2 and equalsOrdered[1].length - equalsOrdered[0].length < 60:

                thisEqual = equalsOrdered[0]
                thisEqual = equalsOrdered.index(thisEqual)

                elem1InPair = equalsOrdered.pop(thisEqual)
                elem2InPair = equalsOrdered.pop(thisEqual)
                equalsSorted.append(elem1InPair)
                equalsSorted.append(elem2InPair)
      
                return pop_and_append_equals()   

            else:
                return self.compare_bigs_to_middles_length(allBoxes, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes)   
                    
        return pop_and_append_equals()
        


    def compare_bigs_to_middles_length(self, allBoxes, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # układa paczki w pary z list: bigsOrdered i middlesOrdered, wg. ich długości z tolerancją do 100 cm. Usuwa sparowane paczki z list: bigsOrdered i middlesOrdered, następnie zwraca je w nowej liście: bigsWithMiddlesSorted
        # put boxes in pairs from the bigsOrdered and middlesOrdered lists by their length with the tolerance of 100 cm. Remove the paired boxes from the bigsOrdered and middlesOrdered lists, then return them in a new list: bigsWithMiddlesSorted
        
        sortWithWidth = lambda y: y.width
        bigsOrdered = sorted(bigsOrdered, key=sortWithWidth, reverse=True)
        middlesOrdered = sorted(middlesOrdered, key=sortWithWidth, reverse=True)
            
        bigsWithMiddlesSorted = []
            
        if len(bigsOrdered) >= 2 and len(middlesOrdered) >= 2:
                
            for big in bigsOrdered:
                bigIndex = bigsOrdered.index(big)
                        
                for middle in middlesOrdered:
                    if big.width + middle.width <=240 and big.length - middle.length <=100 and middle.length - big.length <= 100: # 100 to adjust??

                        middleIndex = middlesOrdered.index(middle)
                        elem2InPair = middlesOrdered.pop(middleIndex)
                        bigsWithMiddlesSorted.append(elem2InPair)
                                        
                        elem1InPair = bigsOrdered.pop(bigIndex)                
                        bigsWithMiddlesSorted.append(elem1InPair)
                
        return self.compare_bigs_to_smalls_length(allBoxes, bigsWithMiddlesSorted, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes)                    

        
    def compare_bigs_to_smalls_length(self, allBoxes, bigsWithMiddlesSorted, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # układa paczki w pary z list: bigsOrdered i smallsOrdered, wg. ich długości z tolerancją do 100 cm. Usuwa sparowane paczki z list: bigsOrdered i smallsOrdered, następnie zwraca je w nowej liście: bigsWithSmallsSorted
        # put boxes in pairs from the bigsOrdered and smallsOrdered lists by their length with the tolerance of 100 cm. Remove the paired boxes from the bigsOrdered and smallsOrdered lists, then return them in a new list: bigsWithSmallsSorted

        sortWithWidth = lambda y: y.width
        bigsOrdered = sorted(bigsOrdered, key=sortWithWidth, reverse=True)
        smallsOrdered = sorted(smallsOrdered, key=sortWithWidth, reverse=True)
            
        bigsWithSmallsSorted = []
            
        if len(bigsOrdered) >= 2 and len(smallsOrdered) >= 2:
                
            for big in bigsOrdered:
                bigIndex = bigsOrdered.index(big)
                        
                for small in smallsOrdered:
                    if big.width + small.width <=240 and big.length - small.length <=100 and small.length - big.length <= 100: # 100 to adjust

                        smallIndex = smallsOrdered.index(small)
                        elem2InPair = smallsOrdered.pop(smallIndex)
                        bigsWithSmallsSorted.append(elem2InPair)
                                        
                        elem1InPair = bigsOrdered.pop(bigIndex)                
                        bigsWithSmallsSorted.append(elem1InPair)

        return self.compare_equals_to_middles_length(allBoxes, bigsWithSmallsSorted, bigsWithMiddlesSorted, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes)      


    def compare_equals_to_middles_length(self, allBoxes, bigsWithMiddlesSorted, bigsWithSmallsSorted, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # układa paczki w pary z list: equalsOrdered i middlesOrdered, wg. ich długości z tolerancją do 100 cm. Usuwa sparowane paczki z list: equalsOrdered i middlesOrdered, następnie zwraca je w nowej liście: equalsWithMiddlesSortedLength
        # put boxes in pairs from the equalsOrdered and middlesOrdered lists by their length with the tolerance of 100 cm. Remove the paired boxes from the equalsOrdered and middlesOrdered lists, then return them in a new list: equalsWithMiddlesSortedLength

        sortWithWidth = lambda y: y.width
        equalsOrdered = sorted(equalsOrdered, key=sortWithWidth, reverse=True)
        middlesOrdered = sorted(middlesOrdered, key=sortWithWidth, reverse=True)

        equalsWithMiddlesSortedLength = []
            
        if len(equalsOrdered) >= 2 and len(middlesOrdered) >= 2:
                
            for equal in equalsOrdered:
                equalIndex = equalsOrdered.index(equal)
                        
                for middle in middlesOrdered:
                    
                    if equal.width + middle.width <=240 and equal.length - middle.length <=100 and middle.length - equal.length <= 100:

                        middleIndex = middlesOrdered.index(middle)
                        elem2InPair = middlesOrdered.pop(middleIndex)
                        equalsWithMiddlesSortedLength.append(elem2InPair)

                        elem1InPair = equalsOrdered.pop(equalIndex)                
                        equalsWithMiddlesSortedLength.append(elem1InPair)
                                                    
        return self.compare_equals_to_smalls_length(allBoxes, bigsWithMiddlesSorted, bigsWithSmallsSorted, equalsWithMiddlesSortedLength, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes) 
                

    def compare_equals_to_smalls_length(self, allBoxes, bigsWithMiddlesSorted, bigsWithSmallsSorted, equalsWithMiddlesSortedLength, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # put boxes in pairs from the equalsOrdered and smallsOrdered lists by their length with the tolerance of 100 cm. Remove the paired boxes from the equalsOrdered and smallsOrdered lists, then return them in a new list: equalsWithSmallsSortedLength
        # układa paczki w pary z list: equalsOrdered i smallsOrdered, wg. ich długości z tolerancją do 100 cm. Usuwa sparowane paczki z list: equalsOrdered i smallsOrdered, następnie zwraca je w nowej liście: equalsWithSmallsSortedLength

        sortWithLength = lambda x: x.length
        equalsOrdered = sorted(equalsOrdered, key=sortWithLength, reverse=True)
        equalsWithSmallsSortedLength = []
            
        if len(equalsOrdered) >= 2 and len(smallsOrdered) >= 2:
                
            for equal in equalsOrdered:
                equalIndex = equalsOrdered.index(equal)
                        
                for small in smallsOrdered:
                    if equal.length - small.length <=100 and small.length - equal.length <= 100:

                        smallIndex = smallsOrdered.index(small)
                        elem2InPair = smallsOrdered.pop(smallIndex)
                        equalsWithSmallsSortedLength.append(elem2InPair)
                                        
                        elem1InPair = equalsOrdered.pop(equalIndex)                
                        equalsWithSmallsSortedLength.append(elem1InPair)
                        
        return self.create_all_sorted_lists(allBoxes, bigsWithMiddlesSorted, bigsWithSmallsSorted, equalsWithMiddlesSortedLength, equalsWithSmallsSortedLength, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes)                    
        

    def create_all_sorted_lists(self, allBoxes, bigsWithMiddlesSorted, bigsWithSmallsSorted, equalsWithMiddlesSortedLength, equalsWithSmallsSortedLength, equalsSorted, bigsOrdered, equalsOrdered, middlesOrdered, smallsOrdered, garbageBoxes):
        # scala wszystkie utworzone listy w jedną listę: allSortedLists
        # put together all the created lists into one list: allSortedLists
        
        allSortedLists = []
            
        allSortedLists.append(bigsWithMiddlesSorted)
        allSortedLists.append(bigsWithSmallsSorted)
        allSortedLists.append(equalsWithMiddlesSortedLength)
        allSortedLists.append(equalsWithSmallsSortedLength)
        allSortedLists.append(equalsSorted)
        allSortedLists.append(bigsOrdered)
        allSortedLists.append(equalsOrdered)
        allSortedLists.append(middlesOrdered)
        allSortedLists.append(smallsOrdered)

        return self.create_all_sorted_boxes(allBoxes, allSortedLists, garbageBoxes)
            

    def create_all_sorted_boxes(self, allBoxes, allSortedLists, garbageBoxes):
        # tworzy nową listę: allSortedBoxes, następnie umieszcza w niej wszystkie paczki z list umieszczonych w allSortedLists
        # create a new list: allSortedBoxes and put into it all the boxes from all the lists of the allSortedLists
         
        allSortedBoxes = []

        for eachList in allSortedLists:
            for eachBox in eachList:
                allSortedBoxes.append(eachBox)

        return view_module.catch_controller_obj(allBoxes, allSortedBoxes, garbageBoxes)


controller_obj = Controller("undefined", "undefined", "undefined", "undefined")
