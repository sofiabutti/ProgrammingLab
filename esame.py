from csv import reader

#classe per le eccezioni
class ExamException(Exception):
        pass
#classe per la lettura da file
class CSVTimeSeriesFile:
    def __init__(self, name): #istanziata sul nome del file tramite la variabile name 
        if((isinstance(name,str))!=True or name==""):
        #controllo che il parametro passato sia una stringa    
            raise ExamException("Wrong file name")
        else:    
            self.name = name

    def get_data(self): #legge csv e restituisce lista di liste
        time_series =[] #creo una lista per i valori che dovrò restituire
        try:
            with open(self.name, 'r') as f: #apro file
                csv = reader(f) #restituisce un oggetto lettore che cicla per tutte le righe del file csv 
                list_of_rows = list(csv) #creo da csv lista di liste
            return (list_of_rows)  #restituisce lista di liste
        except:
            print("Unable to read file")

        #ciclo i time_series da resituire per controllare la correttezza
        for i in range(len(time_series)-1): # nel range metti la lunghezza di ts -1
            if(time_series[i][0]>=time_series[i+1][0]):
                raise ExamException("Non-ordered measurement history or presence of duplicates")    
        return time_series 

#Con la formula che data riesco a capire se quella osservazione di temperatura appartiene al giorno della precedente:
#- se si mi salvo i valori della temperatura
#- se no calcolo min,max,media e li salvo in una lista che metto nella lista che stamperò alla fine, quindi svuoto la lista v e gli aggiungo la temperatura di quel giorno 
        
def daily_stats(time_series): 
    v = [] #lista che contiene inizio vari giorni
    day_list = [] #lista dele statistiche giornaliere
    head = ["min", "max", "media"]
    day_list.append(head) #aggiungo head alla lista
    epoch = 0
    temp = 1
    time_series.remove(time_series[0]) #rimuovo elemento da time_series

    day_selected = int(time_series[0][epoch]) #orario selezionato

    for hour in time_series:
        current_day = int(hour[epoch]) - (int(hour[epoch]) % 86400) #giorno corrente di riferimento per le misurazioni

        if current_day == day_selected: #finchè sono nella stessa giornata
            try:
                v.append(float(hour[temp]))  #salvo la temperatura dell'ora 

            except:
                print("Cannot save hour")    
        else:
            day_values = [min(v), max(v), (sum(v)/len(v))] #calcoli del giorno
            day_list.append(day_values) #aggiungo valori alla lista
            
            day_selected = current_day #cambio giorno di riferimento
            v = [] #svuoto lista
            v.append(float(hour[temp])) #aggiungo nuova temperatura
            
    return(day_list) 



#===================
#CORPO DEL PROGRAMMA
#=================== 


""" time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
lista = daily_stats(time_series)
for i in lista:
    print(i) """
           