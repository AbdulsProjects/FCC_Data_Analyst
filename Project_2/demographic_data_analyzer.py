import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    sum_total = len(df)

    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    
    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    

    # What is the percentage of people who have a Bachelor's degree?
    education_series = (df['education'].value_counts())
    percentage_bachelors = round((education_series['Bachelors']/education_series.sum())*100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    sum_higher = (education_series['Bachelors']) + (education_series['Masters']) + (education_series['Doctorate'])
    sum_lower = education_series.sum() - sum_higher
    higher_education = ((sum_higher) / education_series.sum())*100
    lower_education = 100 - higher_education


    # percentage with salary >50K

    all_higher_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    sum_higher_rich = len(all_higher_rich)
    higher_education_rich = round((sum_higher_rich / sum_higher) * 100, 1)


    all_lower_rich = df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    sum_lower_rich = len(all_lower_rich)
    lower_education_rich = round((sum_lower_rich / sum_lower) * 100,1)


    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == 1])
    num_min_rich = len(df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])

    rich_percentage = (num_min_rich / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    df2 = df.copy()
    df2 = df2[(df2['salary'] == '>50K')]
    country_rich = (df2['native-country'].value_counts())
    country_total =(df['native-country'].value_counts())
    df3 = pd.concat([country_rich, country_total], axis=1)
    df3.columns.values[0] = 'rich'
    df3.columns.values[1] = 'total'
    df3 = df3.dropna().drop(['?'])
    df3['rich_percent'] = (df3['rich'] / df3['total']) *100

    
    



    highest_earning_country_series = df3.loc[df3['rich_percent'].idxmax()]
    highest_earning_country = highest_earning_country_series.name
    highest_earning_country_percentage = round(highest_earning_country_series[2],1)


    # Identify the most popular occupation for those who earn >50K in India.
    India_50k = df2[df2['native-country'] == 'India']
    top_IN_occupation = (India_50k['occupation'].mode())[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
