#from matplotlib.ticker import PercentFormatter
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

#gROOT.Reset()
#a = TRandom()
#a.SetSeed(1242)

class calciatore:
    m_name = 0
    m_cash = 500

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
#
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


# due funzioni che utilizi dopo. con e senza definizione degli oggetti
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

        return self.m_name

    def GetCash(self):
        return self.m_cash

    def SetName(self,name):
        self.m_name = name

    def SetCash(self,cash):
        self.m_cash = cash
    def SetRatio(self):
        if(float(self.m_Pg)>0):
          self.m_RatioVp = float(self.m_Mv)/float(self.m_Pg) # fv/partite giocate
          self.m_RatioVG = float(self.m_Gf)/float(self.m_Pg) # gf/pg
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
        self.m_SD = 0
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
          if(dist/self.m_SD>0.65 and float(self.m_listcalc[x].m_Pg)>10):
           self.m_listcalc[x].Print()
           #self.m_listcalc[x].PrintEmpyt()

           
    def PrintOne(self,arg):
        self.m_listcalc[arg].Print()
    def CalcMedia(self): # media delle medie dei calciatori (x) dal primo all'ultimo (solo quelli che non hanno 0)
        voto = 0
        media = 0
        non_zero = 0
        for x in range(len(self.m_listcalc)):
         voto = float(self.m_listcalc[x].m_Mv)
         media = media+voto
         if (voto!=0):
          non_zero = non_zero+1
        self.m_Media= media / non_zero 
    def CalcSD(self):
        voto = 0
        delta = 0
        SD = 0
        non_zero = 0
        for x in range(len(self.m_listcalc)):
         voto = float(self.m_listcalc[x].m_Mv)
         delta = voto - self.m_Media
         if (voto!=0):
          SD = SD + delta*delta
          non_zero = non_zero+1
        self.m_SD = (SD / non_zero)**(0.5)
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
          return appo / self.m_SD
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


