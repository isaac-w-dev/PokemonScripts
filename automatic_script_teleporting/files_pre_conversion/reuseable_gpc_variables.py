dr = "SWI_RIGHT"
dl = "SWI_LEFT"
du = "SWI_UP"
dd = "SWI_DOWN"
plus = "SWI_PLUS"
min = "SWI_MINUS"
ab = "SWI_A"
yb = "SWI_Y"
bb = "SWI_B"
xb = "SWI_X"
zr = "SWI_ZR"
zl = "SWI_ZL"
rb = "SWI_R"
lb = "SWI_L"

tab = '\t'

# Arguments: controller input
get_val = "get_val"

# Arguments: input, intensity out of 100
set_val = "set_val"

# Argument: Waittime in milliseconds i.e. 1000ms = 1s
wait = "wait"

# Argument: combo to stop
combo_stop = "combo_stop"

# Argument: combo to run
combo_run = "combo_run"

# Arguments 1 selection of LED_1 through LED_4 and a boolean on whether it is on or off
# Update when colors known
set_led = "set_led"

# DISPLAY to screen with print(x_coordinates, y_coordinates, font_size, color, string_variable)
prnt = "print"

# Arguments: controller_input
# Different from get_val because it prevents the game from reading it in as a normal input
event_press = "event_press"