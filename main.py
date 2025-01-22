# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    """Display a welcome message for the donut shop."""
    print("🍩 Welcome to North Loop Provisions! 🍩")
    print("Crafting artisanal donuts in Minneapolis's North Loop")
    print("-------------------------------------------")

def show_menu():
    """Display our current donut menu."""
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "MN Berry": 4.25,
        "Local Honey": 4.00
    }
    
    print("\nToday's Donut Menu:")
    print("------------------")
    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")

        """'2f' = 2 decimal places for clear cost reading"""

# Main program
if __name__ == "__main__":
    welcome_message()
    show_menu()
    print("\nReady to serve our community with the finest donuts!")

    #Our complete menu organized by category
    #dictionary with key-value pairs where the value is a list
    donut_menu = {
        'Small Batch': [
            'Wild Rice & Honey',
            'Maple Bacon',
            'Swedish Cardamom'
        ],
        'Seasonal': [
            'Apple Cider',
            'Juicy Lucy',
            'Lake of the Woods'
        ],
        'Local Collabs': [
            'Spyhouse Coffee Cake',
            'Fulton Beer & Pretzel',
            'Sweet Science Ice Cream'
        ]}
        
        # Locally-sourced toppings
    toppings = [
        'House-Made Sprinkles',
        'Candied Hazelnuts',
        'Bee Pollen',
        'Cookie Butter Drizzle'
        ]
    
    # Track our morning sales
    morning_sales = []

    # Record our first sale (by appending a transaction to the sales dictionary)
    morning_sales.append({
        'item': 'Wild Rice & Honey',
        'quantity': 2,
        'toppings': ['Bee Pollen'],
        'time': '7:30 AM'
    })

    # Display our current menu - using a for loop
    print("Today's Morning Menu:")
    for category, items in donut_menu.items():
        print(category + ":")
        for item in items:
            print(" - " + item)