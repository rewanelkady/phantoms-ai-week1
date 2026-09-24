def process_team_scores(scores_list):

    total_score = 0
    passed_members = []

    for i in range(len(scores_list)): 
        # i = 0,1,2,3,4     # [45, 50, 75, 90, 60]
        score = scores_list[i] 
        total_score += score  # 320
        
        if score >= 50: 
            passed_members.append(score)  # [50,75,90,60]
        
    try:
        average = total_score / len(scores_list)  # 64
    except ZeroDivisionError:
        print ("Find Error")
        average = 0

    return average, passed_members

sample_scores = [45, 50, 75, 90, 60]
avg, passed = process_team_scores(sample_scores)
print(f"Average: {avg}, Passed: {passed}")