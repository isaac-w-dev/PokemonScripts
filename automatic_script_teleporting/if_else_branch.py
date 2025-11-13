if_else_branch = '''    if(get_val(SWI_ZL)){

        if(event_press(SWI_UP)){
            if (category == 0){
                category = 4;
            }
            else{
                category -= 1;
            }
        }

        if(event_press(SWI_DOWN)){
            if (category == 4){
                category = 0;
            }
            else{
                category += 1;
            }
        }

        if(event_press(SWI_LEFT) & category != 0){
            if (location == 0){
                location = locations_per_catagory[category];
            }
            else{
                location -= 1;
            }
        }

        if(event_press(SWI_RIGHT) & category != 0){
            if (location == locations_per_catagory[category]){
                location = 0;
            }
            else{
                location +=  1;
            }
        }

        if (event_press(SWI_R) & category != 0 & location != 0){
            SCRIPT_RUNNING = !SCRIPT_RUNNING;
        }

        if (!SCRIPT_RUNNING){
            print(10, 20, OLED_FONT_MEDIUM, OLED_WHITE, locations_by_type[category][location]);
        }
        if (SCRIPT_RUNNING){
'''