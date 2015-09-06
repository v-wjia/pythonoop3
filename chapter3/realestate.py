__author__ = 'v-wjia'


class Property:
    def __init__(self, square_feet='', beds='', bath='', **kwargs):
        self.square_feet = square_feet
        self.beds = beds
        self.bath = bath

    def display(self):
        print("Property Details")
        print("================")
        print("Square footage: {}".format(self.square_feet))
        print("Bedrooms: {}".format(self.beds))
        print("Bathrooms: {}".format(self.bath))
        print()

    def prompt_init():
        return dict(square_foot=input("Enter the square feet:"),
                    beds=input("Enter the number of bedrooms:"),
                    bath=input("Enter the number of bathrooms:")
                    )

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    input_string += " ({}) ". format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    valid_laundries = ("coins", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment Details")
        print("Laundry: %s" % self.laundry)
        print("has Balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have?", Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?", Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("House Details")
        print("number of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?", House.valid_fenced)
        garage = get_valid_input("Is there a garage?", House.valid_garage)
        num_stories = input("How many stories?")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("Purchase Details")
        print("Selling price: {} ".format(self.price))
        print("Estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price=input("What is the selling price?"),
            taxes=input("What are the estimated taxes?"),
        )

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("Rental Details")
        print("Rent: {}".format(self.rent))
        print("Estimated utilities: {}".format(self.utilities))
        print("Furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent?"),
            utilities=input("What are the estimate utilities?"),
            furnished=get_valid_input("Is the property furnished?", ("yes", "no"))
        )

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)
