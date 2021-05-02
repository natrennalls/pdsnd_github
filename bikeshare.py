import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def input_filter(printed_input, entered_list):
    """
    Simplify the code for the user when choosing cities
    or the month's data
    Arguments:
         (str) printed_input = the questions being asked
         (str) entered_list = finds the list(cities or months)
    Returns:
         (str) choice - returns user's choice for city, month, or day
    """
    while True:
        choice = input(printed_input).title()
        if choice in entered_list:
            return choice.lower()
            break
        print('Whoops! Make sure you enter the {}.'.format(entered_list))

def select_set(data):
    """
    User chooses data set to input
    Arg:
        (str) data - choose a catergory to input (cities, months, days)
    Return:
        (str) city, month, or day - returns the users choice
    """
    cities = ['Chicago', 'New York City', 'Washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    days = {'1':'Sunday', '2':'Monday', '3':'Tuesday' , '4':'Wednesday', '5':'Thursday', '6':'Friday', '7':'Saturday'}
    while True:
        #gets user's input for cities
        if data == 'cities':
            return input_filter('Would you like to see the data for Chicago, New York City, or Washington: \n', cities)
        #gets user's input for which month
        elif data == 'months':
            return input_filter('Which month? January, February, March, Arpil, May, or June? \n', months)
        elif data == 'days':
            while True:
                day = input('Which day? Integers only please (example: 1 = Sunday): \n')
                if day in days:
                    return days[day]
                    break
                print('Whoops! Make sure to enter an integer for the day (examples: 1 = Sunday, 3 = Tuesday)')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs week (all, monday, tuesday, ... sunday)
    city = select_set('cities')
    while True:
        enter = input('Would you like to filter this data by month, day, both, or no filter at all? Type "no filter" for no time filter. \n').lower()
        if enter == 'no filter':
            month == 'all'
            day == 'all'
            break
        elif enter == 'both':
            month == select_set('months')
            day == select_set('days')
            break
        elif enter == 'month':
            month == select_set('months')
            day == 'all'
            break
        elif enter == 'day':
            month == 'all'
            day == select_set('days')
            break
        else:
            print('Whoops! Make sure to input month, day, both, or no filter.')


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
    # First, load the data into the dataframe
    df = pd.load_csv(CITYDATA[city])
    #Then, convert the Start Time to datetime w/ to_datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract month and day of the week from the new Start Time to make new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    # filter for the months
    if month != 'all':
        # use a months list to get the matching integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # now filter by month to make a new dataframe
        df = df[df['month'] == month]
    #filter for the days
    if days != 'all':
        # filter by the day of week to make a new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most popular month of rentals: {}'.format(popular_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular day for rentals: {}'.format(popular_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour for rentals: {}'.format(popular_hour))

    #Prints the total processing time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most popular starting station: {}'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most popular ending station: {}'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combo = df['combination'].mode()[0]
    print('Most popular combination of starting and ending stations: {}'.format(common_combo))
    #Prints the total processing time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(total_travel))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time: {}'.format(avg_travel_time))

    #Prints the total processing time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type\n{}: {}\n{}: {}'.format(user_type_count.index[0], user_type_count.iloc[0], user_type_count.index[1], user_type_count.iloc[1]))

    # TO DO: Display counts of gender
    cities_columns = df.columns
    if 'Gender' in cities_columns:
        gender = df['Gender'].value_counts()
        print('Male:{0}\nFemale:{1}. '.format(gender.loc['Male'], gender.loc['Female'])
    else:
        print('There\'s no gender info for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print('Earliest birth year: {}'.format(earliest))
        recent = df['Birth_Year'].max()
        print ('Most recent birth year: {}'.format(recent))
        common = df['Birth_Year'].mode()[0]
        print('Most common birth year: {}'.format(common))
    else:
        print('There\'s no birth year info for this city.')
    #Prints the total processing time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    raw_data = 0
    while True:
        answer = input('Do you want to see the raw data? Yes or No').lower()
        if answer not in ['yes', 'no']:
              answer = input('Whoops! Make sure you type Yes or No.').lower()
        elif answer == 'yes':
              raw_data += 5
              print(df.iloc[raw_data:raw_data + 5])
              again = input('Do you want to see more? Yes or No').lower()
              if again == 'no':
                  break
              elif answer == 'no':
                  return

def main():
    while True:
        city, month, day = get_filters(city,month,day)
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
