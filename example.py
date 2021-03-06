# Example test for pypowerwall

import pypowerwall

# Optional: Turn on Debug Mode
pypowerwall.set_debug(True)

# Credentials for your Powerwall - Customer Login Data
password='password'
email='email@example.com'
host = "localhost"                # Change to the IP of your Powerwall
timezone = "America/Los_Angeles"  # Change to your local timezone/tz

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

# Display Metric Examples
print("Battery power level: %0.0f%%" % pw.level())
print("Power response: %r" % pw.power())
print("Grid Power: %0.2fkW" % (float(pw.grid())/1000.0))
print("Solar Power: %0.2fkW" % (float(pw.solar())/1000.0))
print("Battery Power: %0.2fkW" % (float(pw.battery())/1000.0))
print("Home Power: %0.2fkW" % (float(pw.home())/1000.0))

# Raw JSON Data Examples
print("Grid raw: %r" % pw.grid(verbose=True))
print("Solar raw: %r" % pw.solar(verbose=True))

