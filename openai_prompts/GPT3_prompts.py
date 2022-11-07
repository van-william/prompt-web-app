
# Sandwich Prompt
def sandwich_prompt(sandwich_toppings):
    return """Suggest three names for a custom sandwich order.

Sandwich Toppings: Genoa Salami, Capocollo,Provolone, Hot Peppers, onion, lettuce, tomato & easy mayo
Sandwich Name: Spicy East Coast Italian
Sandwich Toppings: Turkey, Provolone, Avocado, cucumber, lettuce, tomato & mayo
Sandwich Name: Beach Club
Sandwich Toppings: a biscuit, a piece of fried chicken, and some sausage gravy
Sandwich Name: The East Nasty
Sandwich Toppings: {}
Sandwich Name:""".format(
        sandwich_toppings.capitalize()
    )


def book_prompt(book_topics):
    return """Suggest Three Books to Read based upon topics.

Topics: Business, Economics, Strategy, Management Consulting
Books: Good to Great by Jim Collins, Fit for Growth by Deniz Caglar, Strategy that Works by Cesare Mainardi
Topics: Science Fiction, Space, Fantasy
Books: Out of the Silent Planet by C.S. Lewis, The Hitchhiker's Guide to the Galaxy by Douglas Adams, Dune by Frank Herbert
Topics: Christian, Bible, Theology
Books: Every Good Endeavor by Timothy Keller, Mere Christianity by C.S. Lewis, The Purpose Driven Life by Rick Warren
Topics: {}
Books:""".format(
        book_topics.capitalize()
    )