
# Day 31 - Sort Colors
# Dutch National Flag Algorithm

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    step = 1

    print("Original:", nums)
    print("\n--- Pointer Movement ---")

    while mid <= high:
        if nums[mid] == 0:
            # Move red (0) to the left
            if low != mid:
                nums[low], nums[mid] = nums[mid], nums[low]

            low += 1
            mid += 1

        elif nums[mid] == 1:
            # White (1) is already in the correct section
            mid += 1

        else:
            # Move blue (2) to the right
            if mid != high:
                nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

        print(
            f"Step {step}: {nums} | "
            f"low={low}, mid={mid}, high={high}"
        )
        step += 1

    return nums


colors = [2, 0, 2, 1, 1, 0]

result = sort_colors(colors)

print("\nSorted Colors:", result)
print("Sorting completed successfully!")
