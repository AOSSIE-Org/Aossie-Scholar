import datetime
now = datetime.datetime.now()



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
        return(g_index)

    def m_index(h_index, ist_pub_year):
        now = datetime.datetime.now()
        cur_year= now.year
        print (cur_year, ist_pub_year)
        time_gap= cur_year-int(ist_pub_year)+1
        mindex= float(h_index/time_gap)
        m_index= round(mindex, 2)
        return (m_index)



