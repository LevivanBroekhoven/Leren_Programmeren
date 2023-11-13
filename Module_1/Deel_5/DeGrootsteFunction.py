def GroterGetal(nr1, nr2):
      if nr1 == nr2:
        return 'Beide getallen zijn even groot'
      elif nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
      else:
        return f'Maximum: {nr2} en minimum: {nr1}'
    
nr1 = 1
nr2 = 1
resultaat = GroterGetal(nr1, nr2)
print (resultaat)