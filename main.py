a = 1
pos = ("")
board = [["⬜", "⬜", "⬜", "⬜", "⬜"], ["⬜", "⬛", "⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜", "⬜", "⬜"]]
pos = 111
Xpos = ("")
Ypos = ("")


def display():
  print ("------------------------------")
  for i in range (0,5):
    print (board[i])
  print ("-----------------------------")


#the code can be easily optimised, but I cannot be asked!
display()
while a == 1:
  instructions = (input(""))
  length = len(instructions)
  for i in range(0,length):
    if instructions[i] == ("u"):
      temp1 = str(pos)
      temp2 = temp1[1] + temp1[2]
      temp3 = int(temp2)
      if temp3 < 10:
        continue
      else:
        Xpos = str(pos)[1]
        Ypos = str(pos)[2]
        Xpos = int(Xpos)
        Ypos = int(Ypos)
        board[Xpos][Ypos] = "⬜"
        board[Xpos-1][Ypos] = "⬛"
        pos =  (Xpos - 1) * 10 + Ypos + 100
        display()
    if instructions[i] == ("d"):
      temp1 = str(pos)
      temp2 = temp1[1] + temp1[2]
      temp3 = int(temp2)
      if temp3 > 34:
        continue
      else:
        Xpos = str(pos)[1]
        Ypos = str(pos)[2]
        Xpos = int(Xpos)
        Ypos = int(Ypos)
        board[Xpos][Ypos] = "⬜"
        board[Xpos+1][Ypos] = "⬛"
        pos = (Xpos + 1) * 10 + Ypos + 100
        display()
    if instructions[i] == ("l"):
      temp1 = str(pos)
      temp2 = temp1[1] + temp1[2]
      temp = str(temp2)[1]
      if int(temp) < 1:
        continue
      else:
        Xpos = str(pos)[1]
        Ypos = str(pos)[2]
        Xpos = int(Xpos)
        Ypos = int(Ypos)
        board[Xpos][Ypos] = "⬜"
        board[Xpos][Ypos-1] = "⬛"
        pos = (Xpos * 10) + Ypos + 99
        display()
    if instructions[i] == ("r"):
      temp1 = str(pos)
      temp2 = temp1[1] + temp1[2]
      temp = str(temp2)[1]
      if int(temp) > 3:
        continue
      else:
        Xpos = str(pos)[1]
        Ypos = str(pos)[2]
        Xpos = int(Xpos)
        Ypos = int(Ypos)
        board[Xpos][Ypos] = "⬜"
        board[Xpos][Ypos+1] = "⬛"
        pos = (Xpos * 10) + Ypos + 101
        display()
