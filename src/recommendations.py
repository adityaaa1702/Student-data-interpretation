def generate_recommendations(performance_report):
    recommendations = []
    for test_id, test_report in performance_report.items():
        for section_id, section_report in test_report.items():
            if section_id != "overall":
                if section_report["accuracy"] < 0.7:
                    recommendations.append(f"Review material for section {section_id} in test {test_id}")
                if section_report["time_spent"] > ideal_time_for_section(section_id):
                    recommendations.append(f"Improve time management for section {section_id} in test {test_id}")
            overall_report = test_report["overall"]
            if overall_report["fatigue_trends"]:
                recommendations.append(f"Develop test stamina for test {test_id} by practicing longer test sessions")
    return recommendations

def ideal_time_for_section(section_id):
    return 600  # Example: 10 minutes per section
