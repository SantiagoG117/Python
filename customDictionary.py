""" 
    Tag Cloud Custom Container:
    Keeps track of the number of various tags in a Blog.
    How many posts do we have that are tagged with Python, JavaScript, etc.

    It should support:
        The number of items in the container
        Get an item by its key cloud["python"]
        Iterate over the container:
            for tag in cloud:
                print(tag)

 """


class TagCloud:
    # Constructor
    def __init__(self):
        self.tags = {}  # Empty dictionary allows us to quicly get the number of givent tags. Key: tag, Value: count

    # Add a tag to the cloud
    def add(self, tag_name):
        # Update the count of the tag in the tags dictionary
        self.tags[tag_name.lower()] = self.tags.get(  # Get the value of the tag (item) with the specified tag name (key)
            tag_name.lower(),  # Key
            # If the tag is not in the dictionary, add it with a value of 0 and increment it by 1. If it is in the dictionary, increment it by 1.
            0) + 1

    # Set the number of tags under a given tag

    def __setitem__(self, tag_name, count):
        self.tags[tag_name.lower()] = count

    # Get the number of tags under a given tag
    def __getitem__(self, tag_name):
        return self.tags.get(tag_name.lower(), 0)

    # Get the the total number of tags in the cloud
    def __len__(self):
        count = 0

        for value in self.tags.values():
            count += value

        return count

    # Return an iterator object with all the tags in the cloud
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Joe Momma")


print(len(cloud))
