# Dictionary to store the count of each type of vulnerability severity.
# The keys represent the severity categories and the initial values ​​are 0.
# This dictionary will be updated as vulnerabilities are classified.
rating_types_counts = {
       "None": 0,
       "Low": 0,
       "Medium": 0,
       "High": 0,
       "Critical": 0,
       "Invalid score": 0
}
    
    
def get_rating_types_counts(score):
    """
    Function that classifies a score 
    
    Args:
        score (float): The score to be ranked.

    Returns:
        dict: A dictionary with the updated count for each type of classification.
    """
    if score == 0.0:
        rating_types_counts["None"] += 1
    elif 0.1 <= score and score <= 3.9:
        rating_types_counts["Low"] += 1
    elif 4.0 <= score and score <= 6.9:
        rating_types_counts["Medium"] += 1
    elif 7.0 <= score and score <= 8.9:
        rating_types_counts["High"] += 1
    elif 9.0 <= score and score <= 10.0:
        rating_types_counts["Critical"] += 1
    else:
        return "Invalid score"
    return rating_types_counts
