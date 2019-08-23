#from ROOT import *
#from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
#from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
import math
from math import fsum,fabs
from array import array
from scipy.cluster.hierarchy import fclusterdata
import sys
import os
import re


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from pylab import figure, axes, pie, title, show

#from matplotlib.ticker import PercentFormatter


#gROOT.Reset()
#a = TRandom()
#a.SetSeed(1242)

class calciatore:
    m_name = 0
    m_cash = 350

    def __init__(self):
      '''
      self.m_Nome = "VUOTO"
 
      self.m_Nome = 0  #nome
      self.m_R = 0   #ruolo
      self.m_Rm = 0   #ruolo MANTRA

      self.m_Qi = 0  #Quotazione Iniziale
      self.m_Qa = 0  #Quotazione Attuale
      self.m_Squadra = 0  #squadra
      '''

      #R Giocatore MP  MV  Go  As  Am  Es  Au  Rig Resa  Squadra Pr  Ti  Qu
      self.m_R=0  #Ruolo
      self.m_Id=0 #Giocatore
      self.m_Mv=0 #MP
      self.m_Mf=0 #MV
      self.m_Gf=0 #Goal fatti
      self.m_Ass=0 #Assist
      self.m_Amm=0 #Ammonizioni
      self.m_Esp=0 #Espulsione
      self.m_A=0   #Autoreti
      self.m_Rc=0  #Rigori parai /fatti
      self.m_Resa =0 #Resa
      self.m_Squadra=0
      self.m_Pg=0  #Presenze
      self.m_PgT=0  #Presenze Titolare 
      self.m_Qi = 0  #Quotazione Iniziale
      self.m_RatioVp = 0#float(self.m_Mv)/float(self.m_Pg)
      self.m_RatioVG = 0#float(self.m_Mv)/float(self.m_Gf)
      #self.m_RatioGPg = 0#float(self.m_Mv)/float(self.m_Gf)

    def SetAll(self,stat_gioc):

       self.m_R = stat_gioc[0]
       self.m_Id = stat_gioc[1]
       self.m_Mv = stat_gioc[2]
       self.m_Mf = stat_gioc[3]
       self.m_Gf = stat_gioc[4]
       self.m_Ass = stat_gioc[5]
       self.m_Amm = stat_gioc[6]
       self.m_Esp = stat_gioc[7]
       self.m_A = stat_gioc[8]
       self.m_Rc = stat_gioc[9]
       self.m_Resa = stat_gioc[10]
       self.m_Squadra = stat_gioc[11]
       self.m_Pg = stat_gioc[12]
       self.m_PgT = stat_gioc[13]
       self.m_Qi = stat_gioc[14]
       self.m_RatioVp = 0#float(self.m_Mv)/float(self.m_Pg)
       self.m_RatioVG = 0#float(self.m_Mv)/float(self.m_Gf)
       #self.m_RatioGPg = 0#float(self.m_Mv)/float(self.m_Gf)



    def Print(self):
        #print "Nome ",self.m_Nome," R ",self.m_R," RM ",self.m_Rm," Qi ",self.m_Qi," Qa ",self.m_Qa," Squadra ",self.m_Squadra
        #print "Nome ",self.m_Nome," Squadra ",self.m_Squadra," m_Mf ",self.m_Mf," m_Gf ",self.m_Gf," m_Gs ",self.m_Gs," m_Pg ",self.m_Pg," m_Ass ",self.m_Ass," m_RatioVp ",self.m_RatioVp, " m_RatioVG ",self.m_RatioVG
        #print "Nome ",self.m_Nome," Squadra ",self.m_Squadra," m_Mf ",self.m_Mf," m_Gf ",self.m_Gf," m_Gs ",self.m_Gs," m_Pg ",self.m_Pg," m_Ass ",self.m_Ass," m_RatioVp ",self.m_RatioVp, " m_RatioVG ",self.m_RatioVG
        #print " Ruolo ",self.m_R, " Giocatore ",self.m_Id, " MP ",self.m_Mv, " MV ",self.m_Mf, " Goal fatti ",self.m_Gf, " Assist ",self.m_Ass, " Ammonizioni ",self.m_Amm, " Espulsione ",self.m_Esp, " Autoreti ",self.m_A, " Rigori parai /fatti ", self.m_Rc, " resa ",self.m_Resa, " squadra ",self.m_Squadra, " Presenze ",self.m_Pg, " Presenze Titolare  ",self.m_PgT, " Quotazione Iniziale ",self.m_Qi
        print "  ",self.m_Id, " MP ",self.m_Mv, " MV ",self.m_Mf, " Goal fatti ",self.m_Gf, " Assist ",self.m_Ass, " Ammonizioni ",self.m_Amm, " Espulsione ",self.m_Esp, " Autoreti ",self.m_A, " squadra ",self.m_Squadra, " Presenze ",self.m_Pg, " Presenze Titolare  ",self.m_PgT

    def PrintEmpyt(self):
        #print "Nome ",self.m_Nome," R ",self.m_R," RM ",self.m_Rm," Qi ",self.m_Qi," Qa ",self.m_Qa," Squadra ",self.m_Squadra
        #print "Nome ",self.m_Nome," Squadra ",self.m_Squadra," m_Mf ",self.m_Mf," m_Gf ",self.m_Gf," m_Gs ",self.m_Gs," m_Pg ",self.m_Pg," m_Ass ",self.m_Ass," m_RatioVp ",self.m_RatioVp, " m_RatioVG ",self.m_RatioVG
        #print "Nome ",self.m_Nome," Squadra ",self.m_Squadra," m_Mf ",self.m_Mf," m_Gf ",self.m_Gf," m_Gs ",self.m_Gs," m_Pg ",self.m_Pg," m_Ass ",self.m_Ass," m_RatioVp ",self.m_RatioVp, " m_RatioVG ",self.m_RatioVG
        #print " Ruolo ",self.m_R, " Giocatore ",self.m_Id, " MP ",self.m_Mv, " MV ",self.m_Mf, " Goal fatti ",self.m_Gf, " Assist ",self.m_Ass, " Ammonizioni ",self.m_Amm, " Espulsione ",self.m_Esp, " Autoreti ",self.m_A, " Rigori parai /fatti ", self.m_Rc, " resa ",self.m_Resa, " squadra ",self.m_Squadra, " Presenze ",self.m_Pg, " Presenze Titolare  ",self.m_PgT, " Quotazione Iniziale ",self.m_Qi
        print "  ",self.m_Id, "  ",self.m_Mv, "  ",self.m_Mf, "  ",self.m_Gf, "  ",self.m_Ass, "  ",self.m_Amm, "  ",self.m_Esp, "  ",self.m_A, "  ",self.m_Squadra, "  ",self.m_Pg, "   ",self.m_PgT


    def GetName(self):

        return self.m_Id

    def GetCash(self):
        return self.m_cash

    def SetName(self,name):
        self.m_Id = name

    def SetCash(self,cash):
        self.m_cash = cash
    def SetRatio(self):
        if(float(self.m_Pg)>0):
          self.m_RatioVp = float(self.m_Mv)/float(self.m_Pg)
          self.m_RatioVG = float(self.m_Gf)/float(self.m_Pg)
          #self.m_RatioGPg = float(self.m_Gs)/float(self.m_Pg)


        else:
          self.m_RatioVp = 0
          self.m_RatioVG = 0
          #self.m_RatioGPg = 0
class Lista_Calciatori:

    
    def __init__(self):
        self.m_Ruolo = "VUOTO"
        self.m_listcalc = []
        self.m_Ruolo = 0
        self.m_Media = 0    
        self.m_RMS = 0
        #self.m_listcalc.append( calciatore())
    def AddDiff(self, arg):
        self.m_listcalc.append(arg)
    def DoStat(self):
        for x in range(len(self.m_listcalc)):
          self.m_listcalc[x].SetRatio()

    def PrintDiff(self):
        for x in range(len(self.m_listcalc)):
          #if(float(self.m_listcalc[x].m_Pg)>4):
          dist = float(self.m_listcalc[x].m_Mv) - float(self.m_Media)
          if(dist/self.m_RMS>0.75 and float(self.m_listcalc[x].m_Pg)>9):
           self.m_listcalc[x].Print()
           #self.m_listcalc[x].PrintEmpyt()

           
    def PrintOne(self,arg):
        self.m_listcalc[arg].Print()
    def CalcMedia(self):
        voto = 0
        media = 0
        non_zero = 0
        for x in range(len(self.m_listcalc)):
         voto = float(self.m_listcalc[x].m_Mv)
         media = media+voto
         if (voto!=0):
          non_zero = non_zero+1
        self.m_Media= media / non_zero
    def CalcRMS(self):
        voto = 0
        delta = 0
        RMS = 0
        non_zero = 0
        for x in range(len(self.m_listcalc)):
         voto = float(self.m_listcalc[x].m_Mv)
         delta = voto - self.m_Media
         if (voto!=0):
          RMS = RMS + delta*delta
          non_zero = non_zero+1
        self.m_RMS = (RMS / non_zero)**(0.5)
    def FindName(self,arg):
      position = -99999
      for x in range(len(self.m_listcalc)):
         name = self.m_listcalc[x].m_Id
         if(arg in name): 
          #print "trovato ",name,": ",x
          position = x
      return position

    def MeasureDistance(self,arg):
        pos = self.FindName(arg)
        if (pos> -99999):
          sigma = float(self.m_listcalc[pos].m_Mv) - self.m_Media
          segno = math.copysign(1,float(self.m_listcalc[pos].m_Mv) - self.m_Media)
          appo = segno*(sigma*sigma)**(0.5)
          return appo / self.m_RMS
        else:
          return -99999
    def FindMax_Qa(self):
    	appo = 0
    	index = 0
        for x in range(len(self.m_listcalc)):
#          print "m_Qa",self.m_listcalc[x].m_Qa," vs ",appo
          if(self.m_listcalc[x].m_Qa>=appo):
          	index = x
          	appo = self.m_listcalc[x].m_Qa
        return index

    def FindMax_Mv(self):
        appo = 0
        index = 0
        for x in range(len(self.m_listcalc)):
#          print "m_Qa",self.m_listcalc[x].m_Qa," vs ",appo
          if(self.m_listcalc[x].m_Mv>=appo):
            index = x
            appo = self.m_listcalc[x].m_Mv
        return index

    def Ordina(self):
      AppoCalciatore = 0
      appo = 0
      index = 0
      index_2 = 0
      lenght=len(self.m_listcalc)
      for x in range(len(self.m_listcalc)):
           index=lenght-x
           for y in range(len(self.m_listcalc)-1):
            index_2 = y+1
            #print "lenght ",lenght," index_2 ",index_2
            if(self.m_listcalc[index_2-1].m_Mv>=self.m_listcalc[index_2].m_Mv):
             AppoCalciatore = self.m_listcalc[index_2-1]
             self.m_listcalc[index_2-1] = self.m_listcalc[index_2]
             self.m_listcalc[index_2] = AppoCalciatore

    def Ordina_RatioVG(self):
      AppoCalciatore = 0
      appo = 0
      index = 0
      index_2 = 0
      lenght=len(self.m_listcalc)
      for x in range(len(self.m_listcalc)):
           index=lenght-x
           for y in range(len(self.m_listcalc)-1):
            index_2 = y+1
            print "lenght ",lenght," index_2 ",index_2
            if(self.m_listcalc[index_2-1].m_RatioVG>=self.m_listcalc[index_2].m_RatioVG):
             AppoCalciatore = self.m_listcalc[index_2-1]
             self.m_listcalc[index_2-1] = self.m_listcalc[index_2]
             self.m_listcalc[index_2] = AppoCalciatore
   
    def Ordina_RatioGPg(self):
      AppoCalciatore = 0
      appo = 0
      index = 0
      index_2 = 0
      lenght=len(self.m_listcalc)
      for x in range(len(self.m_listcalc)):
           index=lenght-x
           for y in range(len(self.m_listcalc)-1):
            index_2 = y+1
            print "lenght ",lenght," index_2 ",index_2
            if(self.m_listcalc[index_2-1].m_RatioGPg>=self.m_listcalc[index_2].m_RatioGPg):
             AppoCalciatore = self.m_listcalc[index_2-1]
             self.m_listcalc[index_2-1] = self.m_listcalc[index_2]
             self.m_listcalc[index_2] = AppoCalciatore



#########################################################################################
def usage():
     print 'Usage:\n python %s <input txt> <nome calciatore>' % ( sys.argv[0] )
#########################################################################################  
if __name__ == "__main__":
 #window = pMainFrame( ROOT.gClient.GetRoot(), 200, 200 )
 if len( sys.argv ) < 2:
        usage()
        sys.exit( 1 )    
 
 file_name = 0
 datrovare = 0
 
 if len( sys.argv )==3:
  file_name,datrovare= sys.argv[1],sys.argv[2]    
 if len( sys.argv )==2:
  file_name= sys.argv[1]
  datrovare = raw_input("Chi vuoi controllare? ")
  print("Hai scelto " + file_name + "!")

  #Id	R	Nome	Squadra	Pg	Mv	Mf	Gf	Gs	Rp	Rc	R+	R-	Ass	Asf	Amm	Esp	Au
 Stagione_17 = []
 acc = 0
 #with open('Presenti20172018.txt','r') as f:
 with open(file_name,'r') as f:
    for line in f:
        currentline = line.split(";")
        #print currentline
        #print acc
        acc = acc+1
        cal = calciatore()
        cal.SetAll(currentline)
        #cal.Print()
        Stagione_17.append(cal)
        #print currentline[0]," ",currentline[1]," ",currentline[2]
        #for word in line.split():
        #   print(word)    

 Por_17 = Lista_Calciatori()
 D_17 = Lista_Calciatori()
 C_17 = Lista_Calciatori()
 WT_17 = Lista_Calciatori()
 A_17 = Lista_Calciatori()

 for x in range(len(Stagione_17)): 
    if Stagione_17[x].m_R == "P":
        #print "is P | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm
        Por_17.AddDiff(Stagione_17[x])
    if Stagione_17[x].m_R == "D":
        #print "is D | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm
        D_17.AddDiff(Stagione_17[x])
    if Stagione_17[x].m_R == "A":
        A_17.AddDiff(Stagione_17[x])
        #print "is A | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm

    if Stagione_17[x].m_R == "C":
        C_17.AddDiff(Stagione_17[x])
        #print "is C | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm
         
    '''
    if (re.search("E", Stagione_17[x].m_Rm ) or re.search("C", Stagione_17[x].m_Rm )  or  re.search("M", Stagione_17[x].m_Rm )  ):
        C_17.AddDiff(Stagione_17[x])
        print "is C | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm
          
    if (re.search("W", Stagione_17[x].m_Rm )  or re.search("T", Stagione_17[x].m_Rm )   ):
        WT_17.AddDiff(Stagione_17[x])
        print "is W | Name ",Stagione_17[x].m_Nome," ruolo Mantra ",Stagione_17[x].m_Rm
    '''

 #indice = WT_17.FindMax_Qa()
 #print indice
 #WT_17.PrintOne(indice)
 #histo=TH1F("histo","histo",10,0.,10)
 print "------------------------------------------------------------"
 D_17.CalcMedia()
 D_17.CalcRMS()
 D_17.DoStat()
 D_17.Ordina()
 #C_17.Ordina_RatioVG()
 D_17.PrintDiff() 
 print "------------------------------------------------------------"

 C_17.CalcMedia()
 C_17.CalcRMS()
 C_17.DoStat()
 C_17.Ordina()
 #C_17.Ordina_RatioVG()
 C_17.PrintDiff() 
 print "------------------------------------------------------------"

 A_17.CalcMedia()
 A_17.CalcRMS()
 A_17.DoStat()
 A_17.Ordina()
 A_17.PrintDiff()

 # N_points = 100000
 # n_bins = 20
 
 # # Generate a normal distribution, center at x=0 and y=5
 # x = np.random.randn(N_points)
 # y = .4 * x + np.random.randn(100000) + 5
 
 # fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
 
 # # We can set the number of bins with the `bins` kwarg
 # axs[0].hist(x, bins=n_bins)
 # axs[1].hist(y, bins=n_bins)
 continua_ciclo = True
 print "end is near? ",continua_ciclo
 while continua_ciclo:
 	 print "inside"
	 pos_tmp_D  = D_17.MeasureDistance(datrovare)
	 if (pos_tmp_D>-99999):
	  print "distance: ",datrovare," ",D_17.MeasureDistance(datrovare)


	 pos_tmp_C  = C_17.MeasureDistance(datrovare)
	 if (pos_tmp_C>-99999):
	 	print "distance: ",datrovare," ",C_17.MeasureDistance(datrovare)


	 pos_tmp_A  = A_17.MeasureDistance(datrovare)
	 if (pos_tmp_A>-99999):
		 print "distance: ",datrovare," ",A_17.MeasureDistance(datrovare)



	 n_bins = 10
	 x=[]

	 
	 pos_tmp = D_17.FindName(datrovare)
	 if(pos_tmp>-99999):
	   for i in range(len(D_17.m_listcalc)):
	     voto = float(D_17.m_listcalc[i].m_Mv)
	     if(voto>0): 
	      x.append(voto)

	   plt.hist(x, normed=True, bins=n_bins,label='Difensori')   
	   plt.ylabel('A.U.');
	   plt.xlabel('Media Fanta Voto');
	   
	   x1=D_17.m_listcalc[pos_tmp].m_Mv
	   x2=D_17.m_listcalc[pos_tmp].m_Mv
	   plt.plot([x1, x2], [0, 1], color='k', linestyle='-', linewidth=2,label=D_17.m_listcalc[pos_tmp].m_Id)

	   x1=D_17.m_Media
	   x2=D_17.m_Media
	   plt.plot([x1, x2], [0, 1], color='r', linestyle='-', linewidth=2,label='media')


	   plt.legend(loc='upper left')


	 pos_tmp = C_17.FindName(datrovare)
	 if(pos_tmp>-99999):
	   for i in range(len(C_17.m_listcalc)):
	     voto = float(C_17.m_listcalc[i].m_Mv)
	     if(voto>0): 
	      x.append(voto)
	   plt.hist(x, normed=True, bins=n_bins,label='Centrocampisti')  
	   plt.ylabel('A.U.');
	   plt.xlabel('Media Fanta Voto');

	   x1=C_17.m_listcalc[pos_tmp].m_Mv
	   x2=C_17.m_listcalc[pos_tmp].m_Mv
	   plt.plot([x1, x2], [0, 1], color='k', linestyle='-', linewidth=2,label=C_17.m_listcalc[pos_tmp].m_Id)
	   
	   x1=C_17.m_Media
	   x2=C_17.m_Media
	   plt.plot([x1, x2], [0, 1], color='r', linestyle='-', linewidth=2,label='media')

	   plt.legend(loc='upper left')


	 pos_tmp = A_17.FindName(datrovare)
	 if(pos_tmp>-99999):
	   for i in range(len(A_17.m_listcalc)):
	     voto = float(A_17.m_listcalc[i].m_Mv)
	     if(voto>0): 
	      x.append(voto)

	   plt.hist(x, normed=True, bins=n_bins, label='Attaccanti') 
	   plt.ylabel('A.U.');
	   plt.xlabel('Media Fanta Voto');
	   
	   x1=A_17.m_listcalc[pos_tmp].m_Mv
	   x2=A_17.m_listcalc[pos_tmp].m_Mv
	   plt.plot([x1, x2], [0, 1], color='k', linestyle='-', linewidth=2,label=A_17.m_listcalc[pos_tmp].m_Id)

	   x1=A_17.m_Media
	   x2=A_17.m_Media
	   plt.plot([x1, x2], [0, 1], color='r', linestyle='-', linewidth=2,label='media')

	   #pylab.plot(x, y1, '-b', label='sine')
	   #pylab.plot(x, y2, '-r', label='cosine')
	   plt.legend(loc='upper left')
	   FileNameOutSave = A_17.m_listcalc[pos_tmp].m_Id + "pdf"
	   plt.savefig(FileNameOutSave)
	 StringCheck = raw_input("Vuoi fermarti? Inserisci Nome nuovo se vuoi continuare ")      
	 if (StringCheck ==""):
	  continua_ciclo=False
	  print "so long gay boys"
	 else:
	  print("Hai scelto " + StringCheck + "!")
	  datrovare = StringCheck
 



 #show()  
 