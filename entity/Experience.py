class Experience:

    def __init__(self, domain, years, projects):
        self.domain = domain
        self.years = years
        self.projects = projects

    def serialize(self):
        return {
            "domain": self.domain,
            "years": self.years,
            "projects": [prj.serialize() for prj in self.projects]
        }
