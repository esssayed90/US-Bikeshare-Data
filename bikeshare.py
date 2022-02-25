import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city_data):pd.read_csv(city_data[city])
    """
    Asks user to specify a city, month, and day to analyze.
df['city'] = df['start time'].dt.city
df['month'] = df['start time'].dt.month
df['day_of_week'] = df['start time'].dt.weekday_name
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
month= months.index(month) + 1

    # TO DO: get user input for month (all, january, february, ... , june)
df = df[df['month'] == month]

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
if day != 'all':
df = df[df['day_of_week'] == day.title()]
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
   print('most common start station:', start_station)

    # TO DO: display most commonly used end station
print('most common end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('start_station + end_station:;' trip[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
travel_time = Start_time + end_time
print(travel_time)

    # TO DO: display mean travel time
    print(start_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
user_types = df['user type'].value_counts()

    # TO DO: Display counts of gender
gender_types = df['gender type'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth

print(types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
