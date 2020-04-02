# Constants are a good way to always have things you need on hand!
# They are also great for code readability.
# The weight of something on the moon is 16.5% of it's weight on earth.
EARTH_TO_MOON_RATIO = 0.165

def earth_to_moon_weight():
	# To find out how much someone weighs on the moon,
	# we need to know their terrestrial (earth-based) weight first!
	# Let's ask for that from our user:
	earth_weight_str = input("What is the earth weight (in lbs)? ")

	# Now that we have their input, let's make it more usable
	# for our script.
	earth_weight = int(earth_weight_str)

	# Let's use the variables and constants we have to get
	# our correct moon weight!
	moon_weight = earth_weight * EARTH_TO_MOON_RATIO

	# Now that we've got what we want, let's give it back to the user.
	print("The weight on the moon would be " + str(moon_weight) + " lbs.")

# Always make sure the system knows what part of our script to run:
if __name__ == '__main__':
	earth_to_moon_weight()