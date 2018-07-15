###############################################################
# Computer Project #1: Unit Conversions 
#
# 1. User inputs a particular number of rods.
# 2. The program is made to use simple mathematical formulas to
#    print out the unit conversions of the rods into meters,feet,
#    miles, and furlongs.
# 3. It also calculates how much time it takes to walk the
#    inputed amount of rods assuming the average walking speed
#    is 3.1 miles/hour.
# 4. Displays a closing message
###############################################################



userinput_flt = float ( input( "Input the number of rods:  " ) )

rods_to_meters = 5.0292 * userinput_flt
rods_to_feet = userinput_flt * 16.5
rods_to_miles = rods_to_meters / 1609.34
rods_to_furlongs = userinput_flt / 40
time_taken =  (rods_to_meters / 1609.34)/(3.1/60)

print(" ")
print("The following are the conversions made:")
print(" ")
print( "Meters:", rods_to_meters )
print( "Feet:", rods_to_feet)
print( "Miles:", rods_to_miles)
print( "Furlongs:", rods_to_furlongs)
print( "Minutes to walk", userinput_flt, "rods:", time_taken )
print(" ")
print("Thank you for your time!")
    