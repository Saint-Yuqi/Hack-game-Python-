#Hacking version2
#This is a text-based password quessing game that displays a 
#list of potential computer passwords.The player is allowed
#1 attempt to guess the password correctly.
from time import sleep 
from uagame import Window


#display a window
window = Window('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

#display a header
line_y = 0
string_height = window.get_font_height()

window.draw_string('DEBUG MODE',0,line_y)
line_y = line_y + string_height
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('1 ATTEMPT(S) LEFT',0,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#draw blank line
window.draw_string('',0,line_y)
window.update()
sleep(0.1)
line_y = line_y + string_height

#display passward list
window.draw_string('PROVIDE',0,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('SETTING',0,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('CANTINA',0,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('CUTTING',0,line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HUNTERS', 0, line_y)
line_y = line_y + string_height
window.update()
sleep(0.3)

window.draw_string('SURVIVE', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HEARING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('HUNTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('REALIZE', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('NOTHING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('OVERLAP', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('FINDING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

window.draw_string('PUTTING', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#   display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#prompt for guess
guess = window.input_string('ENTER PASSWORD >',0,line_y)

#end game
#clear window
window.clear()

# compute x coordinate
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2 
#compute y coordinate
outcome_height = 7 * string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

window.draw_string(guess , line_x , line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#      display failure line 2
#         compute x coordinate
x_space = window.get_width() - window.get_string_width('LOGIN FAILURE - TERMINAL LOCKED')
line_x = x_space // 2

window.draw_string('LOGIN FAILURE - TERMINAL LOCKED', line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height   

#      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#      display failure line 3
#         compute x coordinate
x_space = window.get_width() - window.get_string_width('PLEASE CONTACT AN ADMINISTRATOR')
line_x = x_space // 2

window.draw_string('PLEASE CONTACT AN ADMINISTRATOR', line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height   

#      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

#   prompt for end
#      compute x coordinate
x_space = window.get_width() - window.get_string_width('PRESS ENTER TO EXIT')
line_x = x_space // 2
window.input_string('PRESS ENTER TO EXIT', line_x, line_y)

#   close window
window.close()