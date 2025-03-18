from django.core.management.base import BaseCommand
from recommenderApp.models import IQQuestion


class Command(BaseCommand):
    help = 'Create sample IQ test questions'
    
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating sample IQ test questions...'))
    
        existing_questions = set(IQQuestion.objects.values_list('question', flat=True)) #get existing questions
        
        all_questions = create_sample_questions()
        new_questions = [q for q in all_questions if q['question'] not in existing_questions] #create list of new questions to add
        
        self.stdout.write(f"Found {len(existing_questions)} existing questions")
        self.stdout.write(f"Found {len(new_questions)} new questions to add")
        
        #create only the new questions
        for q_data in new_questions:
            IQQuestion.objects.create(**q_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(new_questions)} new questions!'))


        
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
        {
            'question': 'If A implies B, and B implies C, then:',
            'option_a': 'C implies A',
            'option_b': 'A implies C',
            'option_c': 'A and C are equivalent',
            'option_d': 'None of the above',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'Continue the pattern: 3, 6, 9, 18, 27, ?',
            'option_a': '36',
            'option_b': '54',
            'option_c': '81',
            'option_d': '108',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 3
        },
        {
            'question': 'If all Zorks are Blips and no Blips are Quids, then:',
            'option_a': 'Some Zorks are Quids',
            'option_b': 'All Zorks are Quids',
            'option_c': 'No Zorks are Quids',
            'option_d': 'Some Quids are Zorks',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'What comes next in the sequence: J, F, M, A, M, J, ?',
            'option_a': 'S',
            'option_b': 'O',
            'option_c': 'J',
            'option_d': 'A',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 1
        },
        {
            'question': 'Which number does not belong in this series: 2, 5, 10, 17, 26, 37, 50, 64',
            'option_a': '17',
            'option_b': '37',
            'option_c': '50',
            'option_d': '64',
            'correct_answer': 'D',
            'question_type': 'logical',
            'difficulty': 3
        },
        {
            'question': 'If 5 cats can catch 5 mice in 5 minutes, how long would it take 1 cat to catch 1 mouse?',
            'option_a': '1 minute',
            'option_b': '5 minutes',
            'option_c': '25 minutes',
            'option_d': 'The information is insufficient',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'In a race, if you overtake the second person, what position are you in?',
            'option_a': 'First',
            'option_b': 'Second',
            'option_c': 'Third',
            'option_d': 'Cannot be determined',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 1
        },
        {
            'question': 'Which statement logically follows: "If it rains, the ground gets wet"?',
            'option_a': 'If it does not rain, the ground does not get wet',
            'option_b': 'If the ground is wet, it rained',
            'option_c': 'If the ground is not wet, it did not rain',
            'option_d': 'None of the above',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'Continue the sequence: 1, 3, 6, 10, 15, ?',
            'option_a': '18',
            'option_b': '20',
            'option_c': '21',
            'option_d': '25',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'If no A is B, and all B are C, then:',
            'option_a': 'No A is C',
            'option_b': 'Some A are C',
            'option_c': 'All A are C',
            'option_d': 'No conclusion is possible',
            'correct_answer': 'D',
            'question_type': 'logical',
            'difficulty': 3
        },
        {
            'question': 'If R comes before S, and T comes before R, which comes first?',
            'option_a': 'R',
            'option_b': 'S',
            'option_c': 'T',
            'option_d': 'Cannot be determined',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 1
        },
        {
            'question': 'What is the next number in the sequence: 1, 4, 9, 16, 25, 36, ?',
            'option_a': '42',
            'option_b': '47',
            'option_c': '49',
            'option_d': '51',
            'correct_answer': 'C',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'If a = 2b, b = 3c, and c = 4, what is the value of a?',
            'option_a': '16',
            'option_b': '24',
            'option_c': '28',
            'option_d': '32',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 2
        },
        {
            'question': 'All Flinks are Blops. Some Blops are Clunks. Therefore:',
            'option_a': 'All Flinks are Clunks',
            'option_b': 'Some Flinks are Clunks',
            'option_c': 'No Flinks are Clunks',
            'option_d': 'None of the above can be concluded',
            'correct_answer': 'D',
            'question_type': 'logical',
            'difficulty': 3
        },
        {
            'question': 'If all As are Bs, and all Bs are Cs, then:',
            'option_a': 'Some Cs are As',
            'option_b': 'All As are Cs',
            'option_c': 'No Cs are As',
            'option_d': 'All Cs are As',
            'correct_answer': 'B',
            'question_type': 'logical',
            'difficulty': 1
        },
        {
            'question': 'Continue the pattern: 8, 16, 24, 32, ?',
            'option_a': '36',
            'option_b': '38',
            'option_c': '40',
            'option_d': '48',
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
        {
            'question': 'Choose the word that means the same as BENEVOLENT:',
            'option_a': 'Malicious',
            'option_b': 'Kind',
            'option_c': 'Intelligent',
            'option_d': 'Cautious',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'Complete the analogy: Hand is to Glove as Head is to:',
            'option_a': 'Neck',
            'option_b': 'Brain',
            'option_c': 'Hat',
            'option_d': 'Hair',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 1
        },
        {
            'question': 'Choose the word that does not belong with the others:',
            'option_a': 'Symphony',
            'option_b': 'Concerto',
            'option_c': 'Orchestra',
            'option_d': 'Sonata',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'ADUMBRATE is to OUTLINE as CASTIGATE is to:',
            'option_a': 'Praise',
            'option_b': 'Punish',
            'option_c': 'Forgive',
            'option_d': 'Forget',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Choose the word that best completes the sentence: The professor\'s lecture was so _____ that many students fell asleep.',
            'option_a': 'Stimulating',
            'option_b': 'Provocative',
            'option_c': 'Soporific',
            'option_d': 'Contentious',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Complete the analogy: Winter is to Summer as Cold is to:',
            'option_a': 'Snow',
            'option_b': 'Hot',
            'option_c': 'Spring',
            'option_d': 'Weather',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 1
        },
        {
            'question': 'The opposite of ACQUIESCE is:',
            'option_a': 'Resist',
            'option_b': 'Accept',
            'option_c': 'Question',
            'option_d': 'Agree',
            'correct_answer': 'A',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Choose the word that does not belong:',
            'option_a': 'Furtive',
            'option_b': 'Covert',
            'option_c': 'Clandestine',
            'option_d': 'Overt',
            'correct_answer': 'D',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Complete the analogy: Fish is to School as Wolf is to:',
            'option_a': 'Flock',
            'option_b': 'Pack',
            'option_c': 'Herd',
            'option_d': 'Pride',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'Identify the synonym for EPHEMERAL:',
            'option_a': 'Lasting',
            'option_b': 'Temporary',
            'option_c': 'Significant',
            'option_d': 'Sturdy',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Choose the word that best completes the sentence: The politician was known for his _____ speeches that never addressed the real issues.',
            'option_a': 'Concise',
            'option_b': 'Verbose',
            'option_c': 'Laconic',
            'option_d': 'Pertinent',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'Choose the word most opposite to VERBOSE:',
            'option_a': 'Quiet',
            'option_b': 'Concise',
            'option_c': 'Silent',
            'option_d': 'Lengthy',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'Complete the analogy: Paint is to Canvas as Ink is to:',
            'option_a': 'Pen',
            'option_b': 'Writer',
            'option_c': 'Paper',
            'option_d': 'Book',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 1
        },
        {
            'question': 'Choose the word that best completes this sentence: Despite his reputation for being _____, the professor gave a surprisingly short lecture.',
            'option_a': 'Loquacious',
            'option_b': 'Taciturn',
            'option_c': 'Reticent',
            'option_d': 'Reserved',
            'correct_answer': 'A',
            'question_type': 'verbal',
            'difficulty': 3
        },
        {
            'question': 'Choose the word that does not belong:',
            'option_a': 'Ecstatic',
            'option_b': 'Euphoric',
            'option_c': 'Melancholic',
            'option_d': 'Jubilant',
            'correct_answer': 'C',
            'question_type': 'verbal',
            'difficulty': 2
        },
        {
            'question': 'Complete the analogy: Doctor is to Hospital as Teacher is to:',
            'option_a': 'Student',
            'option_b': 'School',
            'option_c': 'Education',
            'option_d': 'Knowledge',
            'correct_answer': 'B',
            'question_type': 'verbal',
            'difficulty': 1
        }
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
        {
            'question': 'If 3 apples and 4 oranges cost $2.85, and 5 apples and 2 oranges cost $2.65, what is the cost of 1 apple?',
            'option_a': '$0.30',
            'option_b': '$0.35',
            'option_c': '$0.40',
            'option_d': '$0.45',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 3
        },
        {
            'question': 'If a number is increased by 20% and then decreased by 20%, the final result is:',
            'option_a': 'Same as original',
            'option_b': '4% less than original',
            'option_c': '4% more than original',
            'option_d': '20% less than original',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'What is the next number in this sequence: 1, 2, 4, 8, 16, ?',
            'option_a': '24',
            'option_b': '30',
            'option_c': '32',
            'option_d': '36',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'A clock shows 3:15. What is the angle between the hour and minute hands?',
            'option_a': '7.5 degrees',
            'option_b': '15 degrees',
            'option_c': '22.5 degrees',
            'option_d': '30 degrees',
            'correct_answer': 'A',
            'question_type': 'numerical',
            'difficulty': 3
        },
        {
            'question': 'What is the sum of the first 50 natural numbers?',
            'option_a': '1225',
            'option_b': '1250',
            'option_c': '1275',
            'option_d': '1300',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If a rectangle has a perimeter of 30 units and a width of 5 units, what is its area?',
            'option_a': '50 square units',
            'option_b': '75 square units',
            'option_c': '100 square units',
            'option_d': '150 square units',
            'correct_answer': 'A',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If the probability of an event occurring is 0.4, what is the probability of it not occurring?',
            'option_a': '0.4',
            'option_b': '0.6',
            'option_c': '0.8',
            'option_d': '1.0',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'If 3x - 5 = 10, what is the value of 2x + 7?',
            'option_a': '12',
            'option_b': '15',
            'option_c': '17',
            'option_d': '20',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'A tank can be filled by pipe A in 3 hours and by pipe B in 6 hours. How long would it take to fill the tank if both pipes are used?',
            'option_a': '1 hour',
            'option_b': '2 hours',
            'option_c': '3 hours',
            'option_d': '4 hours',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If √(x + 5) = 4, what is the value of x?',
            'option_a': '9',
            'option_b': '11',
            'option_c': '16',
            'option_d': '21',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'In a class of 30 students, 60% are girls. How many boys are in the class?',
            'option_a': '12',
            'option_b': '15',
            'option_c': '18',
            'option_d': '20',
            'correct_answer': 'A',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'If 3x + 7 = 22, what is the value of x?',
            'option_a': '3',
            'option_b': '5',
            'option_c': '7',
            'option_d': '9',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'A book costs $24 after a 20% discount. What was the original price?',
            'option_a': '$28.80',
            'option_b': '$30',
            'option_c': '$32',
            'option_d': '$38.40',
            'correct_answer': 'B',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If a car travels 240 miles on 10 gallons of gas, how many miles can it travel on 15 gallons?',
            'option_a': '320 miles',
            'option_b': '350 miles',
            'option_c': '360 miles',
            'option_d': '400 miles',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 1
        },
        {
            'question': 'What is the next number in the sequence: 2, 6, 12, 20, 30, ?',
            'option_a': '36',
            'option_b': '40',
            'option_c': '42',
            'option_d': '48',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 2
        },
        {
            'question': 'If log(x) = 3, what is the value of x?',
            'option_a': '30',
            'option_b': '100',
            'option_c': '1000',
            'option_d': '10000',
            'correct_answer': 'C',
            'question_type': 'numerical',
            'difficulty': 3
        }
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
            'question_type': 'spatial',
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
        {
            'question': 'Rearrange the letters in "NOITACUDE" to get a common word:',
            'option_a': 'DEDICATION',
            'option_b': 'CAUTIONED',
            'option_c': 'EDUCATION',
            'option_d': 'AUCTIONED',
            'correct_answer': 'C',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'If you rearrange the letters in "LISTEN", you get:',
            'option_a': 'ENLIST',
            'option_b': 'SILENT',
            'option_c': 'TINSEL',
            'option_d': 'All of the above',
            'correct_answer': 'D',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'A cube has how many edges?',
            'option_a': '6',
            'option_b': '8',
            'option_c': '10',
            'option_d': '12',
            'correct_answer': 'D',
            'question_type': 'spatial',
            'difficulty': 1
        },
        {
            'question': 'What is the minimum number of straight cuts needed to divide a circular cake into 8 equal pieces?',
            'option_a': '3',
            'option_b': '4',
            'option_c': '7',
            'option_d': '8',
            'correct_answer': 'A',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'If a cube has a surface area of 24 square units, what is its volume?',
            'option_a': '4 cubic units',
            'option_b': '6 cubic units',
            'option_c': '8 cubic units',
            'option_d': '12 cubic units',
            'correct_answer': 'C',
            'question_type': 'spatial',
            'difficulty': 3
        },
        {
            'question': 'Unscramble "MROFPRET" to get a common word:',
            'option_a': 'PLATFORM',
            'option_b': 'PERFORM',
            'option_c': 'TRANSFORM',
            'option_d': 'FRAGMENT',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'How many squares are there on a standard 8×8 chessboard?',
            'option_a': '64',
            'option_b': '128',
            'option_c': '204',
            'option_d': '256',
            'correct_answer': 'C',
            'question_type': 'spatial',
            'difficulty': 3
        },
        {
            'question': 'If you invert the following sequence, what shape would you get? /\\__/',
            'option_a': '/\\__/',
            'option_b': '\\/__\\',
            'option_c': '/--\\',
            'option_d': '\\__/',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 1
        },
        {
            'question': 'A cylindrical tank with radius 7 units and height 10 units is filled with water. If the water is transferred to a cubic tank with side length 10 units, what fraction of the cubic tank will be filled?',
            'option_a': '49%',
            'option_b': '70%',
            'option_c': '73%',
            'option_d': '77%',
            'correct_answer': 'A', # π*7²*10 ÷ 10³ ≈ 0.49
            'question_type': 'spatial',
            'difficulty': 3
        },
        {
            'question': 'Unscramble the letters "TAREASDIS" to form a common word:',
            'option_a': 'ASSISTANCE',
            'option_b': 'RESISTANCE',
            'option_c': 'STAIRCASED',
            'option_d': 'DISASTREA',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'When three identical cubes are stacked in a row, what is the minimum number of faces that can be seen from the outside?',
            'option_a': '12',
            'option_b': '14',
            'option_c': '16',
            'option_d': '18',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'Which of these nets will fold into a cube?',
            'option_a': 'Six squares in a straight line',
            'option_b': 'Six squares arranged in a T-shape',
            'option_c': 'Six squares arranged in a 2×3 rectangle',
            'option_d': 'Five squares arranged in a cross shape',
            'correct_answer': 'B',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'If you unscramble "GEARRIB", you will get:',
            'option_a': 'BARRIER',
            'option_b': 'BAGGER',
            'option_c': 'BARGAIN',
            'option_d': 'BRAGIER',
            'correct_answer': 'A',
            'question_type': 'spatial',
            'difficulty': 2
        },
        {
            'question': 'How many faces does a triangular prism have?',
            'option_a': '3',
            'option_b': '4',
            'option_c': '5',
            'option_d': '6',
            'correct_answer': 'C',
            'question_type': 'spatial',
            'difficulty': 1
        },
        {
            'question': 'Which shape has the most sides?',
            'option_a': 'Pentagon',
            'option_b': 'Hexagon',
            'option_c': 'Octagon',
            'option_d': 'Nonagon',
            'correct_answer': 'D',
            'question_type': 'spatial',
            'difficulty': 1
        },
        {
            'question': 'What is the volume of a sphere with radius 3 units?',
            'option_a': '36π cubic units',
            'option_b': '27π cubic units',
            'option_c': '12π cubic units',
            'option_d': '4π cubic units',
            'correct_answer': 'A',
            'question_type': 'spatial',
            'difficulty': 3
        },
    ]
    
    # Combine all questions
    all_questions = logical_questions + verbal_questions + numerical_questions + spatial_questions
    
    return all_questions