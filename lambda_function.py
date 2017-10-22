import random 

dinnerOptions = ["Chicken", "Beef", "Pork", "Fish", "Vegetarian"]

def lambda_handler(event, context):
    dinner = random.choice(dinnerOptions)
    response = {
        'version': '1.0', 
        'response': {
            'outputSpeech': {
                'type': 'PlainText', 
                'text': 'pizza with chicken noodle soup and rice and broclli beef and corn and sprite with lemonade'
            }
        }
    }
    return response
