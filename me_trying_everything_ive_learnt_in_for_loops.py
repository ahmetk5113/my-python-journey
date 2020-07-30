apples = ['green apple','yellow apple','red apple']
prices_for_apples = ['2.4','2.75','3.10']
for fruit, prices in zip(apples,prices_for_apples):
    print(fruit + ':'+ '' + prices)

# soo what i' ve learnt is that  we can choose the index position or starting point for enumerate function
# example:
books = ['lord of the rings', 'harry potter', 'serenad']
for index, book in enumerate(books,3):
    print('{}: {}'.format(index,book))
# results
# 3: lord of the rings
# 4: harry potter
# 5: serenad
