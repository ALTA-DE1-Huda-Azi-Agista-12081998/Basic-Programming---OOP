def count_item_and_sort(items):
    item_count = {}
    
    # Count the occurrences of each item
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    # Sort the items based on their counts in descending order
    sorted_items = sorted(item_count.items(), key=lambda x: x[1], reverse=True)

    # Create the result string
    result = ""
    for item, count in sorted_items:
        result += f"{item}->{count} "

    # Remove the trailing space
    result = result.rstrip()

    return result


print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
# Output: "A->4 B->3 D->2 C->1"

print(count_item_and_sort(["football", "basketball", "tenis"]))
# Output: "basketball->2 football->1 tenis->1"
