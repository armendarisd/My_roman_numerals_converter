

dict_units = {
  1:"I",
  2:"II",
  3:"III",
  4:"IV",
  5:"V",
  6:"VI",
  7:"VII",
  8:"VIII",
  9:"IX"
}

dict_decimals = {
  1:"X",
  2:"XX",
  3:"XXX",
  4:"XL",
  5:"L",
  6:"LX",
  7:"LXX",
  8:"LXXX",
  9:"XC"
}

dict_centimals = {
  1:"C",
  2:"CC",
  3:"CCC",
  4:"CD",
  5:"D",
  6:"DC",
  7:"DCC",
  8:"DCCC",
  9:"CM"
}

dict_milesimals = {
  1:"M",
  2:"MM"
}

def four_digits(param_1):
  roman_num = []
  
  for clave in dict_milesimals:
    if clave == param_1[0]:
      roman_num.append(dict_milesimals[clave])

  for clave in dict_centimals:
    if clave == param_1[1]:
      roman_num.append(dict_centimals[clave])

  for clave in dict_decimals:
    if clave == param_1[2]:
      roman_num.append(dict_decimals[clave])

  for clave in dict_units:
    if clave == param_1[3]:
      roman_num.append(dict_units[clave])

  roman_num = ''.join(roman_num)
  
  return roman_num
 
def three_digits(param_1):
  roman_num = []
  
  for clave in dict_centimals:
    if clave == param_1[0]:
      roman_num.append(dict_centimals[clave])

  for clave in dict_decimals:
    if clave == param_1[1]:
      roman_num.append(dict_decimals[clave])

  for clave in dict_units:
    if clave == param_1[2]:
      roman_num.append(dict_units[clave])

  roman_num = ''.join(roman_num)
  
  return roman_num

def two_digits(param_1):
  roman_num = []

  for clave in dict_decimals:
    if clave == param_1[0]:
      roman_num.append(dict_decimals[clave])

  for clave in dict_units:
    if clave == param_1[1]:
      roman_num.append(dict_units[clave])

  roman_num = ''.join(roman_num)
  
  return roman_num

def one_digits(param_1):     

  roman_num = []

  for clave in dict_units:
    if clave == param_1[0]:
      roman_num.append(dict_units[clave])

  roman_num = ''.join(roman_num)
  
  return roman_num
      
def my_roman_numerals_converter(param_1):

    arabic_num = [int(a) for a in str(param_1)]

    if(len(arabic_num) == 4):
        return four_digits(arabic_num)
    elif(len(arabic_num) == 3):
        return three_digits(arabic_num)
    elif(len(arabic_num) == 2):
        return two_digits(arabic_num)
    elif(len(arabic_num) == 1):
        return one_digits(arabic_num)

  




















    return 0