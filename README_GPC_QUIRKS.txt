Quirks of gpc
Not all of the following is confirmed, but following these tips can prevent you from completely overhauling program logic

Any combos must have wait at the top level

All programs need compartmentalized into stages

For loops and while loops are a massive headache so utilize the main loop

Strings cannot be reassigned in gpc (that I know of) so every string used needs hard coded and referenced directly

Arrays of ints cannot use int must utilize int16 or another type

Combos are sequential, but their calls are not.

Adding a brief waiting period when reassigning variables prevents many headaches

No known way of introducing parameters, functions and combos must reference global variables

LED_2 - Green
LED_3 - Red

No local variables can be declared period (including int i in for loops).

Combos cannot be called like functions must be passed into combo_run

Combos will repeat unless explicitly stopped using combo_stop

Any button presses need to be undone using values 100 and 0 respectively

String addresses need to referenced index 0 ([0] at the end of the variable)