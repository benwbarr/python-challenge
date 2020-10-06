# Dependencies
import os
import csv

# Pathing for data file in the Resources folder
budget_data_csv = os.path.join("c:/", "Users", "downr", "python-challenge", "PyBank", "Resources", "budget_data.csv")
# budget_data_csv = pd.read_csv("Resources", "budget_data.csv")

profit_losses = []
revenue = []
net_total = 0
average = []
months = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)


    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
        months_total = len(months)
        net_total += int(row[1])

    for x in range(0, months_total):
        if x == 0:
            average.append(0)
        else:
            average.append(profit_losses[x] - profit_losses[x - 1])
    # average
    average_change = round(sum(average) / (len(average) - 1), 2)

    # Greatest increase month
    greatest_increase = max(average)
    Max = average.index(greatest_increase)
    max_month = months[Max]
    # Greatest decrease month
    greatest_decrease = min(average)
    Min = average.index(greatest_decrease)
    min_month = months[Min]

    print("")
    print("Financial Data Analysis")
    print("----------------------------")
    print("Total Months: {}".format(months_total))
    print("Total: $" +str(net_total))
    print("Average Change: ${:,.2f}".format(average_change))
    print("Greatest Increase in Profits: " + str(max_month + " " + "${:,.2f}".format(max(average))))
    print("Greatest Decrease in Profits: " + str(min_month + " " + "${:,.2f}".format(min(average))))
    print("")
    print("")

    # Path to export text file
    file_to_output = os.path.join("c:/", "Users", "downr", "python-challenge", "PyBank", "analysis", "New_budget_data.csv")

Print_terminal = (
    f"Financial Data Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\n")


# Print to terminal
print(Print_terminal)

# Export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(Print_terminal)
