def float_default(string, default_float):
   try:
      return float(string)
   except ValueError:
      return default_float
