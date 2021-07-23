import pandas as pd
import statistics
import csv
df=pd.read_csv("StudentsPerformance.csv")
gender_list=df["gender"].to_list()
level_list=df["parental level of education"].to_list()
gender_mean=statistics.mean(gender_list)
level_mean=statistics.mean(level_list)
gender_median=statistics.median(gender_list)
level_median=statistics.median(level_list)
gender_mode=statistics.mode(gender_list)
level_mode=statistics.mode(level_list)
gender_std_deviation=statistics.stdev(gender_list)
level_std_deviation=statistics.stdev(level_list)

print("mean, median, and mode of gender is{}, {} and{}".format(gender_mean, gender_median, gender_mode))
print("mean, median, and mode of level is {}, {}, and{}".format(level_mean, level_median, level_mode))
gender_first_std_deviation_start,gender_first_std_deviation_end=gender_mean-gender_std_deviation, gender_mean+gender_std_deviation
gender_second_std_deviation_start, gender_second_std_deviation_end=gender_mean-(2*gender_std_deviation), gender_mean+(2*gender_std_deviation)
gender_third_std_devation_start, gender_third_std_deviation_end=gender_mean-(3*gender_std_deviation), gender_mean+(3*gender_std_deviation)

level_first_std_deviation_start,level_first_std_deviation_end=level_mean-level_std_deviation, level_mean+level_std_deviation
level_second_std_deviation_start, level_second_std_deviation_end=level_mean-(2*level_std_deviation), level_mean+(2*level_std_deviation)
level_third_std_devation_start, level_third_std_deviation_end=level_mean-(3*level_std_deviation), level_mean+(3*level_std_deviation)

gender_list_of_data_within_1_std_deviation=[result for result in gender_list if result>gender_first_std_deviation_start and result< gender_first_std_deviation_end]
gender_list_of_data_within_2_std_deviation=[result for result in gender_list if result>gender_second_std_deviation_start and result< gender_second_std_deviation_end]
gender_list_of_data_within_3_std_deviation=[result for result in gender_list if result>gender_third_std_devation_start and result< gender_third_std_deviation_end]

level_list_of_data_within_1_std_deviation=[result for result in level_list if result>level_first_std_deviation_start and result<level_first_std_deviation_end]
level_list_of_data_within_2_std_deviation=[result for result in level_list if result>level_second_std_deviation_start and result<level_second_std_deviation_end]
level_list_of_data_within_3_std_deviation=[result for result in level_list if result>level_third_std_devation_start and result< level_third_std_deviation_end]

print("{}% of data for gender lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 2 stadard deviation". format(len(gender_list_of_data_within_2_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 3 standard deviation". format(len(gender_list_of_data_within_3_std_deviation)*100.0/len(gender_list)))

print("{}% of data for level lies within 1 standard deviation".format(len(level_list_of_data_within_1_std_deviation)*100.0/len(level_list)))
print("{}% of data for level lies within 2 stadard deviation". format(len(level_list_of_data_within_2_std_deviation)*100.0/len(level_list)))
print("{}% of data for level lies within 3 standard deviation". format(len(level_list_of_data_within_3_std_deviation)*100.0/len(level_list)))