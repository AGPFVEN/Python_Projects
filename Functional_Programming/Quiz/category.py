from category import Category


class Quiz:
    def __init__(self):
        category_names = [
            "animals", "brain-teasers", "celebrities", "entertainment",
            "for-kids", "general", "geography", "history", "hobbies",
            "humanities", "literature", "movies", "music", "newest",
            "people", "rated", "religion-faith",  "science-technology",
            "sports", "television", "video-games", "world"
        ]
        self.categories = { name: None for name in category_names }
        

    def get_category(self, category_name):
        # Check if is a valid category
        if not category_name in self.categories:
            print("Invalid category '" + category_name + "'.")
            exit()
        
        # Check if category has already been downloaded
        if not self.categories[category_name] is None:
            return self.categories[category_name]

        # If all valid, but not downloaded, create the category new, and download
        # the questions.
        c = Category(category_name)
        c.download()
        # Save the category into the dictionary
        self.categories[category_name] = c
        return c
