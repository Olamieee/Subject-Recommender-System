from django.core.management.base import BaseCommand
from recommenderApp.models import IQQuestion


class Command(BaseCommand):
    help = 'Create sample IQ test questions'
    
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating sample IQ test questions...'))
        create_sample_questions()
        self.stdout.write(self.style.SUCCESS('Done!'))

        
def create_sample_questions():
    # Logical Reasoning Questions
    logical_questions = [
        {
            'question': 'If all roses are flowers and some flowers fade quickly, then:',
            'option_a': 'All roses fade quickly',
            'option_b': 'Some roses fade quickly',
            'option_c': 'No roses fade quickly',
            'option_d': 'Roses never fade quickly',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'Continue the sequence: 2, 6, 12, 20, 30, ?',
            'option_a': '36',
            'option_b': '40',
            'option_c': '42',
            'option_d': '48',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'If water is to ice as milk is to:',
            'option_a': 'Coffee',
            'option_b': 'Cheese',
            'option_c': 'Cream',
            'option_d': 'Yogurt',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 1
        },
        {
            'question': 'Which shape doesn\'t belong in this group?',
            'option_a': 'Square',
            'option_b': 'Rectangle',
            'option_c': 'Triangle',
            'option_d': 'Pentagon',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 1
        },
    ]
    
    # Verbal Reasoning Questions
    verbal_questions = [
        {
            'question': 'Choose the word that is most dissimilar to the others:',
            'option_a': 'Swift',
            'option_b': 'Quick',
            'option_c': 'Rapid',
            'option_d': 'Sluggish',
            'correct_answer': 'D',
            'question_type': 'verbal',
            'difficulty': 1
        },
        {
            'question': 'Complete the analogy: Book is to Reader as Movie is to:',
            'option_a': 'Director',
            'option_b': 'Actor',
            'option_c': 'Viewer',
            'option_d': 'Screen',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 1
        },
        {
            'question': 'If the meaning of TACIT is unspoken, which word is closest in meaning?',
            'option_a': 'Verbose',
            'option_b': 'Implicit',
            'option_c': 'Redundant',
            'option_d': 'Overt',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'The opposite of FRUGAL is:',
            'option_a': 'Wealthy',
            'option_b': 'Extravagant',
            'option_c': 'Miserly',
            'option_d': 'Prudent',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 2
        },
    ]
    
    # Numerical Reasoning Questions
    numerical_questions = [
        {
            'question': 'If a shirt originally costs $80 and is discounted by 25%, what is the new price?',
            'option_a': '$55',
            'option_b': '$60',
            'option_c': '$65',
            'option_d': '$70',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'If 5 people can complete a project in 10 days, how many days would it take 2 people to complete the same project?',
            'option_a': '20 days',
            'option_b': '25 days',
            'option_c': '30 days',
            'option_d': '40 days',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If x² + 6x + 9 = 16, what is the value of x?',
            'option_a': '1',
            'option_b': '2',
            'option_c': '3',
            'option_d': '4',
            'correct_answer': 'D',
            'question_type': 'numerical',
            'difficulty': 3
        },
        {
            'question': 'A car travels 150 miles in 3 hours. What is its average speed in miles per hour?',
            'option_a': '30 mph',
            'option_b': '45 mph',
            'option_c': '50 mph',
            'option_d': '60 mph',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 1
        },
    ]
    
    # Spatial Reasoning Questions
    spatial_questions = [
        {
            'question': 'If you rearrange the letters "CIFAIPC", you would get the name of a:',
            'option_a': 'City',
            'option_b': 'Country',
            'option_c': 'Ocean',
            'option_d': 'Animal',
            'correct_answer': 'A',  # PACIFIC
            'question_type': 'spatial',  # Keep the categorization if needed
            'difficulty': 2
        },
        {
            'question': 'Which number should come next in this series: 1, 4, 9, 16, 25, ...?',
            'option_a': '30',
            'option_b': '36',
            'option_c': '49',
            'option_d': '64',
            'correct_answer': 'B',  # 36 (square of 6)
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'Which word does NOT belong with the others?',
            'option_a': 'Rectangle',
            'option_b': 'Triangle',
            'option_c': 'Circle',
            'option_d': 'Sphere',
            'correct_answer': 'D',  # 3D shape vs 2D shapes
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'If you fold a square paper in half diagonally, what shape do you get?',
            'option_a': 'Rectangle',
            'option_b': 'Triangle',
            'option_c': 'Pentagon',
            'option_d': 'Hexagon',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 1
        },
    ]
    
    # Combine all questions
    all_questions = logical_questions + verbal_questions + numerical_questions + spatial_questions
    
    # Create the questions in the database
    for q_data in all_questions:
        IQQuestion.objects.create(**q_data)
    
    print(f"Created {len(all_questions)} IQ test questions")



# To run this script
# python manage.py create_sample_questions
# Or call the create_sample_questions() function directly in a migration or from a shell