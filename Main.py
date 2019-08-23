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
from Calciatori import calciatore 
from Calciatori import Lista_Calciatori 
#execfile(os.path.expandvars("Calciatori.py"))

#########################################################################################
# messaggio d'errore
def usage():
     print 'Usage:\n python %s <input txt> <nome calciatore>' % ( sys.argv[0] )
#########################################################################################  
if __name__ == "__main__":
 #window = pMainFrame( ROOT.gClient.GetRoot(), 200, 200 )
 if len( sys.argv ) < 3:
        usage()
        sys.exit( 1 )    
        
 file_name,datrovare= sys.argv[1],sys.argv[2]    
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
 D_17.CalcSD()
 D_17.DoStat()
 D_17.Ordina()
 #C_17.Ordina_RatioVG()
 D_17.PrintDiff() 
 print "------------------------------------------------------------"

 C_17.CalcMedia()
 C_17.CalcSD()
 C_17.DoStat()
 C_17.Ordina()
 #C_17.Ordina_RatioVG()
 C_17.PrintDiff() 
 print "------------------------------------------------------------"

 A_17.CalcMedia()
 A_17.CalcSD()
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


 n_bins = 15
 x_D=[]
 x_C=[]
 x_A=[]
 for i in range(len(D_17.m_listcalc)):
      voto = float(D_17.m_listcalc[i].m_Mv)
      if(voto>0): 
       x_D.append(voto)
 plt.figure(1)
 plt.hist(x_D, normed=True, bins=n_bins, color='c',label='Difensori')   
 plt.ylabel('A.U.');
 plt.xlabel('Media Fanta Voto');
 x1=D_17.m_Media
 x2=D_17.m_Media
 plt.plot([x1, x2], [0, 1], color='r', linestyle='-.', linewidth=4,label='media')
 plt.legend(loc='upper left')

 
 for i in range(len(C_17.m_listcalc)):
    voto = float(C_17.m_listcalc[i].m_Mv)
    if(voto>0): 
      x_C.append(voto)
 plt.figure(2)
 plt.hist(x_C, normed=True, bins=n_bins, color='c', label='Centrocampisti')  
 plt.ylabel('A.U.');
 plt.xlabel('Media Fanta Voto');
 x1=C_17.m_Media
 x2=C_17.m_Media
 plt.plot([x1, x2], [0, 1], color='r', linestyle='-.', linewidth=4,label='media')
 plt.legend(loc='upper left') 
 
 for i in range(len(A_17.m_listcalc)):
      voto = float(A_17.m_listcalc[i].m_Mv)
      if(voto>0): 
       x_A.append(voto)
 plt.figure(3)
 plt.hist(x_A, normed=True, bins=n_bins, color='c', label='Attaccanti') 
 plt.ylabel('A.U.');
 plt.xlabel('Media Fanta Voto');
 x1=A_17.m_Media
 x2=A_17.m_Media
 plt.plot([x1, x2], [0, 1], color='r', linestyle='-.', linewidth=4,label='media')

 plt.legend(loc='upper left')



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

   
   pos_tmp = D_17.FindName(datrovare)
   if(pos_tmp>-99999):

     
     x1=D_17.m_listcalc[pos_tmp].m_Mv
     x2=D_17.m_listcalc[pos_tmp].m_Mv
     plt.figure(1)
     plt.plot([x1, x2], [0, 1], linewidth=2, label=D_17.m_listcalc[pos_tmp].m_Id)
     plt.legend(loc='upper left')
     #plt.clear()

   pos_tmp = C_17.FindName(datrovare)
   if(pos_tmp>-99999):
     x1=C_17.m_listcalc[pos_tmp].m_Mv
     x2=C_17.m_listcalc[pos_tmp].m_Mv
     plt.figure(2)
     plt.plot([x1, x2], [0, 1], linewidth=2,label=C_17.m_listcalc[pos_tmp].m_Id)
     plt.legend(loc='upper left')
     #plt.clear()

   pos_tmp = A_17.FindName(datrovare)
   if(pos_tmp>-99999):
     
     x1=A_17.m_listcalc[pos_tmp].m_Mv
     x2=A_17.m_listcalc[pos_tmp].m_Mv
     plt.figure(3)
     #plt.plot([x1, x2], [0, 1], color='k', linestyle='-', linewidth=2,label=A_17.m_listcalc[pos_tmp].m_Id)
     plt.plot([x1, x2], [0, 1] , linewidth=2,label=A_17.m_listcalc[pos_tmp].m_Id)

     #pylab.plot(x, y1, '-b', label='sine')
     #pylab.plot(x, y2, '-r', label='cosine')
     plt.legend(loc='upper left')
     FileNameOutSave = A_17.m_listcalc[pos_tmp].m_Id + "pdf"
     #plt.savefig(FileNameOutSave)
     #plt.clear()
   
   StringCheck = raw_input("Vuoi fermarti? Inserisci Nome nuovo se vuoi continuare ")      
   if (StringCheck ==""):
    continua_ciclo=False
    print "so long"
   else:
    print("Hai scelto " + StringCheck + "!")
    datrovare = StringCheck


 show()  