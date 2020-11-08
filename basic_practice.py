import spacy
import pandas as pd


nlp = spacy.load('en_core_web_lg')
list_1 = [
    'Explain how AI impacts society',
    'Apply AI methods to perform practical tasks',
    'Synthesize a simple AI system',
    'Evaluate different AI approaches to solve a problem',
    'Explain the basic principles of the data mining process',
    'Prepare data for mining and exploration',
    'Use data mining techniques and modern tools to discover trends and patterns in realistic datasets',
    'Evaluate different data mining models/techniques with respect to their performance accuracy',
    'Function on teams and communicate effectively in written and oral forms.',
    'Explain techniques of mathematical models.',
    'Design models for simple and complex problems.',
    'Model discrete event systems.',
    'Use simulation software to solve complicated problems.',
    'Evaluate the performance of different systems using simulation techniques.',
    'Describe the main components of a machine learning system.',
    'Design training sets and testing sets for machine learning tasks.',
    'Apply machine learning techniques to discover trends and patterns in realistic datasets.',
    'Evaluate different machine learning techniques in terms of their applicability to different Machine Learning problems',
    'Explain the engineering design process, principles, and standards',
    'Use project management tools in Computer Science projects'
]
index = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14', 'c15','c16','c17','c18','c19','c20']
list_2 = [
    'Analyze a complex computing problem and to apply principles of computing and other relevant disciplines to identify solutions.',
    'Design, implement, and evaluate a computing-based solution to meet a given set of computing requirements in the context of the program’s discipline',
    'Communicate effectively in a variety of professional contexts',
    'Recognize professional responsibilities and make informed judgments in computing practice based on legal and ethical principles',
    'Function effectively as a member or leader of a team engaged in activities appropriate to the program’s discipline.',
    'Apply computer science theory and software development fundamentals to produce computing-based solutions.'
    ]
column = ['p1','p2','p3','p4','p5','p6']
nlp= spacy.load('en_core_web_lg')
print(nlp('asif').similarity(nlp('asif')))
def calculate_similarity():
    result = []
    for obj_p in list_1:
        sim_list = []
        for obj_c in list_2:
            sim_list.append(nlp(obj_p).similarity(nlp(obj_c)))
        result.append(sim_list)
    return result
df = pd.DataFrame(calculate_similarity(), index=index,columns=column)
print(df)
