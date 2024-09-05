# collection of vat key:value pairs for vat-keys: F, L and H
VAT_PERC = {'F': 0, 'L': 9, 'H': 21}
YES_OPTIONS = ('j','J')
NO_OPTIONS = ('n','N')
YES_NO_OPTIONS = YES_OPTIONS + NO_OPTIONS

# input function given prompt asks for integer, return only valid integers between limits: min and max
def input_int(prompt: str, min: int = 0, max: int = 10000) -> int:
  while True:
    try:
      answer = input(prompt + '\n')
      amount = int(answer)
      if amount < min:
        print(f'Mimimum is: {min}')
      elif amount > max:
        print(f'Maximum is: {max}')
      else:
        return amount
    except:
      print(f'Geen geldig getal: {answer}')

# input function for valid options, returns answer only when found in options collection 
def input_option(prompt: str, options: list) -> str:
  while True:
    answer = input(prompt+'\n')
    if answer in options:
      return answer
    else:
      print(f'Verwacht alleen optie uit: {" of ".join(options)}') 

def input_yes_no(prompt: str) -> str:
  return input_option(prompt,YES_NO_OPTIONS)

# function returns percentage for given VAT key, invalid VAT key causes type-error
def get_vat_perc(vat_key: str) -> int:
  if not vat_key.upper() in VAT_PERC:
    raise TypeError(f"BTW code {vat_key} onbekend")  
  return VAT_PERC[vat_key.upper()]

# function returns VAT for given amount excl VAT and VAT key, invalid vat-key causes type-error
# returned result rounded to 2 decimals
def get_vat_from_amount_excl(amount: float, vat_key: str) -> float:
  perc = get_vat_perc(vat_key)
  return round(amount * perc / 100,2)

# function returns VAT for given amount incl VAT and VAT key, invalid vat-key causes type-error
# returned result rounded to 2 decimals
def get_vat_from_amount_incl(amount: float, vat_key: str) -> float:
  perc = get_vat_perc(vat_key)
  return round(amount / (100 + perc) * perc,2)

