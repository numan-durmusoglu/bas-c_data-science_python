# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:06:48 2019

@author: numan
"""

class describe(object):
    
    
    def __init__(self,liste):
        
        self.liste = liste
        
    def mod(liste):
    
        en_yuksek = 0
        for s in liste:
            if liste.count(s) > liste.count(en_yuksek):
                en_yuksek = s
        return en_yuksek
    
    
    
    def ortalama(self):
        
        return sum(liste)/len(liste)
        
    def son_aciklik(self):
        siralama = sorted(liste)
        uzunluk = len(liste)
        index = ((uzunluk-1)//2)
       
        if (index %2==0):
            
            son = siralama[index+1:]
            index2 = (len(son)-1)//2
            
            if (index2 %2==0):
                
                return son[index2]
            
            else:
                
                return(son[index2]+son[index2+1])/2
                
        else:
            son2 = siralama[index+1:]
            index3 = (len(son2)-1)//2
            
            if (index3 %2==0):
                    
                return son2[index3]
                
            else:
                    
                return (son2[index3]+son2[index3+1])//2     
                 
                 
    def ilk_aciklik(self):
        siralama = sorted(liste)
        uzunluk = len(liste)
        index = (uzunluk-1)//2
   
        if (index %2==0):
            ilk = siralama[:index+1]
            index2 = (len(ilk)-1)//2
            
            if (index2 %2==0):
                return ilk[index2]
            else:
                return (ilk[index2]+ilk[index2+1])//2
        
        else:
            ilk2 = siralama[:index]
            index3 = (len(ilk2)-1)//2
            
            if (index3 %2==0):
                
                return ilk2[index3]
            
            else:
                
                return (ilk2[index3]+ilk2[index3+1])//2
            
        
    def maximum(self):
        return max(liste)
    
    def minimum(self):
        return min(liste)
    
    def standart_sapma(self):
         return (sum([((sum(liste)/len(liste))-i)**2  for i in liste])/(len(liste)-1))**0.5   
    
    def medyan(self):
        
        med_sorted = sorted(liste)
        med_len = len(liste)
        index = (med_len-1)//2
   
        if (index %2==0):
            
            return liste[index]
        
        else:
            
            return (liste[index] + liste[index+1])/2
                
    def rassal_sayi_poison(lam,size):
        return np.random.poisson(lam,size)
    
    

