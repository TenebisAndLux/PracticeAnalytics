def min_districts_to_visit(Andrey_support, Boris_support):
    if not Andrey_support or not Boris_support:
        return 0

    total_votes = sum(Andrey_support) + sum(Boris_support)
    if total_votes <= 0:
        return 0

    Boris_votes = sum(Boris_support)
    districts_to_visit = 0
    if Boris_votes < (total_votes / 2):
        sorted_districts = sorted(enumerate(Boris_support), key=lambda x: x[1], reverse=True)
        for district, votes in sorted_districts:
            Boris_votes += votes
            districts_to_visit += 1
            if Boris_votes > (total_votes / 2):
                break

    if districts_to_visit == 0:
        for votes in Boris_support:
            if votes > 0:
                districts_to_visit += 1
                break

    return districts_to_visit


n = int(input())
if n <= 0:
    print(0)
else:
    boris = []
    andrey = []
    for _ in range(n):
        votes = input().split()
        if len(votes) >= 2:
            boris.append(int(votes[1]))
            andrey.append(int(votes[0]))

    print(min_districts_to_visit(andrey, boris))
