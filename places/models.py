import django

class Place(django.db.models.Model):
  name  = django.db.models.TextField(help_text="Name")
  state = django.db.models.ForeignKey("State", on_delete=django.db.models.SET_NULL, null=True)
  # population
    # population density
  # affordability
    # median household income
    # median housing price
    # average housing price per square foot
  # racial diversity
  # age
  # climate
    # temperature
    # snowfall
    # sunniness
    # climate risk score
  # politics
  # schools
  # crime
  # commute
  
  def __str__(self):
    """String for representing the Model object."""
    return self.name

  def get_absolute_url(self):
    """Returns the url to access a detail record for this book."""
    return django.urls.reverse('place', args=[str(self.id)])

class State(django.db.models.Model):
  """Model representing a book genre."""
  name = django.db.models.TextField(help_text='Enter a U.S. state (e.g. Science Fiction)')