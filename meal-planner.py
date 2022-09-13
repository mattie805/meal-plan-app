'''
Meal Plan App MVP
v0.1
By Helen Lindsey
The purpose of this app is to plan vegan meals, create a grocery list, and direct users to online recipes. I created this app during a Applause Interactive,
Digital Skills for Life Skillshare course. I expanded the project a bit to include recipes and enhance user experience. All of these recipes came from
nutritionfacts.org, which is a site created by Dr. Michael Greger. Dr. Greger is a well-respected physician who encourages healing through diet and a
plant-based lifestyle.
'''
#-------Imports--------

from random import choice
import webbrowser
import time

# -------A. Functions--------

# A1. Choose Dishes

def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(veganMeals)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Here is your menu:")
    for dish in myMenu:
        print(dish)
    print("\nThis is a great menu! My favorite dish is " + choice(myMenu) + "!")

    
# A2. Build Shopping List

def buildShoppingList():
    myShoppingList = []
    print("\nOkay! Here is your grocery list:")
    print("---------------------------------------------------------------------")
    if "Quinoa Kitchari" in myMenu:
        myShoppingList.append(quinoaKitchari)
    if "Red Beans and Quinoa" in myMenu:
        myShoppingList.append(redBeansAndQuinoa)
    if "Sheet Pan Meal" in myMenu:
        myShoppingList.append(sheetPanMeal)
    if "Rainbow Salad" in myMenu:
        myShoppingList.append(rainbowSalad)
    if "Lentil Soup" in myMenu:
        myShoppingList.append(lentilSoup)
    if "Hearty Veggie Soup" in myMenu:
        myShoppingList.append(heartyVeggieSoup)
    if "Quinoa Kitchari" in myMenu:
        myShoppingList.append(cauliflowerAlfredoLinguine)
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print("---------------------------------------------------------------------")

#-------B. Lists-------

veganMeals = ["Quinoa Kitchari","Red Beans and Quinoa","Sheet Pan Meal","Rainbow Salad","Lentil Soup","Hearty Veggie Soup","Cauliflower Alfredo Linguine"]

myMenu = []

quinoaKitchari = ["½ cup moong dal (split yellow mung beans)",
"½ cup uncooked quinoa, well rinsed and drained",
"1 cup small-chopped cauliflower",
"½ cup green peas",
"2 teaspoons grated fresh ginger"
"1 teaspoon ground coriander"
"½ teaspoon ground cumin"
"½ teaspoon ground turmeric (or 1 (½-inch) piece fresh turmeric, grated)",
"1 teaspoon white miso paste",
"¼ teaspoon ground black pepper",
"½ cup chopped fresh cilantro",
"1 lemon, cut into wedges"]

redBeansAndQuinoa = ["2 lemons",
"1 medium onion, chopped",
"1 large bell pepper, chopped",
"1 cup chopped celery",
"1 ½ cups cooked or 1 (15.5-ounce) BPA-free can or Tetra Pak salt-free kidney beans, drained and rinsed",
"1 teaspoon garlic powder",
"1 teaspoon dried thyme",
"1 teaspoon dried oregano",
"½ teaspoon paprika",
"¼-½ teaspoon black pepper",
"½ teaspoon turmeric powder",
"¼ teaspoon cayenne",
"¼-½ cup no-salt added vegetable broth or water",
"Cooked quinoa"]

sheetPanMeal = ["4 cups diced sweet potatoes (purple or orange)",
"3 cups cooked chickpeas",
"2 cups diced zucchini",
"1 ½ - 2 cups sliced Brussels Sprouts",
"2-3 cups chopped cauliflower",
"2 cups chopped carrots",
"1 medium onion, chopped",
"2-3 cups sliced cherry or grape tomatoes",
"4-5 tablespoons lemon juice (about 2 lemons)",
"1 tablespoon garlic powder",
"1 teaspoon onion powder",
"1 ½ teaspoon chipotle powder"]

rainbowSalad = ["1 ½ cups or 1 (15.5 oz) BPA-free can of salt-free chickpeas, drained and rinsed",
"1 ½ cups or 1 (15.5 oz) BPA-free can of salt-free cannellini beans, drained and rinsed",
"2 cups cherry tomatoes, cut in half",
"1 cucumber, sliced into ½ inch pieces",
"2 yellow bell peppers, sliced into ½ inch pieces",
"½ cup red onion, cut and sliced into thin strips",
"20 fresh basil leaves, minced",
"1 tablespoon fresh minced garlic",
"1 tablespoon salt free stone-ground mustard",
"1 tablespoon balsamic vinegar",
"1 tablespoon apple cider vinegar",
"3 tablespoons lemon juice",
"1 teaspoon ground turmeric",
"½ teaspoon ground pepper"]

lentilSoup = ["1½ cups dry brown lentils, soaked overnight",
"2-3 garlic cloves, peeled and minced",
"1 cup white onion, chopped",
"1 medium potato, chopped",
"2 medium carrots, chopped",
"1 cup red bell pepper, chopped",
"1 cup green bell pepper, chopped",
"1 cup zucchini, chopped",
"1 bay leaf (2 if small)",
"½ teaspoon ground turmeric",
"¼ teaspoon ground ginger",
"Black pepper, to taste",
"4-5 cups water",
"1 teaspoon white miso paste (optional)"]

heartyVeggieSoup = ["1 medium onion, chopped",
"2 garlic cloves, minced",
"2 cups broccoli chopped",
"2 medium sweet potatoes, diced",
"1 large carrot, chopped",
"2 large tomatoes, chopped",
"2 teaspoons ginger powder",
"1 teaspoon black pepper",
"2 teaspoons ground turmeric",
"4 teaspoons paprika",
"¼ cup nutritional yeast",
"8 cups water"]

cauliflowerAlfredoLinguine = ["½ cup yellow onion, chopped or 2 large shallots, chopped",
"3 garlic cloves, minced",
"1 head cauliflower, cored and chopped (3 to 4 cups)",
"1 cup Light Vegetable Broth",
"2 tablespoons nutritional yeast",
"1 tablespoon white miso paste",
"½ tablespoon fresh lemon juice",
"1 pound asparagus, trimmed and cut into 1 1/2-inch pieces",
"8 ounces whole-grain or bean-based linguine",
"Nutty Parm",
"2 tablespoons chopped fresh basil",
"coarsely ground black pepper"]

#1. How many days to plan

print("Hello, my name is Veegs and I was created to help you plan for and create vegan meals. My specialty is dinner! I can provide you with upto 7 unique dishes, along with a grocery list and recipes for each. Let's get started!")

time.sleep(8)

answer = input("\nFirst off, how many dinners would you like me to plan for you? \nPlease enter a number between 1 and 7:")

print("Okay, I will plan " + answer + " dinner(s) for you.\n")

time.sleep(2)

#2. Chooses Dishes

chooseDishes(answer)

# 3.Build shopping list

answer = input("Would you like me to create a grocery list for this menu? \nPlease answer yes or no: ")

if answer == 'yes':
    buildShoppingList()
    print()
else:
    print("Okay.")
    print()

# 4. Do you want the recipe for a specific meal?

answer = input("Would you like the recipe for a specific meal? \nPlease respond with yes or no:")


if answer == 'yes':
    recipe = input("\nGreat! What meal would you like a recipe for? \nPease copy and paste your response from the menu I provided above:")
    if recipe == "Quinoa Kitchari":
        print("\nOkay, I will redirect you to the recipe website for Quinoa Kitchari. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/quinoa-kitchari/")
    if recipe == "Red Beans and Quinoa":
        print("\nOkay, I will redirect you to the recipe website for Red Beans and Quinoa. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/red-beans-and-quinoa/")
    if recipe == "Sheet Pan Meal":
        print("\nOkay, I will redirect you to the recipe website for Sheet Pan Meal. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/sheet-pan-meals/")
    if recipe == "Rainbow Salad":
        print("\nOkay, I will redirect you to the recipe website for Rainbow Salad. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/rainbow-salad/")
    if recipe == "Lentil Soup":
        print("\nOkay, I will redirect you to the recipe website for Lentil Soup. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/lentil-soup/")
    if recipe == "Hearty Veggie Soup":
        print("\nOkay, I will redirect you to the recipe website for Hearty Veggie Soup. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/hearty-veggie-soup/")
    if recipe == "Cauliflower Alfredo Linguine":
        print("\nOkay, I will redirect you to the recipe website for Cauliflower Alfredo Linguine. \nThank you for working with me and enjoy your meals!")
        time.sleep(6)
        webbrowser.open("https://nutritionfacts.org/recipe/cauliflower-alfredo-linguine-with-roasted-asparagus/")
else:
    print("\nOkay. Thank you for working with me and enjoy your meals!")
