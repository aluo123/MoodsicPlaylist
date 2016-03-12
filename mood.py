import indicoio
import json
indicoio.config.api_key = 'b3bd6711d937ffd4255ea0cea8f91c2a'

#print indicoio.fer("henry.jpg")
#print indicoio.fer("happy.jpg")
print json.dumps( indicoio.fer("sad1.jpg"), indent=4)
#print indicoio.fer("angry.jpg")

