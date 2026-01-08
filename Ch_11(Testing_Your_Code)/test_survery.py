import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = 'What language did you first learn to speak?'
        my_survery = AnonymousSurvey(question)

        my_survery.store_response('English')

        self.assertIn('English', my_survery.responses)

    def test_store_three_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for res in responses:
            self.assertIn(res, my_survey.responses)

unittest.main()