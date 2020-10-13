from Animal import Animal
from AnimalShelter import AnimalShelter

"""Animal Shelter:
--- An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
--- People must adopt either:
    --- the oldest (based on arrival time) of all animals at the shelter, OR!!!
    --- they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
-- They CANNOT select which specific animal they would like.

Create the data structures to maintain this system and implement operations such as enqueue, dequeue_any, dequeue_dog, and dequeue_cat."""

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("Astrid", "dog")
    print(shelter)
    print(shelter.pet_count)
    shelter.enqueue("Bella", "dog")
    shelter.enqueue("Chase", "dog")
    print(shelter)
    print(shelter.pet_count)
    shelter.enqueue("Daisy", "cat")
    shelter.enqueue("Ender", "cat")
    print(shelter)
    print(shelter.pet_count)
    shelter.enqueue("Fido", "dog")
    shelter.enqueue("Gigi", "dog")
    shelter.enqueue("Horace", "cat")
    print(shelter)
    print(shelter.pet_count)
    shelter.dequeue_any()
    shelter.dequeue_any()
    print(shelter)
    print(shelter.pet_count)
    shelter.dequeue_cat()
    print(shelter)
    shelter.dequeue_any()
    shelter.dequeue_dog()
    print(shelter)
