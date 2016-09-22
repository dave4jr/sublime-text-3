#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	members/models.py
#*=========================== #
from django.db import models
from tinymce.models import HTMLField
import datetime

#	Choices
# ========================= #
STATE_CHOICES = (("Alabama", "Alabama"), ("Alaska", "Alaska"), ("Arizona", "Arizona"), ("Arkansas", "Arkansas"), ("California", "California"), ("Colorado", "Colorado"), ("Connecticut", "Connecticut"), ("Delaware", "Delaware"), ("Florida", "Florida"), ("Georgia", "Georgia"), ("Hawaii", "Hawaii"), ("Idaho", "Idaho"), ("Illinois", "Illinois"), ("Indiana", "Indiana"), ("Iowa", "Iowa"), ("Kansas", "Kansas"), ("Kentucky", "Kentucky"), ("Louisiana", "Louisiana"), ("Maine", "Maine"), ("Maryland", "Maryland"), ("Massachusetts", "Massachusetts"), ("Michigan", "Michigan"), ("Minnesota", "Minnesota"), ("Mississippi", "Mississippi"), ("Missouri", "Missouri"), ("Montana", "Montana"), ("Nebraska", "Nebraska"), ("Nevada", "Nevada"), ("New Hampshire", "New Hampshire"), ("New Jersey", "New Jersey"), ("New Mexico", "New Mexico"), ("New York", "New York"), ("North Carolina", "North Carolina"), ("North Dakota", "North Dakota"), ("Ohio", "Ohio"), ("Oklahoma", "Oklahoma"), ("Oregon", "Oregon"), ("Pennsylvania", "Pennsylvania"), ("Rhode Island", "Rhode Island"), ("South Carolina", "South Carolina"), ("South Dakota", "South Dakota"), ("Tennessee", "Tennessee"), ("Texas", "Texas"), ("Utah", "Utah"), ("Vermont", "Vermont"), ("Virginia", "Virginia"), ("Washington", "Washington"), ("West Virginia", "West Virginia"), ("Wisconsin", "Wisconsin"), ("Wyoming", "Wyoming"), )
COUNTRY_CHOICES = (("US", "United States"), ("BD", "Bangladesh"), ("BE", "Belgium"), ("BF", "Burkina Faso"), ("BG", "Bulgaria"), ("BA", "Bosnia and Herzegovina"), ("BB", "Barbados"), ("WF", "Wallis and Futuna"), ("BL", "Saint Bartelemey"), ("BM", "Bermuda"), ("BN", "Brunei Darussalam"), ("BO", "Bolivia"), ("BH", "Bahrain"), ("BI", "Burundi"), ("BJ", "Benin"), ("BT", "Bhutan"), ("JM", "Jamaica"), ("BV", "Bouvet Island"), ("BW", "Botswana"), ("WS", "Samoa"), ("BR", "Brazil"), ("BS", "Bahamas"), ("JE", "Jersey"), ("BY", "Belarus"), ("O1", "Other Country"), ("LV", "Latvia"), ("RW", "Rwanda"), ("RS", "Serbia"), ("TL", "Timor-Leste"), ("RE", "Reunion"), ("LU", "Luxembourg"), ("TJ", "Tajikistan"), ("RO", "Romania"), ("PG", "Papua New Guinea"), ("GW", "Guinea-Bissau"), ("GU", "Guam"), ("GT", "Guatemala"), ("GS", "South Georgia and the South Sandwich Islands"), ("GR", "Greece"), ("GQ", "Equatorial Guinea"), ("GP", "Guadeloupe"), ("JP", "Japan"), ("GY", "Guyana"), ("GG", "Guernsey"), ("GF", "French Guiana"), ("GE", "Georgia"), ("GD", "Grenada"), ("GB", "United Kingdom"), ("GA", "Gabon"), ("SV", "El Salvador"), ("GN", "Guinea"), ("GM", "Gambia"), ("GL", "Greenland"), ("GI", "Gibraltar"), ("GH", "Ghana"), ("OM", "Oman"), ("TN", "Tunisia"), ("JO", "Jordan"), ("HR", "Croatia"), ("HT", "Haiti"), ("HU", "Hungary"), ("HK", "Hong Kong"), ("HN", "Honduras"), ("HM", "Heard Island and McDonald Islands"), ("VE", "Venezuela"), ("PR", "Puerto Rico"), ("PS", "Palestinian Territory"), ("PW", "Palau"), ("PT", "Portugal"), ("SJ", "Svalbard and Jan Mayen"), ("PY", "Paraguay"), ("IQ", "Iraq"), ("PA", "Panama"), ("PF", "French Polynesia"), ("BZ", "Belize"), ("PE", "Peru"), ("PK", "Pakistan"), ("PH", "Philippines"), ("PN", "Pitcairn"), ("TM", "Turkmenistan"), ("PL", "Poland"), ("PM", "Saint Pierre and Miquelon"), ("ZM", "Zambia"), ("EH", "Western Sahara"), ("RU", "Russian Federation"), ("EE", "Estonia"), ("EG", "Egypt"), ("TK", "Tokelau"), ("ZA", "South Africa"), ("EC", "Ecuador"), ("IT", "Italy"), ("VN", "Vietnam"), ("SB", "Solomon Islands"), ("EU", "Europe"), ("ET", "Ethiopia"), ("SO", "Somalia"), ("ZW", "Zimbabwe"), ("SA", "Saudi Arabia"), ("ES", "Spain"), ("ER", "Eritrea"), ("ME", "Montenegro"), ("MD", "Moldova, Republic of"), ("MG", "Madagascar"), ("MF", "Saint Martin"), ("MA", "Morocco"), ("MC", "Monaco"), ("UZ", "Uzbekistan"), ("MM", "Myanmar"), ("ML", "Mali"), ("MO", "Macao"), ("MN", "Mongolia"), ("MH", "Marshall Islands"), ("MK", "Macedonia"), ("MU", "Mauritius"), ("MT", "Malta"), ("MW", "Malawi"), ("MV", "Maldives"), ("MQ", "Martinique"), ("MP", "Northern Mariana Islands"), ("MS", "Montserrat"), ("MR", "Mauritania"), ("IM", "Isle of Man"), ("UG", "Uganda"), ("TZ", "Tanzania, United Republic of"), ("MY", "Malaysia"), ("MX", "Mexico"), ("IL", "Israel"), ("FR", "France"), ("IO", "British Indian Ocean Territory"), ("FX", "France, Metropolitan"), ("SH", "Saint Helena"), ("FI", "Finland"), ("FJ", "Fiji"), ("FK", "Falkland Islands (Malvinas)"), ("FM", "Micronesia, Federated States of"), ("FO", "Faroe Islands"), ("NI", "Nicaragua"), ("NL", "Netherlands"), ("NO", "Norway"), ("NA", "Namibia"), ("VU", "Vanuatu"), ("NC", "New Caledonia"), ("NE", "Niger"), ("NF", "Norfolk Island"), ("NG", "Nigeria"), ("NZ", "New Zealand"), ("NP", "Nepal"), ("NR", "Nauru"), ("NU", "Niue"), ("CK", "Cook Islands"), ("CI", "Cote d'Ivoire"), ("CH", "Switzerland"), ("CO", "Colombia"), ("CN", "China"), ("CM", "Cameroon"), ("CL", "Chile"), ("CC", "Cocos (Keeling) Islands"), ("CA", "Canada"), ("CG", "Congo"), ("CF", "Central African Republic"), ("CD", "Congo, The Democratic Republic of the"), ("CZ", "Czech Republic"), ("CY", "Cyprus"), ("CX", "Christmas Island"), ("CR", "Costa Rica"), ("CV", "Cape Verde"), ("CU", "Cuba"), ("SZ", "Swaziland"), ("SY", "Syrian Arab Republic"), ("KG", "Kyrgyzstan"), ("KE", "Kenya"), ("SR", "Suriname"), ("KI", "Kiribati"), ("KH", "Cambodia"), ("KN", "Saint Kitts and Nevis"), ("KM", "Comoros"), ("ST", "Sao Tome and Principe"), ("SK", "Slovakia"), ("KR", "Korea, Republic of"), ("SI", "Slovenia"), ("KP", "Korea, Democratic People's Republic of"), ("KW", "Kuwait"), ("SN", "Senegal"), ("SM", "San Marino"), ("SL", "Sierra Leone"), ("SC", "Seychelles"), ("KZ", "Kazakhstan"), ("KY", "Cayman Islands"), ("SG", "Singapore"), ("SE", "Sweden"), ("SD", "Sudan"), ("DO", "Dominican Republic"), ("DM", "Dominica"), ("DJ", "Djibouti"), ("DK", "Denmark"), ("VG", "Virgin Islands, British"), ("DE", "Germany"), ("YE", "Yemen"), ("DZ", "Algeria"), ("UY", "Uruguay"), ("YT", "Mayotte"), ("UM", "United States Minor Outlying Islands"), ("LB", "Lebanon"), ("LC", "Saint Lucia"), ("LA", "Lao People's Democratic Republic"), ("TV", "Tuvalu"), ("TW", "Taiwan"), ("TT", "Trinidad and Tobago"), ("TR", "Turkey"), ("LK", "Sri Lanka"), ("LI", "Liechtenstein"), ("A1", "Anonymous Proxy"), ("TO", "Tonga"), ("LT", "Lithuania"), ("A2", "Satellite Provider"), ("LR", "Liberia"), ("LS", "Lesotho"), ("TH", "Thailand"), ("TF", "French Southern Territories"), ("TG", "Togo"), ("TD", "Chad"), ("TC", "Turks and Caicos Islands"), ("LY", "Libyan Arab Jamahiriya"), ("VA", "Holy See (Vatican City State)"), ("VC", "Saint Vincent and the Grenadines"), ("AE", "United Arab Emirates"), ("AD", "Andorra"), ("AG", "Antigua and Barbuda"), ("AF", "Afghanistan"), ("AI", "Anguilla"), ("VI", "Virgin Islands, U.S."), ("IS", "Iceland"), ("IR", "Iran, Islamic Republic of"), ("AM", "Armenia"), ("AL", "Albania"), ("AO", "Angola"), ("AN", "Netherlands Antilles"), ("AQ", "Antarctica"), ("AP", "Asia/Pacific Region"), ("AS", "American Samoa"), ("AR", "Argentina"), ("AU", "Australia"), ("AT", "Austria"), ("AW", "Aruba"), ("IN", "India"), ("AX", "Aland Islands"), ("AZ", "Azerbaijan"), ("IE", "Ireland"), ("ID", "Indonesia"), ("UA", "Ukraine"), ("QA", "Qatar"), ("MZ", "Mozambique"))
ENDORSEMENT_CHOICES = ((1, "Yes"), (0, "No"))
TSHIRT_SIZE_CHOICES = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'))



class ReferralSource(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name = "Referral Source"
	def __unicode__(self):
		return self.name


class Level(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	class Meta:
		verbose_name = "Level"
	def __unicode__(self):
		return self.name


class Certification(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name = "Certification"
	def __unicode__(self):
		return self.name


class Expertise(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name = "Expertise"
	def __unicode__(self):
		return self.name


class Member(models.Model):
	first_name = models.CharField(max_length=40, blank=True, null=True)
	last_name = models.CharField(max_length=40, blank=True, null=True)
	member_id = models.CharField(max_length=10, null=True)
	level = models.ForeignKey(Level, null=True, blank=True)
	dob = models.DateField(blank=True, null=True)
	street = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=20, null=True, choices=STATE_CHOICES, default="Oregon")
	zipcode = models.CharField(max_length=5, blank=True, null=True)
	phone_cell = models.CharField(max_length=14,null=True, blank=True)
	phone_home = models.CharField(max_length=14,null=True, blank=True)
	email = models.EmailField(max_length=254, blank=True, null=True)
	emergency_contact_name = models.CharField(verbose_name="Emergency Contact", max_length=40, blank=True, null=True)
	emergency_contact_number = models.CharField(max_length=14,null=True, blank=True)
	emergency_contact_relation = models.CharField(max_length=100,null=True, blank=True)
	referral_source = models.ForeignKey(ReferralSource, null=True, blank=True)
	expertise = models.ManyToManyField(Expertise, blank=True)
	membership_start_date = models.DateField(blank=True, null=True, default=datetime.datetime.today)
	photo = models.ImageField(upload_to='members/', blank=True, null=True)
	certifications = models.ManyToManyField(Certification, blank=True)
	notes = models.TextField(null=True, blank=True)

	def address(self):
		return "%s %s, %s %s" % (self.street, self.city, self.state, self.zipcode )
	address = property(address)

	def name_first_last(self):
		return "%s %s" % (self.first_name, self.last_name)
	name_first_last = property(name_first_last)

	def name_last_first(self):
		return "%s, %s" % (self.last_name, self.first_name)
	name_last_first = property(name_last_first)
	
	def __unicode__(self):
		return self.name_last_first
