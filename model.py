from google.appengine.ext import db
#import properties



class ActivityProfile(db.Model): 
		#key_name - app_username
		client = db.StringProperty(default="twitter")
		platform = db.StringProperty(default="twitter")
		name = db.StringProperty(required=False)
		profile_image_url = db.StringProperty(required=False)
		username = db.StringProperty(required=False)
		update_count = db.IntegerProperty(default=0)
		date = db.DateTimeProperty(auto_now_add=True)
		modified = db.DateTimeProperty(auto_now=True)


class StatusUpdate(db.Model):
	#key_name - user.key().name()_update-id
	user = db.ReferenceProperty(ActivityProfile)
	platform = db.StringProperty(default="twitter") 
	id = db.StringProperty() # platform id
	location_service = db.StringProperty(required=False)
	location_id = db.StringProperty(required=False)
	venue_name = db.StringProperty(required=False)
	lat = db.FloatProperty(required=False)
	lon = db.FloatProperty(required=False)
	date = db.DateTimeProperty() # from update
	text = db.StringProperty() # update text
	
	saved = db.DateTimeProperty(auto_now_add=True)

	
	
	
def getUserKeyName(client, username):
	return client + "_" + username

def getStatusKeyName(client, username, update_id):
	return client + "_" + username	+ "_" + update_id