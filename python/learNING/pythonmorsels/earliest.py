# Python Morsels - week 1
# https://www.pythonmorsels.com/exercises/01435c5112a04587ae52d8529ba8b2eb/


def get_earliest(*dates):

    """find earliest date from list of dates"""

    res = dates[0].split('/')

    for date in dates:
        date_split = date.split('/')
        for i in [2, 0, 1]:
            if res[i] < date_split[i]:
                break
            if res[i] == date_split[i]:
                continue
            if res[i] > date_split[i]:
                res = date_split

    return str.join('/', res)


# print(get_earliest("12/30/2007", "11/20/2010"))
# print(get_earliest("12/30/2010", "11/20/2010"))
# print(get_earliest("12/30/2010", "11/20/2010", "10/20/2011"))
# print(get_earliest("12/30/2006", "11/20/2010", "10/20/2011"))

