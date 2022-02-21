map={}
for i in range(26):
    map.update({chr(i+65):str(i+11)})
    map.update({str(i+11):chr(i+65)})
for i in range(26):
    map.update({chr(i+97):str(i+40)})
    map.update({str(i+40):chr(i+97)})
map.update({' ':'90'})
map.update({'90':' '})
