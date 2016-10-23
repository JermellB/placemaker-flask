import mongoengine
from datetime import datetime


class Coc(mongoengine.DynamicDocument):
	coc_id = mongoengine.UUIDField(primary_key=True)


class Organization(mongoengine.DynamicDocument):
	pass


class Form(mongoengine.DynamicDocument):
	pass


class Question(mongoengine.DynamicDocument):
	pass


class NameInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store name information
	"""
	first_name = mongoengine.StringField()
	middle_name = mongoengine.StringField()
	last_name = mongoengine.StringField()
	suffix = mongoengine.StringField()
	name_tuples = ("Full name reported",
				   "Partial, street name, or code name reported",
				   "Client doesn\'t know",
				   "Client refused",
				   "Data not collected")
	name_type = mongoengine.StringField(choices=name_tuples)


class SSNInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store social security number information
	"""
	ssn = mongoengine.StringField()
	ssn_tuples = ("Full SSN reported",
				  "Approximate or partial SSN reported",
				  "Client doesn\'t know",
				  "Client refused",
				  "Data not collected")
	ssn_type = mongoengine.StringField(choices=ssn_tuples)


class DOBInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store date of birth information
	"""
	dob = mongoengine.DateTimeField()
	dob_type_tuples = ("Full DOB reported",
					   "Approximate or partial DOB reported",
					   "Client doesn\'t know",
					   "Client refused",
					   "Data not collected")
	dob_type = mongoengine.StringField(choices=dob_type_tuples)


class GenderInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store gender information
	"""
	gender_tuples = ("Female",
					 "Male",
					 "Transgender male to female",
					 "Transgender female to male",
					 "Doesn\'t identify as male, female or transgender",
					 "Client doesn\'t know",
					 "Client refused",
					 "Data not collected")
	gender = mongoengine.StringField(choices=gender_tuples)
	# gender_specify field is used for further specification only if gender field is set to "Other - please specify"


class DisablingConditionInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store disabling condition information
	"""
	disabling_condition_tuples = ("No",
								  "Yes",
								  "Client doesn\'t know",
								  "Client refused",
								  "Data not collected")
	disabling_condition = mongoengine.StringField(choices=disabling_condition_tuples)
	disability_condition_specify = mongoengine.StringField()


class LivingSituationInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store living situation information
	Captures 3 possible subtypes of living situations: literally homeless, institutional situations, and transitional/permanent situations

	For people under the "Literally Homeless" residence type, typical HMIS Project Types include: Street Outreach, Emergency Shelter, & Safe Haven
	fields of information collected cover the following categories:
	- the type of living arrangement (3 categories)
		- subtype specific to each living arrangement
	- length of time spent at current residence
		- definition of this field changes from subtype to subtype, this is a catch-all field for all the different values for residence_type
	- prior residence if current residence is either institutional or transitional
		- if current
	- approximate date they became homeless
	- number of instances they have been homeless
	- total number of months they have been homeless
	"""
	residence_type_tuples = ("Literally Homeless",
							 "Institutional Situation",
							 "Transitional & Permanent Housing Situation",
							 "Data not collected")
	residence_type = mongoengine.StringField(choices=residence_type_tuples)

	residence_subtype_tuples = ("Place not meant for habitation (e.g. a vehicle, an abandoned building, bus/train/subway station/airport or anywhere outside)",
								"Emergency shelter, including hotel or motel paid for with emergency",
								"Safe Haven",
								"Interim Housing",
								"Foster care home or foster care group home",
								"Hospital or other residential non-psychiatric medical facility",
								"Jail, prison or juvenile detention facility",
								"Long-term care facility or nursing home",
								"Psychiatric hospital or other psychiatric facility",
								"Substance abuse treatment facility or detox center",
								"Hotel or motel paid for without emergency shelter voucher",
						 		"Owned by client, no ongoing housing subsidy",
						 		"Owned by client, with ongoing housing subsidy",
						 		"Permanent housing for formerly homeless persons (such as: a CoC project; HUD legacy programs; or HOPWA PH)",
							 	"Rental by client, no ongoing housing subsidy",
							 	"Rental by client, with VASH subsidy",
							 	"Rental by client, with GPD TIP subsidy",
							 	"Rental by client, with other ongoing housing subsidy",
							 	"Residential project or halfway house with no homeless criteria",
							 	"Staying or living in a family member\'s room, apartment or house",
							 	"Staying or living in a friend\'s room, apartment or house",
							 	"Transitional housing for homeless persons (including homeless youth)",
							 	"Client doesn\'t know",
							 	"Client refused",
								"Data not collected")
	residence_subtype = mongoengine.StringField(choices=residence_subtype_tuples)


	current_length_of_stay_tuples = ("One night or less",
									 "Two to six nights",
									 "One week or more, but less than one month",
									 "One month or more, but less than 90 days",
									 "90 days or more, but less than one year",
									 "One year or longer",
									 "Client doesn\'t know",
									 "Client refused",
									 "Data not collected")
	current_length_of_stay = mongoengine.StringField(choices=current_length_of_stay_tuples)
	current_approx_start_date = mongoengine.DateTimeField()
	total_count_tuples = ("One Time",
						  "Two times",
						  "Three times",
						  "Four or more times",
						  "Client doesn\'t know",
						  "Client refused",
						  "Data not collected")
	total_count = mongoengine.StringField(choices=total_count_tuples)
	total_months = mongoengine.IntField()
	prior_residence_type = mongoengine.StringField(choices=residence_type_tuples)
	prior_residence_subtype = mongoengine.StringField(choices=residence_subtype_tuples)
	prior_approx_start_date = mongoengine.DateTimeField()

class DestinationInfo(mongoengine.DynamicEmbeddedDocument):
	"""
	Embedded Document under Person used to store destination information
	"""
	destination_tuples = ("Deceased",
						  "Emergency shelter, including hotel or motel paid for with emergency shelter voucher",
						  "Foster care home or foster care group home",
						  "Hospital or other residential non-psychiatric medical facility",
						  "Hotel or motel paid for without emergency shelter voucher",
						  "Jail, prison or juvenile detention facility",
						  "Long-term care facility or nursing home",
						  "Moved from one HOPWA funded project to HOPWA PH",
						  "Moved from one HOPWA funded project to HOPWA TH",
						  "Owned by client, no ongoing housing subsidy",
						  "Owned by client, with ongoing housing subsidy",
						  "Permanent housing for formerly homeless persons (such as: CoC project; or HUD",
						  "legacy programs; or HOPWA PH)",
						  "Place not meant for habitation (e.g., a vehicle, an abandoned building,",
						  "bus/train/subway station/airport or anywhere outside)",
						  "Psychiatric hospital or other psychiatric facility",
						  "Rental by client, no ongoing housing subsidy",
						  "Rental by client, with VASH housing subsidy",
						  "Rental by client, with GPD TIP housing subsidy",
						  "Rental by client, with other ongoing housing subsidy",
						  "Residential project or halfway house with no homeless criteria",
						  "Safe Haven",
						  "Staying or living with family, permanent tenure",
						  "Staying or living with family, temporary tenure (e.g., room, apartment or house)",
						  "Staying or living with friends, permanent tenure",
						  "Staying or living with friends, temporary tenure (e.g., room apartment or house)",
						  "Substance abuse treatment facility or detox center",
						  "Transitional housing for homeless persons (including homeless youth)",
						  "Other - please specify",
						  "No exit interview completed",
						  "Client doesn\'t know",
						  "Client refused")
	destination = mongoengine.StringField(choices=destination_tuples)
	# destination_specify field is used for further specification only if gender field is set to "Other - please specify"
	destination_specify = mongoengine.StringField()

class Person(mongoengine.DynamicDocument):
	"""
	The Person class is built to HMIS Data Standards:
	https://www.hudexchange.info/resources/documents/HMIS-Data-Standards-Manual.pdf
	All Universal Data Elements (UDEs) for registering homeless persons are expressed here.
	"""

	# Name - HIMS UDE Standard (3.1)
	name_info = mongoengine.EmbeddedDocumentField(NameInfo)

	# Social Security Number - HIMS UDE standard (3.2)
	ssn_info = mongoengine.EmbeddedDocumentField(SSNInfo)

	# Date of Birth - HIMS UDE standard (3.3)
	dob_info = mongoengine.EmbeddedDocumentField(DOBInfo)

	# Race - HIMS UDE Standard (3.4)
	race_tuples = ("American Indian or Alaska Native",
				   "Asian",
				   "Black or African American",
				   "Native Hawaiian or Other Pacific Islander",
				   "White",
				   "Client doesn\'t know",
				   "Client refused",
				   "Data not collected")
	race = mongoengine.StringField(choices=race_tuples)

	# Ethnicity - HIMS UDE Standard (3.5)
	ethnicity_tuples = ("Non-Hispanic/Non-Latino",
						"Hispanic/Latino",
						"Client doesn\'t know",
						"Client refused",
						"Data not collected")
	ethnicity = mongoengine.StringField(choices=ethnicity_tuples)

	# Gender - HIMS UDE Standard (3.6)
	gender_info = mongoengine.EmbeddedDocumentField(GenderInfo)

	# Veteran Status - HIMS UDE Standard (3.7)
	veteran_status_tuples = ("No",
							 "Yes",
							 "Client doesn\'t know",
							 "Client refused",
							 "Data not collected")
	veteran = mongoengine.StringField(choices=veteran_status_tuples)

	# Disabling Condition - HIMS UDE Standard (3.7)
	disabling_condition_info = mongoengine.EmbeddedDocumentField(DisablingConditionInfo)

	# Living Situation - HIMS UDE Standard (3.917A)
	living_situation_info = mongoengine.EmbeddedDocumentField(LivingSituationInfo)

	# Project Entry Date - HIMS UDE Standard (3.10)
	project_entry_date = mongoengine.DateTimeField(default=datetime.now())

	# Project Exit Date - HIMS UDE Standard (3.11)
	project_exit_date = mongoengine.DateTimeField()

	# Destination - HIMS UDE Standard (3.12)
	destination_info = mongoengine.EmbeddedDocumentField(DestinationInfo)

	# Personal ID - HIMS UDE Standard (3.13)
	personal_id = mongoengine.UUIDField()
	legacy_id = mongoengine.IntField()


	# Household ID - HIMS UDE Standard (3.14)
	# Household isn't expressed in the Person schema, rather, Households are their own collection of embedded persons

	# relationship between person and the head of their household
	household_head_relationship_tuples = ("Self (head of household)",
										  "Head of household\'s child",
										  "Head of household\'s spouse or partner",
										  "Head of household\'s other relation member (other relation to head of household)",
										  "Other: non-relation member")
	household_head_relationship = mongoengine.StringField(choices=household_head_relationship_tuples)

	# Client Location
	coc_id = mongoengine.ReferenceField(Coc)


# class Household(mongoengine.DynamicEmbeddedDocument):
# 	"""
# 	The Household class is built to fulfill the Household IDs HIMS UDE Standard (3.14)
# 	This schema is used by a separate Households collection that has documents with embedded document lists containing all the persons in a household
# 	"""
# 	household_id = mongoengine.UUIDField()
# 	members = mongoengine.ListField(Person)
# 	coc = mongoengine.ReferenceField(Coc)


# class Household(mongoengine.DynamicEmbeddedDocument):
# 	"""
# 	The Household class is built to fulfill the Household IDs HIMS UDE Standard (3.14)
# 	This schema is used by a separate Households collection that has documents with embedded document lists containing all the persons in a household
# 	"""
# 	household_id = mongoengine.UUIDField(primary_key=True)
# 	members = mongoengine.EmbeddedDocumentListField(Person)



class User(mongoengine.DynamicDocument):
	pass