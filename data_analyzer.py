import statistics


def calculate_statistics(number_list):
    """
    Takes a list of numbers and returns a dictionary with
    mean, median, mode, and range.
    """

    if not number_list:
        return None

    # result
    results = {}

    # 1. mean: the average value
    results['average'] = statistics.mean(number_list)

    # 2. median: The middle number when sorted
    results['middle_value'] = statistics.median(number_list)

    # 3. mode: the number that appear most often
    try:

        results['most_frequent'] = statistics.multimode(number_list)
    except AttributeError:

        try:
            results['most_frequent'] = [statistics.mode(number_list)]
        except statistics.StatisticsError:
            results['most_frequent'] = ["No pattern found"]

    # 4. range: the gap between the smallest and largest number
    smallest = min(number_list)
    largest = max(number_list)
    results['gap'] = largest - smallest

    # store these too, just in case we want to show them
    results['smallest'] = smallest
    results['largest'] = largest
    results['total_count'] = len(number_list)

    return results


def show_friendly_results(stats):

    if not stats:
        print("\nOops! It looks like there's no data to analyze.")
        return

    print("\n" + "=" * 40)
    print("      HERE IS YOUR DATA REPORT      ")
    print("=" * 40)

    print(f"Items analyzed: {stats['total_count']}")
    print("-" * 40)
    print(f"Smallest number: {stats['smallest']}")
    print(f"Largest number:  {stats['largest']}")
    print(f"Range (Gap):     {stats['gap']}")
    print("-" * 40)
    print(f"Mean (Average):  {stats['average']:.2f}")
    print(f"Median (Middle): {stats['middle_value']}")


    modes = stats['most_frequent']
    if len(modes) == 1:
        print(f"Mode (Frequent): {modes[0]}")
    else:

        modes.sort()
        modes_string = ', '.join(str(m) for m in modes)
        print(f"Mode (Frequent): {modes_string} (It's a tie!)")

    print("=" * 40 + "\n")


def main():
    print("\n--- Welcome to this Data Analyzer ---")
    print("just type your numbers below, separated by commas.")
    print("example: 5, 10, 5, 20")

    while True:
        user_input = input("\nplease enter your numbers: ")

        # simple check to see if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye.")
            break

        if not user_input.strip():
            print("no numbers there. Please try again!")
            continue

        try:

            clean_data = []
            for item in user_input.split(','):
                if item.strip():
                    clean_data.append(float(item.strip()))

            if not clean_data:
                print("couldn't find any valid numbers. try again")
                continue


            stats = calculate_statistics(clean_data)


            show_friendly_results(stats)

            # Ask if they want to go again
            again = input("do you want to analyze another set? (yes/no): ").lower()
            if again not in ['y', 'yes', 'sure', 'ok']:
                print("thanks for using this analyzer")
                break

        except ValueError:
            print("that wasn't a number.")
            print("Please make sure you only use numbers and commas.")


if __name__ == "__main__":
    main()