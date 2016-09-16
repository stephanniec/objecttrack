import serial


def start_up():
    ser_com = serial.Serial('/dev/ttyACM0') #Create open port to Command port
    ser_ttl = serial.Serial('/dev/ttyACM1') #Create open port to TTL port

    command_servo2 = [chr(0x84), chr(0x02),'','']
    command_servo5 = [chr(0x84), chr(0x05),'','']
    home_pos = set_home()
    ser_com.write(''.join(home_pos[0]))
    ser_com.write(''.join(home_pos[1]))
    pos_x = 1500
    pos_y = 1500

    input = raw_input('Use WASD to control robot.(Enter q to quit)')

    while(input.lower() != 'q'):
        if(input == 'w' or input == 'W'):
            pos_y = pos_y - 100
            new_target = pos_to_bin(pos_y)
            command_servo5[2] = chr(new_target[1])
            command_servo5[3] = chr(new_target[0])
            ser_com.write(''.join(command_servo5))

        elif (input == 'a' or input == 'A'):
            pos_x = pos_x - 100
            new_target = pos_to_bin(pos_x)
            command_servo2[2] = chr(new_target[1])
            command_servo2[3] = chr(new_target[0])
            ser_com.write(''.join(command_servo2))

        elif (input == 's' or input == 'S'):
            pos_y = pos_y + 100
            new_target = pos_to_bin(pos_y)
            command_servo5[2] = chr(new_target[1])
            command_servo5[3] = chr(new_target[0])
            ser_com.write(''.join(command_servo5))

        elif (input == 'd' or input == 'D'):
            pos_x = pos_x + 100
            new_target = pos_to_bin(pos_x)
            command_servo2[2] = chr(new_target[1])
            command_servo2[3] = chr(new_target[0])
            ser_com.write(''.join(command_servo2))

        elif (input == 'h' or input == 'H'):
            pos_x = 1500
            pos_y = 1500
            ser_com.write(''.join(home_pos[0]))
            ser_com.write(''.join(home_pos[1]))
        else:
            print 'Please input only WASD'
        input = raw_input('Use WASD to control robot.(Enter q to quit)')
    ser_com.close()
    ser_ttl.close()

def pos_to_bin(target): #returns hex values of high binary and low binary numbers.
    value = target * 4
    bin_value = bin(value)

    high_bin = bin_value[:8] # Need 0b to make it distinguish as a binary number instead of decimal number
    low_bin = '0b' + bin_value[8:]

    return int(high_bin,2), int(low_bin,2)

def set_home():
    home = pos_to_bin(1500);
    servo2 = [chr(0x84), chr(0x02),chr(home[1]),chr(home[0])]
    servo5 = [chr(0x84), chr(0x05),chr(home[1]),chr(home[0])]
    return servo2, servo5

if __name__ == "__main__":
    start_up()

