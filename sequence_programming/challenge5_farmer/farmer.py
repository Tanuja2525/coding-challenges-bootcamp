def farmer_sales():
    total_acres = 80
    acres_per_segment = total_acres / 5

    tomato_yield = (0.3 * 10 + 0.7 * 12) * acres_per_segment
    tomato_sales = tomato_yield * 1000 * 7

    potato_sales = 10 * acres_per_segment * 1000 * 20
    cabbage_sales = 14 * acres_per_segment * 1000 * 24
    sunflower_sales = 0.7 * acres_per_segment * 1000 * 200
    sugarcane_sales = 45 * acres_per_segment * 4000

    total_sales = (tomato_sales + potato_sales +
                   cabbage_sales + sunflower_sales +
                   sugarcane_sales)

    chemical_free_sales = (tomato_sales + potato_sales +
                           cabbage_sales + sunflower_sales)

    return total_sales, chemical_free_sales


def main():
    total, chemical_free = farmer_sales()

    print("Total Sales from 80 acres =", total)
    print("Chemical-free Sales after 11 months =", chemical_free)


if __name__ == "__main__":
    main()
