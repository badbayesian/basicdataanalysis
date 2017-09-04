import numpy

payments=[
{

    "loan_provider" : "greatlakes",
    "payment_type" : "MONTHLY",
    "payment_amount" : 295.39,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-04-21T20:46:03.357Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-02T20:56:18.392Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-08T20:58:26.932Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-09T21:09:51.490Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-11T21:10:36.491Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-15T21:11:36.776Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-17T21:12:10.762Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 10,
    "payment_success": False,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-18T21:27:26.543Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 10,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-21T21:31:51.581Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 10,
    "payment_success": False,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-22T21:32:46.375Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 10,
    "payment_success": True,
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-22T21:34:49.579Z",
    "lastName" : "Barr",
    "firstName" : "Madeleine"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "MONTHLY",
    "payment_amount" : 295.39,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-24T21:35:37.919Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-27T12:29:23.593Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-29T17:40:23.727Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-29T16:51:19.844Z"
},
{
    "loan_provider" : "g5reatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": False,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-05-30T19:52:33.675Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-01T10:32:59.815Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": False,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-03T20:35:35.851Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-05T20:36:03.795Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-08T18:06:22.589Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 10,
    "payment_success": False,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-10T18:11:30.300Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-11T18:14:10.345Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-17T18:40:26.137Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-17T09:08:45.366Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "OTHER",
    "payment_amount" : 5,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-25T17:14:36.542Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "MONTHLY",
    "payment_amount" : 295.39,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-06-27T19:47:55.143Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "MONTHLY",
    "payment_amount" : 295.39,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-07-19T15:59:55.467Z"
},
{
    "loan_provider" : "greatlakes",
    "payment_type" : "MONTHLY",
    "payment_amount" : 295.39,
    "payment_success": True,
    "lastName" : "Barr",
    "firstName" : "Madeleine",
    "email" : "madeleine.barr13@gmail.com",
    "payment_date" : "2017-07-19T18:35:18.248Z"
}]

# Often times when dealing with data, we can run into type errors
# As in we are trying to mix and manipulate data and objects that
# have different types
# You can determine the type of data this way:


def typeOfPayments():
    return (type(payments))

# We want to calculate total payments made
# This function takes payment_amount for each item
# in every item payments

def totalPayments():
	return (sum(item['payment_amount'] for item in payments))


# We might also want to count the number of elements in a list:
def numberOfPayments():
	return (len(payments))

April = [295.39]
May = [5, 5, 5, 5, 5, 5, 10, 10, 10, 295.39, 5, 5, 5, 5]
June = [5, 5, 5, 5, 10, 5, 5, 5, 5, 295.39]
July = [295.39, 295.39]

# Gives you the average payment for April

def aprilAverage():
    return "The average payment made in April was " + "$" + str(round(numpy.mean(April), 2))
# Gives you the average payment for May
def mayAverage():
    return "The average payment made in May was " + "$" + str(round(numpy.mean(May), 2))
# Gives you the average payment for June
def juneAverage():
    return "The average payment made in June was " + "$" + str(round(numpy.mean(June), 2))
# Gives you the average payment for July
def julyAverage():
    return "The average payment made in July was " + "$" + str(round(numpy.mean(July), 2))
# Gives you the average total payment
def averagePayment():
    return "The average payment made per payment was " + "$" + str(round(sum(item['payment_amount'] for item in payments) / (len(payments)), 2))

aprilTotal = sum(April)
mayTotal = sum(May)
juneTotal = sum(June)
julyTotal = sum(July)

dictOfTotal = [aprilTotal, mayTotal, juneTotal, julyTotal]

def whichMonthHasHighestPayment():
    if max(dictOfTotal) == aprilTotal:
        return "April is the month with the highest monthly payment!"
    elif max(dictOfTotal) == mayTotal:
        return "May is the month with the highest monthly payment!"
    elif max(dictOfTotal) == juneTotal:
        return "June is the month with the highest monthly payment!"
    elif max(dictOfTotal) == julyTotal:
        return "July is the month with the highest monthly payment!"

def paymentsMadeInApril():
    if len(April) == 1:
        return "There was " + str(len(April)) + " payment made in April"
    elif len(April) > 1:
        return "There were " + str(len(April)) + " payments made in April"

def paymentsMadeInMay():
    if len(May) == 1:
        return "There was " + str(len(May)) + " payment made in May"
    elif len(May) > 1:
        return "There were " + str(len(May)) + " payments made in May"

def paymentsMadeInJune():
    if len(June) == 1:
        return "There was " + str(len(June)) + " payment made in June"
    elif len(June) > 1:
        return "There were " + str(len(June)) + " payments made in June"

def paymentsMadeInJuly():
    if len(July) == 1:
        return "There was " + str(len(July)) + " payment made in July"
    elif len(July) > 1:
        return "There were " + str(len(July)) + " payments made in July"


list_payment_types = ["MONTHLY", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "MONTHLY", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER", "MONTHLY", "MONTHLY", "MONTHLY"]
OTHER = "OTHER"
MONTHLY = "MONTHLY"

def monthyPaymentsMade():
    counterOther = 0
    for item in list_payment_types:
        if item == 'OTHER':
            counterOther += 1
    return "There were " + str(counterOther) + " other type payments made"


def otherPaymentsMade():
    counterMonthly = 0
    for item in list_payment_types:
        if item == 'MONTHLY':
            counterMonthly += 1
    return "There were " + str(counterMonthly) + " monthly type payments made"
