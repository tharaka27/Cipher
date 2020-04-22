# Cipher

Continuous assessment for Week 1 - Classical Encryption/Substitution Cipher


1. Select a Wikipedia article of minimum 10,000 words as your plaintext P.
2. Decide on a simple mono-alphabetic substitution cipher for the alphabet of English characters A to Z (be case agnostic) and use it as your encryption scheme E.
3. Compute your ciphertext C as C = E(P) by encrypting only the alphabetic characters (leaving all other characters, symbols, etc as is)
4. Compute the character frequency graph for your ciphertext C and draw it as a bar chart with x-axis in alphabetic order.
5. Identify the 5 ciphertext characters with the highest frequency and speculate on the mapping to the plaintext characters in the alphabet.
6. Prepare a partial decryption of the ciphertext with only the identified top-5 characters replaced with their corresponding plaintext guesses.


## Code 
The code for encrypting

```python
   def Encrypt(v, Original, Key):
    Encypted_String = ""
    for i in v:
        if i in Original:
            Encypted_String = Encypted_String + Key[Original.find(i)]
        else:
            Encypted_String = Encypted_String +i 
            
    return Encypted_String
```

The code for counting occurrence of characters

```python
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
```

## Libraries used

- numpy
- matplotlib
