import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Would you like to see data for Chicago, New York City, or Washington?")
    city = input("please enter city name: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("The name you entered is not on the list!")
        city = input("Please enter city name: ").lower()

    print("You have chosen ", city)
    # get user input for month (all, january, february, ... , june)
    print("Would you like to filter the data by month or show all?")
    month = input("Please enter month or all: ").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("This month is not on the list!")
        month = input("Please enter month or all: ").lower()

    print("You have chosen to filter by ", month)
    # get user input for day of week (all, monday, tuesday, ... sunday)

    print("Would you like to filter the data by day or show all?")
    day = input("Please enter day or all: ").lower()
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        print("The name is not on the list!")
        day = input("Please enter a day: ").lower()

    print("You chose to filter by: ", day)

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common start station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station:', common_end)

    # display most frequent combination of start station and end station trip
    print('Most common trip is from ', common_start + ' to ', common_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mode()[0]
    print('Average trip duration:', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count:', gender_count)
    except:
        print('This information is not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Year'].min()
        print('Earliest year of birth:', earliest_birth_year)
    except:
        print('This information is not available')

    try:
        most_recent_birth_year = df['Year'].max()
        print('Most recent year of birth:', most_recent_birth_year)
    except:
        print('This information is not available')

    try:
        most_common_year = df['Year'].mode()
        print('Most common year of birth:', most_common_year)
    except:
        print('This information is not available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """ Displays data at users's request."""

   #TO DO: get user's input for whether to print 5 lines of data or not.
    rows = 0
    while True:
        displayed_data = input('\nWould you like to see 5 lines of data at a time? Enter yes or no.\n')
        if displayed_data.lower() !='yes':
            break
        rows += 5
        print(df.iloc[rows:rows+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
