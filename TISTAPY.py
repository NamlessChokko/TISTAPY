import math  
import TISTAUTI as UT


def z_test(p_sample: float, p_null: float, sampleSize: int) -> float:
    # Conditions to check if the sample size is large enough for a Z-test
    conditionsForZTest = [(sampleSize * p_sample) < 10, sampleSize * (1 - p_sample) < 10]

    # If either of the conditions is violated (n*p or n*(1-p) should be >= 10), the test can't be executed
    if conditionsForZTest[0] or conditionsForZTest[1]:
        print("*Failed to execute operation: ")
        # Print specific failure conditions
        if conditionsForZTest[0]:
            UT.errorDetection(301) 
        if conditionsForZTest[1]:
            UT.errorDetection(302)
        return None  # Return 0 to indicate failure to execute test

    # Calculate the numerator (difference between sample proportion and null proportion)
    numerator = p_sample - p_null
    # Calculate the denominator (standard error of the sample proportion)
    denominator = math.sqrt((p_null * (1 - p_null)) / sampleSize)

    # Return the Z-test statistic, which is the ratio of the numerator and denominator
    return numerator / denominator

def t_test(x_bar: float, mu_null: float, s_sample: float, sampleSize: int) -> float:
    # Conditions to determine whether the sample size is appropriate for a t-test
    conditionsForTTest = [sampleSize < 15, sampleSize >= 15 and sampleSize < 40]

    # Check for the condition when sample size is less than 15
    if conditionsForTTest[0]:
        print("\n𝑛 < 15. The data should be very close to a Normal model. Do not use t-methods if there is strong skewness or outliers.")
    # Check for the condition when sample size is between 15 and 40
    elif conditionsForTTest[1]:
        print("\n15 ≤ 𝑛 < 40. t-methods should work as long as the data is unimodal and reasonably symmetric (make a histogram). t-methods should not be used in the presence of outliers or strong skewness.")

    # Calculate the numerator (difference between sample mean and null hypothesis mean)
    numerator = x_bar - mu_null
    # Calculate the denominator (standard error of the sample mean)
    denominator = s_sample / (math.sqrt(sampleSize))

    # Return the t-test statistic, which is the ratio of the numerator and denominator
    return numerator / denominator


