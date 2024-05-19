import pandas as pd
import json

def preprocess_data(json_data):
    preprocessed_data = []

    for test in json_data:
        try:
            test_id = test['_id']['$oid']
            user_id = test['userId']['$oid']
            is_bonus_attempted = test.get('isBonusAttempted', False)

            for section in test['sections']:
                section_id = section['_id']['$oid']

                for question in section['questions']:
                    question_id = question['_id']['$oid']
                    marked_options = [opt['optionId'] for opt in question.get('markedOptions', [])]
                    is_correct = all(opt.get('isCorrect', False) for opt in question.get('markedOptions', []))
                    input_value = question.get('inputValue', {}).get('value', None)
                    time_taken = question.get('timeTaken', 0)
                    time_left_when_attempted = question.get('timeLeftWhenAttempted', 0)
                    status = question.get('status', 'unknown')

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
        except KeyError as e:
            print(f"Missing key in data: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return pd.DataFrame(preprocessed_data)

def analyze_overall_performance(data):
    overall_analysis = []

    grouped_data = data.groupby('test_id')

    for test_id, group in grouped_data:
        total_time_taken = group['time_taken'].sum()
        total_correct_answers = group['is_correct'].sum()
        total_questions = group['question_id'].nunique()
        total_sections = group['section_id'].nunique()

        performance = {
            'test_id': test_id,
            'total_time_taken': total_time_taken,
            'total_correct_answers': total_correct_answers,
            'total_questions': total_questions,
            'total_sections': total_sections,
            'accuracy': total_correct_answers / total_questions if total_questions > 0 else 0
        }
        overall_analysis.append(performance)

    return pd.DataFrame(overall_analysis)

if __name__ == "__main__":
    try:
        # Load JSON data from file
        with open('student_data.json') as file:
            json_data = json.load(file)

        # Preprocess data
        preprocessed_data = preprocess_data(json_data)

        # Analyze overall performance
        overall_performance = analyze_overall_performance(preprocessed_data)

        # Print results
        print(overall_performance.head())
    except FileNotFoundError:
        print("The file 'student_data.json' was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    except Exception as e:
        print(f"Unexpected error: {e}")
