
class Job:
    """User object with all properties of a user in the system"""
    id = None
    title = None
    description = None
    salary = None
    location = None
    company = None
    category = None
    created_at = None
    updated_at = None

    def __str__(self):
        """String representation of the JOb object with all properties"""
        return ("Job(id =%s, title =%s, description =%s, salary =%s, location =%s, company =%s, category =%s, created_at=%s, updated_at=%s)" %
                (self.id, self.title, self.description, self.salary, self.location, self.company, self.category, self.created_at, self.updated_at))