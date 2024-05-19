import pandas as pd

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
