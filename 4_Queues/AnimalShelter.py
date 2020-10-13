from Animal import Animal

class AnimalShelter(object):

    def __init__(self):
        self.first_cat = None
        self.last_cat = None
        self.first_dog = None
        self.last_dog = None
        self.pet_count = 0

    def __repr__(self):
        cat_counter = 0
        dog_counter = 0
        current_cat = self.first_cat
        current_dog = self.first_dog
        while current_cat is not None:
            current_cat = current_cat.next
            cat_counter += 1
        while current_dog is not None:
            current_dog = current_dog.next
            dog_counter += 1

        return "Total cats: {}; Total dogs: {}".format(cat_counter, dog_counter)

    def enqueue(self, name, species):
        self.pet_count += 1
        new_pet = Animal(name, species)
        new_pet.tracker_counter = self.pet_count
        
        if species == 'cat':
            if self.first_cat is None:
                self.first_cat = new_pet
            if self.last_cat is not None:
                self.last_cat.next = new_pet
            self.last_cat = new_pet

        elif species == 'dog':
            if self.first_dog is None:
                self.first_dog = new_pet
            if self.last_dog is not None:
                self.last_dog.next = new_pet
            self.last_dog = new_pet

    def dequeue_cat(self):
        if self.first_cat is not None:
            placeholder_cat = self.first_cat
            self.first_cat = placeholder_cat.next
            self.pet_count -= 1
            return ("Dequeued cat: ", str(placeholder_cat.name))
        else:
            return "No cats to dequeue"

    def dequeue_dog(self):
        if self.first_dog is not None:
            placeholder_dog = self.first_dog
            self.first_dog = placeholder_dog.next
            self.pet_count -= 1
            return ("Dequeued dog: ", str(placeholder_dog.name))
        else:
            return "No dogs to dequeue"

    def dequeue_any(self):
        if self.first_cat is not None and self.first_dog is None:
            return self.dequeueCat()
        elif self.first_cat is None and self.first_dog is not None:
            return self.dequeueDog()
        else:
            if self.first_cat.tracker_counter < self.first_dog.tracker_counter:
                return self.dequeue_cat()
            else:
                return self.dequeue_dog()