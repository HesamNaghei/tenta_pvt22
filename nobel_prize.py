# Elev: Hesameddin Naghiei
import requests

HELP_STRING = """
Ange ett år och fält
Tillgängliga fält: fysik, kemi, litteratur, ekonomi, fred, medicin
Exempelvis 1965 fysik
Skriv Q för att avsluta programmet.
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}


def calculate_prize_money(share: float, prize_amount: float) -> float:
    """Calculates the prize money for a laureate given the share of the prize and the total prize amount.
    Args:
        share: The fraction of the prize that the laureate received.
        prize_amount: The total prize amount.
    Returns:
        The prize money for the laureate.
    """
    return share * prize_amount


def main():
    print(HELP_STRING)
    while True:
        aaa = input(">")
        try:
            a, b = aaa.split()
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        c = {"nobelPrizeYear": int(a), "nobelPrizeCategory": cat[b]}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()

        if 'prizes' in res:
            for award in res['prizes']:
                print("-------------------------")
                print(f"År: {award['year']}")
                print(f"Kategori: {award['category']}")
                print(f"Motivering: {award['motivation']}")
                print("Laureater:")
                for laureate in award['laureates']:
                    print(f"{laureate['firstname']} {laureate['surname']}")
        else:
            print("No prizes found for the specified year and category.")

        for p in res["nobelPrizes"]:
            peng = p["prizeAmount"]
            idagpeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")

        for m in p["laureates"]:
            print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']


if __name__ == '__main__':
    main()
