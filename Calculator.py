
# coding: utf-8

# In[79]:


#!/usr/bin/env python

OutFile = open('output', 'w')

def Concentration_pM(d_factor,ct,Yint,slope,frag):
   result = (d_factor*(10**((float(ct)-Yint)/float(slope)))*(452/float(frag)))
   return result
def Concentration_uguL(concentration_pM,frag):
    result = ((concentration_pM)*(10**-15)*frag*617.9*10**6)
    return result

#Examples to verify math
#pm = Concentration_pM(100000,30,11,-3.3,248)
#print(pm)
#print(Concentration_uguL(pm,248))

OutFile.write('Sample\tConcentration(pM)\tConcentration(ug/uL)')
OutFile.write(%s'\t'%d'\t'%d) % (Samples,PM,uguL)
#OutFile.write('test')

OutFile.close()

