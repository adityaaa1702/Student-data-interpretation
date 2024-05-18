import os
import pandas as pd
import json

def preprocess_data(json_data):
    preprocessed_data = []

    for test in json_data:
        test_id = test['_id']['$oid']
        user_id = test['userId']['$oid']
        is_bonus_attempted = test['isBonusAttempted']

        for section in test['sections']:
            section_id = section['_id']['$oid']

            for question in section['questions']:
                question_id = question['_id']['$oid']
                marked_options = [opt['optionId'] for opt in question.get('markedOptions', [])]
                is_correct = all(opt['isCorrect'] for opt in question.get('markedOptions', []))
                input_value = question['inputValue'].get('value') if question['inputValue'] else None
                time_taken = question['timeTaken']
                time_left_when_attempted = question['timeLeftWhenAttempted']
                status = question['status']

                preprocessed_data.append({
                    'test_id': test_id,
                    'user_id': user_id,
                    'is_bonus_attempted': is_bonus_attempted,
                    'section_id': section_id,
                    'question_id': question_id,
                    'marked_options': marked_options,
                    'is_correct': is_correct,
                    'input_value': input_value,
                    'time_taken': time_taken,
                    'time_left_when_attempted': time_left_when_attempted,
                    'status': status
                })

    return pd.DataFrame(preprocessed_data)

if __name__ == "__main__":
    # Get the full path to the student_data.json file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, 'data', 'student_data.json')

    # Load JSON data from file
    with open(data_file_path) as file:
        json_data = json.load(file)
    
    # Preprocess data
    preprocessed_data = preprocess_data(json_data)

    # Save preprocessed data to a CSV file
    output_file_path = os.path.join(script_dir, 'notebooks/data', 'preprocessed_data.csv')
    preprocessed_data.to_csv(output_file_path, index=False)

    print("Data preprocessing completed. Preprocessed data saved to:", output_file_path)
