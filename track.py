import phonenumbers
from phonenumbers import timezone ,geocoder, carrier

mobileNo = input("Enter Mobile number with your country code :")
mobileNo = phonenumbers.parse(mobileNo)

#get timezone 
print(timezone.time_zones_for_number(mobileNo))

#get carrier of phone number
print(carrier.name_for_number(mobileNo, "en"))

#get geocoder or region information
print(geocoder.description_for_number(mobileNo, "en"))

#validating a phone number
print("valid Mobile Number :" ,phonenumbers.is_valid_number(mobileNo))

#checking possibility of a number
print("checking possibilty of Number :" ,phonenumbers.is_possible_number(mobileNo))

