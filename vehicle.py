vehicle_type=input("Enter the vehicle type:")
hours=int(input("Enter the parking duration in hours:"))
if vehicle_type == "two-wheeler":fee=hours*20
elif vehicle_type == "four-wheeler":fee=hours*50
elif vehicle_type == "Heavy-vehicle":fee=hours*100
else:
    fee=0
    print("Invalde vehicle_type")
print("Vehicle Type:",vehicle_type)
print("Enter the parking duration in hours:",hours)
print("Total parking fee:",fee)