from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
my_survery = AnonymousSurvey(question)

my_survery.show_questions()

print("Enter 'q' to exit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break   
    my_survery.store_response(response)

print("\nThank you everyone who participated in the survey!")
my_survery.show_results()