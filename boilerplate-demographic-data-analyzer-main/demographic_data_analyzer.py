import pandas as pd

def calculate_demographic_data(print_data=True):
  # Read data from file
  data = pd.read_csv(
    r'https://replit.com/@Pranay_Agl7/MildLustrousManagement#boilerplate-demographic-data-analyzer-main/adult.data.csv'
  )

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = data['race'].value_counts()

  # What is the average age of men?
  average_age_men = data[data.sex == 'Male'].age.mean()

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(
    data.education.value_counts(normalize=True).Bachelors * 100, 2)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  q1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
  q2 = df['salary'] == '>50K'

  # percentage with salary >50K
  higher_education_rich = round((q1 & q2).sum() / q1.sum() * 100, 1)
  lower_education_rich = round((~q1 & q2).sum() / (~q1).sum() * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = data['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  people = round(
    data[data['hours-per-week'] == min_work_hours].value_counts(normalise=True)
    * 100, 2)
  num_min_workers = people

  people = data[data['hours-per-week'] == min_work_hours]
  people_min_salary = people.salary.value_counts(normalize=True)['>50K']

  min_salary = round(people_min_salary * 100, 2)

  rich_percentage = min_salary

  # What country has the highest percentage of people that earn >50K?
  country_data = data.groupby('native-country')
  ['salary'].value_counts(normalize=True)[:, '>50K']
  country_data_round = round(country_data * 100, 2)

  highest_earning_country = country_data.sort_values(ascending=False).index[0]

  highest_earning_country_percentage = country_data_round.max()

  # Identify the most popular occupation for those who earn >50K in India.
  mask = (data['salary'] == '>50K') & (data['native-country'] == 'India')

  top_IN_occupation = (data[mask]['occupation'].value_counts(
    normalize=True)[:1].index[0])

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
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
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
