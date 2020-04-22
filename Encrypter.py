
'''
   Copyright (c) 2020, Tharaka Ratnayake,
   email: tharakasachintha.17@cse.mrt.ac.lk
   All rights reserved. https://github.com/tharaka27/
   
   Revision history:
	  April 22th, 2020: initial version.
'''

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def CountCharacter(String):
    Original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    letter_dic = {}
    for i in String:
        if i in Original :
            try:
                letter_dic[i] = letter_dic[i] + 1

            except:
                letter_dic[i] =  1
    print (letter_dic)
    return letter_dic
    

def Encrypt(v, Original, Key):
    #Key = "GFWAVQXBNZKUDYILJSTCRMPHEOgfwavqxbnzkudyiljstcrmpheo"

    Encypted_String = ""
    for i in v:
        if i in Original:
            Encypted_String = Encypted_String + Key[Original.find(i)]
        else:
            Encypted_String = Encypted_String +i 
            
    return Encypted_String



#
#
#  Encrypting the Original text using the given Key
#
#
file = open("Original.txt","r", encoding='utf-8')
file2 = open("Original_Encryted.txt", "w", encoding="utf-8")
v = file.read()


Original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
Key = "GFWAVQXBNZKUDYILJSTCRMPHEOGFWAVQXBNZKUDYILJSTCRMPHEO"
return_string  = Encrypt(v,Original,Key)
letter_dic = CountCharacter(return_string)
file2.write(return_string)

file.close()
file2.close()



#
#
#  Count the occurrence of each letter and plot it.
#
#
objects = ('A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z')
y_pos = np.arange(len(objects))
performance = []
for i in objects:
    performance.append(letter_dic[i])

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number')
plt.title('Character distribution')
plt.show()


#
#
#  Identify 5 ciphertext characters with the highest frequency
#  and Prepare a partial decryption of the ciphertext with only the
#  identified top-5characters replaced with their corresponding
#  plaintext guesses.
#
#
#  using Relative frequecy of letters in english, the most appeard 
#  5 characters are e,t,a,r,i
#  source - https://en.wikipedia.org/wiki/Letter_frequency
#

sorted_letter_dic = {k: v for k, v in sorted(letter_dic.items(),
                            key=lambda item: item[1],reverse =True )}
most_used_letters = ""
counter = 5
for i in sorted_letter_dic:
    if counter ==0:
        break
    most_used_letters = most_used_letters + i
    counter = counter - 1
Key = "ETARI"
return_string  = Encrypt(return_string,most_used_letters,Key)
print(most_used_letters)
file3 = open("Original_Partially_decrypted.txt", "w", encoding="utf-8")
file3.write(return_string)
file3.close()

