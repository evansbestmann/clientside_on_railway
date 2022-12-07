import re
parameters=('elbestmann@gmail.com,evansbestmann@gmail.com')
quoted_planets = [p for p in parameters.split(",") if len(p) > 0]
print(quoted_planets)
