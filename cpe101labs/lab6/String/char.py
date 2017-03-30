def is_lower_101(char):
   i = ord(char)
   if i in range(97, 123):
      return True
   else:
      return False

def char_rot_13(char):
   if ord(char) in range(65, 78):
      rot_13 = ord(char) + 13
      return chr(rot_13)
   elif ord(char) in range(78, 91):
      rot_13 = ord(char) - 13
      return chr(rot_13)
   elif ord(char) in range(97, 110):
      rot_13 = ord(char) + 13
      return chr(rot_13)
   elif ord(char) in range(110, 123):
      rot_13 = ord(char) - 13
      return chr(rot_13)

