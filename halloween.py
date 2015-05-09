# I can't be bothered to think of a Hallowe'en costume so
# can you help me generate one randomly?


nouns = []
adjectives = []

with open('things.txt') as f:
    # We don't want those stinky \n newline characters
    # so we call strip() before adding it to our nouns list.
    for line in f:
        nouns.append(line.strip())

with open('descriptors.txt') as f:
    for line in f:
        adjectives.append(line.strip())


def generate_costume():
    import random
    # pick something random from the nouns and adjectives list

    noun = random.choice(nouns)
    adj = random.choice(adjectives)

    return (noun, adj)


while True:
    (noun, adj) = generate_costume()

    print "You go dressed as a {} {} to the party.".format(adj, noun)

    happy = raw_input("Are you happy with this choice? ")

    # Check if the user typed something like 'yes' or 'y' and
    # quit the program if they are happy.

    if happy == 'y' or happy == 'yes':
        exit()
    else:
        print "OK, I will choose another costume. Hold on..."
