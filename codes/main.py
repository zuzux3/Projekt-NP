from Expo_Euler import Euler_Exp
from Impo_Euler import Euler_Imp
from trapez import trapez

string = "Podaj wybor operacji: "
string1 = "1 - Jawny Euler, 2 - Niejawny Euler, 3 - Metoda Trapezowa"

print(string)
print(string1)
w = input()
if w == '1':
    Euler_Exp()
elif w == '2':
    Euler_Imp()
elif w == '3':
    trapez()
else:
    string2 = "Wybor niepoprawny"
    print(string2)
