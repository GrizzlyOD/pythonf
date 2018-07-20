sentence=input("sentence:")
sentence_width=len(sentence)
screen_width=80
box_width=sentence_width+6
left=(screen_width-box_width)//2
left_l=(screen_width-sentence_width)//2
print()
print(" "*left+"+"+"-"*(box_width-2)+"+")
print(" "*(left_l-1)+"|"+" "*sentence_width+"|")
print(" "*(left_l-1)+"|"+sentence+"|")
print(" "*(left_l-1)+"|"+" "*sentence_width+"|")
print(" "*left+"+"+"-"*(box_width-2)+"+")
