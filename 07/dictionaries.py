# Dictionaries - used to store data values that are in ket value pairs - JS Objects
band = {
	"vocals":"Plant",
	"guitar":"Page"
}

band2 = dict(vocals="Plant", guitar="Page")

# print(band)
# print(band2)
# print(type(band))
# print(len(band))

# access items in a dict

# print(band["vocals"])
# print(band.get("guitar"))

# list all keys
# print(band.keys())
# print(band.values())
# list of key/value pairs as tuples
# print(band.items())
# verify a key exists
# print("guitar" in band)
# print("triangle" in band)
# change values

band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

# remove itesm
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
# print(band)
# print(band.popitem()) #tuple
# print(band)

# detele and clear
band["drums"] = "Bonham"
del band["drums"]
# print(band)

band2.clear()
# print(band2)

del band2

# Copy dict - very careful with copying the reference to the dic and not the actual dic
band2 = band.copy()
band2["drums"] = "Dave"
print("good copy!")
print(band)
print(band2)

# or use the dict() constructor copy
band3 = dict(band)
print("Good Copy")
print(band3)

# nested dict
member1 = {
	"name": "Plant",
	"instrument": "vocals"
}
member2 = {
	"name": "Page",
	"instrument": "guitar"
}
band = {
	"member1": member1,
	"member2": member2
}
print(band)
print(band["member1"]["name"])

# sets

nums = { 1, 2 , 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))


