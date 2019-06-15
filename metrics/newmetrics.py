class Simple_Metrics():

    def h_index(newCitations):
        newCitations.sort(reverse= True)
        counter= 0
        for i in (newCitations):
            counter+= 1
            if (counter >= i):  
                h_index= counter
                break
        return (h_index)

    def g_index(newCitations):
        newCitations.sort(reverse= True)
        counter= 0
        addupC= 0
        for i in newCitations:
            counter+= 1
            addupC+= i
            if (addupC >= counter**2):
                g_index= counter
                continue
            else:
                break


