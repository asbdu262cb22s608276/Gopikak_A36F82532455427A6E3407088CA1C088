def linear_search_product(products, target_product):
    indices = []

    # Iterate through the list of products and check for the target product
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)

    return indices

# Test the function
if __name__ == "__main__":
    # Sample list of products
    products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

    # Target product to search for
    target_product = "Apple"

    # Perform the linear search
    result = linear_search_product(products, target_product)

    if result:
        print(f"The target product '{target_product}' was found at indices: {result}")
    else:
        print(f"The target product '{target_product}' was not found in the list.")