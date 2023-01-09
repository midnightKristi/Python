from protein_lengths import naa
'''
# FIBONACCI
lead_count = [0,0,0,0,0,0,0,0,0,0]

try:
    # Open the file.
    file = open("fib500.txt", "r")
except:
    print("can't open file")
    exit()

for line in file:
    index = int(line[0])
    lead_count[index] += 1

print("Digit  Count  Percent")

for i in range(0, len(lead_count)):
  percentage = (lead_count[i]/500)*100
  print(f"{i}        {lead_count[i]}    {round(percentage, 2)}")

print(f"Total {sum(lead_count)}  100 \n")
print("\n")
file.close()

# PROTEIN
lead_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in naa:
    index = int(line[0])
    lead_counter[index] +=1

print("Digit  Count  Percent \n")

for i in range(1, len(lead_counter)):
  percentage = (lead_counter[i] / 500) * 100
  print(f"{i}        {lead_counter[i]}    {round(percentage, 2)}")

print(f"Total {sum(lead_counter)}  100")
print("\n")
'''

# COUNTY
print("county.txt")
lead_count = [0,0,0,0,0,0,0,0,0,0]

try:
    # Open the file.
    file = open("county.txt", "r")
except:
    print("can't open file")
    exit()

for line in file:
    index = int(line[0])
    lead_count[index] += 1

print("Digit  Count  Percent")

for i in range(1, len(lead_count)):
  percentage = (lead_count[i]/500)*100
  print(f"{i}        {lead_count[i]}    {round(percentage, 2)}")

print(f"Total   {sum(lead_count)}   100.0 \n")
file.close()