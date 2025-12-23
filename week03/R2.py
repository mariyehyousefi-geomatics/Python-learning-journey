def scores_report(*scores):
    return sum(scores)/len(scores)
op=scores_report(100,96,50,65,73)
print(f"average of the scores is:{op}")
