class User(AbstractUser):
	role = 0 or 1


class Profile(models.Model):
	user = models.OneToOneField(User)
	name = CharField 
	roll = CharField
	avatar = ImageField
	approved = Boolean

	votes = IntegerField
	has_voted = Boolean
	post = CharField