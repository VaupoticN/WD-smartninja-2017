print "Hi, hello! " \
      "Let me introduce myself - my name is KMtoML and I do a splendid job of converting from kilometers to miles."

km = float( raw_input("Please, enter kilometers here:"))

print "This equals to", km*0.621, "miles"

while True:
      another = raw_input("Do you wish to do another conversion? Please answer with yes or no.")

      if another == "no":
            print "Okay! :) Have a nice day!"
            break

      if another == "yes":
            km2 = float( raw_input("Please, enter kilometers here:"))
            print "This equals to", km2*0.621, "miles"
