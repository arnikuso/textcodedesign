from drawbot_skia.drawbot import fontSize, size, font, text, newPage, fill, rect, saveImage
#задание 1#

fill(0.71,0.345,0.596)
vertical = [0, 120, 240, 360, 480];

for y in vertical:
     rect(10, y, 100, 100)

saveImage ('task1.pdf')

#задание 2#
horizontal = [0, 120, 240, 360, 480]
for y in vertical:
     for x in horizontal:   
       rect(x, y, 100, 100)
       
saveImage('task2.pdf')

#задание 3#
size(300, 300)
fill (1, 0.965, 0.89)
rect (0, 0, 300, 300)

fontSize(30)
font('times-bold')
fill (0.812,0.604,0.804)
text('Kitchen (noun)', (25, 40))



newPage()
fill (1, 0.965, 0.89)
rect (0, 0, 300, 300)

fontSize(10)
font('times-italic')
fill (0.322,0,0.314)
text('This is a kitchen. A place for creativity,', (50, 250))
text ('a place to dream. Dream to be brave.', (50, 230))
text ('Never be afraid of mistakes. Always', (50, 210))
text('questioning the possibilities, never', (50, 190))
text('sitting still, but always evolving and', (50, 170))
text('pushing ourselves. We still respect the', (50, 150))
text('past and never forget where we came', (50, 130))
text('from. Humility is our key ingredient.', (50, 110))
text('We are here not to feed the stomach', (50, 90))
text('but to fill the heart and soul. It is', (50, 70))
text('not about the country or the culture,', (50, 50))
text('its about the state of mind.', (51, 30))
saveImage('task3.pdf')