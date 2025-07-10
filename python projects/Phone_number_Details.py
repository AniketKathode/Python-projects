import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number= input("Enter the phone number with country code:")
phone_number = phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone_number)
car=carrier.name_for_number(phone_number, 'en')
reg=geocoder.description_for_number(phone_number, 'en')
print(time)
print(reg)
print(car)
