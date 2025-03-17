git config pull.rebase false
import csv
with open('security_incidents.csv', 'r', newline='') as file:
    reader= csv.reader(file)
    incidents_list = list(reader)
new_column_name = 'Status'
default_value = 'Pending'
incidents_list[0].append("Status")
print(incidents_list)
Status = ["yes", "yes", "yes", "yes", "yes"]
for i in range(1,len(incidents_list)):
    if i-1 < len(Status):
        incidents_list[i].append(Status[i-1])
    else:
        incidents_list[i].append("unknown")
with open('security_incidents_modified.csv', 'w', newline ='') as file:
    writer = csv.writer(file)
    writer.writerows(incidents_list)